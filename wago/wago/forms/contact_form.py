from django import forms

class ContactForm(forms.Form):
    """Contact form declaration"""
    sender_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder':'Votre nom'})
        )
    sender_mail = forms.EmailField(
        max_length=100,
        help_text='<small id="emailHelp" class="form-text text-muted">Nous ne partagerons jamais votre email avec quelqu\'un d\'autre.</small>',
        widget=forms.EmailInput(attrs={'placeholder':'Votre mail'})
    )
    subject = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder':'Sujet de votre message'})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder':'Votre message'})
    )
    cc_myself = forms.BooleanField(
        required=False,
        label='M\'envoyer une copie par mail'
    )
