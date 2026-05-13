#enviroment class 
# author : Emmanuel Ashimwe 222127212 
from models.schedule import  Schedule 
from core.userState import UserState
from patterns.observer.absObserver import AbstractObserver
from patterns.observer.subject import Subject

class Enviroment(Subject):

    observers: list[AbstractObserver]
    schedule : Schedule
    state : UserState

    


