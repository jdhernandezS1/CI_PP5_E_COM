"""
Imports
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render, get_object_or_404
from django.shortcuts import reverse, get_list_or_404
from django.views import generic, View
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
# Internal
from .forms import ContactForm
from django.conf import settings
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter


class ContactUs(View):
    """
    A class for the Contact Us Page
    """
    def get(self, request, *args, **kwargs):
        """
        Get Function
        """
        template = "contact/contact_us.html"
        act_user = request.user
        form = ContactForm()
        context = {
            "act_user": act_user,
            "form": form,
            }
        return render(
            request,
            template,
            context,
        )

    def post(self, request, *args, **kwargs):
        """
        POST Function
        """
        template = "contact/contact_us.html"
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Thanks To contact Us"
            message = form.cleaned_data['your_message']
            recipients = [form.cleaned_data['your_email'],]
            cc_myself = 'store.capricci.ch@gmail.com'
            sender = settings.EMAIL_HOST_USER
            if cc_myself:
                recipients.append(sender)

            send_mail(subject, message, sender, recipients)
            template = "contact/contact_thanks.html"
            return render(
                request,
                template,
            )
        else:
            form = ContactForm()
        context = {
            "form": form,
            }
        return render(
            request,
            template,
            context,
            )
