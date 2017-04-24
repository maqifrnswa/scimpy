#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Module to control soundcard input and output for impedance measurements

The main class is SpeakerTestEngine, which is initialized with no arguments.
Data is collected with the run() method. FFT corresponding to the left and
right channel are available after run() in the input_data_fft0 and
input_data_fft1 attributes """
import time
import logging
import pyaudio
import matplotlib.ticker
import numpy as np
import scipy.signal
import scimpy.speakermodel as speakermodel


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
        self.device_ndx = {}
        self.counter = None  # is this necessary to be an atribute?
        self.plotwidget = plotwidget
        self.pya = pyaudio.PyAudio()

    def set_device_ndx(self, dev, role):
        self.device_ndx[role] = dev

    def run(self,
            framesize=0,
            datarate=44100,
            duration=4,
            width=2,
            testr=12):
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
            global message
            if status != 0:
                message = "WARNING: unknown error"
                if status == pyaudio.paInputUnderflow:
                    message = "WARNING: Input Underflow. Directly choose \
sound device instead of using \"default.\""
                if status == pyaudio.paInputOverflow:
                    message = "ERROR: Input Overflow. Reduce CPU usage or \
increase buffer size."
                if status == pyaudio.paOutputUnderflow:
                    message = "ERROR: Output Underflow. Reduce CPU usage or \
increase buffer size."
                if status == pyaudio.paOutputOverflow:
                    message = "ERROR: Output Overflow. Reduce buffer size."
            data_out = data[
                self.counter*2:(self.counter+frame_count)*2]
            self.counter = self.counter+frame_count
            return(data_out, pyaudio.paContinue)

        pya = self.pya
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
            logging.error("Bit width should be 1, 2, or 4 bytes")
        data = scipy.signal.chirp(t=np.arange(0, duration, 1./datarate),
                                  f0=10,
                                  t1=duration,
                                  f1=22050,
                                  method='log',
                                  phi=-90)*((2**(8*width))/2.-1)
        data = np.concatenate((np.zeros(int(duration*.1 * datarate)),
                               data,
                               np.zeros(int(duration * 0.1 * datarate))))
        if width == 1:
            data = data+(2**(8*width))/2-1
        data = data.astype(dtype=np_type, copy=False)

        # make it stereo
        data = np.array([data, data]).transpose().flatten()

        # use as a list of byte objects for speed, then convert
        # actually faster than byte array
        input_data = []
        global message
        message = ""

        logging.info("Opening input device %d and output device %d"
                    % (self.device_ndx["Input"], self.device_ndx["Output"]))

        self.counter = 0
        self.stream = pya.open(format=pa_format,
                               channels=2,
                               rate=datarate,
                               output=True,
                               input=True,
                               input_device_index=self.device_ndx["Input"],
                               output_device_index=self.device_ndx["Output"],
                               stream_callback=cb_stream_processing,
                               frames_per_buffer=framesize)

        while self.stream.is_active():
            time.sleep(0.2)

        self.plotwidget.window().statusbar.showMessage(message)

        input_data = np.fromstring(b''.join(input_data), dtype=np_type)
        logging.info("Input data length: %f, Output data length: %f"
                    % (len(input_data), len(data)))
        # two channels
        input_data =\
            np.reshape(input_data, (int(len(input_data)/2), 2))
        input_data_fft0 = np.fft.rfft(input_data[:, 0])
        input_data_fft1 = np.fft.rfft(input_data[:, 1])

        data = np.reshape(data, (int(len(data)/2), 2))
        data = data[:, 0]
        data_fft = np.fft.rfft(data)
        if width == 1:  # stupid 8 bit uints...
            input_data_fft0[0] = 0
            input_data_fft1[0] = 0
            data_fft[0] = 0
        # print(input_data.buffer_info())

        # Close the open _channel(s)_...
        self.stream.close()

        # TODO: put pyaudioterminte in the destructor?
        # pyaudio.PyAudio().terminate()

        # inputdata2=array.array('h',b''.join(input_data) )
        # print(inputdata2)
        # plt.magnitude_spectrum(inputdata2, Fs=datarate)
        # input_data=scipy.signal.savgol_filter(input_data,11,3)

        # plt.figure()
        self.plotwidget.clear_axes()
        # plt.subplot(2, 2, 1)
        ax1 = self.plotwidget.axes1
        ax2 = self.plotwidget.axes2
        ax1b = self.plotwidget.axes1b
        # ax4 = self.plotwidget.axes4
        timedata = np.arange(0, len(input_data[:, 0]))/datarate
        ax2.plot(timedata, input_data[:, 1]/((2**(8*width))/2.-1))
        ax2.plot(timedata, input_data[:, 0]/((2**(8*width))/2.-1))

        # commented out all except microphont in and mic FFT
        # ax2.plot(data)  # left

        x_data = np.fft.rfftfreq(input_data[:, 0].size,
                                 d=1./datarate)
        imp_data = testr*input_data_fft0/(input_data_fft1-input_data_fft0)
        # TODO: only plot for freq 10-20kHz

        speakermodel.plot_impedance(ax1=ax1,
                                    ax2=ax1b,
                                    freqs=x_data,
                                    magnitude=np.abs(imp_data),
                                    phase=np.angle(imp_data)*180/np.pi)

        # ax2.plot(x_data,
        #          scipy.signal.savgol_filter(np.abs(imp_data),
        #                                     1, 0))

        # Top to tip: black green white(ring) red(tip);
        # don't use "default" device
        # output: headphones
        # input: line in (right goes to speaker+, left goes to line in)
        # headphones: positive to test resistor
        # test resistor to speaker+
        # speaker- to headphones minus
        # line in: "right" goes to speaker+, "left" goes to headphones+
        # line in ground goes to headphones-
        # in sound card settings, PCM capture: line in, set Line in to capture
#        ax2.plot(x_data,
#                 scipy.signal.savgol_filter(np.abs(input_data_fft0),
#                                            1, 0),
#                 x_data,
#                 scipy.signal.savgol_filter(np.abs(input_data_fft1),
#                                            1, 0))

        # pick filter with 10 Hz filtering?
        ax2.set_xlim([0, max(timedata)])

        ax2.set_ylabel('Measured Signal (clipping at 1)')
        ax2.set_xlabel('Time (s)')
#        ax2.set_ylabel('abs(FFT) Left/(Left-Right)', color='b')
        ax1.set_xlabel('Frequency (Hz)')
#        ax2.set_xscale('log')
#        ax2.xaxis.set_major_formatter(
#            matplotlib.ticker.FormatStrFormatter("%d"))
        ax2.yaxis.set_major_formatter(
            matplotlib.ticker.FormatStrFormatter("%g"))
        self.plotwidget.draw()