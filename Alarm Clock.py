import time
import pyttsx3

standard_time = "00:00:00"
name = input("Please Enter Your Name : ")
current_time_now = time.strftime("%H:%M:%S")
print("Current Time : " , current_time_now)
input_ = input("Enter the Alarm Time (HH:MM:SS) : ")
current_time = time.strftime("%H:%M:%S")
#hours for current time
a = (int(current_time[0] + current_time[1]) - int(standard_time[0] + standard_time[1]))*3600
#minutes for current time
b = ((int(current_time[3] + current_time[4]) - int(standard_time[3] + standard_time[4])))*60
#seconds for current time
c = (int(current_time[6] + current_time[7]) - int(standard_time[6] + standard_time[7]))

#hours for alarm time
d = (int(input_[0] + input_[1]) - int(standard_time[0] + standard_time[1]))*3600
#minutes for alarm time
e = ((int(input_[3] + input_[4]) - int(standard_time[3] + standard_time[4])))*60
#seconds for alarm time
f = (int(input_[6] + input_[7]) - int(standard_time[6] + standard_time[7]))

current_time_in_sec = a+b+c
alarm_in_sec = d+e+f
print(alarm_in_sec-current_time_in_sec)
time.sleep(alarm_in_sec - current_time_in_sec)
print("ALARM REMINDER !!!!!!!!".center(100))
time_current = time.strftime("%H:%M:%S")

engine = pyttsx3.init("sapi5") #Windows default Voices Present
voices = engine.getProperty("voices")
engine.setProperty("voive",voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak(f"Hi {name} , It's Your Reminder for {time_current} , if you want to snooze , type snooze , if you want to exit type done .")
i = 1
while True:
    user_answer = input("What's Your Command : ")
    if user_answer == "snooze":
        current_time = time.time()
        future_time = current_time+300
        current_time_in_sec= time.ctime(future_time)
        time_only = current_time_in_sec[11:19]
        speak(f"OK , will meet you in 5 minutes at {time_only}")
        time.sleep(295)
        print("ALARM REMINDER !!!!!!!!".center(100))
        time_current = time.strftime("%H:%M:%S")
        speak(f"Hi {name} , This is snooze number {i} and this is your Reminder for {time_current} , if you want to snooze again , type snooze , if you want to exit type done")
        i += 1
        continue


    elif user_answer == "done":
        speak("Thanks For Using the Alarm Clock")
        break

    else:
        speak("Invalid Command")
        break


input("Press Enter To EXIT")