from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.home, name='home'),
    path('ask/',views.ask_gemini,name="ask_gemini"),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pricing/', views.pricing, name='pricing'),
    path('memberships/', views.membership_view, name='membership_view'),
    path('submit/', views.submit, name='submit'),
    path('gallery/', views.gallery, name='gallery'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('admin-login/', views.admin_login_view, name='admin-login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('admin-dashboard',views.admin_dashboard,name="admin-dashboard"),
    path('members',views.members,name = "members"),
    path('member/<int:pk>/view/', views.membership_view, name='membership-view'),
    path('member/<int:pk>/update/', views.membership_update, name='membership-update'),
    path('member/<int:pk>/delete/', views.membership_delete, name='membership-delete'),
]