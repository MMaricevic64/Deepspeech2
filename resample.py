import scipy.io.wavfile
import scipy.signal
import os
import numpy as np

path = os.getcwd()
os.chdir(path)

cnt_wav = 0

#Create resampled directory
if os.path.isdir("resampled"):
    pass
else:
    os.mkdir("resampled")

#Resample .wav files to 16khz
new_rate = 16000
print("Resampling .wav files to 16khz in progress. It may take a few minutes...") 
for name in sorted(os.listdir("wav")):    
    rate, wav = scipy.io.wavfile.read(os.path.join(path, "wav", name))
    samples = round(len(wav) * float(new_rate) / rate)
    new_data = scipy.signal.resample(wav, samples)
    scipy.io.wavfile.write(os.path.join(path, "resampled", name), new_rate, new_data.astype(np.dtype('i2')))
    cnt_wav += 1
print("Resampled files: {cnt_wav}\n")
print("Resampling of .wav files is done!")
