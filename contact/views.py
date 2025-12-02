from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_view(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("core:home")
    return render(request, "contact/contact.html", {"form": form})
