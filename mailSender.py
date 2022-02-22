import smtplib
import threading
# from time import sleep
import random

subjs=["Get Fked","Get rekt"]               #add more subjects for more damage!
sender=["Christ","Jesus","Akbar","Birbal"]   #add more sender names
sender_email="" #replace with sender email address
sender_passwd = ""  #replace with sender password

#or read from file
bodys=["Tosser  Supreme Asshole or jerk.", "Wanker  Idiot", "Slag  Whore  the worst kind", "Cheese Eating Surrender Monkeys  The French", "Lost the plot  Gone crazy or completely stupid.", "Daft Cow  Dumb, large woman", "Arsehole  Asshole", "Barmy  Stupid or crazy.", "Chav  White Trash / Low Class", "Dodgy  Shady character", "Git  Moron, Idiot", "Gormless  Complete lack of common sense", "Manky  Disgusting", "Minger  Very unattractive woman", "Muppet  Dimwit (not the puppet variety)", "Naff  Tacky", "Nutter  Someone’s who’s clearly crazy", "Pikey  White trash  also used to slight Gypsies or Irish Travellers", "Pillock  Idiot", "Plonker  Idiot", "Prat  Idiot, asshole", "Scrubber  A nicer way to say slag", "Trollop  A lady of questionable morals", "Uphill Gardener  Another way of saying homosexual", "Twit  Idiot", "Knob Head  Dickhead", "Piss Off  Go Away", "Bell End  Dick Head (bell end also means penis)", "Lazy Sod  Useless idiot", "Skiver  Lazy sod", "Knob  Dick", "Wazzock  Someone so dumb they can only do manual labor (from Yorkshire)", "Ninny  Brilliant but inferior", "Berk  Idiot", "Airy-fairy  Not strong, weak.", "Ankle-biters  Children", "Arse-licker  A sycophant", "Arsemonger  A person that generate contempt.", "Chuffer  An annoying perfusion", "Daft as a bush  Silly, Crazy", "Dead from the neck up  Stupid.", "Gannet  Greedy person.", "Gone to the dogs  rotten, deteriorated", "Ligger  freeloader", "Like a dog with two dicks  Man whore", "Mad as a bag of ferrets  Crazy", "Maggot  A despicable person", "Mingebag  A bad person, an asshole who might be cheap.", "Not batting on a full wicket  Eccentric person a little crazy or odd.", "Plug-Ugly  Very Ugly person", ]

def sendMails():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_passwd)
    for i in range(10):
        ind=random.randint(0,len(bodys)-1)
        bos=bodys[ind].replace(", ","  ").split("  ")
        message=f"From:{random.choice(sender)} <from@{random.choice(sender)}_{random.choice(sender)}.com>\n" \
                f"To: {bos[0]} <yesYou.com>\n" \
                f"Subject: {bos[0]} {random.choice(subjs)}\n\n" \
                f"Your are an/a {' '.join(bos)}"
        server.sendmail(sender_email, ['reciever1@gmail.com','reciever2@gmail.com'], message)
        print("Mail Sent!!!")

    # server.sendmail()

threads=[]

for i in range(50):
    t=threading.Thread(target=sendMails)
    t.daemon=True
    threads.append(t)
for t in threads:
    t.start()
for t in threads:
    t.join()

#by RoyalReaper
