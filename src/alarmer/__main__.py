from pydub import AudioSegment
from pydub.playback import play

class Alarmer:

    @staticmethod
    def playsound():
        sound = AudioSegment.from_wav("../../assets/alarm.wav")
        play(sound)


Alarmer.playsound()
