from django.shortcuts import render
from . models import  CustomUser
from .forms import *

def password_Change(request):
    if request.method =="GET":
        form=Password
        return render(request ,"registration/Change_password.html",{'forms':form})

    if request.method =="POST":
        try:
            user=request.POST['usrid']
            security=request.POST['security_Question']
            id=CustomUser.objects.get(username=user,security_question=security)
            form=PasswordChangeForm
            return render(request, "registration/Change_password.html", {'forms': form, 'id':id})
        except:
            pass1=request.POST['pass1']
            pass2=request.POST['pass2']
            user=request.POST['id']
            if pass1 == pass2:
                u = CustomUser.objects.get(username=user)
                u.set_password(pass1)
                u.save()
                return render(request, "registration/password_change_done.html")
            else:
                form = Password
                return render(request, "registration/Change_password.html", {'forms': form})



