

class UserState: 

    def __init__(self): # the intitial user state before anythinng
        self.cortisol = 0.0
        self.dopamine = 0.0
        self.norepinephrine = 0.0
        self.urgencyVal = 0.0
        self.completionVal = 0.0
        self.neglectionVal = 0.0

    def estimateLevels(self, totalTasks): # the estimation play around with it to improve it
        self.urgencyVal = min(1.0, totalTasks * 0.15)
        self.cortisol = min(1.0, totalTasks * 0.10)
        self.dopamine = max( 0.1, 1.0 - self.cortisol)
        self.norepinephrine = min(1.0, 0.4 + self.urgencyVal)
        self.completionVal = max( 0.0, 1.0 - self.urgencyVal)
        self.neglectionVal = min(1.0, totalTasks * 0.05)



