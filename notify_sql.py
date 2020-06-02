import os 
import notify 
from data import Sql 

dt = Sql('database123', 'server001') #setup the connection to SQL Server

for i, file in enumerate(os.listdir('../data/new')):
    dt.push_raw(f'../data/new/{file}') #push a file to SQL Server

    #once the upload is complete send a notification 
    # first we create the message 
    msg = notify.message(
        subject='SQL Data Upload',
        text=f'Data upload complete, {i} files uplaoded.',
    )

    # send the message 
    notify.send(msg)

    #If errors are occasionally thrown, we could also add a try-except clause to catch the error