
from core.userState import UserState
from patterns.observer.absObserver import AbstractObserver

class UserFiniteStateMachine(AbstractObserver):
    currentState : UserState

    def update(self, enviroment):
        total = self.countTasks(enviroment)

        enviroment.state.estimateLevels(total)
        print("FSM Noticed the change in enviroment");

    def transition(state: UserState):
        pass

    def updateMetrics():
        pass

    def estimateEmotionalState():
        pass
    
    def countTasks(self, enviroment):
        total = 0
        for daySched in enviroment.schedule.daySchedules.values():
            total += len(daySched.tasks)
        return total
    
    