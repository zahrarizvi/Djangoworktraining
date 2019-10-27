from django.shortcuts import render
from . import forms
# Create your views here.
def index(request):
    return render(request,'App1module/index.html')
def form_name_view(request):
    form = forms.FormName()
    if request.method == "POST":
        form = forms.FormName(request.POST)
    if form.is_valid():
        print("Validation is awesome worked fine")
        print("Name:"+form.cleaned_data['name'])
        print("Email:" + form.cleaned_data['email'])
        print("Re-Email:" + form.cleaned_data['verify_email'])
        print("Content:" + form.cleaned_data['text'])

    return render(request,'App1module/forms.html',{'form':form})