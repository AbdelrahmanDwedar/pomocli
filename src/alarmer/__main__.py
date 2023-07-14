import playsound


class Alarmer:
    
    @staticmethod
    def playsound():
        playsound.playsound('../../assets/alarm.wav', block=True)


Alarmer.playsound()