
from patterns.observer.absObserver import AbstractObserver
from core.userState import UserState
from models.task import Task
from enumsProj.actionType import ActionType

class ModelReflexAgent(AbstractObserver):
   # commands : # must get the abstract commnad thing fixed 

    def update(self, enviroment):
        action = self.chooseAction(enviroment.state)

        self.performAction(action,enviroment)
        print(f"MODEL REFLEX chose action: {action.value}");

    def chooseAction(self,state: UserState):
        if state.urgencyVal >= 0.7:
            return ActionType.RESCHDEULE
        if state.cortisol >= 0.5:
            return ActionType.PRIORITIZE
        return ActionType.SCHEDULE

    def performAction(self, action : ActionType, enviroment):
        if action == ActionType.RESCHDEULE:
            self.rescheduleTasks(enviroment)
        elif action == ActionType.PRIORITIZE:
            self.prioritizeTasks(enviroment)
        elif action == ActionType.SCHEDULE:
            self.scheduleTasks(enviroment)

    def rescheduleTask(self,task: Task):
        task.dynamicPriority += 1

    def rescheduleTasks(self,enviroment):
        for dayShced in enviroment.schedule.daySchedules.values():
            for task in dayShced.tasks:
                task.dynamicPriority += 1
        
        self.scheduleTasks(enviroment)

    def scheduleTasks(self,enviroment):
        for dayShced in enviroment.schedule.daySchedules.values():
           dayShced.tasks.sort(
               key = lambda task: task.dynamicPriority,
               reverse = True
           )

    def scheduleTask(self,task: Task):
        pass

    def smartScheduling(self):
        pass

    def suggestOptimalTime(self):
        pass

    def predictFutureState(self):
        pass 

    def storeExperience(self):
        pass

    def prioritizeTasks(self, enviroment):
        for dayShced in enviroment.schedule.daySchedules.values():
            for task in dayShced.tasks:
                task.dynamicPriority = task.basePriority + 1
        
        self.scheduleTasks(enviroment)
