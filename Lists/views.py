from django.urls import reverse_lazy
from .models import Cases, Products, Customers, Contractors, Prices, Gaityus
from .forms import CaseForm, ProductForm, CustomerForm, ContractorForm, PriceForm, GaityuForm
from django.forms import modelformset_factory
from django.shortcuts import render, redirect

# View
def ListsView(request):
    context = {
        "title": "リスト",
        "object_list": Customers.objects.all(),
    }
    return render(request, 'lists/lists.html', context)

def CustomerListsView(request):
    context = {
        "title": "顧客情報",
        "object_list": Customers.objects.all(),
    }
    return render(request, 'lists/customer_lists.html', context)

def ContractorListsView(request):
    context = {
        "title": "外注先",
        "object_list": Contractors.objects.all(),
    }
    return render(request, 'lists/Contractor_lists.html', context)

# Create
def CaseCreate(request):
    if request.method == "POST":
        object = Cases.objects.create(
            mitsumori_request_date = request.POST['mitsumori_request_date'],
            customer = Customers.objects.get(id=request.POST['customer']),
            deadline = request.POST['deadline'],
            drawing_data = request.POST['drawing_data'],
        )
        object.save()
        return redirect('lists')
    else:
        context = {
            'title': "依頼追加",
            'form': CaseForm,
        }
        return render(request, 'lists/case_form.html', context)

def CustomerCreate(request):
    if request.method == "POST":
        object = Customers.objects.create(
            name = request.POST['name'],
            address = request.POST['address'],
            tanto = request.POST['tanto'],
            mail = request.POST['mail'],
            tel = request.POST['tel'],
            phone = request.POST['phone'],
        )
        object.save()
        return redirect('customer_lists')
    else:
        context = {
            'title': "顧客追加",
            'form': CustomerForm,
        }
        return render(request, 'lists/customer_form.html', context)

def ContractorCreate(request):
    if request.method == "POST":
        object = Contractors.objects.create(
            name = request.POST['name'],
            address = request.POST['address'],
            tanto = request.POST['tanto'],
            mail = request.POST['mail'],
            tel = request.POST['tel'],
            phone = request.POST['phone'],
        )
        object.save()
        return redirect('contractor_lists')
    else:
        context = {
            'title': "外注先追加",
            'form': ContractorForm,
        }
        return render(request, 'lists/contractor_form.html', context)

def ProductCreate(request, case_id):
    if request.method == "POST":
        object = Products.objects.create(
            case = Cases.objects.get(id=request.POST['case']),
            name = request.POST['name'],
            drawing_num = request.POST['drawing_num'],
            material = request.POST['material'],
            surface = request.POST['surface'],
            volume = request.POST['volume'],
        )
        object.save()
        return redirect('lists')
    else:
        context = {
            'title': '製品追加',
            'form': ProductForm,
            'case': Cases.objects.get(id=case_id),
            'page': "CREATE"
        }
        return render(request, 'lists/product_form.html', context)

def PriceCreate(request, case_id, gaityu_id):
    case = Cases.objects.get(id=case_id)
    FormSet = modelformset_factory(
        model = Prices,
        form = PriceForm,
        extra=case.products.count(),
    )
    if request.method == "POST":
        # object = Prices.objects.create(
        #     product = Products.objects.get(id=request.POST['product']),
        #     gaityu = Gaityus.objects.get(id=request.POST['gaityu']),
        #     price = request.POST['price'],
        # )
        # object.save()
        formset = FormSet(request.POST) 
        formset.save()
        return redirect('lists')
    else:
        formset = FormSet()
        context = {
            'title': '単価追加',
            'formset': formset,
            'gaityu': Gaityus.objects.get(id=gaityu_id),
            'gaityu_id': gaityu_id,
            'products': case.products.all(),
        }
        return render(request, 'lists/price_form.html', context)

def GaityuCreate(request, case_id):
    if request.method == "POST":
        object = Gaityus.objects.create(
            case = Cases.objects.get(id=request.POST['case']),
            contractor = Contractors.objects.get(id=request.POST['contractor']),
        )
        object.save()
        return redirect('lists')
    else:
        context = {
            'title': '外注先追加',
            'form': GaityuForm,
            'case': Cases.objects.get(id=case_id),
        }
        return render(request, 'lists/gaityu_form.html', context)

# Update
def CaseUpdate(request, case_id):
    case = Cases.objects.get(id=case_id)
    form = CaseForm(instance=case)
    if request.method == "POST":
        case.mitsumori_request_date = request.POST['mitsumori_request_date']
        case.customer = Customers.objects.get(id=request.POST['customer'])
        case.deadline = request.POST['deadline']
        case.drawing_data = request.POST['drawing_data']
        case.save()
        return redirect('lists')
    else:
        context = {
            'title': "依頼追加",
            'form': form,
        }
        return render(request, 'lists/case_form.html', context)

def CustomerUpdate(request, customer_id):
    customer = Customers.objects.get(id=customer_id)
    form = CustomerForm(instance=customer)
    if request.method == "POST":
        customer.name = request.POST['name']
        customer.address = request.POST['address']
        customer.tanto = request.POST['tanto']
        customer.mail = request.POST['mail']
        customer.tel = request.POST['tel']
        customer.phone = request.POST['phone']
        customer.save()
        return redirect('customer_lists')
    else:
        context = {
            'title': "顧客追加",
            'form': form,
        }
        return render(request, 'lists/customer_form.html', context)

def ContractorUpdate(request, contractor_id):
    contractor = Contractors.objects.get(id=contractor_id)
    form = ContractorForm(instance=contractor)
    if request.method == "POST":
        contractor.name = request.POST['name']
        contractor.address = request.POST['address']
        contractor.tanto = request.POST['tanto']
        contractor.mail = request.POST['mail']
        contractor.tel = request.POST['tel']
        contractor.phone = request.POST['phone']
        contractor.save()
        return redirect('contractor_lists')
    else:
        context = {
            'title': "外注先追加",
            'form': form,
        }
        return render(request, 'lists/contractor_form.html', context)

def ProductUpdate(request, product_id):
    product = Products.objects.get(id=product_id)
    form = ProductForm(instance=product)
    if request.method == "POST":
        product.case = Cases.objects.get(id=request.POST['case'])
        product.name = request.POST['name']
        product.drawing_num = request.POST['drawing_num']
        product.material = request.POST['material']
        product.surface = request.POST['surface']
        product.volume = request.POST['volume']
        product.save()
        return redirect('lists')
    else:
        context = {
            'title': '製品追加',
            'form': form,
            'page': "UPDATE"
        }
        return render(request, 'lists/product_form.html', context)