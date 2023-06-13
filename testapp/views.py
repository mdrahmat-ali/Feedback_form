from django.shortcuts import render
from . import forms

def thanku_view(request):
    return render(request,'thanku.html')

def feedback_view(request):
    if request.method=='GET':
        form=forms.FeedBackForm()
    if request.method=='POST':
        form=forms.FeedBackForm(request.POST)
        if form.is_valid():
            print('Form validation success')
            print('Student Name:',form.cleaned_data['name'])
            print('Student RollNo:',form.cleaned_data['rollno'])
            print('Student Mail Id:',form.cleaned_data['email'])
            print('Student Feedback:',form.cleaned_data['feedback'])
    return render(request,'feedback.html',{'form':form})
       

