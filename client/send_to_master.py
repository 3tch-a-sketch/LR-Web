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
bodyId = 0
subjectId = 0
recipientId = 0
mail_user = 'lora.w3b@gmail.com'
with open("password.ini", "r") as f:
  password = f.read()
if not password:
    throw("Password not found, make a password.ini file in this directory.")

for i in sys.argv:
    if i == '--help' or i == '-h':
        print(helpembed)
    elif i == '-b':
        bodyId = sys.argv.index(i)+1
    elif i == '-s':
        subjectId = sys.argv.index(i)+1
    elif i == '-r':
        recipientId = sys.argv.index(i)+1

body = sys.argv[bodyId]
subject = sys.argv[subjectId]
recipient = sys.argv[recipientId]

if debugSw == True: # DEBUG: Prints args
    print(recipientId)
    print(recipient)
    print(subjectId)
    print(subject)
    print(bodyId)
    print(body)
    recipient = "sametchells@icloud.com"


email_text = """\
To: %s
Subject: %s

%s
""" % (recipient,subject, body)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(mail_user, password)
    server.sendmail(mail_user, recipient, email_text)
except:
    print('Something went wrong...')
