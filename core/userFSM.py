
from core.userState import UserState
from patterns.observer.absObserver import AbstractObserver

class UserFiniteStateMachine(AbstractObserver):
    currentState : UserState

    def update():
        pass

    def transition(state: userState):
        pass

    def updateMetrics():
        pass

    def estimateEmotionalState():
        pass
    
    