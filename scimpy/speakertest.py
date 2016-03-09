#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Module to control soundcard input and output for impedance measurements

The main class is SpeakerTestEngine, which is initialized with no arguments.
Data is collected with the run() method. FFT corresponding to the left and
right channel are available after run() in the input_data_fft0 and
input_data_fft1 attributes """
import pyaudio
import time

import numpy as np
import scipy.signal

# Open the stream required, mono mode only...
# Written _longhand_ so that youngsters can understand how it works...

# 2000 1600 more frames recorded than played
# 2205
# 3000 600 frames
# 4000 3600
# framesize=17640, was excatly 17640 too long!
# full time would be 176400 frames, so time must be integer number of frames
# time not in second, but integer of #frames (closest integer total # frames?)


class SpeakerTestEngine():
    """Class that will control signal I/O during speaker testing"""
    def __init__(self, plotwidget):
        self.input_device_ndx = 0
        self.output_device_ndx = 0
        self.counter = None  # is this necessary to be an atribute?
        self.plotwidget = plotwidget

    def set_input_device_ndx(self, dev):
        self.input_device_ndx = dev

    def set_output_device_ndx(self, dev):
        self.output_device_ndx = dev

    def run(self,
            framesize=0,
            datarate=44100,
            duration=4,
            width=2):
        """Runs speaker impedance test

        Arguments:
        framesize -- chunk size that is read from sound card each callback
        datarate  -- sound card data acquisition/output rate in Hz
        duration  -- time for test, in seconds
        width     -- sound card bit width, in bytes (e.g., "2" = 16 bits)

        Output:
        Input_data_fft0 -- left-channel fft
        input_data_fft1 -- right-channel fft
        """
        # TODO update doc string with output types, and real outputs!
        def cb_stream_processing(in_data, frame_count, time_info, status):
            """PyAudio callback to fill output buffer and handle input
            buffer"""
            input_data.append(in_data)
            frames_to_write = frame_count
            data_out = data[
                self.counter*2:(self.counter+frames_to_write)*2].tostring()
            self.counter = self.counter+frames_to_write
            print(self.counter, len(data)/2-self.counter,
                  frames_to_write,
                  len(data_out))
            return(data_out, pyaudio.paContinue)

        pya = pyaudio.PyAudio()
        # maybe make framesize=int(datarate/10)
        # duration seconds
        # volume max of 1
        # width in bytes, need to update format below, why does 4 not work?
        # because I have 16bit le at 44100 Hz! microphone
        if width == 1:
            # array_type = 'B' #1 byte unsigned char
            # pa_format = pya.get_format_from_width(width)
            pa_format = pyaudio.paUInt8
            np_type = np.uint8  # pyaudio returns uint for 8 bit
        elif width == 2:
            # array_type = 'H' #2 byte unsigned short int
            pa_format = pyaudio.paInt16
            np_type = np.int16
        elif width == 4:
            # array_type = 'I' #4 byte unsigned int
            pa_format = pyaudio.paInt32
            np_type = np.int32
        else:
            print("Bit width should be 1, 2, or 4 bytes")

        data = (scipy.signal.chirp(t=np.arange(0, duration, 1/datarate),
                                   f0=0,
                                   t1=duration,
                                   f1=20000,
                                   method='lin',
                                   phi=-90)*((2**(8*width))/2-1))
        if width == 1:
            data = data+(2**(8*width))/2-1
        data = data.astype(dtype=np_type, copy=False)

        # make it stereo
        data = np.array([data, data]).transpose().flatten()

        # use as a list of byte objects for speed, then convert
        input_data = []

        print("Opening input device %d and output device %d" % (
            self.input_device_ndx, self.output_device_ndx))

        self.counter = 0
        self.stream = pya.open(format=pa_format,
                               channels=2,
                               rate=datarate,
                               output=True,
                               input=True,
                               input_device_index=self.input_device_ndx,
                               output_device_index=self.output_device_ndx,
                               stream_callback=cb_stream_processing,
                               frames_per_buffer=framesize)

        while self.stream.is_active():
            time.sleep(0.2)

        input_data = b''.join(input_data)  # [3:]
        input_data = np.fromstring(input_data, dtype=np_type)
        print(len(input_data), len(data))
        # two channels
        input_data =\
            np.reshape(input_data, (len(input_data)/2, 2))
        input_data_fft0 = np.fft.rfft(input_data[:, 0])
        input_data_fft1 = np.fft.rfft(input_data[:, 1])

        data = np.reshape(data, (len(data)/2, 2))
        data = data[:, 0]
        data_fft = np.fft.rfft(data)
        if width == 1:  # stupid 8 bit uints...
            input_data_fft0[0] = 0
            input_data_fft1[0] = 0
            data_fft[0] = 0
        # print(input_data.buffer_info())

        # Close the open _channel(s)_...
        self.stream.close()
        pyaudio.PyAudio().terminate()
        # inputdata2=array.array('h',b''.join(input_data) )
        # print(inputdata2)
        # plt.magnitude_spectrum(inputdata2, Fs=datarate)
        # input_data=scipy.signal.savgol_filter(input_data,11,3)

        # plt.figure()
        self.plotwidget.clear_axes()
        # plt.subplot(2, 2, 1)
        ax1 = self.plotwidget.axes1  # can do this programatically with figure.axes()
        ax2 = self.plotwidget.axes2
        ax3 = self.plotwidget.axes3
        ax4 = self.plotwidget.axes4
        ax1.plot(input_data[:, 0])  # left
        # plt.subplot(2, 2, 2)
        ax2.plot(data)  # left
        #plt.subplot(2, 2, 3)

        x_data = np.fft.rfftfreq(input_data[:, 0].size,
                                 d=1./datarate)
        ax3.plot(x_data,
                 scipy.signal.savgol_filter(np.abs(input_data_fft0),
                                            1, 0))
        # pick filter with 10 Hz filtering?
        ax3.set_xlim(xmin=20)
        ax3.set_xscale('log')

        # plt.subplot(2, 2, 4)
        # plt.plot(x_data, np.abs(input_data_fft1))
        data_x_data = np.fft.rfftfreq(data.size,
                                      d=1./datarate)
#        plt.plot(data_x_data, scipy.signal.savgol_filter(
#            np.abs(np.fft.rfft(data)), 41, 1))
        ax4.plot(data_x_data, np.abs(data_fft))
        ax4.set_xlim(xmin=20)
        ax4.set_xscale('log')

        self.plotwidget.draw()

if __name__ == "__main__":
    ENGINE = SpeakerTestEngine()
    ENGINE.run()
