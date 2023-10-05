import socket
import os

ip = input("IP ADDRESS : ")

chunk = 4096*8  

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((ip,27015))

filesize = client.recv(4)

filesize = int.from_bytes(filesize , byteorder='big')

bytes_received = 0

with open('data_from_server.bin','wb') as file:

    clear = None
    
    if os.name == 'nt':
        clear = 'cls'
    else:
        clear = 'clear'
    
    while True:
        data = client.recv(chunk)
        if not data:
            break
        bytes_received += len(data)
        complete = (bytes_received / filesize) * 100 
        os.system(clear)        
        print(f"Progress : %{complete:.2f}")        
        file.write(data)    


print(f"Total File Size = {(filesize / 1024):.2f}kb")

if os.name == 'nt':
    os.system("pause")
        
client.close()