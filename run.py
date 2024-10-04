from os import path 
from app.audio_tools import detectbeats
from app.utils import file_utils

SAMPLERATE = 44100

def main():
    file_path_song = path.expanduser("~/Desktop/Song & Sample/Devil In a New Dress/Devil In A New Dress.mp3")
    file_path_sample= path.expanduser("~/Desktop/Song & Sample/Devil In a New Dress/Will You Love Me Tomorrow.mp3")
    if path.exists(file_path_song):
        print("File found.")
    else:
        print("File not found. Check the path.")    
    
    #audio_data1, audio_data2 = file_utils.loadSongs(file_path_song,file_path_sample,SAMPLERATE)
    beatsSong, dominant_tempo_song, tempo_strength_song = detectbeats.detectbeat2(file_path_song)
    beatsSample, dominant_tempo_sample, tempo_strength_sample= detectbeats.detectbeat2(file_path_sample)
    
    print("Song Tempo: ", dominant_tempo_song, " Tempo Stength: ", tempo_strength_song )
    print("Sample Tempo: ", dominant_tempo_sample, " Tempo Stength: ", tempo_strength_sample)

if __name__ == "__main__":
    main()
