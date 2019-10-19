import socket               # Import socket module

from CA import SimpleCA
from AESCipher import AESCipher

serverName = "Server1"
publickey="mysecretpassword"

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 9500                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
SimpleCA().storePublicKey(serverName,publickey)


s.listen(10)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   print('Got connection from', addr)
   inputData=c.recv(2000)
   data = inputData.decode()
   print(data)
   if(data=="init"):
       #sending the server name during initial call
       c.sendto(serverName.encode(),(host, port))
   elif(data=="goodbye"):
       invalidKey="GoodBye, Not a valid message"
       c.sendto(invalidKey.encode(),(host, port))
   else:
       #Decrypting the message and appending the "acknowledged" to the received message
       cipher = AESCipher(SimpleCA().getPublicKey(serverName))
       decrypted = cipher.decrypt(data)
       acknowledgeMessage = decrypted.decode()+" acknowledged"
       c.sendto(acknowledgeMessage.encode(),(host, port))
       
   c.close()                # Close the connection