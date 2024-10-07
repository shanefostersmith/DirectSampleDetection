import librosa
from pydub import AudioSegment
import os

def convert_to_wav(file_mp3, file_wav):
    audio = AudioSegment.from_file(file_mp3)
    audio.export(file_wav, format="wav")
    return file_wav

def loadSongs(file_path_song,file_path_sample,samplerate):
    file_path_song_wav = os.path.expanduser("~/Desktop/Song & Sample/converted_audio_song.wav")
    file_path_sample_wav = os.path.expanduser("~/Desktop/Song & Sample/converted_audio_sample.wav")
    song_wav = convert_to_wav(file_path_song,file_path_song_wav)
    sample_wav = convert_to_wav(file_path_sample,file_path_sample_wav)
    
    audio_data1,sample_rate1 = librosa.load(song_wav, sr=samplerate)
    audio_data2,sample_rate2 = librosa.load(sample_wav, sr=samplerate)
    
    if (len(audio_data1) == 0):
        print("Audio data empty")
    return audio_data1, audio_data2, song_wav, sample_wav

