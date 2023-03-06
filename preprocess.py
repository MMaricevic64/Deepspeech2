import os

path = os.getcwd()
os.chdir(path)
txt = list()
wav = list()

cnt_txt = 0
cnt_wav = 0
cnt_log = 0

for t in sorted(os.listdir("txt")):
  for file in sorted(os.listdir(os.path.join(path, "txt", t))):
    txt.append(os.path.splitext(file)[0])

for w in sorted(os.listdir("wav")):
  for file in sorted(os.listdir(os.path.join(path, "wav", w))):
    if file.endswith(".wav"):
      wav.append(os.path.splitext(file)[0])
    else:
      os.remove(os.path.join(path, "wav", w, file))
      cnt_log += 1
      print(file + "has no .wav extension! Deleted!")

for w in wav:
  if w not in txt:
    for r, d, f in os.walk("wav"):
      for file in f:
        if file == w + ".wav":
          os.remove(os.path.join(r, file))
          cnt_wav += 1
    print(w + ".wav has no transcription .txt file! Deleted!")
    
for t in txt:
  if t not in wav:
    for r, d, f in os.walk("txt"):
      for file in f:
        if file == t + ".txt":
          os.remove(os.path.join(r, file))
          cnt_txt += 1
    print(t + ".txt has no correspondence .wav file! Deleted!")
    
print("Data is ready!\nDeleted .wav files: {cnt_wav}\nDeleted .txt files: {cnt_txt}\nDeleted other files: {cnt_log}")