from django.shortcuts import render, redirect
from .models import User
def index(request):
    context = {
        "all_users": User.objects.all()
    }
    return render(request,"index.html", context)

def process(request):
    retreivedFName = request.POST['first_name']
    retreivedLName = request.POST['last_name']
    retrievedEmail = request.POST['email']
    retrievedAge = request.POST['age']
    
    new_user = User.objects.create(first_name = retreivedFName, last_name = retreivedLName, email_address = retrievedEmail, age = int(retrievedAge))
    new_user.save()
    return redirect("/")
    
    

