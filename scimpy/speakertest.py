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
import matplotlib.pyplot as plt
import scipy.signal

# Open the stream required, mono mode only...
# Written _longhand_ so that youngsters can understand how it works...

# 2000 1600 more frames recorded than played
# 2205
# 3000 600 frames
# 4000 3600
# self.framesize=17640, was excatly 17640 too long!
# full time would be 176400 frames, so time must be integer number of frames
# time not in second, but integer of #frames (closest integer total # frames?)


class SpeakerTestEngine():
    """Class that will control signal I/O during speaker testing"""
    def __init__(self):
        self.input_data_fft1 = None
        self.input_data_fft0 = None
        self.data = None
        self.datarate = None
        self.counter = None
        self.input_data = None
        self.framesize = None

#TODO: make this a function, not a class method?
    def cb_stream_processing(self, in_data, frame_count, time_info, status):
        """PyAudio callback to fill output buffer and handle input buffer"""
        self.input_data.append(in_data)
        # print(self.input_data[1])
        # self.input_data=np.append(self.input_data,in_data)
#        data_out =\
#            self.data[(self.framesize*2)*self.counter:
#                      (self.framesize*2)*(self.counter+1)].tostring()  # stereo
        frames_to_write = frame_count
        data_out =\
            self.data[self.counter*2:
                      (self.counter+frames_to_write)*2].tostring()  # stereo
        self.counter = self.counter+frames_to_write
        print(self.counter, len(self.data)/2-self.counter,
              frames_to_write,
              len(data_out)
      #        time_info,
      #        self.datarate*time_info['input_buffer_adc_time'] +
      #        frame_count + self.datarate*time_info['output_buffer_dac_time'],
              )
        return(data_out, pyaudio.paContinue)

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
        self.framesize = framesize
        self.datarate = datarate
        pya = pyaudio.PyAudio()
        # maybe make self.framesize=int(self.datarate/10)
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

#        self.data = np.array(
#            np.random.random_integers(0, 2**(8*width)-1,
#                                      duration*self.datarate),
#            dtype=np_type)  # this works because fixed-width ints wrap

        # print(self.data.shape)
        self.data = (scipy.signal.chirp(np.arange(0,duration,1/self.datarate),
                                        0,
                                        duration,
                                        20000,
                                        method='lin',
                                        phi=-90
                    )*((2**(8*width))/2-1))#.astype(dtype=np_type,copy=False)
        if width == 1:
            self.data=self.data+(2**(8*width))/2-1
        self.data=self.data.astype(dtype=np_type,copy=False)
        # self.data=scipy.hanning(len(self.data))*self.data
        # make it stereo
        self.data = np.array([self.data, self.data]).transpose().flatten()
        # print(self.data.shape)

        # self.input_data=np.array([],dtype=np_type)

        # use as a list of byte objects for speed, then convert
        self.input_data = []

        self.counter = 0

        

        self.stream = pya.open(format=pa_format,
                          channels=2,
                          rate=self.datarate,
                          output=True,
                          input=True,
                          stream_callback=self.cb_stream_processing,
                          frames_per_buffer=self.framesize)

        # print(pya.get_default_output_device_info())
        # print(pya.get_default_input_device_info())
        # print(p.get_default_host_api_info())
        # print(p.get_host_api_count())

        while self.stream.is_active():
            time.sleep(0.2)

        self.input_data = b''.join(self.input_data)  # [3:]
        self.input_data = np.fromstring(self.input_data, dtype=np_type)
        print(len(self.input_data),len(self.data))
        # two channels
        self.input_data =\
            np.reshape(self.input_data, (len(self.input_data)/2, 2))
        self.input_data_fft0 = np.fft.rfft(self.input_data[:, 0])
        self.input_data_fft1 = np.fft.rfft(self.input_data[:, 1])


        self.data = np.reshape(self.data, (len(self.data)/2, 2))
        self.data = self.data[:, 0]
        self.data_fft=np.fft.rfft(self.data)
        if width == 1:  # stupid 8 bit uints...
            self.input_data_fft0[0] = 0
            self.input_data_fft1[0] = 0
            self.data_fft[0] = 0
        # print(self.input_data.buffer_info())

        # Close the open _channel(s)_...
        self.stream.close()
        pyaudio.PyAudio().terminate()
        # inputdata2=array.array('h',b''.join(self.input_data) )
        # print(inputdata2)
        # plt.magnitude_spectrum(inputdata2, Fs=self.datarate)
        # self.input_data=scipy.signal.savgol_filter(self.input_data,11,3)
        plt.subplot(2, 2, 1)
        plt.plot(self.input_data[:, 0])  # left
        plt.subplot(2, 2, 2)
        plt.plot(self.data)  # left
        plt.subplot(2, 2, 3)

        x_data = np.fft.rfftfreq(self.input_data[:, 0].size,
                                 d=1./self.datarate)
        plt.plot(x_data,
                 scipy.signal.savgol_filter(np.abs(self.input_data_fft0),
                                            1, 0))
        # pick filter with 10 Hz filtering?
        plt.xlim(xmin=20)
        plt.xscale('log')

        plt.subplot(2, 2, 4)
        # plt.plot(x_data, np.abs(self.input_data_fft1))
        data_x_data = np.fft.rfftfreq(self.data.size,
                                      d=1./self.datarate)
#        plt.plot(data_x_data, scipy.signal.savgol_filter(
#            np.abs(np.fft.rfft(self.data)), 41, 1))
        plt.plot(data_x_data, np.abs(self.data_fft))
        plt.xlim(xmin=20)
        plt.xscale('log')

        plt.show()

if __name__ == "__main__":
    ENGINE = SpeakerTestEngine()
    ENGINE.run()
