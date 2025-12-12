# contact/forms.py (مثال)
from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(
        label="نام",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "نام"
        })
    )
    last_name = forms.CharField(
        label="نام خانوادگی",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "نام خانوادگی"
        })
    )
    email = forms.EmailField(
        label="ایمیل",
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "example@email.com"
        })
    )
    subject = forms.CharField(
        label="موضوع",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "موضوع پیام"
        })
    )
    message = forms.CharField(
        label="متن پیام",
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "rows": 5,
            "placeholder": "متن پیام خودت را بنویس..."
        })
    )
