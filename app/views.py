import random, string
from django.contrib import messages
from django.shortcuts import redirect, render
from .models import Carousel, ServiceRequest, UserProfile, Mechanics
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    CreateView,
    TemplateView,
    UpdateView,
    DetailView,
    DeleteView,
    ListView,
)
from django.contrib.auth.models import User
from .forms import (
    UserRegisterForm,
    ServiceRequestForm,
    UserForm1,
    UserForm2,
    CarouserForm,
)
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse_lazy
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import get_user_model

# Create your views here.


# ________________________________________________________for Anonymous User______________________________
def index(request):
    if request.user.is_superuser:
        context = {
            "users": get_user_model().objects.all().filter(is_superuser=False),
            "recent": ServiceRequest.objects.all().order_by("-user")[:10],
            "servicerequest": ServiceRequest.objects.all(),
            "pending": ServiceRequest.objects.filter(status="p"),
            "approve": ServiceRequest.objects.filter(status="a"),
        }
        return render(
            request=request, template_name="admin-panel/index.html", context=context
        )
    elif request.user.is_active:
        return render(
            request=request,
            template_name="user/home.html",
            context={
                "service_request": ServiceRequest.objects.all().filter(
                    user=request.user
                )
            },
        )
    else:
        return render(
            request=request,
            template_name="home/index.html",
            context={"obj": Carousel.objects.all()},
        )


class RegisterUserView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = "/login/"
    template_name = "home/registration.html"


def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect("home")

        else:
            messages.error(request, "Please correct the error")
    else:
        form = PasswordChangeForm(request.user)

    return render(request, "home/change_password.html", {"form": form})

@login_required(login_url="/login/")
def update_profile(request):
    if request.method == "POST":
        form1 = UserForm1(request.POST, instance=request.user)
        form2 = UserForm2(
            request.POST, request.FILES, instance=request.user.userprofile
        )
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            return redirect("/")
    else:
        form1 = UserForm1(instance=request.user)
        form2 = UserForm2(instance=request.user.userprofile)
    return render(
        request, "home/update_profile.html", context={"form1": form1, "form2": form2}
    )


class ProfileDetailView(LoginRequiredMixin, DetailView):
    login_url = "/login/"
    model = User
    queryset = User.objects.all()
    template_name = "home/profile.html"
    slug_field = "username"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["userprofile"] = UserProfile.objects.all()
        return context


# _______________________________for User___________________________________


def random_generator():
    c = "".join(
        random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)
        for _ in range(20)
    )
    return c


class ServiceRequestView(LoginRequiredMixin, CreateView):
    login_url = "/login/"
    model = ServiceRequest
    form_class = ServiceRequestForm
    template_name = "user/service_request.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.service_request_no = random_generator()
        return super().form_valid(form)





class ServiceDetailview(LoginRequiredMixin, DetailView):
    login_url = "/login/"
    model = ServiceRequest
    queryset = ServiceRequest.objects.all()
    slug_field = "service_request_no"
    template_name = "user/service_view.html"


class ServiceDeleteView(LoginRequiredMixin, DeleteView):
    login_url = "/login"
    model = ServiceRequest
    template_name = "user/servicerequest_confirm_delete.html"
    slug_field = "service_request_no"
    success_url = reverse_lazy("user")


# _____________________________for admin__________________________________


class SuperuserRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["users"] = get_user_model().objects.all().filter(is_superuser=False)
        context["recent"] = ServiceRequest.objects.all().order_by("-user")[:10]
        context["servicerequest"] = ServiceRequest.objects.all()
        context["pending"] = ServiceRequest.objects.filter(status="p")
        context["approve"] = ServiceRequest.objects.filter(status="a")
        return context


class CarouselView(LoginRequiredMixin, SuperuserRequiredMixin, TemplateView):
    login_url = "/login/"
    template_name = "admin-panel/carousel/view.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["carousel"] = Carousel.objects.all()
        return context


