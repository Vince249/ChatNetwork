EXIT_CLIENT = "#Exit" #Command used by clients to leave

def Client_Exit (msg):
    print(msg)

def Client_Test (msg):
    print("Bonjour")
options = {
        "#Exit" : Client_Exit,
        "#Hello" : Client_Test
    }
def Check_client_functions(msg_recu):
    commande = msg_recu.split(' ')[0]
    options[commande]("yo")



Check_client_functions("#Exit rezrfazetfazefaez")