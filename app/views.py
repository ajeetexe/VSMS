import django, random, string
from django.contrib import messages
from django.db.models.fields import SlugField, UUIDField
from django.shortcuts import redirect, render
from .models import Carousel, ServiceRequest, UserProfile
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, TemplateView, UpdateView, DetailView, DeleteView
from  django.contrib.auth.models import User
from .forms import UserRegisterForm, ServiceRequestForm, UserForm1, UserForm2
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy 
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
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
    return render(request=request, template_name='user/home.html',context={'service_request':ServiceRequest.objects.all()})


def random_generator():
    c = ''.join(random.choice(string.ascii_uppercase +string.ascii_lowercase + string.digits) for _ in range(20))
    return c

class ServiceRequestView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    model = ServiceRequest
    form_class = ServiceRequestForm
    template_name = 'user/service_request.html'
    success_url = reverse_lazy('user')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.service_request_no = random_generator()
        return super().form_valid(form)


class ProfileDetailView(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    model = User
    queryset = User.objects.all()
    template_name = 'user/profile.html'
    slug_field = 'username'


    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['userprofile'] = UserProfile.objects.all()
        return context



@login_required(login_url='/login/')
def update_profile(request):
    if request.method == 'POST':
        form1 = UserForm1(request.POST, instance=request.user)
        form2= UserForm2(request.POST, request.FILES, instance=request.user.userprofile)
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            return redirect('user')
    else:
        form1 = UserForm1(instance=request.user)
        form2 = UserForm2(instance=request.user.userprofile)
    return render(request, 'user/update_profile.html',context={
            'form1':form1,
            'form2':form2
    })

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('user')

        else:
            messages.error(request, 'Please correct the error')
    else:
        form = PasswordChangeForm(request.user)
    return render(request,'user/change_password.html',{'form':form})



class ServiceDetailview(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    model = ServiceRequest
    queryset = ServiceRequest.objects.all()
    slug_field = 'service_request_no'
    template_name = 'user/service_view.html'



class ServiceDeleteView(LoginRequiredMixin, DeleteView):
    model = ServiceRequest
    template_name = 'user/servicerequest_confirm_delete.html'
    slug_field = 'service_request_no'
    success_url = reverse_lazy('user')