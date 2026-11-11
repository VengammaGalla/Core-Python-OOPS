class Playlist:
    def __init__(self,l=[]):
        self.l=l
    def valid_songs(self,song):
        if len(song)>4:
            n=len(song)
            return song[n-4:].lower()==".mp3"
        return False
    def __len__(self):
        return len(self.l)
    def __contains__(self,other):
        return other in self.l
p1=Playlist("fear.mp3","sun.mp3")
p2=Playlist()


