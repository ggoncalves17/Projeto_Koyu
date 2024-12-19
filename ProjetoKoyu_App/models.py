from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class Equipamento(models.Model): 
  eq_nome = models.CharField(max_length=512) 
  eq_foto = models.CharField(max_length=512) 

class UtilizadorManager(BaseUserManager):
  def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("O email é obrigatório!")
        user = self.model(ut_mail=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

  def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class Utilizador(AbstractBaseUser):
  ut_mail = models.EmailField(unique=True)
  ut_nome = models.CharField(max_length=512)
  password = models.CharField(max_length=512)
  ut_estado = models.IntegerField()
  ut_telefone = models.IntegerField()
  ut_foto = models.CharField(max_length=512)
  ut_tipo = models.CharField(max_length=512)
  ut_nif = models.IntegerField()

  objects = UtilizadorManager()

  USERNAME_FIELD='ut_mail'

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