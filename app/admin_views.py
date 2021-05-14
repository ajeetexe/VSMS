from django.db.models.fields import SlugField
from django.forms import widgets
from django.views.generic import TemplateView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import get_user_model
from .models import ServiceRequest, Carousel, Mechanics, UserProfile
from django.urls import reverse_lazy
from .forms import CarouserForm, UserForm1, UserForm2
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.contrib.auth.models import User



class SuperuserRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser


class Index(LoginRequiredMixin,SuperuserRequiredMixin,TemplateView):
    login_url = '/login/'
    template_name = 'admin-panel/index.html'
    


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] =  get_user_model().objects.all().filter(is_superuser=False)
        context['recent'] =  ServiceRequest.objects.all().order_by('-user')[:10]
        context['servicerequest'] =  ServiceRequest.objects.all()
        context['pending'] =  ServiceRequest.objects.filter(status='p')
        context['approve'] =  ServiceRequest.objects.filter(status='a')
        print(ServiceRequest.objects.filter(status='p').count())
        return context


class CarouselView(LoginRequiredMixin,SuperuserRequiredMixin, TemplateView):
    login_url = '/login/'
    template_name = 'admin-panel/carousel/view.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['carousel'] = Carousel.objects.all()
        return context


class CarouselUpdateView(LoginRequiredMixin,SuperuserRequiredMixin, UpdateView):
    login_url = '/login/'
    template_name = 'admin-panel/carousel/update.html'
    model = Carousel
    form_class = CarouserForm
    queryset = Carousel.objects.all()
    slug_field = 'id'
    success_url = reverse_lazy('carousel')

class CarouselCreateView(LoginRequiredMixin,SuperuserRequiredMixin, CreateView):
    login_url = '/login/'
    template_name = 'admin-panel/carousel/create.html'
    model = Carousel
    fields = '__all__'
    success_url = reverse_lazy('carousel')


class CarouselDeleteView(LoginRequiredMixin,SuperuserRequiredMixin, DeleteView):
    login_url = '/login/'
    template_name = 'admin-panel/carousel/delete_confirm.html'
    model = Carousel
    slug_field ='id'
    success_url = reverse_lazy('carousel')


class MechanicsView(LoginRequiredMixin,SuperuserRequiredMixin, TemplateView):
    login_url = '/login/'
    template_name = 'admin-panel/mechanics/view.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['mechanics'] = Mechanics.objects.all()
        return context


class MechanicsUpdateView(LoginRequiredMixin,SuperuserRequiredMixin, UpdateView):
    login_url = '/login/'
    template_name = 'admin-panel/mechanics/update.html'
    model = Mechanics
    fields = '__all__'
    queryset = Mechanics.objects.all()
    slug_field = 'id'
    success_url = reverse_lazy('mechanics')

class MechanicsCreateView(LoginRequiredMixin,SuperuserRequiredMixin, CreateView):
    login_url = '/login/'
    template_name = 'admin-panel/mechanics/create.html'
    model = Mechanics
    fields = '__all__'
    success_url = reverse_lazy('mechanics')


class MechanicsDeleteView(LoginRequiredMixin,SuperuserRequiredMixin, DeleteView):
    login_url = '/login/'
    template_name = 'admin-panel/mechanics/delete_confirm.html'
    model = Mechanics
    slug_field ='id'
    success_url = reverse_lazy('mechanics')


class ProfileDetailView(LoginRequiredMixin,SuperuserRequiredMixin, DetailView):
    login_url = '/login/'
    model = User
    queryset = User.objects.all()
    template_name = 'admin-panel/profile.html'
    slug_field = 'username'


    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['userprofile'] = UserProfile.objects.all()
        return context



@login_required(login_url='/login/')
@user_passes_test(lambda u: u.is_superuser)
def update_profile(request):
    if request.method == 'POST':
        form1 = UserForm1(request.POST, instance=request.user)
        form2= UserForm2(request.POST, request.FILES, instance=request.user.userprofile)
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            return redirect('admin_panel')
    else:
        form1 = UserForm1(instance=request.user)
        form2 = UserForm2(instance=request.user.userprofile)
    return render(request, 'admin-panel/update_profile.html',context={
            'form1':form1,
            'form2':form2
    })



class TotalServiceTemplateView(LoginRequiredMixin,SuperuserRequiredMixin,TemplateView):
    login_url = '/login/'
    template_name = 'admin-panel/service/total_view.html'


    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['service'] = ServiceRequest.objects.all()
        return context



class ServiceUpdateView(LoginRequiredMixin, SuperuserRequiredMixin, UpdateView):
    login_url = '/login/'
    model = ServiceRequest
    queryset = ServiceRequest.objects.all()
    slug_field = 'service_request_no'
    template_name = 'admin-panel/service/update.html'
    fields = ['mechanics_name','service_charge','parts_charge','status']
    success_url = reverse_lazy('admin_panel')


    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['service'] = ServiceRequest.objects.filter(service_request_no = self.object.service_request_no)
        return context