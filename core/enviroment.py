#enviroment class 
# author : Emmanuel Ashimwe 222127212 
from datetime import date

from models.schedule import  Schedule 
from core.userState import UserState
from patterns.observer.absObserver import AbstractObserver
from patterns.observer.subject import Subject
from core.userFSM import UserFiniteStateMachine
from core.modelReflexAgent import ModelReflexAgent
from models.task import Task
from enumsProj.actionType import ActionType
from utils.taskFinder import TaskFinder
from models.daySchedule import DaySchedule

class Enviroment(Subject):


   

    def __init__(self):
        super().__init__()
        # making my observers 
        self.schedule = Schedule()
        self.state = UserState()
        self.lastEvent = None
        FSM = UserFiniteStateMachine()
        taskAgent = ModelReflexAgent()
        # attach them
        self.attach(FSM)
        self.attach(taskAgent)
        self.lastAgentAction = None
    
    def attach(self, observer : AbstractObserver):
        return self.observers.append(observer)
    
    def detach(self, observer : AbstractObserver):
        if observer in self.observers:
            self.observers.remove(observer)
    
    def notify(self):
        for observer in self.observers:
            observer.update(self)
    
    def addTask( self, day : str, task: Task):
        self.createDayIfMissing(day)
        daySched = self.schedule.getDay(day)

        daySched.tasks.append(task)

        self.lastEvent = "ADD_TASK"
        self.notify()

    def removeTask(self,day : str,index : int):
        removedTask = TaskFinder.removeTaskByIndex(self.schedule,day,index)

        if removedTask is None:
            print("invalid task selected")
            return
        
        self.lastEvent = "REMOVE_TASK"
        self.notify()

    def addUrgentTask(self, day : str, task : Task):
        daySched = self.schedule.getDay(day)

        daySched.tasks.append(task)

        self.lastEvent = "ADD_URGENT"
        self.notify()

    def updateTask(self, day : str, index : int, task : Task):
        updatedTask = TaskFinder.updateTaskByIndex(self.schedule,day,index,task)

        if updatedTask is None:
            print("Invalid task Selected")
            return 
        
        self.lastEvent = "UPDATE_TASK"
        self.notify()

    def getTasksForDay(self, day : str):
        return TaskFinder.getTasksForDay(self.schedule, day)
    

    # helpers 
    def createDayIfMissing(self,day : str):
        if self.schedule.getDay(day) is None:
            daySched = DaySchedule(
                name = day,
                dayDate= date.today(),
                dateTime=(0,0),
                tasks=[]
            )
        
            self.schedule.addDaySchedule(day,daySched)