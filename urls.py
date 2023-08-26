from django.urls import path
from propostas.views import listar_propostas, criar_proposta

urlpatterns = [
    path('propostas/', listar_propostas, name='listar_propostas'),
    path('propostas/nova/', criar_proposta, name='criar_proposta'),
]from django.urls import path
from propostas.views import listar_propostas, criar_proposta

urlpatterns = [
    path('propostas/', listar_propostas, name='listar_propostas'),
    path('propostas/nova/', criar_proposta, name='criar_proposta'),
]