from django import forms
from django.core import validators

def check_for_a(value):
    if value[0].lower()!='a':
        raise forms.ValidationError("Make sure to give name starting with A as a character")
class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_a])
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Enter the email")
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])
    #def clean_botcatcher(self):
    #    botcatcher = self.cleaned_data['botcatcher']
    #    if len(botcatcher)>0:
    #        raise forms.ValidationError("Hello I caught you!!")
    #    return botcatcher
    def clean(self):
        all_clean_data=super(FormName,self).clean()
        email=all_clean_data['email']
        vmail=all_clean_data['verify_email']
        if email!=vmail:
            raise forms.ValidationError("Hey Enter correct email")