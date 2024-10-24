# Import required libraries
from TTS.api import TTS
import pandas as pd
import os
from TTS.api import TTS

# Define the output folder for generated audio
output_folder = r'C:/Users/pk612/Documents/TTS_Assignment/generated_audio'

# Check if the folder exists, if not, create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    print(f"Folder created: {output_folder}")

# Step 1: Verify Data Integrity
# Load the CSV dataset
csv_file = r'C:\Users\pk612\Documents\TTS_Assignment\datasets\data.csv'  # Path to your CSV file
dataset = pd.read_csv(csv_file)

# Display the first few rows to inspect
print("First few rows of the dataset:")
print(dataset.head())  # Check if the dataset has the right structure

# Step 2: Check if all audio files exist
print("\nVerifying if audio files exist...")
for idx, row in dataset.iterrows():
    audio_path = row['audio_file_path'].strip('"')  # Remove quotes if any
    if not os.path.exists(audio_path):
        print(f"Audio file does not exist: {audio_path}")
    else:
        print(f"Audio file found: {audio_path}")

# Step 3: Initialize the TTS model
model_name = "tts_models/en/ljspeech/tacotron2-DDC"  # Example model from TTS library
tts = TTS(model_name)

# Step 4: Generate TTS outputs and save them as audio files
output_dir = "C:/Users/pk612/Documents/TTS_Assignment/generated_audio/"
os.makedirs(output_dir, exist_ok=True)  # Create output directory if it doesn't exist

# Fine-tuning loop and saving generated audio
for idx, row in dataset.iterrows():
    audio_path = row['audio_file_path']
    transcription = row['text']

    # Define the output file path for each generated audio file
    output_file = os.path.join(output_folder, f"output_{idx}.wav")
    
    # Generate and save audio for the current transcription
    tts.tts_to_file(text=transcription, file_path=output_file)
    
    print(f"Audio generated for transcription: '{transcription}' and saved to {output_file}")

