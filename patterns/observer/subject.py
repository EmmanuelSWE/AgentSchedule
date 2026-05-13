# Subject interface 
# author : Emmanuel Ashimwe 
from abc import ABC, abstractmethod 
from observer.absObserver import abstractObserver

class Subject(ABC):

    
    observers: list[abstractObserver]

    @abstractmethod
    def attach(self):
        pass

    
    @abstractmethod
    def detach(self):
        pass

    @abstractmethod
    def notify(self):
        pass