class Forme:
	def __init__(self):
		self.couleur = ""
	def changer_couleur(self, c):
		self.couleur = c

class Carre(Forme):
	def __init__(self):
		Forme.__init__(self)
		self.x1 = 0
		self.x2 = 0
		self.y1 = 0
		self.y2 = 0
	def deplacer(self, dx, dy):
		self.x1 += dx
		self.x2 += dx
		self.y1 += dy
		self.y2 += dy

class Cercle(Forme):
	def __init__(self):
		Forme.__init__(self)
		self.x = 0
		self.y = 0
		self.rayon = 0
	def deplacer(self, dx, dy):
		self.x += dx
		self.y += dy

carre = Carre()
cercle = Cercle()
carre.deplacer(1,2)
cercle.deplacer(3,4)
