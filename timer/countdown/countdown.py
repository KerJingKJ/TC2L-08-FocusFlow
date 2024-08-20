import time

t = int(input("How long do you want to set the the timer for? "))

#decrease 1 sec till hit 0 sec 
while t:
    mins = t // 60 #this is to convert sec to min
    secs = t % 60 # baki
    timer = '{:02d}:{:02d}'.format(mins, secs) # 2 width digit value
    print(timer, end="\r") #pronounce the timer
    time.sleep(1) #sleep for 1 sec b4 countsdown
    t -= 1 # when almost finish
print("Blast off!")