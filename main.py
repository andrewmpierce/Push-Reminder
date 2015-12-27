import smtplib
import os
import requests


gmail_pass = os.environ["GMAILPASS"]
number = os.environ["TEST_NUMBER"]

server = smtplib.SMTP( "smtp.gmail.com", 587 )

server.starttls()
server.login( 'pushreminderapp@gmail.com', gmail_pass )

server.sendmail( 'Skynet', number+'@vtext.com', 'This is an automated message from Push Reminder' )
