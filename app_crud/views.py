from django.shortcuts import render,redirect
from .forms import StudentRegForm
from .models import User
from django.http import HttpResponseRedirect


# Create your views here.
def add_show_fun(request):
    if request.method=='POST':
        obj=StudentRegForm(request.POST)

# easy method of saving
        # if obj.is_valid():
        #     obj.save()
# other method of saving with cleaned data
        if obj.is_valid():
            x = obj.cleaned_data['name']
            y = obj.cleaned_data['email']
            z = obj.cleaned_data['pwd']
            rec=User(name=x,email=y,pwd=z)
            rec.save()
            obj = StudentRegForm() # to make the input fields empty after add data/saving data
    else:
        obj = StudentRegForm() # else generate blank
    stud=User.objects.all()
    return render(request, 'add_show.html', {'form': obj ,'stu':stud}) #stu key,

def delete(request,id):
    if request.method=='POST':
        obj = User.objects.get(pk=id) # obj just a variable
        obj.delete()
        return HttpResponseRedirect('/')# home

#  function to update and edit
def update(request,id):
    if request.method=="POST":
        obj=User.objects.get(pk=id)
        fm=StudentRegForm(request.POST, instance=obj)
        if fm.is_valid():
            fm.save()
    else:

        obj=User.objects.get(pk=id)
        fm=StudentRegForm(instance=obj)
    # return render(request, 'updatestudent.html',{'id':id}) # working chk
    return render(request, 'updatestudent.html', {'form': fm , 'id':id})  # working chk