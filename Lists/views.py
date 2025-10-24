from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Cases
from .forms import CaseForm

class ListsView(ListView):
    template_name = "lists/lists.html"
    model = Cases

class Detail(DetailView):
    template_name = "lists/detail.html"
    model = Cases

class CaseCreate(CreateView):
    template_name = "lists/create/case_create.html"
    form_class = CaseForm
    success_url = reverse_lazy("lists")

class Update(UpdateView):
    template_name = "lists/update.html"
    model = Cases
    form_class = CaseForm
    success_url = reverse_lazy("lists")

class Delete(DeleteView):
    template_name = "lists/delete.html"
    model = Cases
    success_url = reverse_lazy('lists')