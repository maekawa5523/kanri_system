from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Cases, Products, Customers, Contractors
from .forms import CaseForm, ProductForm, CustomerForm, ContractorForm

class ListsView(ListView):
    template_name = "lists/lists.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "リスト"
        return context
    model = Customers

class CustomerListsView(ListView):
    template_name = "lists/customer_lists.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "顧客情報"
        return context
    model = Customers

class ContractorListsView(ListView):
    template_name = "lists/contractor_lists.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "外注先情報"
        return context
    model = Contractors

class Detail(DetailView):
    template_name = "lists/detail.html"
    model = Cases

class CaseCreate(CreateView):
    template_name = "lists/case_form.html"
    form_class = CaseForm
    success_url = reverse_lazy("lists")

class CustomerCreate(CreateView):
    template_name = "lists/customer_form.html"
    form_class = CustomerForm
    success_url = reverse_lazy("customer_lists")

class ContractorCreate(CreateView):
    template_name = "lists/contractor_form.html"
    form_class = ContractorForm
    success_url = reverse_lazy("contractor_lists")

class ProductCreate(CreateView):
    template_name = "lists/product_form.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "詳細追加"
        context["case"] = Cases.objects.get(pk=self.kwargs['pk'])
        return context
    title = "詳細追加"
    # case = Cases.objects.get(id=1)
    form_class = ProductForm
    success_url = reverse_lazy("lists")

class CaseUpdate(UpdateView):
    template_name = "lists/case_form.html"
    model = Cases
    form_class = CaseForm
    success_url = reverse_lazy("lists")

class CaseUpdate(UpdateView):
    template_name = "lists/case_form.html"
    model = Cases
    form_class = CaseForm
    success_url = reverse_lazy("lists")

class ProductUpdate(UpdateView):
    template_name = "lists/product_form.html"
    model = Products
    form_class = ProductForm
    success_url = reverse_lazy("lists")

class CustomerUpdate(UpdateView):
    template_name = "lists/customer_form.html"
    model = Customers
    form_class = CustomerForm
    success_url = reverse_lazy("customer_lists")

class ContractorUpdate(UpdateView):
    template_name = "lists/contractor_form.html"
    model = Contractors
    form_class = ContractorForm
    success_url = reverse_lazy("contractor_lists")

class Delete(DeleteView):
    template_name = "lists/delete.html"
    model = Cases
    success_url = reverse_lazy('lists')