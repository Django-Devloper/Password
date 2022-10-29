from django import forms

class Password(forms.Form):
    usrid = forms.CharField(label='User Id', max_length=100)
    security_Question = forms.CharField(label='Security Question', max_length=100)

class PasswordChangeForm(forms.Form):
    pass1 = forms.CharField(label='New Password', max_length=100)
    pass2 = forms.CharField(label='Repeat Password', max_length=100)
