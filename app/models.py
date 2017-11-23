from django.db import models
from django.contrib.auth.models import User
# Create your models here.
opcoes = (
	('Disponível', 'Disponível'),
	('Reservada', 'Reservada'),
	('Indisponível', 'Indisponível'),
)

blocos = (
	('A', 'A'),
	('B', 'B'),
	('C', 'C'),
	('D', 'D'),
	('E', 'E'),
)

horarios = (
	('1° Horário - Manhã', '1° Horário - Manhã'),
	('2° Horário - Manhã', '2° Horário - Manhã'),
	('3° Horário - Manhã', '4° Horário - Manhã'),
	('4° Horário - Manhã', '4° Horário - Manhã'),
	('5° Horário - Manhã', '5° Horário - Manhã'),
	('6° Horário - Manhã', '6° Horário - Manhã'),

	('1° Horário - Tarde', '1° Horário - Tarde'),
	('2° Horário - Tarde', '2° Horário - Tarde'),
	('3° Horário - Tarde', '4° Horário - Tarde'),
	('4° Horário - Tarde', '4° Horário - Tarde'),
	('5° Horário - Tarde', '5° Horário - Tarde'),
	('6° Horário - Tarde', '6° Horário - Tarde'),

	('1° Horário - Noite', '1° Horário - Noite'),
	('2° Horário - Noite', '2° Horário - Noite'),
	('3° Horário - Noite', '3° Horário - Noite'),
	('4° Horário - Noite', '4° Horário - Noite'),
)
class Sala(models.Model):
	nome = models.CharField(max_length=50)
	numero = models.IntegerField()
	bloco = models.CharField(max_length=1, choices=blocos)
	
	#Manhã
	h1_Matutino = models.CharField(max_length=12, choices=opcoes, default='Disponível',) #07:00 - 07:45
	j1_Matutino = models.CharField(max_length=300, default='-')
	h2_Matutino = models.CharField(max_length=12, choices=opcoes, default='Disponível',) #07:45 - 08:30
	j2_Matutino = models.CharField(max_length=300, default='-')
	h3_Matutino = models.CharField(max_length=12, choices=opcoes, default='Disponível',) #08:50 - 09:35
	j3_Matutino = models.CharField(max_length=300, default='-')
	h4_Matutino = models.CharField(max_length=12, choices=opcoes, default='Disponível',) #09:35 - 10:20
	j4_Matutino = models.CharField(max_length=300, default='-')
	h5_Matutino = models.CharField(max_length=12, choices=opcoes, default='Disponível',) #10:30 - 11:15
	j5_Matutino = models.CharField(max_length=300, default='-')
	h6_Matutino = models.CharField(max_length=12, choices=opcoes, default='Disponível',) #11:15 - 12:00
	j6_Matutino = models.CharField(max_length=300, default='-')
	#Tarde
	h1_Vespertino = models.CharField(max_length=12, choices=opcoes, default='Disponível',) #13:00 - 13:45
	j1_Vespertino = models.CharField(max_length=300, default='-')
	h2_Vespertino = models.CharField(max_length=12, choices=opcoes, default='Disponível',) #13:45 - 14:30
	j2_Vespertino = models.CharField(max_length=300, default='-')
	h3_Vespertino = models.CharField(max_length=12, choices=opcoes, default='Disponível',) #14:50 - 15:35
	j3_Vespertino = models.CharField(max_length=300, default='-')
	h4_Vespertino = models.CharField(max_length=12, choices=opcoes, default='Disponível',) #15:35 - 16:20
	j4_Vespertino = models.CharField(max_length=300, default='-')
	h5_Vespertino = models.CharField(max_length=12, choices=opcoes, default='Disponível',) #16:30 - 17:15
	j5_Vespertino = models.CharField(max_length=300, default='-')
	h6_Vespertino = models.CharField(max_length=12, choices=opcoes, default='Disponível',) #17:15 - 18:00
	j6_Vespertino = models.CharField(max_length=300, default='-')
	#Noite
	h1_Noturno = models.CharField(max_length=12, choices=opcoes, default='Disponível',) #19:00 - 19:45
	j1_Noturno = models.CharField(max_length=300, default='-')
	h2_Noturno = models.CharField(max_length=12, choices=opcoes, default='Disponível',) #19:45 - 20:00
	j2_Noturno = models.CharField(max_length=300, default='-')
	h3_Noturno = models.CharField(max_length=12, choices=opcoes, default='Disponível',) #20:45 - 21:30
	j3_Noturno = models.CharField(max_length=300, default='-')
	h4_Noturno = models.CharField(max_length=12, choices=opcoes, default='Disponível',) #21:30 - 22:15
	j4_Noturno = models.CharField(max_length=300, default='-')
	def __str__(self):
		return self.nome + ' | ' + str(self.numero) + ' | ' + self.bloco

