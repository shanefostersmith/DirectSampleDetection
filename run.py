from os import path 
from app.audio_tools import detectbeats
from app.utils import file_utils
import librosa
import math
import soundfile as sf

SAMPLERATE = 44100

def main():
    file_path_song = path.expanduser("~/Desktop/Song & Sample/Devil In a New Dress/Devil In A New Dress_Section.mp3")
    file_path_sample= path.expanduser("~/Desktop/Song & Sample/Devil In a New Dress/Will You Love Me Tomorrow.mp3")
    if path.exists(file_path_song):
        print("File found.")
    else:
        print("File not found. Check the path.")    
    
    audio_data_song, audio_data_sample, song_wav, sample_wav = file_utils.loadSongs(file_path_song,file_path_sample,SAMPLERATE)
    beatsSong, dominant_tempo_song, tempo_strength_song = detectbeats.detectbeat2(file_path_song)
    beatsSample, dominant_tempo_sample, tempo_strength_sample= detectbeats.detectbeat2(file_path_sample)
    
    print("Song Tempo: ", dominant_tempo_song)
    print("Sample Tempo: ", dominant_tempo_sample)
    
    semitone_shift = round(12*math.log2(dominant_tempo_song/dominant_tempo_sample))
    print("Semitone shift", semitone_shift)        
    shifted_audio = librosa.effects.pitch_shift(y=audio_data_sample, sr=SAMPLERATE, n_steps=semitone_shift)
    shifted_sample_filename = 'sample_pitch_shifted_audio.wav'
    sf.write(shifted_sample_filename, shifted_audio, SAMPLERATE)
    
    

if __name__ == "__main__":
    main()
