
from patterns.observer.absObserver import AbstractObserver
from core.userState import UserState
from models.task import Task

class ModelReflexAgent(AbstractObserver):
    commands # must get the abstract commnad thing fixed 

    def update(self):
        pass

    def chooseAction(state: UserState):
        pass

    def rescheduleTask(task: Task):
        pass

    def scheduleTask(task: Task):
        pass

    def smartScheduling():
        pass

    def suggestOptimalTime():
        pass

    def predictFutureState():
        pass 

    def storeExperience():
        pass
