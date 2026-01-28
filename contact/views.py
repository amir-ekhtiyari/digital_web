from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import ContactForm


@login_required(login_url="accounts:login")
def contact_view(request):
    form = ContactForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        contact = form.save(commit=False)


        # contact.user = request.user

        contact.save()

        messages.success(
            request,
            "پیام شما با موفقیت ارسال شد. به‌زودی با شما تماس می‌گیریم."
        )

        return redirect("contact:form")

    return render(request, "contact/contact.html", {
        "form": form
    })
