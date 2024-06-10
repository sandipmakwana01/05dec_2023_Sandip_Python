from django.urls import path
from . import views

urlpatterns = [
    path('register/doctor/', views.register_doctor, name='register_doctor'),
    path('register/patient/', views.register_patient, name='register_patient'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('doctors/', views.view_doctors, name='view_doctors'),
    path('patients/', views.view_patients, name='view_patients'),
    path('book/', views.book_appointment, name='book_appointment'),
    path('profile/', views.profile, name='profile'),
]
