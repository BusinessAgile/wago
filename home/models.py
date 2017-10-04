from __future__ import absolute_import, unicode_literals

from wagtail.wagtailcore.models import Page
from wago.forms.contact_form import ContactForm

from django.core.mail import send_mail
from django.http import HttpResponseRedirect

class HomePage(Page):
    """Homepage Wagtail declaration"""
    def get_context(self, *args, **kwargs):
        """Pass form intance to context"""
        context = super(HomePage, self).get_context(*args, **kwargs)
        context['form'] = ContactForm()
        return context

    def serve(self, request):
        """Capture form data"""
        form = ContactForm(request.POST or None)
        if form.is_valid():
            sender_name = form.cleaned_data['sender_name']
            sender_mail = form.cleaned_data['sender_mail']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            cc_myself = form.cleaned_data['cc_myself']

            sender = "{}<{}>".format(sender_name, sender_mail)

            recipients = ['Business Agile <contact@businessagile.eu>']
            if cc_myself:
                recipients.append(sender)
            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect('/')
        return super(HomePage, self).serve(request)
