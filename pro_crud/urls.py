
from django.contrib import admin
from django.urls import path
from app_crud import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.add_show_fun, name='add_show'),
    path('delete/<int:id>/', views.delete, name='deletedata'), # dynamic url
    path('update/<int:id>/', views.update, name='updatedata'),
]
