#build a message object 
msg = message(text = "see attached!", img='important.png', 
              attachment='data.csv')

send(msg)  # send the email (defaults to outlook)