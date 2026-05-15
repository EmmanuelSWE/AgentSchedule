# Abstract observer interface 
# Author Emmanuel Ashimwe 


from abc import ABC, abstractmethod 

class AbstractObserver(ABC):

    @abstractmethod
    def update(self, environment): # updates itself
        pass
