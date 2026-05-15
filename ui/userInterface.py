# user Interface python file 
# author : Emmanuel Ashimwe 

from ui.taskController import TaskController
import os 
class userInterface:
    controller : TaskController = TaskController()
    blnContinue = True

    def handleinput(self,input : int):
        os.system("cls")
        if(input == 6):
            self.blnContinue = False
            print("shutting down good bye")
        else:
            self.controller.handleInput(input)

        

    def displayOptions(self):
        pass

    def showMenu(self):
        
        print("hello this is the menu")
        print("here is the selection of choices")
        print("1. input task")
        print("2. remove Task")
        print("3. update Task")
        print("4. show Tasks")
        print("5. show Statusk")
        print("6. Exit")
    

    
    def run(self):
        while(self.blnContinue):
            self.showMenu()
            userInput = int(input("input choice"))
            self.handleinput(userInput)
           
        

