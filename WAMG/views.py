from django.http import HttpResponseRedirect,HttpResponse
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse , reverse_lazy
from django.views import generic
from django.views.generic import CreateView
from django.utils import timezone
from .models import contact,things
from .forms import CreateUserForm,AddThingsForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('system')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {'form': form}
        return render(request, 'register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('system')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('system')
            else:
                messages.info(request, 'Username or password is incorrect. Please check your data and try again.')

        context = {}
        return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('index')

@login_required(login_url='login')
def system(request):
    context = {}
    return render(request, 'system.html', context)

@login_required(login_url='login')
def addThings(request):
        form = AddThingsForm()

        if request.method == 'POST':


            form = AddThingsForm(request.POST,request.FILES)
            if form.is_valid():

                #images = form.cleaned_data['photo']
                #img_mod = "/images/{}/{}".format(profile,images)
                #form.cleaned_data['photo'] = img_mod
                #test = form.cleaned_data['photo']
                #print(test)
                form.save()
                messages.success(request, 'Form submission successful')
                return redirect('addedThing')
        else:
            initial = {'user': request.user.username}
            form = AddThingsForm(initial=initial)

        context = {'form': form }
        print(request)
        return render(request, 'system.html', context)

@login_required(login_url='login')


def getThings(request):
        thing = things.objects.all()
        #Lista pomieszczeń. Do zrobienia - aby w tabeli wyświetlana była nazwa zamiast id.

        m1 = things.TYPE_LIST
        m2 = things.COLOR_LIST
        context = {'thing':thing, 'place_types':m1, 'color_list':m2, 'nl':request.user.username}
        print(context)
        return render(request, 'getdata.html', context)

@login_required(login_url='login')

def updateThings(request,names):
    print(request.method)
    thing = things.objects.get(name=names).delete()
    context = {'thing': thing, 'nl': request.user.username}
    print(context)
    return render(request, 'getdata.html', context)

class HomePage(generic.ListView):
    model = contact
    template_name = "index.html"

    def get_success_url(self):
        return reverse('WAMG:index')

