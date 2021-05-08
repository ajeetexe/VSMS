from django.shortcuts import redirect, render
from .models import Carousel
from django.views.generic import CreateView, TemplateView
from  django.contrib.auth.models import User
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    obj = Carousel.objects.all()
    context = { 
        'obj' : obj
    }
    return render(request=request,template_name='home/index.html',context=context)

class RegisterUserView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url ='/login/'
    template_name = 'home/registration.html'


@login_required(login_url='/login/')
def profilePage(request):
    if request.user.is_superuser:
        return redirect('/admin/')
    else:
        return redirect('user')

@login_required(login_url='/login/')
def userProfile(request):
    return render(request=request, template_name='user/home.html')