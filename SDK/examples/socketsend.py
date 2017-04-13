import socket  
  
address = ('localhost',9999)  
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
s.connect(address)  
  
s.send('type=digital&num=1111')  
data = s.recv(512)  
print 'the data received is',data  
s.close()  
