from abc import ABC, abstractmethod

class MusicMix:
    def play_music(self):
        print('I Bealive '
              'I Can Fly')

class Transport(ABC):
    @abstractmethod
    def ride_on_earth(self):
        pass

    @abstractmethod
    def rude_on_water(self):
        pass

class Car(Transport):
    def ride_on_earth(self):
        print('Едем по земле')

class Boat(Transport):
    def rude_on_water(self):
        print('Ходим по воде')

class Amphibian(Car, Boat, MusicMix):
    pass

amph = Amphibian()
amph.ride_on_earth()
amph.play_music()
amph.rude_on_water()