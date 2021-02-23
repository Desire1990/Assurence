from django.db import models
from django.utils import timezone

periodes = (
	(1,'------------------------'),
	('Trois mois', 'Trois mois'),
	('Six mois', 'Six mois'),
	('1 an', '1 an')
)
marque = (
	(1,'------------------------'),
	('Toyota','Toyota'),
	('Volkswagen','Volkswagen'),
	('Volvo','Volvo')
)

modele = (
	(1,'------------------------'),
	('Allion','Allion'),
	('Axio','Axio'),
	('Volkswagen','Volkswagen')
)

puissance = (
	(1,'------------------------'),
	('7cv a 9cv','7cv a 9cv'),
	('8cv a 12cv','8cv a 12cv')
)


PAYMENTS = ( 
	(1, '---------------------'),
	("Ecocash", "Ecocash"), 
	("Lumicash", "Lumicash")
)

type_assurence = (
	(1, '------------------'),
	('Assurence tous risques', 'Assurence tous risques'),
	('Assurence au tiers', 'Assurence au tiers')
)


class Profile(models.Model):
	first_name = models.CharField(max_length = 64)
	last_name = models.CharField(max_length = 64)
	address = models.CharField(max_length=50)
	CNI = models.CharField(max_length=50, unique = True, null=True, blank=True)
	birthdate = models.DateField(null=True, blank=True);
	nationalite = models.CharField(max_length = 30)
	contact_number = models.CharField(max_length = 30, unique = True)
	


	def __str__(self):
		return f" {self.first_name} {self.last_name}"

class Payment(models.Model):
	profile = models.ForeignKey(Profile, null = False, on_delete = models.CASCADE)
	type_payement = models.CharField(choices=PAYMENTS, max_length=50)
	id_transaction = models.CharField(max_length=50, unique=True)
	date = models.DateField(default=timezone.now)		
	
	def __str__(self):
		return f"{self.id_transaction} <=> {self.profile.first_name} {self.profile.last_name}"


class Automobile(models.Model):
	profile = models.ForeignKey(Profile, null = False, on_delete = models.CASCADE)
	plaque = models.CharField(max_length = 10, unique = True)
	marque_vehicule = models.CharField(max_length = 50, choices = marque) # BMW, TOYOTA NISSANI
	modele_vehicule = models.CharField(max_length = 50,   choices = modele) #BMW(SERIE 1 A 8),
	puissance_moteur = models.CharField(max_length = 50,   choices = puissance )
	numero_de_chassis = models.CharField(max_length = 64, unique = True, default = 'WDB20102916014000')
	numero_de_moteur = models.CharField(max_length = 64, unique = True, default = '2FMGK5CC2BBD13558')
	annee_de_fabrication = models.DateField()
	number_seat = models.IntegerField()
	periode = models.CharField(max_length = 30,  choices = periodes)
	type_insurence = models.CharField(max_length = 30, choices=type_assurence)
	photo  = models.ImageField(upload_to = 'Upload/')

	def __str__(self):
		return f"{self.plaque } <=> {self.profile.first_name} {self.profile.last_name}"

