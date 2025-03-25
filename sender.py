import socket 

s= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip_add ="192.168.137.87"
port=1228 
complete =(ip_add,port)
message =input("machine learning")
encode_msg=message.encode('ascii')
s.sendto(encode_msg,complete)

