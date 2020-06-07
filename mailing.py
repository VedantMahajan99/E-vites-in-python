
import smtplib
from email.message import EmailMessage
import imghdr
from game import *

for gamer in attending_game_night:

    with smtplib.SMTP('smtp.gmail.com' , 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        str = form_email.format(name=gamer, day_of_week = game_night, game = "Poker")

        msg = EmailMessage()
        msg['Subject'] = 'E-vite for the game'
        msg['From'] = 'themahajan99@gmail.com'
        msg['To'] = gamer
        msg.set_content(str)

        with open('/Users/vedantmahajan/Desktop/poker.jpeg' , 'rb') as f:
            file_data = f.read()
            file_type = imghdr.what(f.name)
            file_name = f.name

        msg.add_attachment(file_data, maintype = 'image' , subtype = file_type , filename = file_name)
        
        # use password instead of ****
        smtp.login('themahajan99@gmail.com' , '**********')

        smtp.send_message(msg)
