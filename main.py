from django.db import models

class Proposta(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    valor_solicitado = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('pendente', 'Pendente'), ('aprovada', 'Aprovada'), ('negada', 'Negada')], default='pendente')
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome