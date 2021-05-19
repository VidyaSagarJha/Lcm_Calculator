"""django_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import include,path
from lcm import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lcm/',views.lcm1, name="lcm1"),
    path('lcm-of-<int:num1>-and-<int:num2>/', views.lcm_func, name="lcm_func"),
    path("lcm_calculator/",views.lcm_calculator, name="lcm_calculator"),

]


"""
app_name = 'lcm'
urlpatterns = [
    path('',lcm1, name="lcm1"),
    path('lcm-of-<int:num1>-and-<int:num2>/', lcm_func, name="lcm_func"),
    path("/lcm_calculator/",lcm_calculator, name="lcm_calculator")
    ]
"""