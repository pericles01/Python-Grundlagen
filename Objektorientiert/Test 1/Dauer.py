class Dauer:
	def __init__(self,min=0, sec=0):
		self.min=min
		self.sec=sec
	
	def __str__(self):
		return "{0:02}:{1:02}".format(self.min,self.sec)
		
	def __getattr__(self, x):
		print("Achtung!! {} exestiert nicht".format(x))
        
    def __add__(self,a):
        neueDauer=Dauer()
        neueDauer.min=self.min
        neueDauer.sec=self.sec
        neueDauer.sec+=a
        if neueDauer.sec>=60:
            neueDauer.min+=neueDauer.sec//60
            neueDauer.sec=neueDauer.sec%60
        
        return neueDauer
    
    def __radd__(self,b):
        return self+b
     
    