import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import sys
import getopt

#for more info on getopt see https://docs.python.org/3/library/getopt.html

def sine_synth(freq, dur_ms, amp=1, pha=0, sr=48000):

    t = np.arange(0,dur_ms/1000,1/sr)
    s = amp*np.sin(2*np.pi*freq*t+pha)

    return s


def main():

    print('Number of arguments:', len(sys.argv), 'arguments.')
    print('Argument List:', str(sys.argv))
    try:
        opts, args = getopt.getopt(sys.argv[1:],"hi:o:",["help","infile=","outfile="]) #list of possible arguments
        print("opts:",opts)
        print("args:",args)
    except getopt.GetoptError: #this is executed when we pass to the script an argument not in the above list
      print ("Something went wrong - best would be to specify how to run the command")
      sys.exit(2)


    for i in range(200):
        print(i,end=' ')

    signal = sine_synth(440, 500)

    plt.figure(figsize=(14, 3))
    plt.plot(signal)
    plt.show()

    sd.play(signal, 48000)
    status = sd.wait()

    print('\ndone!')

# run the main function only if this script is executed
if __name__ == "__main__":
    print('__name__ is',__name__)
    main()
