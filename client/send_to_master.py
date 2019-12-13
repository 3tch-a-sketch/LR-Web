import sys

debugSw = True
helpembed = '''
HELP PAGE:
--help          Displays the help page you see here.
-r              Specifies the desired recipient of the communication.
-s              Specifies the desired subject of the communication.
-b              Specifies the body of the communication.
'''

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
