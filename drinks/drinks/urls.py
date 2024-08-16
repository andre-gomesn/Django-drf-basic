from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('drinks/',views.drinks_page,name='drinks'),
    path('drinks/<int:id>',views.especific_drink_page,name='specific-drink')
]
