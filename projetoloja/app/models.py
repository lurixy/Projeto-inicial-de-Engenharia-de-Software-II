from django.db import models

class UF(models.Model):
    sigla = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "UF"

    def __str__(self):
        return self.sigla

class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    uf = models.ForeignKey(UF, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Cidades"

    def __str__(self):
        return self.nome

class Cargo(models.Model):
    nome = models.CharField(max_length=100)
    

    class Meta:
        verbose_name_plural = "Cargos"

    def __str__(self):
        return self.nome

class Bairro(models.Model):
    nome = models.CharField(max_length=100)
    

    class Meta:
        verbose_name_plural = "Bairros"

    def __str__(self):
        return self.nome

class Status(models.Model):
    nome = models.CharField(max_length=100)
    

    class Meta:
        verbose_name_plural = "Status"

    def __str__(self):
        return self.nome

class TipoLogradouro(models.Model):
    nome = models.CharField(max_length=100)
    

    class Meta:
        verbose_name_plural = "TipoLogradouros"

    def __str__(self):
        return self.nome


class Logradouro(models.Model):
    nome = models.CharField(max_length=100)
    numero = models.CharField(max_length=100)
    complemento = models.CharField(max_length=100)
    tipo = models.ForeignKey(TipoLogradouro, on_delete=models.CASCADE)
    bairro = models.ForeignKey(Bairro, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Logradouros"

    def __str__(self):
        return self.nome



        
class Tipo(models.Model):
    nome = models.CharField(max_length=100)
    

    class Meta:
        verbose_name_plural = "Tipos"

    def __str__(self):
        return self.nome

class Imovel(models.Model):
    nome = models.CharField(max_length=100)
    tipoimovel = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=100)
    area_contruida = models.CharField(max_length=100)
    numero_comodos = models.CharField(max_length=100)
    cor = models.CharField(max_length=100)
    vagas_caragem = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    tipolog = models.ForeignKey(TipoLogradouro, on_delete=models.CASCADE)
    logradouro = models.ForeignKey(Logradouro, on_delete=models.CASCADE)
    bairro = models.ForeignKey(Bairro, on_delete=models.CASCADE)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    uf = models.ForeignKey(UF, on_delete=models.CASCADE)
    cep = models.CharField(max_length=100)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Imoveis"

    def __str__(self):
        return self.nome


class Categoria(models.Model):
    nome = models.CharField(max_length=100)
   
    class Meta:
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.nome
   
    
    


class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    cpf =  models.CharField(max_length=100)
    rg = models.CharField(max_length=100)
    data_nasc = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    cat = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    

    class Meta:
        verbose_name_plural = "Pessoas"

    def __str__(self):
        return self.nome


        



