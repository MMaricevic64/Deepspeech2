import os

path = os.getcwd()
os.chdir(path)
txt = list()
wav = list()

for t in sorted(os.listdir("txt")):
    txt.append(os.path.splitext(t)[0])
    
for w in sorted(os.listdir("wav")):
    wav.append(os.path.splitext(w)[0])
    
for w in wav:
    if w not in txt:
        os.remove(os.path.join(path, "wav", w + ".wav"))
        print(w + ".wav has no transcription! Deleted!")

for t in txt:
    if t not in wav:
        os.remove(os.path.join(path, "txt", t + ".txt"))
        print(t + ".txt has no correspondence .wav file! Deleted!")
        
with open(os.path.join(path, "txt", "sm04010103201.txt"), "w") as file:
        file.write("i vremenska prognoza za poslijepodne na jadranu prete`ito a u unutra{njosti djelomice sun~ano obla~no i tmurno samo ponegdje u sjeverozapadnom podru~ju i u lici")
        
print("Data is ready!")