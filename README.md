# SPEECH RECOGNITION SYSTEM

---

**COMPANY:** CODTECH IT SOLUTIONS
**NAME:** G M KAIFU
**INTERN ID:** CT06DN1863
**DOMAIN:** ARTIFICIAL INTELLIGENCE
**DURATION:** 6 WEEKS (JUNE-JULY 2024)
**MENTOR:** NEELA SANTOSH

# INTRODUCTION
In the modern era of artificial intelligence and natural language processing, speech recognition systems play a vital role in bridging the gap between humans and machines. From voice assistants like Siri and Alexa to accessibility tools and automated transcription services, speech-to-text technology is being used across various industries to improve communication, accessibility, and automation.

As part of my internship project, the task was to build a basic speech-to-text system using pre-trained models and libraries like SpeechRecognition or Wav2Vec. However, to enhance transcription accuracy and usability, I chose to implement this system using OpenAI's Whisper model, a state-of-the-art pre-trained deep learning model for automatic speech recognition (ASR).

# 📝 Overview

This project fulfills the internship requirement of building a **basic Speech-to-Text system** using **pre-trained models** and libraries like **Whisper** and audio processing tools. The system is designed to **transcribe short English audio clips** using OpenAI's **Whisper** model, which is one of the most powerful open-source speech recognition models available.

The project demonstrates the integration of:
- **Real-time microphone recording**
- **Pre-trained speech recognition model (Whisper)**
- **Audio signal processing**
- **Interactive CLI-based transcription system**

It is a functional, self-contained system that enables users to record short voice inputs or use existing audio files, and get real-time transcription output.

---

# 📌 Features

- ✅ Record short audio clips using the microphone
- ✅ Transcribe English audio clips with high accuracy
- ✅ Use pre-trained Whisper model (`tiny` version for speed)
- ✅ Interactive command-line interface for user-friendly experience
- ✅ Temporary file handling and automatic cleanup
- ✅ Error handling for audio recording, file I/O, and model loading

---

# 📦 Libraries & Requirements

This project uses the following Python libraries:


| Library           | Purpose                                                  |
|------------------ |--------------------------------------------------------  |
| `openai-whisper`  | Load and run pre-trained Whisper model for transcription |
| `torch`           | Backend engine for running Whisper (PyTorch)             |
| `sounddevice`     |  Record audio from the microphone                        |
| `numpy`           | Handle audio data arrays                                 |
| `scipy.io.wavfile`| Save and read WAV files for audio input/output           |
| `os`              | File system operations                                   |
| `warnings`        | Suppress known warnings for cleaner output               |




# 🔧 System Requirements

- Python 3.7+
- `ffmpeg` installed and added to PATH (for audio format compatibility)
- `PortAudio` (may be needed for microphone input on some systems)

Install Required Python Libraries:

   pip install openai-whisper torch sounddevice numpy scipy

Install FFmpeg:

   On Windows: Download from https://ffmpeg.org/download.html and add to PATH.

Install PortAudio:

sudo apt install portaudio19-dev

pip install sounddevice



# Working of the System

_Model Loading:_

The system loads the pre-trained tiny Whisper model on launch.

This model is lightweight and works well for basic transcription tasks.

_User Interface (CLI Menu):_

The user is prompted to either record a new audio clip, use an existing audio file, or exit.

_Audio Recording:_

If the user chooses to record, audio is captured via microphone using sounddevice.

The audio is saved as a temporary WAV file using scipy.

_Transcription:_

The audio file is transcribed using the Whisper model.

Language is explicitly set to English (language="en").

The transcribed text is displayed to the user.

_Cleanup:_

Temporary audio files are automatically deleted after transcription to avoid clutter.

_Run programin terminal:_

Run the Python script: python filename.py

_Choose from the following options in the terminal:_

1. Transcribe an existing ENGLISH audio file
2. Record a new short ENGLISH audio clip (up to 30s)
3. Exit

# OUTPUT 1
    
![Image](https://github.com/user-attachments/assets/77fc7535-cf5f-4e14-bb56-500cc2fa5aca) 

# OUTPUT 2

![Image](https://github.com/user-attachments/assets/4de5d361-06aa-4f10-be06-49083e07b7ac) 

# CONCLUSION

This project successfully demonstrates a basic yet functional speech recognition system using OpenAI's Whisper pre-trained model. It meets the internship task requirements by enabling users to record or upload short English audio clips and receive accurate transcriptions in real time.

By integrating widely used libraries like openai-whisper, sounddevice, and scipy, the system ensures ease of use, efficient processing, and adaptability for further enhancements. Whether it’s for personal productivity, accessibility tools, or academic learning, this project forms a strong foundation for more advanced speech-to-text applications in the future.

In conclusion, this system not only showcases the practical application of pre-trained models but also reinforces key skills in Python programming, audio signal processing, and machine learning integration — providing valuable hands-on experience aligned with real-world development tasks.
   
