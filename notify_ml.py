import notify 

START = datetime.now() #this line wuld be placed before model training begins
MODELNAME = "Synthwave GAN" # giving us our model name 
NOTIFY = 100 # so we send an update notification every 100 epochs

#for each epoch e, we would include the following code 
if e % notify_epoch == 0 and e != 0:
    #here we create the email body message 
    txt = (f"{MODELNAME} update as of  "
           f"{datetime.now().strftime('%H:%M:%S')}.")

# we build the MIME message object with notify. message 
msg = notify.message(
    subject='Syanthwave GAN',
    text=txt,
    img=[
        f'../visuals/{MODELNAME}/epoch_{e}_loss.png',
        f'../visuals/{ MODELNAME}/epoch_{e}_iter_{i}.png'
    ]

) #note that we attach two images here, the loss plot and 
# ..... a generated image output from our model

notify.send(msg) #we then send the message