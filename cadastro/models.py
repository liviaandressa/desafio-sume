from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



class Contas(models.Model):

    TIPO_CONTA = (('poupança','poupança'),('corrente','corrente'))
    TIPO_BANCO = (('banco 1', 'banco 1'), ('banco 2', 'banco 2'), ('banco 3', 'banco 3'), ('banco 4', 'banco 4'))
    id_conta = models.AutoField(primary_key=True) 
    tp_conta = models.CharField(max_length=30, choices=TIPO_CONTA, default='poupança')
    id_banco = models.IntegerField()
    banco = models.CharField(max_length=50, choices=TIPO_BANCO, default='banco 1')
    conta = models.IntegerField()
    agencia = models.IntegerField()
    operacao = models.IntegerField()

    class Meta:
        db_table = 'Contas'
        verbose_name_plural = 'Contas'

    def __str__(self):

        return str(self.conta) + '/'+ str(self.agencia)


class Ufs(models.Model):

    id_uf = models.AutoField(primary_key=True) 
    nome_uf = models.CharField(max_length=30)
    sigla_uf = models.CharField(max_length=2)

    class Meta:

        db_table = 'Ufs'
        verbose_name_plural = 'Ufs'

    def __str__(self):
        return self.nome_uf


class Cidades(models.Model):

    id_cidade = models.AutoField(primary_key=True)  
    id_uf = models.ForeignKey(Ufs, on_delete=models.CASCADE)   
    nome_cidade = models.CharField(max_length=50)


    class Meta:
        db_table = 'Cidades'
        verbose_name_plural = 'Cidades'

    def __str__(self) :
        return self.nome_cidade + '-' + self.id_uf.sigla_uf


class Enderecos(models.Model):

    id_enderecos = models.AutoField(primary_key=True)  
    id_cidade = models.ForeignKey(Cidades, on_delete=models.CASCADE)
    logradouro = models.CharField(max_length=150)
    numero = models.CharField(max_length=8)
    cep = models.CharField(max_length=10)
    bairro = models.CharField(max_length=80)   
    complemento = models.CharField(max_length=60, blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True)
    
    class Meta:
        db_table = 'Enderecos'
        verbose_name_plural = 'Endereços'

    def __str__(self) :
        return self.logradouro + '-' + self.numero



class Pessoas(models.Model):

    TIPO_VINCULO = (('vinculo 1', 'vinculo 1'), ('vinculo 2', 'vinculo 2'))
    id_pessoa = models.AutoField(primary_key=True) 
    nome = models.CharField(max_length=200)
    vinculo = models.CharField(max_length=20, choices=TIPO_VINCULO, default='vinculo 1')
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)  
    id_endereco = models.ForeignKey(Enderecos, on_delete=models.CASCADE) 
    id_conta = models.ForeignKey(Contas, on_delete=models.CASCADE) 
    telefone = models.CharField(max_length=16)
    email = models.EmailField()
    cpf = models.IntegerField()

    class Meta:
        db_table = 'Pessoas'
        verbose_name_plural = 'Pessoas'

    def __str__(self):
        return self.nome


class Ocorrencias(models.Model):
    
    id_ocorrencia = models.AutoField(primary_key=True) #chave primária
    id_pessoa = models.ForeignKey(Pessoas, on_delete=models.CASCADE)
    data = models.DateField()
    realizada = models.BooleanField(default=True)
    ocorrencia = models.TextField(max_length=100000)

    class Meta:
        db_table = 'Ocorrencias'
        verbose_name_plural = 'Ocorrências'

    def __str__(self) :
        return self.id_ocorrencia + '-' + self.data