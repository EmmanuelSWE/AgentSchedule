# task controller class 
# author : Emmanuel Ashimwe 
from patterns.controller.abstractController import abstractController
from models.task import Task
from models.daySchedule import DaySchedule
from models.schedule import Schedule
from core.enviroment import Enviroment
from utils.taskFinder import TaskFinder

class TaskController(abstractController):

    def __init__(self):
        super().__init__()
        self.enviroment = Enviroment()
   
    def handleInput(self,val : int):
        if val == 1:
            self.addTask()
        elif val ==2:
            self.removeTask()
        elif val ==3:
            self.updateTask()
        elif val ==4:
            self.showTasks()
        elif val ==5:
            self.showStatus()
        else:
            print("Invalid Option")

   

    def addTask(self):
        day = input("Enter day")
        name = input("Enter task")
        basePriority= int(input("Enter base priority: "))

        task = Task(
            name = name,
            basePriority= basePriority,
            dynamicPriority= basePriority
        )

        self.enviroment.addTask(day,task)

   
    def removeTask(self):
        day, task = self.selectTaskFromDay()

        if task is None:
            return 
        
        index = int(input("Enter task num: ")) -1 
        self.enviroment.removeTask(day,index)
    


   
    def updateTask(self):
        day, oldTask = self.selectTaskFromDay()

        if oldTask is None:
            return 

        index = int(input("Enter Task to update"))-1

      
        name = input("Enter new task")
        basePriority= int(input("Enter new base priority: "))

        task = Task(
            name = name,
            basePriority= basePriority,
            dynamicPriority= basePriority
        )
        self.enviroment.updateTask(day,index,task)

   
    def showTasks(self):
        self.showTasksForDay()

   
    def showStatus(self):
        print(f"last event: {self.enviroment.lastEvent}")
        print(f"days in schedule: {len(self.enviroment.schedule.daySchedules)}")
        print(f"cortisol: {self.enviroment.state.cortisol}")
        print(f"dopamine: {self.enviroment.state.dopamine}")
        print(f"norepinephrine: {self.enviroment.state.norepinephrine}")
        print(f"urgencyVal: {self.enviroment.state.urgencyVal}")
        print(f"completionVal: {self.enviroment.state.completionVal}")
        print(f"neglectionVal: {self.enviroment.state.neglectionVal}")

   
    def addUrgent(self):
        pass

   
    def prioritizeTask(self):
        pass

   
    def delayTask(self):
        pass


    # HELPERS for class 
    def showTasksForDay(self):
        day = input("Enter Day: ")

        tasks = TaskFinder.getTasksForDay(
            self.enviroment.schedule,
            day
        )

        if len(tasks) == 0:
            print("NO tasks found for this day")
            return

        for index, task in enumerate(tasks, start = 1):
            print(f"{index}. {task.name} | Priority: {task.dynamicPriority}")
        
    def selectTaskFromDay(self):
        day = input("Enter Day: ")

        tasks = TaskFinder.getTasksForDay(
            self.enviroment.schedule,
            day
        )

        if len(tasks) == 0:
            print("NO tasks found for this day")
            return None, None

        for index, task in enumerate(tasks, start = 1):
            print(f"{index}. {task.name} | Priority: {task.dynamicPriority}")
        
        index = int(input("choose task number: ")) -1
        task = TaskFinder.getTaskByIndex(self.enviroment.schedule, day, index)

        if task is None:
            print(" Invalid task selected")
            return None, None
        
        return day,task
