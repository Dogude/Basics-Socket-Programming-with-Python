import socket
import os

path = input("FILE PATH : ")

chunk = 4096*8  

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('',27015))

server.listen(5)

client_socket , client_address = server.accept()

print(f"starting with {client_address}...")

file_size = os.path.getsize(path)
client_socket.sendall(file_size.to_bytes(4,byteorder='big'))


with open(path,'rb') as file:
    
    while True:
        data = file.read(chunk)
        if not data:
            break
        client_socket.sendall(data)    
        
print('DONE!')    
client_socket.close()
    


        

  