from django import forms
from .models import Product,category
from userview.models import UserProfile

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'imageUrl', 'date', 'weight', 'category']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = category
        fields = ['name', 'aciklama']



class rentUserForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['user','startdate', 'stopdate', 'product']

    def __init__(self, *args, **kwargs):
        super(rentUserForm, self).__init__(*args, **kwargs)
        # Kullanıcı alanını görüntülenemez ve değiştirilemez hale getir
        self.fields['user'].widget = forms.HiddenInput()
        

    def save(self, commit=True):
        instance = super(rentUserForm, self).save(commit=False)
          # Mevcut kullanıcıyı ata
        if commit:
            instance.save()
        return instance