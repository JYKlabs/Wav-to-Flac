import os
import soundfile as sf
from tkinter import Tk, filedialog

def select_folder():
    root = Tk()
    root.withdraw()  # Hide the main window
    folder = filedialog.askdirectory(title="Select the folder containing WAV files")
    return folder

def convert_wav_to_flac(folder_path):
    if not folder_path:
        print("No folder selected.")
        return
    
    # Iterate through all files in the folder
    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.wav'):
            wav_path = os.path.join(folder_path, filename)
            flac_path = os.path.join(folder_path, os.path.splitext(filename)[0] + '.flac')
            
            try:
                # Read the WAV file
                data, samplerate = sf.read(wav_path)
                
                # Write to FLAC file (preserving original sample rate and bit depth)
                sf.write(flac_path, data, samplerate, format='FLAC')
                print(f"Conversion completed: {filename} -> {os.path.basename(flac_path)}")
                
            except Exception as e:
                print(f"Error occurred: Failed to convert {filename} - {str(e)}")
    
    print("All conversions completed.")

if __name__ == "__main__":
    folder = select_folder()
    convert_wav_to_flac(folder)
