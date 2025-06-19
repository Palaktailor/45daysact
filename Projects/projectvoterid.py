voted_emails = set()

def vote(email):
    if email in voted_emails:
         return f" you have already voted{email}"
    else:
        voted_emails.add(email)
        return f"vote recorded successfully  : {email}"
    
while True:
    email= input("enter you mail: (ot type 'exit')")
    if email.lower()  == "exit":
      break
    print(vote(email))

print("\n voters who have voted ")

for i in voted_emails:
    print(i)