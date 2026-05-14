from enum import Enum
# sub Task enum 
# author : Emmanuel

class SubTaskStatus(Enum): 
    INCOMPLETE : str = "incomplete"
    COMPLETE : str = "complete"
    DISCARDED : str = "discarded"
    RESCHEDULED : str = "rescheduled"
    ON_HOLD : str = "on hold"
