'''
• Server function (command line):
1) #Help (list command)
#! 2) #Exit (server shutdown)
3) #Kill <user>
4) #ListU (list of users in a server)
5) #ListF (list of files in a server)
6) # Private <user> (private chat with another user)
7) #Alert <all users>
'''
# Import sockets libraries
import socket

#Import display libraries
from datetime import datetime


#! Commandes serveur
EXIT_SERVER = "#Exit" #Command used by server to shutdown
HELP_SERVER = "#Help" #Command used by server to get help
KILL_SERVER = "#Kill" #Command used by server to kill user terminal

def Server_Exit(input_server, clients_connectes,connexion_principale):
    if(input_server == EXIT_SERVER):
        #use ALERT function to alert users that the server will close
        print("Server closing...")
        for client in clients_connectes:
            client.socket.send(b"Closing")
            client.socket.close()
        connexion_principale.close()
        return "exit"

    else :
        raise Exception

def Server_Kill(input_server, clients_connectes,connexion_principale):
    if(len(input_server.split(' ')) == 2): #on peut se permettre de verifier s'il n'y a que deux termes car le username ne peut pas contenir d'espace (regle qu'on a fixée)
        for client in clients_connectes:
            if (client.username == input_server.split(' ')[1]):
                client.socket.send(b"Closing")
                client.socket.close()
                clients_connectes.remove(client)
                print("User {} was kicked by server at {} from @{}:{}".format(client.username, datetime.now(), client.IP, client.port))
            else:
                msg = "User {} was kicked by server".format(input_server.split(' ')[1])
                client.socket.send(msg.encode())
    else :
        raise Exception



options = {
        EXIT_SERVER : Server_Exit,
        KILL_SERVER : Server_Kill,
        #HELP_SERVER : Server_Help
    }

def Check_server_functions(input_server, clients_connectes,connexion_principale):
    commande = input_server.split(' ')[0]

    try:
        return options[commande](input_server, clients_connectes,connexion_principale)
    except :
        msg = "Command not found, try using #Help"
        print(msg)