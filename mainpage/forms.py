from django import forms

class RequestCallForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control", "type":"text", "placeholder":"First Name"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control", "type":"text", "placeholder":"Last Name"}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control", "type":"text", "placeholder":"City"}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control", "type":"text", "placeholder":"Phone Number"}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class':"form-control", "placeholder":"Message", "cols":30, "rows":2}))


class ContactUsForm(forms.Form):
    your_name = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control", "type":"text", "placeholder":"Your Name"}))
    your_email = forms.EmailField(widget=forms.TextInput(attrs={'class':"form-control", "type":"email", "placeholder":"Your Email"}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control", "type":"text", "placeholder":"Subject"}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class':"form-control", "placeholder":"Message", "cols":30, "rows":7}))
