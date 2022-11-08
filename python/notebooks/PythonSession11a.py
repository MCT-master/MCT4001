import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd


def sine_synth(freq, dur_ms, amp=1, pha=0, sr=48000):

    t = np.arange(0,dur_ms/1000,1/sr)
    s = amp*np.sin(2*np.pi*freq*t+pha)

    return s

for i in range(200):
    print(i,end=' ')

signal = sine_synth(440, 500)

plt.figure(figsize=(14, 3))
plt.plot(signal)
plt.show()

sd.play(signal, 48000)
sd.wait()

print('\ndone!')

##%%