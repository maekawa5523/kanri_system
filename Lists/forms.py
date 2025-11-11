from django import forms
from .models import Cases, Products, Customers, Contractors
 
class CaseForm(forms.ModelForm):
    class Meta:
        model = Cases
        fields = (
            'mitsumori_request_date',
            'customer',
            'deadline',
            'drawing_data',
        )
        labels = {
            'mitsumori_request_date':'見積依頼日',
            'customer':"顧客名",
            'deadline':'納期',
            'drawing_data':'図面データ',
        }
        widgets = {
            'deadline':forms.NumberInput(attrs={"type":"date"}),
            'mitsumori_request_date':forms.NumberInput(attrs={"type":"date"}),
        }

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customers
        fields = (
            'name',
            'address',
            'tanto',
            'mail',
            'tel',
            'phone',
        )
        labels = {
            'name':'顧客名',
            'address':'住所',
            'tanto':'担当者',
            'mail':'メール',
            'tel':'電話',
            'phone':'携帯',
        }

class ContractorForm(forms.ModelForm):
    class Meta:
        model = Contractors
        fields = (
            'name',
            'address',
            'tanto',
            'mail',
            'tel',
            'phone',
            'quality',
            'sheet',
            'cut',
            'can',
            'coat',
        )
        labels = {
            'name':'企業名',
            'address':'住所',
            'tanto':'担当者',
            'mail':'メール',
            'tel':'電話',
            'phone':'携帯',
            'quality':'品質',
            'sheet':'板金',
            'cut':'切削',
            'can':'製缶',
            'coat':'塗装',
        }
        widgets = {
            'sheet':forms.CheckboxInput(attrs={'class': 'check'}),
            'cut':forms.CheckboxInput(attrs={'class': 'check'}),
            'can':forms.CheckboxInput(attrs={'class': 'check'}),
            'coat':forms.CheckboxInput(attrs={'class': 'check'}),
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = (
            'num',
            'name',
            'drawing_num',
            'material',
            'surface',
            'volume',
        )
        labels = {
            'drawing_num':'図番',
            'name':'品名',
            'material':'材質',
            'surface':'処理',
            'volume':'数量',
        }
        widgets = {
            'num':forms.HiddenInput,
        }