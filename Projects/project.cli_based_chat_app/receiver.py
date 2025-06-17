import socket
try:
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    print("socket created")
    #sender ke andr receiver ka hi ip address aayega
    #humehsa pr receiver ke andr khudka hi ip address aayega
    ip_add = "172.16.1.226"
    port = 8888
    complete_add = (ip_add,port)
    s.bind(complete_add)

    while True:
        message , sender_address = s.recvfrom(1024)

        print("Raw message" , message) 
        print("sender_address",sender_address)

        decoded_msg = message.decode("ascii")
        print("message",decoded_msg)

except Exception as e:                           
    print("an error occured ", e)