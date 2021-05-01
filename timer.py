from time import sleep, strftime
import datetime

print("Welcome to the Timex v1.0")

class Pomodoro():

    #Class Variables
    normal_timming = 0
    break_timming = 0

    def __init__(self, normal_timming=1500,break_timming=300,rounds=4):#1500 secs == 25min for pomodoro & 300secs == 5min Break
        self.normal_timming = normal_timming
        self.break_timming = break_timming
        self.rounds = rounds
       

        
    def standard_config_time(self):
        response_usr = str(input("Do you want to start? Y/N ")).upper()
        self.rounds = int(input("How many rounds? **Default 4 "))
        if response_usr == "Y":
            self.countdown() #Calling function to start the countdown      
  
    def countdown(self):
    
        while self.normal_timming:
            sleep(0.01)
            self.normal_timming -= 5
            print(datetime.timedelta(seconds=self.normal_timming), end="\r")
            
        while self.break_timming:
            sleep(0.01)
            self.break_timming-=5
            print(datetime.timedelta(seconds=self.break_timming), end="\r")
            
d = Pomodoro()
d.standard_config_time()








