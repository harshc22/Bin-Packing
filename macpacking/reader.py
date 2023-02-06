from abc import ABC, abstractmethod
from os import path
from random import shuffle, seed
from . import WeightSet, WeightStream


class DatasetReader(ABC):

    def offline(self) -> WeightSet:
        '''Return a WeightSet to support an offline algorithm'''
        (capacity, weights) = self._load_data_from_disk()
        seed(42)          # always produce the same shuffled result
        shuffle(weights)  # side effect shuffling
        return (capacity, weights)

    def online(self) -> WeightStream:
        '''Return a WeighStream, to support an online algorithm'''
        (capacity, weights) = self.offline()

        def iterator():  # Wrapping the contents into an iterator
            for w in weights:
                yield w  # yields the current value and moves to the next one

        return (capacity, iterator())

    @abstractmethod
    def _load_data_from_disk(self) -> WeightSet:
        '''Method that read the data from disk, depending on the file format'''
        pass


class BinppReader(DatasetReader):
    '''Read problem description according to the BinPP format'''

    def __init__(self, filename: str) -> None:
        if not path.exists(filename):
            raise ValueError(f'Unkown file [{filename}]')
        self.__filename = filename

    def _load_data_from_disk(self) -> WeightSet:
        with open(self.__filename, 'r') as reader:
            nb_objects: int = int(reader.readline())
            capacity: int = int(reader.readline())
            weights = []
            for _ in range(nb_objects):
                weights.append(int(reader.readline()))

            return (capacity, weights)

class JburkardtReader(DatasetReader):
    '''Read problem description according to the Jburkardt format'''

    def __init__(self, file_capacity: str, file_weights:str) -> None:
        if not path.exists(file_capacity):
            raise ValueError(f'Unknown file [{file_capacity}]')

        if not path.exists(file_weights):
            raise ValueError(f'Unknown file [{file_weights}]')
        self.__file_capacity = file_capacity
        self.__file_weights = file_weights

    def _load_data_from_disk(self) -> WeightSet:
        with open(self.__file_capacity, 'r') as reader:
            capacity: int = int(reader.readline())
            reader.close()
        
        with open(self.__file_weights,'r') as reader:
            nb_objects = reader.readlines()
            weights=[]
            
            for _ in range (len(nb_objects)-1):
                    num=nb_objects[_].replace(" ","")
                    weights.append(int(num.strip()))

        return (capacity,weights)