class CarouselUpdateView(LoginRequiredMixin, SuperuserRequiredMixin, UpdateView):
    login_url = "/login/"
    template_name = "admin-panel/carousel/update.html"
    model = Carousel
    form_class = CarouserForm
    queryset = Carousel.objects.all()
    slug_field = "id"
    success_url = reverse_lazy("carousel")


class CarouselCreateView(LoginRequiredMixin, SuperuserRequiredMixin, CreateView):
    login_url = "/login/"
    template_name = "admin-panel/carousel/create.html"
    model = Carousel
    fields = "__all__"
    success_url = reverse_lazy("carousel")


class CarouselDeleteView(LoginRequiredMixin, SuperuserRequiredMixin, DeleteView):
    login_url = "/login/"
    template_name = "admin-panel/carousel/delete_confirm.html"
    model = Carousel
    slug_field = "id"
    success_url = reverse_lazy("carousel")


class MechanicsView(LoginRequiredMixin, SuperuserRequiredMixin, TemplateView):
    login_url = "/login/"
    template_name = "admin-panel/mechanics/view.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["mechanics"] = Mechanics.objects.all()
        return context


class MechanicsUpdateView(LoginRequiredMixin, SuperuserRequiredMixin, UpdateView):
    login_url = "/login/"
    template_name = "admin-panel/mechanics/update.html"
    model = Mechanics
    fields = "__all__"
    queryset = Mechanics.objects.all()
    slug_field = "id"
    success_url = reverse_lazy("mechanics")


class MechanicsCreateView(LoginRequiredMixin, SuperuserRequiredMixin, CreateView):
    login_url = "/login/"
    template_name = "admin-panel/mechanics/create.html"
    model = Mechanics
    fields = "__all__"
    success_url = reverse_lazy("mechanics")


class MechanicsDeleteView(LoginRequiredMixin, SuperuserRequiredMixin, DeleteView):
    login_url = "/login/"
    template_name = "admin-panel/mechanics/delete_confirm.html"
    model = Mechanics
    slug_field = "id"
    success_url = reverse_lazy("mechanics")

class TotalServiceTemplateView(
    LoginRequiredMixin, SuperuserRequiredMixin, TemplateView
):
    login_url = "/login/"
    template_name = "admin-panel/service/total_view.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["service"] = ServiceRequest.objects.all()
        return context


class ServiceUpdateView(LoginRequiredMixin, SuperuserRequiredMixin, UpdateView):
    login_url = "/login/"
    model = ServiceRequest
    queryset = ServiceRequest.objects.all()
    slug_field = "service_request_no"
    template_name = "admin-panel/service/update.html"
    fields = ["mechanics_name", "service_charge", "parts_charge", "status"]
    success_url = reverse_lazy("home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["service"] = ServiceRequest.objects.filter(
            service_request_no=self.object.service_request_no
        )
        return context


class UserListView(LoginRequiredMixin, SuperuserRequiredMixin, ListView):
    login = "/login/"
    model = get_user_model()
    template_name = "admin-panel/userlist.html"
    context_object_name = "userdata"

    def get_queryset(self):
        querset = super().get_queryset()
        return querset.filter(is_superuser=False)


class UserDetailView(LoginRequiredMixin, SuperuserRequiredMixin, DetailView):
    login = "/login/"
    model = User
    template_name = "admin-panel/userdetail.html"
    slug_field = "username"
    context_object_name = "userdetail"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["service"] = ServiceRequest.objects.filter(user=self.object.id)
        return context


class PendingService(LoginRequiredMixin, SuperuserRequiredMixin, ListView):
    login = "/login"
    queryset = ServiceRequest.objects.filter(status="p")
    context_object_name = "pending"
    template_name = "admin-panel/service/pending_view.html"


class ApproveService(LoginRequiredMixin, SuperuserRequiredMixin, ListView):
    login = "/login"
    queryset = ServiceRequest.objects.filter(status="a")
    context_object_name = "approve"
    template_name = "admin-panel/service/approve_view.html"