import os
import whisper

# Load the Whisper model
try:
    model = whisper.load_model("base")
except Exception as e:
    print(f"Error loading model: {e}")
    raise

# Define the path to your audio file
audio_file_path = "dhar.mp3"

# Check if the file exists
if not os.path.exists(audio_file_path):
    print(f"Audio file not found: {audio_file_path}")
else:
    try:
        # Transcribe the audio file
        result = model.transcribe(audio_file_path)
        # Print the transcribed text
        print(result.get("text", "No text found"))
    except Exception as e:
        print(f"Error transcribing audio: {e}")

