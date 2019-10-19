import socket               # Import socket module
from CA import SimpleCA
from AESCipher import AESCipher


s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 9500                # Reserve a port for your service.



s.connect((host, port))
#Getting the initial connection with the server
inputString = "init"
s.send(inputString.encode())

#The server name is received from the server
serverName = s.recv(1024).decode()

#Using the server name obtain the public key of the server from the Certificate Authority implementation class i.e SimpleCA

publicKey = SimpleCA().getPublicKey(serverName)

#To get a invalid key message
#publicKey = SimpleCA().getPublicKey("hello")


s.close()                     # Close the socket when done

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 9500                # Reserve a port for your service.
s.connect((host, port))

#Encrypt the message using the public key received from the SimpleCA
if publicKey == None:
    message = "goodbye"
    s.send(message.encode())
    invalidKeyMessage = s.recv(1024).decode()
    print(invalidKeyMessage)
    
else:
    cipher = AESCipher(publicKey)
    messageTxt = 'session cipher key'
    encrypted = cipher.encrypt(messageTxt)

    #send the encrypted message to the server
    s.send(encrypted)

    #server respond with the acknowldegment by appending "acknowledged" to the message we sent.

    acknowledgmentMessage = s.recv(1024).decode()

    print(acknowledgmentMessage)

s.close()                     # Close the socket when done


