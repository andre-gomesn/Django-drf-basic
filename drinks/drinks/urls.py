from django.contrib import admin
from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('drinks/',views.drinks_page,name='drinks'),
    path('drinks/<int:id>',views.especific_drink_page,name='specific-drink')
]

urlpatterns=format_suffix_patterns(urlpatterns)