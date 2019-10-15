#Pomodoro Application
'''Requires playsound module inorder to play the music. To install --- "pip install playsound". '''

#Module to play audio files
from playsound import playsound
import time

duration = int(input('Enter Duration for your Pomodoro{in minutes}: '))


print(time.asctime())
print('Pomodoro Started. Focus....')
for i in range(10):
    playsound('Tick-Tock.mp3')
    #Giving 0.8 as argument works best for sleeping for 1second
    time.sleep(0.8)

print('Pomodoro Completed!')
playsound('Alarm.mp3')



