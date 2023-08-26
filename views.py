from django.shortcuts import render, redirect
from .models import Proposta

def listar_propostas(request):
    propostas = Proposta.objects.all()
    return render(request, 'propostas/listar_propostas.html', {'propostas': propostas})

def criar_proposta(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        cpf = request.POST['cpf']
        valor_solicitado = request.POST['valor_solicitado']
        proposta = Proposta(nome=nome, cpf=cpf, valor_solicitado=valor_solicitado)
        proposta.save()
        return redirect('listar_propostas')
    return render(request, 'propostas/criar_proposta.html')
