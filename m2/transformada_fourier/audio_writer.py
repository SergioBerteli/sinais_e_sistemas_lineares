from numpy import pi, linspace, cos, int16
from scipy.io.wavfile import write

samp_rate = 44100 # samplings per second
duration = 5 # seconds

t = linspace(0, duration, int(samp_rate * duration), endpoint=False)

def f_1(t):
    return cos(2 * pi * 200 * t) + cos(2 * pi * 400 * t)

def f_2(t):
    return cos(2 * pi * 800 * t) + cos(2 * pi * 1600 * t)

# generating the signals
audio_f1 = f_1(t)
audio_f2 = f_2(t)

# formanting the audio for the compatibility
audio_f1_scaled = int16(audio_f1 * 32767)
audio_f2_scaled = int16(audio_f2 * 32767)

write("audio_outputs\\audio_f1.wav", samp_rate, audio_f1_scaled)
write("audio_outputs\\audio_f2.wav", samp_rate, audio_f2_scaled)
