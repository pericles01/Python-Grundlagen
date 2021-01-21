import os
import pickle
from random import choice
from daten import*
def rekordabholen():
	if os.path.exists(file):
		fscore=open(file,"rb")
		mdepickler=pickle.Unpickler(fscore)
		record=depickler.load()
		fscore.close
		else:
	record={}
	return record

def speichern(record):
	fscore=open(file,"wb")
	mpickler=pickle.Pickler(fscore)
	mpickler.dump(record)
	fscore.close()
def nameabholen():
    mspieler=input("Geben sie ihren Name ein: ")
    mspieler=mspieler.capitalize()
    
def wortabholen():
    wort=input("Geben Sie ein Wort ein: ")
    wort=wort.lower()
    if len(wort)>1 or not wort.isalpha():
        print("Sie haben ein falsches Wort eingegeben")
        return wortabholen()
    else:
        return wort
        
def wortauswahl():
    return choice(woerter)

def versteckt(ganzeswort, gefunden):
    versteckt=""
    for lettre in ganzeswort:
        if lettre in gefunden:
            versteckt+=lettre
        else:
            versteckt+="*"
    return versteckt
	
	