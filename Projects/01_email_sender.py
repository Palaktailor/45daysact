import smtplib   # simple mail transfer protocol
try:
    server = smtplib.SMTP("smtp.gmail.com",port = 587)  #internet protocol address
    server.starttls()

    ##receiver mail
    receiver_mail = input("Enter your mail:")
    ##mail credentials
    sender_email = "palaktailor07@gmail.com"
    password = "bfya mutn omcq iwmv"
 
   #login
    server.login(sender_email,password)

    ##sending email
    subject = input("Enter the subject :")
    body = input("Enter the body :")
    message = f"subject:{subject} \n\n {body}"
    server.sendmail(sender_email,receiver_mail,message)
    print("mail send successfully")
    server.quit()
except Exception as e:
    print("an error occured",e)