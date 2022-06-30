import scipy.io.wavfile
import scipy.signal
import os
import numpy as np

path = os.getcwd()
os.chdir(path)

new_rate = 16000

#Create resampled directory
directory_path = path+"/resampled"
os.mkdir(directory_path)

#Resample .wav files to 16khz
for name in sorted(os.listdir("wav")):    
    rate, wav = scipy.io.wavfile.read(os.path.join(path, "wav", name))
    samples = round(len(wav) * float(new_rate) / rate)
    new_data = scipy.signal.resample(wav, samples)
    scipy.io.wavfile.write(os.path.join(path, "resampled", name), new_rate, new_data.astype(np.dtype('i2')))

print("Resampling of .wav files is done!")