class Material(models.Model):
	nome = models.CharField(max_length=50)
	numero = models.IntegerField()
	localizacao = models.CharField(max_length=50)

	#Manhã
	h1_Matutino = models.CharField(max_length=12, choices=opcoes, default='Disponível',) #07:00 - 07:45
	j1_Matutino = models.CharField(max_length=300, default='-')
	h2_Matutino = models.CharField(max_length=12, choices=opcoes, default='Disponível',) #07:45 - 08:30
	j2_Matutino = models.CharField(max_length=300, default='-')
	h3_Matutino = models.CharField(max_length=12, choices=opcoes, default='Disponível',) #08:50 - 09:35
	j3_Matutino = models.CharField(max_length=300, default='-')
	h4_Matutino = models.CharField(max_length=12, choices=opcoes, default='Disponível',) #09:35 - 10:20
	j4_Matutino = models.CharField(max_length=300, default='-')
	h5_Matutino = models.CharField(max_length=12, choices=opcoes, default='Disponível',) #10:30 - 11:15
	j5_Matutino = models.CharField(max_length=300, default='-')
	h6_Matutino = models.CharField(max_length=12, choices=opcoes, default='Disponível',) #11:15 - 12:00
	j6_Matutino = models.CharField(max_length=300, default='-')
	#Tarde
	h1_Vespertino = models.CharField(max_length=12, choices=opcoes, default='Disponível',) #13:00 - 13:45
	j1_Vespertino = models.CharField(max_length=300, default='-')
	h2_Vespertino = models.CharField(max_length=12, choices=opcoes, default='Disponível',) #13:45 - 14:30
	j2_Vespertino = models.CharField(max_length=300, default='-')
	h3_Vespertino = models.CharField(max_length=12, choices=opcoes, default='Disponível',) #14:50 - 15:35
	j3_Vespertino = models.CharField(max_length=300, default='-')
	h4_Vespertino = models.CharField(max_length=12, choices=opcoes, default='Disponível',) #15:35 - 16:20
	j4_Vespertino = models.CharField(max_length=300, default='-')
	h5_Vespertino = models.CharField(max_length=12, choices=opcoes, default='Disponível',) #16:30 - 17:15
	j5_Vespertino = models.CharField(max_length=300, default='-')
	h6_Vespertino = models.CharField(max_length=12, choices=opcoes, default='Disponível',) #17:15 - 18:00
	j6_Vespertino = models.CharField(max_length=300, default='-')
	#Noite
	h1_Noturno = models.CharField(max_length=12, choices=opcoes, default='Disponível',) #19:00 - 19:45
	j1_Noturno = models.CharField(max_length=300, default='-')
	h2_Noturno = models.CharField(max_length=12, choices=opcoes, default='Disponível',) #19:45 - 20:00
	j2_Noturno = models.CharField(max_length=300, default='-')
	h3_Noturno = models.CharField(max_length=12, choices=opcoes, default='Disponível',) #20:45 - 21:30
	j3_Noturno = models.CharField(max_length=300, default='-')
	h4_Noturno = models.CharField(max_length=12, choices=opcoes, default='Disponível',) #21:30 - 22:15
	j4_Noturno = models.CharField(max_length=300, default='-')


	def __str__(self):
		return self.nome + ' | ' + str(self.numero) + ' | ' + self.localizacao

class ReservarSala(models.Model):
	usuario = models.ForeignKey(User)
	sala = models.ForeignKey(Sala, null = True)
	dataHora_Atual = models.DateTimeField()
	horario_de_Entrada = models.CharField(max_length=18, choices=horarios, default='1° Horário - Manhã',)
	horario_de_Saida = models.CharField(max_length=18, choices=horarios, default='2° Horário - Manhã',)
	justificativa = models.TextField()

	def __str__(self):
		return str(self.sala) + ' | ' + self.justificativa
	
class ReservarMaterial(models.Model):
	usuario = models.ForeignKey(User)
	material = models.ForeignKey(Material, null = True)
	dataHora_Atual = models.DateTimeField()
	horario_de_Entrada = models.CharField(max_length=18, choices=horarios, default='1° Horário - Manhã')
	horario_de_Saida = models.CharField(max_length=18, choices=horarios, default='2° Horário - Manhã')
	justificativa = models.TextField()

	def __str__(self):
		return self.material + ' | ' + self.justificativa