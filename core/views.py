from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from .models import Tarefa
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

class TelaLogin(LoginView):
    template_name = 'core/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tarefas')
    
class TelaCadastro(FormView):
    template_name = 'core/cadastro.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tarefas')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(TelaCadastro, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tarefas')
        return super(TelaCadastro, self,).get(*args, **kwargs)

class ListaDeTarefas(LoginRequiredMixin, ListView):
    model = Tarefa
    context_object_name = 'tarefas'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tarefas'] = context['tarefas'].filter(usuario=self.request.user)
        context['contagem'] = context['tarefas'].filter(concluida=False).count()
        
        pesquisa = self.request.GET.get('pesquisa') or ''
        if pesquisa:
            context['tarefas'] = context['tarefas'].filter(titulo__startswith=pesquisa)
        
        context['pesquisa'] = pesquisa

        return context

class CriarTarefa(LoginRequiredMixin, CreateView):
    model = Tarefa
    fields = ['titulo', 'descricao', 'concluida']
    success_url = reverse_lazy('tarefas')
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super(CriarTarefa, self).form_valid(form)

class ModificarTarefa(LoginRequiredMixin, UpdateView):
    model = Tarefa
    fields = ['titulo', 'descricao', 'concluida']
    success_url = reverse_lazy('tarefas')

class ExcluirTarefa(LoginRequiredMixin, DeleteView):
    model = Tarefa
    fields = '__all__'
    success_url = reverse_lazy('tarefas')
