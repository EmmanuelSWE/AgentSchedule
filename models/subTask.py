 # SubTask Class
 # author  : Emmanuel Ashimwe
 
from enums.subTaskStatus import SubTaskStatus 
from enums.subTaskPriority import SubTaskPriority
from dataclasses import dataclass


@dataclass
class SubTask:
    name : str
    priority : SubTaskPriority
    status : SubTaskStatus

         
   
        
    
    