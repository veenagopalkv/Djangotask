from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from .models import Department,Course
from .forms import personForm,wikiform
import wikipedia




# Create your views here.
def home(request):
    department_list = Department.objects.all()

    return render(request,'home.html',{'department_list':department_list})

def login(request):
    department_list = Department.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/details')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('/login')
    return render(request,'login.html',{'department_list':department_list})

def register(request):
    department_list = Department.objects.all()
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        confirmpassword=request.POST['confirmpassword']
        if password == confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already Taken")
                return redirect('/register')
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save()
                print('user created')
                return redirect('/login')
        else:
            messages.info(request, "Password doesn't match")
            return redirect('/register')
        return redirect('/')
    return render(request,'register.html',{'department_list':department_list})

def details(request):
    department_list = Department.objects.all()
    forms = personForm(request.POST)
    if forms.is_valid():
        forms.save()
        return redirect('/orderconfirm')

    return render(request,'Detailsform.html',{'department_list':department_list,'forms':forms})

def orderconfirm(request):
    print("hello")
    messages.info(request, "Order Is Confirmed")
    return render(request, 'orderconfirm.html')

def load_course(request):

    department_id=request.GET.get("department_id")
    messages.info(request, department_id)
    courses=Course.objects.filter(department_id=department_id).all()
    print(courses)
    return JsonResponse(list(courses.values('id', 'name')), safe=False)

def logout(request):
    print("hai")
    auth.logout(request)
    return redirect('/')

def wikisearch(request,name):

   # department = Department.objects.filter(name=name)
    form = wikiform({'name': name})

    if request.method == "POST":

        search = request.POST["name"]
        try:
            result = wikipedia.summary(search, sentences=10)  # No of sentences that you want as output
        except:
            return HttpResponse("Wrong Input")
        return render(request, "wikipediadepartment.html", {"result": result,'form':form})

    return render(request,'wikipediadepartment.html',{'form':form})