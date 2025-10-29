from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('404/', views.error_404, name='error_404'),
    path('about-us/', views.about_us, name='about-us'),
    path('blog-details/', views.blog_details, name='blog-details'),

    path('blog/', views.blog, name='blog'),
    path('blog/blog-details/', views.blog_details, name='blog-details'),
    
    path('bmi-calculator/', views.bmi_calculator, name='bmi-calculator'),
    path('class-details/', views.class_details, name='class-details'),
    path('class-timetable/', views.class_timetable, name='class-timetable'),
    path('contact/', views.contact, name='contact'),
    path('gallery/', views.gallery, name='gallery'),
    path('index/', views.index, name='index'),
    path('main/', views.main, name='main'),
    path('services/', views.services, name='services'),
    path('team/', views.team, name='team'),
    path('product/', views.product, name='product'),
    path('product_detail/<int:product_id>/', views.product_detail, name='product_detail'),
    path('checkout/', views.checkout, name='checkout'),
    path('thankyou/', views.thankyou, name='thankyou'),
    ]