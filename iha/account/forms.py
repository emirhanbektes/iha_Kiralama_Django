from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Bu kullanıcı adı zaten kullanımda. Lütfen farklı bir kullanıcı adı seçin.")
        return username

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")

        if not email:
            raise forms.ValidationError("E-posta adresi boş olamaz. Lütfen geçerli bir e-posta adresi girin.")

        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Şifreler eşleşmiyor. Lütfen aynı şifreyi girin.")
