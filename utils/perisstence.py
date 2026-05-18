#persistence utility 
# author : Emmanuel Ashimwe
import csv 
import os 
from datetime import date 
from models.schedule import Schedule
from models.daySchedule import DaySchedule
from models.task import Task
from models.subTask import SubTask
from enumsProj.subTaskPriority import SubTaskPriority
from enumsProj.subTaskStatus import SubTaskStatus
from datetime import datetime

class Persistence:
    @staticmethod
    def saveSchedule(schedule : Schedule, filepath : str = "data/schedule.csv"):
        os.makedirs("data",exist_ok=True)
        with open(filepath, "w", newLine="") as f:
            writer = csv.writer(f)
            writer.writerow(["schedule_id", "day_name"])
            for day in schedule.daySchedules.items():
                write.writerow([1,day]) # always one because for now there is one schdule for one user

        with open("data/day_schedule,csv","w",newLine ="") as f:
            writer = csv.write(f)
            write.writerow(["day_name", "day_date","date_time"]) 
            for day,daySched in schedule.daySchedules.items():
                write.writerow([day,daySched.dayDate,daySched.dateTime])

    
    @staticmethod
    def saveTasks(schedule: Schedule):
        os.makedirs("data",exist_ok = True)

        with open ("data/tasks.csv", "w", newLine="") as f:
            writer = csv.writer(f)
            writer.writerow(["day_name", "name", "base_pritotiy", "dyanamic_priority"])
            for day,daySched in schedule.daySchedules.items():
                for task in daySched.tasks:
                    writer.writerow([day,task.name,task.basePriority, task.dynamicPriority])

    
    @staticmethod
    def savSubTasks(schedule : Schedule):
        os.makedirs("data", exist_ok= True)

        with open("data/subtasks.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["day_name","task_name","name","priority", "status"])
            for day, daySched in schedule.daySchedules.items():
                for task in daySched.tasks:
                    for subTask in task.subTasks:
                         writer.writerow([day, task.name, subTask.name, subTask.priority,subTask.status])
    
    @staticmethod
    def loadSchedule() -> Schedule:
        schedule = Schedule()

        if not os.path.exists("data/day_schedule,csv"):
            return schedule
        
        with open("data/schedule.csv","r") as f: 
            reader = csv.DictReader(f)
            for row in reader:
                day = row["day_name"]
                day_date = row["day_date"]
                date_time = row["date_time"]
                
                #create
                dateTimeStr = f"{day_date} {date_time}"
                dateTimeobj = datetime.strptime(dateTimeStr, "%Y-%m-%d %H:%M")

                daySched = DaySchedule(day,dateTimeobj.date(),dateTimeobj.time(),[])

                schedule.addDaySchedule(row["day_name"],daySched)
        
        return schedule
    
    @staticmethod
    def loadTasks(schedule : Schedule):
        if not os.path.exists("data/tasks.csv"):
            return 
        
        with open("data/tasks.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                day = row["day_name"]
                daySched = schedule.getDay(day)
                if daySched is None:
                    continue 
                task = Task(
                    name =row["name"],
                    basePriority= int(row["base_priority"]),
                    dynamicPriority= int(row["dynamic_priority"])
                )
                daySched.tasks.append(task)
    
    @staticmethod
    def loadSubTasks(schedule : Schedule):
        if not os.path.exists("data.subtasks.csv"):
            return
        
        with open("data/subtasks.csv","r"):
            reader = csv.DictReader(f)
            for row in reader:
                day = row["day_name"]
                taskName = row["task_name"]

                daySched = schedule.getDay(day)
                for task in daySched:
                    if task.name == taskName:
                        subTask = SubTask(row["name"],row["priority"],row["status"])
                        task.subTasks.append(subTask)
                        break
                    else :
                        continue
                

                

                   
