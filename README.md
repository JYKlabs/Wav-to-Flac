# WAV to FLAC Converter

A Python script to convert WAV audio files to lossless FLAC format while preserving the original sample rate and bit depth. The original WAV files are kept intact.

## Requirements
- Python 3.x
- Libraries: `soundfile`, `tkinter`
  Install them using:
  ```
  pip install soundfile
  ```

## Usage
1. Run the script:
   ```
   python wav_to_flac.py
   ```
2. A dialog box will prompt you to select a folder containing WAV files.
3. The script will convert all `.wav` files in the selected folder to `.flac`, saving them in the same folder.
4. Conversion progress and any errors will be printed to the console.

## Notes
- The resulting FLAC files are lossless, identical in audio quality to the original WAV files.
- Original WAV files are not deleted.
- The script uses the `soundfile` library to ensure accurate preservation of audio data.

## License
MIT License
