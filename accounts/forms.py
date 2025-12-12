from django import forms
from django.contrib.auth.models import User

from .models import Profile


class SignUpForm(forms.ModelForm):
    password1 = forms.CharField(
        label="رمز عبور",
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label="تکرار رمز عبور",
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name")
        labels = {
            "username": "نام کاربری",
            "email": "ایمیل",
            "first_name": "نام",
            "last_name": "نام خانوادگی",
        }

    def clean_password2(self):
        p1 = self.cleaned_data.get("password1")
        p2 = self.cleaned_data.get("password2")
        if p1 and p2 and p1 != p2:
            raise forms.ValidationError("رمزها یکسان نیستند.")
        return p2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("role", "phone", "avatar")
        labels = {
            "role": "نقش کاربر",
            "phone": "شماره تماس",
            "avatar": "عکس پروفایل",
        }
