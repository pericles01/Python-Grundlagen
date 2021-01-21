from daten import*
from funktion import*

record=rekordabholen()
spieler=nameabholen()

if spieler not in record.keys():
	record[spieler]=0
	
fortsetzen='j'

while fortsetzen!='n':
	print("Spieler {0}: {1} Punkte".format(spieler,record[spieler]))
	zufinden=wortauswahl()
	lt=[]
	mt=versteckt(zufinden,lt)
	nb=bewegung
	while zufinden !=mt and nb>0:
        print("Das zufindende Wort {0} (noch {1} Möglichkeiten").format(mt,nb))
        lettre=wortabholen()
        if lettre in lt:
            print("Sie haben schon dieses Wort ausgewaehlt")
        elif lettre in zufinden:
            lt.append(lettre)
            print("Gut gemacht")
        else:
            nb-=1
            print("Es gibt dieses Wort nicht in dem gesamten Wort")
        mt=versteckt(zufinden,lt)
        
     if zufinden==mt:
        print("Glückwunsch!! Sie haben das Wort gefunden {0}".format(zufinden))
     else:
        print("Sie haben verloren")
        
    record[spieler]+=nb
    
    fortsetzen=input("Wollen Sie fortsetzen?(J/N)")
    fortsetzen=fortsetzen.lower()
    
speichern(record)
    
print("Sie sind mit {0} Punkten fertig".format(record[spieler]))
    

