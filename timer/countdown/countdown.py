import time

def countdown_timer(seconds):
    paused = False 
    while seconds > 0:
        if not paused:
            mins = seconds // 60 #sec to min
            secs = seconds % 60 #min to sec
            timer = '{:02d}:{:02d}.format(mins, secs)'
            print(timer,end="\r")
            time.sleep(1) # rest for 1 sec b4 countdown
            seconds -= 1
        else:
            time.sleep(0.5) #sleep for short time
# Asking for user's input like pause, resume or stop
        info_for_user = input("You can type pause, resume or stop")
        if info_for_user == 'Pause' or "pause":
            paused = True
            print("You've just paused.")
        elif info_for_user == 'Resume' or "resume":
            paused = True
            print("You've just resumed.")
        elif info_for_user == 'Stop' or "stop":
            paused = True
            print("You've just stopped.")
            break
            print("Blast off!")

def is_input_available():
    import sys
    import select
    return select.select([sys.stdin], [], [], 0.0)[0]
# Get user's input for how long they want to do their task
try:
    subject = input("What subject do you want to study today? ").strip()
    t = input(f"How long fo you want to do {subject} for? ")
    t = int(t)
    if t < 0:
        raise ValueError("Time must be in seconds and positive integer!")
    countdown_timer(t)
except ValueError as wrong:
    print(f"Invalid input: {wrong}")