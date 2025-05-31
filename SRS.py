import whisper
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import os
import warnings

# Suppress specific Whisper FP16 CPU warning
warnings.filterwarnings("ignore", message="FP16 is not supported on CPU", category=UserWarning)

# --- Configuration ---
MODEL_TYPE = "tiny"  # Using the "tiny" model as requested
DEFAULT_RECORDING_DURATION = 10  # seconds
MAX_RECORDING_DURATION = 30      # seconds
TEMP_RECORDED_FILENAME = "temp_recorded_audio.wav"
TARGET_LANGUAGE = "en" # Explicitly setting to English

def load_whisper_model():
    """Loads the specified Whisper pre-trained model."""
    print(f"\n🔄 Loading Whisper model ({MODEL_TYPE})...")
    try:
        model = whisper.load_model(MODEL_TYPE)
        print(f"✅ Whisper model ({MODEL_TYPE}) loaded successfully.")
        return model
    except Exception as e:
        print(f"❌ Error loading Whisper model: {e}")
        print("   Ensure you have an internet connection for the first download of the model,")
        print("   and that PyTorch is installed correctly (pip install torch).")
        print("   You might also need to install ffmpeg (see setup notes below).")
        return None

def record_short_audio_clip(filename=TEMP_RECORDED_FILENAME, duration=DEFAULT_RECORDING_DURATION, samplerate=16000):
    """Records a short audio clip from the microphone."""
    print(f"\n🎙️ Recording for {duration} seconds. Please speak clearly in ENGLISH...")
    try:
        sd.query_devices()
        recording = sd.rec(int(samplerate * duration), samplerate=samplerate, channels=1, dtype='int16')
        sd.wait()
        wav.write(filename, samplerate, recording)
        print(f"✅ Recording saved as {filename}")
        return filename
    except Exception as e:
        print(f"⚠️ Error during recording: {e}")
        print("   Please ensure your microphone is connected and permitted.")
        print("   You might need to install PortAudio (see setup notes below).")
        return None

def transcribe_audio_english_only(model, audio_path):
    """
    Transcribes the given audio file using the loaded Whisper model,
    forcing English language transcription.
    """
    if not os.path.exists(audio_path):
        print(f"❌ Error: Audio file not found at {audio_path}")
        return

    print(f"\n🧠 Transcribing audio (expecting ENGLISH) from: {audio_path}...")
    try:
        # Explicitly set language="en" for English-only transcription
        result = model.transcribe(audio_path, language=TARGET_LANGUAGE, fp16=False)
        
        transcribed_text = result["text"]
        # The 'language' field in the result might still show what it detected,
        # but the transcription was guided towards English.
        # We can just state our target.
        print(f"\n🗣️ Target Language: English")
        print(f"📝 Transcription: {transcribed_text}")
        
    except Exception as e:
        print(f"❌ Error during transcription: {e}")
        print(f"   Ensure the audio file '{audio_path}' is a valid audio format (e.g., WAV, MP3).")
        print(f"   If it's not WAV, ensure ffmpeg is installed and in your system's PATH.")


def main_system_loop():
    """Main function to run the English-only speech recognition system."""
    print("-------------------------------------------------")
    print("    ENGLISH-ONLY SPEECH RECOGNITION SYSTEM       ")
    print(f"         (Using Whisper '{MODEL_TYPE}' Model)        ")
    print("-------------------------------------------------")

    model = load_whisper_model()
    if model is None:
        print("\nExiting due to model loading failure. Please check messages above.")
        return

    while True:
        print("\nChoose an option:")
        print("  1. Transcribe an existing ENGLISH audio file")
        print(f"  2. Record a new short ENGLISH audio clip (up to {MAX_RECORDING_DURATION}s)")
        print("  3. Exit")

        choice = input("Enter your choice (1, 2, or 3): ").strip()

        if choice == '1':
            audio_file_path = input("➡️ Enter the path to your ENGLISH audio file: ").strip().strip('"')
            if audio_file_path:
                transcribe_audio_english_only(model, audio_file_path)
            else:
                print("⚠️ No file path entered. Please try again.")
        
        elif choice == '2':
            try:
                duration_input = input(
                    f"🎤 Enter recording duration in seconds (1-{MAX_RECORDING_DURATION}, default {DEFAULT_RECORDING_DURATION}): "
                ).strip()
                
                if not duration_input:
                    duration = DEFAULT_RECORDING_DURATION
                else:
                    duration = int(duration_input)
                
                if not (0 < duration <= MAX_RECORDING_DURATION):
                    print(
                        f"⚠️ Invalid duration. Using default: {DEFAULT_RECORDING_DURATION}s."
                    )
                    duration = DEFAULT_RECORDING_DURATION
            
            except ValueError:
                print(f"⚠️ Invalid input for duration. Using default: {DEFAULT_RECORDING_DURATION}s.")
                duration = DEFAULT_RECORDING_DURATION
            
            recorded_file_path = record_short_audio_clip(duration=duration)
            if recorded_file_path:
                transcribe_audio_english_only(model, recorded_file_path)
                try:
                    if os.path.exists(recorded_file_path):
                        os.remove(recorded_file_path)
                        print(f"🗑️ Temporary file {recorded_file_path} removed.")
                except OSError as e:
                    print(f"⚠️ Could not remove temporary file {recorded_file_path}: {e}")
        
        elif choice == '3':
            print("\n👋 Exiting the Speech Recognition System. Goodbye!")
            break
        
        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    print("---------------------------------------------------------------------")
    print("ENGLISH-ONLY SPEECH RECOGNITION SYSTEM - SETUP NOTE:")
    print("This script requires the following Python packages:")
    print("  - openai-whisper: `pip install openai-whisper`")
    print("  - sounddevice:    `pip install sounddevice`")
    print("  - numpy:          `pip install numpy`")
    print("  - scipy:          `pip install scipy`")
    print("  - PyTorch:        `pip install torch`")
    print("\nAdditional System Dependencies (may be needed):")
    print("  - ffmpeg: For processing various audio formats (other than WAV).")
    print("  - PortAudio: For microphone access via `sounddevice` on some systems.")
    print("  (See previous messages for installation instructions if needed)")
    print("---------------------------------------------------------------------\n")
    
    main_system_loop()
