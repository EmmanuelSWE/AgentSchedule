# Subject interface 
# author : Emmanuel Ashimwe 
from abc import ABC, abstractmethod 


class Subject(ABC):

    
    def __init__(self):
        self.observers = []

    @abstractmethod
    def attach(self, observer ):
        pass

    
    @abstractmethod
    def detach(self, observer ):
        pass

    @abstractmethod
    def notify(self):
        pass