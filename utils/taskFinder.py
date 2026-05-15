#task finder utils class 
# author : Emmanuel Ashimwe

from models.schedule import Schedule
from models.task import Task

class TaskFinder:

    @staticmethod
    def getDaySchedule(schedule: Schedule, key : str):
        if key in schedule.daySchedules:
            return schedule.daySchedules[key]
        return None
    
    @staticmethod
    def getTasksForDay(schedule: Schedule, key : str):
        day = TaskFinder.getDaySchedule(schedule,key)
        if day is None:
            return []       
        return day.tasks
    
    @staticmethod
    def getTaskByIndex(schedule: Schedule, key : str, index : int):
        tasks = TaskFinder.getTasksForDay(schedule,key)
        if 0<= index < len(tasks):
            return tasks[index]
        return None
    
    @staticmethod
    def removeTaskByIndex(schedule: Schedule, key : str, index : int):
        tasks = TaskFinder.getTasksForDay(schedule,key)
        if 0<= index < len(tasks):
             return tasks.pop(index)
        return None

    @staticmethod
    def addTaskByKey(schedule: Schedule, key : str, task : Task):
        tasks = TaskFinder.getTasksForDay(schedule,key)
        tasks.append(task)
    
    @staticmethod
    def updateTaskByIndex(schedule: Schedule, key : str, index : int, task : Task):
        tasks = TaskFinder.getTasksForDay(schedule,key)
        if 0<= index < len(tasks):
             tasks[index] = task
             return task 
        return None
    
    
    
        


    