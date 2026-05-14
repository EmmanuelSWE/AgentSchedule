 # SubTask Class
 # author  : Emmanuel Ashimwe
 
from enumsProj.subTaskStatus import SubTaskStatus 
from enumsProj.subTaskPriority import SubTaskPriority
from dataclasses import dataclass,field


@dataclass
class SubTask:
    name : str
    priority : SubTaskPriority
    status : SubTaskStatus

         
   
        
    
    