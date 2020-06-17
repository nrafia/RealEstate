from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=250, required=True)
    from_email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
