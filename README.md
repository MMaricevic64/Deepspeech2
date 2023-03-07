# Deepspeech2 model for the Croatian language
**Deepspeech2** is an end-to-end deep neural network (DNN) for **automatic speech recognition (ASR)**.

**Speech-to-text (STT)** using Deepspeech2 model can be summarized in the following scheme:
- **Preprocessing** - takes a raw audio waveform signal and converts it into a **log-spectrogram**

- **DNN** - produces **a probability distribution P_t(c)** over vocabulary characters per each time step
- **CTC Loss** - function which is used when we don't know how is the input aligned with the output, i.e. how the characters in the transcription are aligned with the sound
- **Decoder** - converts a probability distribution over characters P_t(c) into text

The vocabulary of the Deepspeech2 model was expanded so that the model could recognize and understand the Croatian language. The model was trained and validated using audio recordings in the Croatian.

The obtained results can be seen by opening the [Python Notebook](https://github.com/MMaricevic64/Deepspeech2/blob/main/Deepspeech2.ipynb) in the **Google Colab** tool.

<img src="https://user-images.githubusercontent.com/61973790/223370054-a1ccc650-e911-404c-bc77-bb9264e894e4.png">

## Dataset
- **VEPRAD base** - consists of **the Croatian audio weather forecasts** recorded from news on the national radio (14 female and 11 male speakers)
- **audio files** ([wav](https://github.com/MMaricevic64/Deepspeech2/tree/main/wav)) - 5257 .wav files (approx. 10 seconds per each)
- **transcriptions** ([txt](https://github.com/MMaricevic64/Deepspeech2/tree/main/txt)) - 4547 .txt files
- [preprocess.py](https://github.com/MMaricevic64/Deepspeech2/blob/main/preprocess.py) - Removes all unpaired files (.wav - .txt) and files with no .wav extension
- 4332 pairs (audio file with corresponding transcription)  

  - 2862 files - female speakers
  - 1470 files - male speakers
- **Training set** - 3898 files (90%)
- **Validation set** - 434 files (10%)
- [resample.py](https://github.com/MMaricevic64/Deepspeech2/blob/main/resample.py) - Resamples all .wav files to **16 kHz frequency** (needed for Tensorflow)
- [dataset.py](https://github.com/MMaricevic64/Deepspeech2/blob/main/dataset.py) - makes **CSV table** with values in 2 columns (file name, transcription) - input in the form of a CSV table is required by Tensorflow

## Model training
- **Google Collab** was used to train the Deepspeech 2 model (an advanced version that ensures a runtime of 24 hours, more advanced hardware and up to 200GB free space)
- **50 epochs - approx. 10 minutes per epoch**
- After about 40 epochs the rate of learning began to decline more significantly and after a certain time stagnation would occur

## Model validation
- **Word Error Rate (WER) - 22%**
- In order to improve the accuracy of the model, it is necessary to:  

  - Use a larger dataset with longer audio recordings and different speakers (needs advanced hardware and more time to train the model)
  - Modify model parameters
