class Mensch:
	""" es behält die Eigentschaften: Name, Vorname,
	Alter und  Adresse"""
	def __init__(self):
		self.nachname="Andjo Foute"
		self.vorname="Junior Pericles"
		self.alter=20
        self._stadt="Brandenburg a.d Havel"
    
    def _get_stadt(self):
        return self._stadt
    
    def _set_stadt(self,neue_stadt):
        print("{} hat zu {} umgezogen".format(\self.vorname,neue_stadt))
        self._stadt=neue_stadt
    
    stadt=property(_get_stadt,_set_stadt)
    
    def __repr__(self):
        return "Vornameame: {},Nachname: {},Alter: {}".format(self.vorname,self.nachname,self.alter) 
