from django.db import models
from django.core.validators import MinLengthValidator

'''
Id
Nome
E-mail - não pode estar em branco
CPF - Máximo de 11 caractere
Data de Nascimento
Número de celular- Máximo de 14 caracteres
'''
class Estudante(models.Model):
    nome = models.CharField(max_length = 100)
    email = models.EmailField(blank = False, max_length = 30)
    cpf = models.CharField(max_length = 11, unique= True)
    data_nascimento = models.DateField()
    celular = models.CharField(max_length = 14)

    def __str__(self):
        return self.nome
    
'''
Id
Código- Máximo 10 caracteres
Descrição - Não pode estar em branco
Nível- Básico, Intermediário, Avançado - Não pode estar em branco/Não pode ser Nulo/Por padrão deve ser básico
'''

class Curso(models.Model):
    NIVEL = (
        ('B','Básico'),
        ('I','Intermediário'),
        ('A','Avançado'),
    )
    codigo = models.CharField(max_length = 10, unique = True, validators=[MinLengthValidator(3)])
    descricao = models.CharField(blank = False, max_length = 100)
    nivel = models.CharField(max_length = 1, choices = NIVEL, blank = False, null = False, default = 'B')   #choices = escolha

    def __str__(self):
        return self.codigo
    
class Matricula(models.Model):
    PERIODO = (
        ('M', 'Matutino'),
        ('V', 'Vespertino'),
        ('N', 'Noturno'),
    )
    estudante = models.ForeignKey(Estudante, on_delete = models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete = models.CASCADE)
    periodo = models.CharField(max_length = 1, choices = PERIODO, blank = False, null = False, default = 'M') 
