from abc import ABC, abstractmethod

class MediaPlayer(ABC):

    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class MP3Player(MediaPlayer):

    def load(self):
        print("Loading MP3")

    def play(self):
        print("Playing MP3")

    def stop(self):
        print("Stopping MP3")

class WAVPlayer(MediaPlayer):

    def load(self):
        print("Loading WAV")

    def play(self):
        print("Playing WAV")

    def stop(self):
        print("Stopping WAV")

class AACPlayer(MediaPlayer):

    def load(self):
        print("Loading AAC")

    def play(self):
        print("Playing AAC")

    def stop(self):
        print("Stopping AAC")

players = [MP3Player(), WAVPlayer(), AACPlayer()]

for player in players:
    player.load()
    player.play()
    player.stop()
    print()