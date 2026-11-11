from abc import ABC, abstractmethod
import os

class MediaFile(ABC):
    def __init__(self, path):
        self.__path = path
        if not path:
            raise ValueError("File path cannot be empty")

    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class MP3File(MediaFile):
    def play(self):
        print("Playing MP3")

    def stop(self):
        print("Stopping MP3")


class MP4File(MediaFile):
    def play(self):
        print("Playing MP4 video")

    def stop(self):
        print("Stopping MP4")


class WAVFile(MediaFile):
    def play(self):
        print("Playing WAV audio")

    def stop(self):
        print("Stopping WAV")


# Duck typing: no inheritance requirement
def start_player(media):
    media.play()


class CustomPlayer:
    def play(self):
        print("Playing custom media")


start_player(MP3File("song.mp3"))
start_player(MP4File("video.mp4"))
start_player(CustomPlayer())