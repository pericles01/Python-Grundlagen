schach={}
schach['a',1]="weisser Turm"
schach['b',1]="weisser Reiter"
schach['d',1]="weisse Koenigin"
schach['e',1]="weisser Koenig"
print(schach)
schrank={"weisses Hemd":2,"schwarzes Hemd":4,"sweatshirt":5}
print(schrank)
for cle in schrank.keys():
    print(cle)
for wert in schrank.values():
    print(wert)
for cle,wert in schrank.items():
    print("key {} behält den Wert {}".format(cle,wert)) 
