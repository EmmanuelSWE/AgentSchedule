# user Interface python file 
# author : Emmanuel Ashimwe 

from ui.taskController import TaskController

class userInterface:
    controller : TaskController
    blnContinue = True

    def handleinput(self,input : int):
        if(input == 1):
            print('adding task')
        elif(input == 2):
            print("2. seeing tasks")
        elif(input == 3):
            print('exiting')
            self.blnContinue = False
        else:
            print("wrong input retry")

    def displayOptions(self):
        pass

    def showMenu(self):
        os.system("cls")
        print("hello this is the menu")
        print("here is the selection of choices")
        print("1. input task")
        print("2. see tasks")
        print("3. exit")

    
    def run(self):
        while(blnContinue):
            self.showMenu()
            self.handleinput(int(input))
        

