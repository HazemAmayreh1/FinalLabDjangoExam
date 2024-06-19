from django.urls import path
from . import views

urlpatterns = [

    path('', views.dashboard, name='dashboard'),
    path('add/', views.student_add, name='student_add'),
    path('edit/<int:id>/', views.student_edit, name='edit_student'),
    path('delete/<int:id>/', views.student_delete, name='delete_student')
]
