# task controller class 
# author : Emmanuel Ashimwe 
from patterns.controller import abstractController
from models.task import Task
from models.daySchedule import DaySchedule
from models.schedule import Schedule

class TaskController(abstractController):
   
    def handleInput(self,val : int):
        pass

   
    def addTask(self):
        pass

   
    def removeTask(self):
        pass

   
    def updateTask(self):
        pass

   
    def showTasks(self):
        pass

   
    def showStatus(self):
        pass

   
    def addUrgent(self):
        pass

   
    def prioritizeTask(self):
        pass

   
    def delayTask(self):
        pass