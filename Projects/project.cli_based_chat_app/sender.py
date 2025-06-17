import socket
try:
    #creating socket
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  #AF_INET -- address family 
    #dgram ---datagram which is used to use udp protocol++++++++++++++++++++.
    print("socket created")
    ip_add = "172.16.3.13"
    port =  8888                                               ## it ranges from 0 to 65535
    target_add = (ip_add,port)
    message = input("Enter the  message : " )
    encoded_msg = message.encode("ascii")
    s.sendto(encoded_msg,target_add)
    print("message sent successfully")
    s.close()

except Exception as e:
    print("an error occured")
