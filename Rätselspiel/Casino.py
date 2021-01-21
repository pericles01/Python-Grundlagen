print("Wie im Kasino sollen wir Ihr Geld auf eine bestimmte Zahl zwischen 0 und 50 wetten")
print("Das Programm erzeugt diese Zahl zufällig")
a=input("wie viel Geld wollen Sie wetten?: ")
a=int(a)
print("Sie haben ",a," EUR gewettet")
b=input("Auf welche Zahl wollen Sie wetten?: ")
b=int(b)
print("Sie wetten auf die Zahl ",b)
from random import*
from math import*
c=randrange(51)
print("Die generierte Zahl ist: ",c)
if b==c:
    print("Glückwunsch Sie haben richtig gewetten")
    print("Ihr Gewinn hat sich verdreifacht: ",a*3)

elif b%2==0 &c%2==0:
    print(c," und ",b," sind beide gerade Zahle, dann erhalten Sie die Hälfte Ihre Wette(aufgerundet): ",ceil(a/2)," Eur")
if b%2==1 & c%2==1:
    print(c," und ",b," sind beide ungerade Zahle, dann erhalten Sie die Hälfte Ihre Wette(aufgerundet): ",ceil(a/2)," Eur")
else:
    print("Tut mir Leid Sie haben keine Chance gehabt, dann verlieren Sie Ihr Geld")
    
