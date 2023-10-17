from django.urls import path
from .views import ListaDeTarefas, CriarTarefa, ModificarTarefa, ExcluirTarefa, TelaLogin, TelaCadastro
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', TelaLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('cadastro/', TelaCadastro.as_view(), name='cadastro'),
    path('', ListaDeTarefas.as_view(), name='tarefas' ),
    path('criar-tarefa', CriarTarefa.as_view(), name='criar-tarefa' ),
    path('modificar-tarefa/<int:pk>/', ModificarTarefa.as_view(), name='modificar-tarefa' ),
    path('excluir-tarefa/<int:pk>/', ExcluirTarefa.as_view(), name='excluir-tarefa' ),
]