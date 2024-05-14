from django.urls import path
from . import views
from .views import SuccessPageView

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('success/', SuccessPageView.as_view(), name='success-page'),
]
