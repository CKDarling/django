from django.shortcuts import render
#from second_app.models import User
from second_app.forms import NewUser
# Create your views here.
def index(request):
    return render(request,'second_app/homepage.html')


def Nerd(request):
    form = NewUser()
    if request.method=="POST":
        form = NewUser(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("u suck")
    return render(request,'second_app/users.html',{'form':form})
