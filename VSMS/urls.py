"""VSMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.index, name="home"),
    path("register/", views.RegisterUserView.as_view(), name="register"),
    path(
        "login/",
        LoginView.as_view(success_url="/", template_name="home/login.html"),
        name="login",
    ),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("admin/", admin.site.urls),
    path("profile/<slug>/", views.ProfileDetailView.as_view(), name="profile"),
    path("update_profile/", views.update_profile, name="update_profile"),
    path("change_password/", views.change_password, name="change_password"),


    # urls for user panel
    path(
        "service-request/", views.ServiceRequestView.as_view(), name="service_request"
    ),
    
    path(
        "service-view/<slug>/", views.ServiceDetailview.as_view(), name="service_view"
    ),
    path(
        "service-delete/<slug>",
        views.ServiceDeleteView.as_view(),
        name="service_delete",
    ),


    # urls for custom admin panel
    path("carousel/", views.CarouselView.as_view(), name="carousel"),
    path(
        "carousel/update/<slug>/",
        views.CarouselUpdateView.as_view(),
        name="update_carousel",
    ),
    path("carousel/add/", views.CarouselCreateView.as_view(), name="add_carousel"),
    path(
        "carousel/delete/<slug>/",
        views.CarouselDeleteView.as_view(),
        name="delete_carousel",
    ),
    path("mechanics/", views.MechanicsView.as_view(), name="mechanics"),
    path("mechanics/add/", views.MechanicsCreateView.as_view(), name="add_mechanics"),
    path(
        "mechanics/update/<slug>/",
        views.MechanicsUpdateView.as_view(),
        name="update_mechanics",
    ),
    path(
        "mechanics/delete/<slug>/",
        views.MechanicsDeleteView.as_view(),
        name="delete_mechanics",
    ),
    path(
        "service/total-view/",
        views.TotalServiceTemplateView.as_view(),
        name="service_total_view",
    ),
    path(
        "service/detail/<slug>/",
        views.ServiceUpdateView.as_view(),
        name="service_detail_view",
    ),
    path("userlist/", views.UserListView.as_view(), name="userlist"),
    path("userdatail/<slug>/", views.UserDetailView.as_view(), name="userdetail"),
    path("service/pending/", views.PendingService.as_view(), name="pending"),
    path("service/approve/", views.ApproveService.as_view(), name="approve"),
]


urlpatterns = urlpatterns + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
