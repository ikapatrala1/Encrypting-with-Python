
class SimpleCA:
    
    #The public keys will be store in a key-value pair fashion, where key is servername, and value is publickey
    # The key-value pair will be stored in a txt file in the "key=value" format
    def storePublicKey(self,key,value):
        f= open("dict.txt","a+")
        f.write(key+'='+value+"\n")
        f.close()

    #This method will return the public key associated to the servername.Basically, it reads the file where
    # the key-value are stored and get the matching value for that key.
    def getPublicKey(self,serverName):
        #Open the file back and read the contents
        d = {}
        with open("dict.txt") as f:
            for line in f:
                (key, val) = line.split("=")
                d[key] = val
        return d.get(serverName)        
            
  