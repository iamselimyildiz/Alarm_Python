import datetime
from playsound import playsound

alarm_hour=int(input('Saat giriniz :'))
alarm_min=int(input('Dakika giriniz :'))


while True:
    if alarm_hour == datetime.datetime.now().hour and alarm_min == datetime.datetime.now().minute:
        print('Playing...')
        playsound('avatar.mp3')
        break