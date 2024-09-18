
# This is a python mini project on Countdown timer

'''
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''

#created by: Anish M
#modified date:18-09-2024
#modified time:06:50 PM

''' this a simple demonstration of COUNTDOWN TIMER created on python 3 . in this code the user inputs seconds .and the console will output the time lap in reverse order

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''



import time

#This line of code import the date mod 

def countdown_timer(t):
    
    #the above code defines the countdown timer
    
    while t:
        #the above code is to tell that this is a contineous loop 
        
        mins, sec = divmod(t, 60)
        #this line of code defines the countdown timer

        
        timer = '{:02d}:{:02d}'.format(mins, sec)
        #This code is to print the timer in the console 
        
        print(timer)

        
        time.sleep(1)
        #count method
        
        t -= 1
    print("Times Up!")
    

if __name__ == "__main__":
    
    try:
        
        t = int(input("Enter the time in seconds:"))
        
        countdown_timer(t)
        
    except ValueError:
        
        print("Invalid Input!")
