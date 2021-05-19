from django.urls import path
from .views import lcm1,lcm_func,lcm_calculator


app_name = 'lcm'
urlpatterns = [
    path('',lcm1, name="lcm1"),
    path('/lcm-of-<int:num1>-and-<int:num2>/', lcm_func, name="lcm_func"),
    path("/lcm_calculator/",lcm_calculator, name="lcm_calculator")
    ]