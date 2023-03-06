import os
import csv

path = os.getcwd()
os.chdir(path)

filenames = list()
transcriptions = list()
       
for name in sorted(os.listdir("txt")):
    filenames.append(os.path.splitext(name)[0])
    with open(os.path.join(path, "txt", name), "r") as file:
        transcriptions.append("".join(file.readline()..strip().split()))

with open("dataset.csv", "w", newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter='|')
    writer.writerow(["filename", "transcription"])
    writer.writerows(zip(filenames, transcriptions))
    
print("Dataset (.csv) is ready!")
