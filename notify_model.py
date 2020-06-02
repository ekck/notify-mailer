end = datetime.datetime.now() #get the ending datetime

# get the total runtime in hours:minutes:seconds 
hours, rem = divmod((end - start).seconds, 3600)
mins, secs = divmod(rem, 60)
runtime = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)

# now built our message 
notify.msg(
    subject="Cashflow Model Completion",
    text=(f'{len(model.output)}loans processed.\n'
          f'Total runtime: {runtime}'),
    img=[
        '../vis/loan01_amortisation.png',
        '../vis/loan07_amortisation.png',
        '../vis/loan01_profit_and_loss.png',
        '../vis/loan07_profit_and_loss.png'
    ]
)

notify.send(msg) #and send it 