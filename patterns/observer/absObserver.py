# Abstract observer interface 
# Author Emmanuel Ashimwe 

from abc import ABC, abstractmethod 

class AbstractObserver(ABC):

    @abstractmethod
    def update(): # updates itself
        pass
