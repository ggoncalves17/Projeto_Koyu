from django.db import models

#Relaçoes
# ------- One-to-Many -------
# class Author(models.Model): 
#  name = models.CharField(max_length=100) 
#  birth_date = models.DateField() 

#class Book(models.Model): 
#  title = models.CharField(max_length=200) 
#  author = models.ForeignKey(Author, on_delete=models.CASCADE) 
#  published_date = models.DateField()

# ------- Many-to-Many ------- 
#class Student(models.Model):
#  name = models.CharField(max_length=100)

#class Course(models.Model):
#  title = models.CharField(max_length=200)
#  students = models.ManyToManyField(Student)

# ------- One-to-One ------- 
#class User(models.Model):
#  username = models.CharField(max_length=100)

#class Profile(models.Model):
#  user = models.OneToOneField(User, on_delete=models.CASCADE)
#  bio = models.TextField()

#https://www.geeksforgeeks.org/django-model-data-types-and-fields-list/


# Create your models here.

class Equipamento(models.Model): 
  eq_nome = models.CharField(max_length=512) 
  eq_foto = models.CharField(max_length=512) 

class Utilizador(models.Model):
  ut_mail = models.CharField(max_length=512)
  ut_nome = models.CharField(max_length=512)
  ut_pass = models.CharField(max_length=512)
  ut_estado = models.IntegerField()
  ut_telefone = models.IntegerField()
  ut_foto = models.CharField(max_length=512)
  ut_tipo = models.CharField(max_length=512)
  ut_nif = models.IntegerField()

class Modalidade(models.Model): 
  ca_nome = models.CharField(max_length=512) 
  ca_foto = models.CharField(max_length=512) 

class PlanoTreinos(models.Model):
  pt_nome = models.CharField(max_length=512)
  pt_foto = models.CharField(max_length=512)
  descricao = models.CharField(max_length=512)
  intensidade = models.CharField(max_length=512)
  duracao = models.IntegerField()
  equipamento = models.BooleanField()
  modalidade = models.ForeignKey(Modalidade, on_delete=models.CASCADE)

class Historico(models.Model):
  hi_data = models.DateField()
  utilizador = models.ForeignKey(Utilizador, on_delete=models.CASCADE)
  planotreinos = models.ForeignKey(PlanoTreinos, on_delete=models.CASCADE) 

class Categoria(models.Model): 
  ca_nome = models.CharField(max_length=512) 
  ca_foto = models.CharField(max_length=512) 
  categoria_planostreino = models.ManyToManyField(PlanoTreinos)

class Exercicios(models.Model):
  ex_nome = models.CharField(max_length=512) 
  ex_descricao = models.CharField(max_length=512) 
  ex_intensidade = models.CharField(max_length=512) 
  ex_foto = models.CharField(max_length=512) 
  ex_video = models.CharField(max_length=512)
  excercicios_categoria = models.ManyToManyField(Categoria)
  equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE) 

class series_planostreino(models.Model):
  sr_series = models.IntegerField()
  sr_repeticoes = models.IntegerField()
  sr_tempo = models.FloatField()
  exercicios = models.ForeignKey(Exercicios, on_delete=models.CASCADE)
  planotreinos = models.ForeignKey(PlanoTreinos, on_delete=models.CASCADE) 