#Task class 
# author : Emmanuel Ashimwe 222127212 

from models.subTask import SubTask
from typing import List
from dataclasses import dataclass,field

@dataclass
class Task: 
    #attributes
    name : str
    basePriority : int 
    dynamicPriority : int 
    subTasks : List[SubTask] = field(default_factory = list); 
