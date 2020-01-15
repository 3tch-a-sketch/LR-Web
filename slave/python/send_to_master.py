#!/usr/bin/env python
import sys
import smtplib

debugSw = False
helpembed = '''
HELP PAGE:
--help          Displays the help page you see here.
-r              Specifies the desired recipient of the communication.
-s              Specifies the desired subject of the communication.
-b              Specifies the body of the communication.
'''

mail_user = 'lora.w3b@gmail.com'

with open("password.ini", "r") as f:
  password = f.read()
if not password:
    print("Password not found, make a password.ini file in this directory")

try:
    for i in range(len(sys.argv)):
        currentArg = sys.argv[i]
        if currentArg == '--help' or currentArg == '-h':
            print(helpembed)
        elif currentArg == '-b':
            body = sys.argv[i+1]
        elif currentArg == '-s':
            subject = sys.argv[i+1]
        elif currentArg == '-r':
            recipient = sys.argv[i+1]
except IndexError:
    print('arg provided but contents not found')

if debugSw == True: # DEBUG: Prints args and changes to test email format
    print("recipient:", recipient)
    print("body:", body)
    print("subject:", subject)
    recipient = "15samueletchells@catmosecollege.com"
    body = "test email."
    subject = "TEST"

email_text = "To: %s\nSubject: %s\n\n%s" % (recipient, subject, body)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(mail_user, password)
    server.sendmail(mail_user, recipient, email_text)
    print("Emails send complete.")
except:
    print('Something went wrong...')
