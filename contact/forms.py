from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["first_name", "last_name", "email", "subject", "message"]

        widgets = {
            "first_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "نام"
            }),
            "last_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "نام خانوادگی"
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "example@email.com"
            }),
            "subject": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "موضوع پیام"
            }),
            "message": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 5,
                "placeholder": "متن پیام خودت را بنویس..."
            }),
        }
