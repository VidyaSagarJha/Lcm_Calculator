from collections import Counter
import math

from django.shortcuts import redirect, render
from django.http import HttpResponse
# Create your views here.

def lcm1(request):
    try:
        if request.method == 'POST':
            res1 = int(request.POST['textfield1'])
            res2 = int(request.POST['textfield2'])
            return redirect('/lcm-of-{}-and-{}'.format(res1,res2))
        else:
            return render(request,'lcm/lcm.html')
    except:
        return redirect('lcm_calculator')



def prime_factors(number):
    prime_factors = []
    while number % 2 == 0:
        prime_factors.append(2)
        number = number / 2
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        while number % i == 0:
            prime_factors.append(int(i))
            number = number / i
    if number > 2:
        prime_factors.append(int(number))

    return prime_factors

def lcm_func(request, num1, num2):
    x = prime_factors(num1)
    y = prime_factors(num2)
    #print(x)
    #print(y)
    c = dict(Counter(x)) #variables to save counter for a
    d = dict(Counter(y)) #variables to save counter for b
    result = []
    for key in sorted(set(c.keys()).union(set(d.keys()))):
        exp = max(c.get(key, 0), d.get(key, 0))
        for i in range(exp):
            result.append(key)
   # print(result)
    mul = 1
    for i in result:
        mul = mul*i
    print(mul)
    context ={
        "num1": num1,
        "num2": num2,
        "prime1": x,
        "prime2" : y,
        "lcm": mul,
    }
    
    return render(request, 'lcm/final_answer.html', context)




def lcm_calculator(request):
    return HttpResponse("This is calc")
