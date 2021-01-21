
print("Dieses Programm sagt ob es um ein Schaltjahr geht oder nicht")
jahr=input("geben sie ein Jahr ein: ")
jahr=int(jahr)
print("Sie haben ",jahr," eingegeben")
if jahr%400==0 or (jahr%4==0 and jahr%100!=0):
    print("Das Jahr ",jahr," ist ein Schaltjahr")
else:
    print("Das Jahr ",jahr," ist kein Schaltjahr")
