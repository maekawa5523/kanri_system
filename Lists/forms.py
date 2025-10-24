from django import forms
from .models import Cases
 
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