#import librosa
from madmom.audio.signal import Signal
from madmom.features.beats import RNNBeatProcessor, BeatTrackingProcessor
from madmom.features.tempo import TempoEstimationProcessor

#def detectbeat(audio_data, sample_rate):
    #onset_env = librosa.onset.onset_strength(y=audio_data,sr = sample_rate)
    #tempo, beat_frames = librosa.beat.beat_track(y=audio_data, sr=sample_rate)
    #beat_times = librosa.frames_to_time(frames=beat_frames,sr=sample_rate)
    #return tempo, beat_times

def detectbeat2(audio_directory):
    proc = RNNBeatProcessor(fps=100)(audio_directory)
    beats = BeatTrackingProcessor(fps=100)(proc)   
    tempo_processor = TempoEstimationProcessor(fps=100)
    tempi = tempo_processor(proc)
    dominant_tempo = tempi[0, 0]
    tempo_strength = tempi[0, 1]
      
    return beats, dominant_tempo, tempo_strength

