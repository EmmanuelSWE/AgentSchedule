# user Interface python file 
# author : Emmanuel Ashimwe 

from ui.taskController import TaskController

class userInterface:
    controller : TaskController

    def handleinput(self,input : int):
        self.controller.handleInput(input)

    def displayOptions(self):
        pass
