from django.shortcuts import render
import random
from datetime import datetime

# Create your views here.
def index(request):
    return render(request, 'index.html')

def hello(request):
    menu = ['닭갈비', '탕수육', '초밥', '스파게티돈까스']
    pick = random.choice(menu)
    return render(request, 'hello.html', {'pick':pick})

def name(request):
    my_name = '김현수'
    return render(request, 'name.html', {'my_name':my_name})

def introduce(request):
    my_info = ['김현수', '100']
    name = '김현수'
    age = 100
    gitAddr = 'https://github.com/wishinghyun'
    addr = '서울 강서구'
    process = 'url -> views -> html'
    hope = '놀고싶다'
    context = {
        'name' : name,
        'age' : age,
        'gitAddr' : gitAddr,
        'addr' : addr,
        'process' : process,
        'hope' : hope
    }
    return render(request, 'introduce.html', context)

def classroom(request):
    student = ['이영주', '윤소윤', '유명인', '성민재', '김민정']
    pick = random.choice(student)
    context = {
        'pick':pick
    }
    return render(request, 'classroom.html', context)

def yourname(request, name):
    context = {
        'name' : name
    }
    return render(request, 'yourname.html', context)

def nameage(request, name, age):
    context = {
        'name' : name,
        'age' : age
    }
    return render(request, 'nameage.html', context)

def multification(request, num1, num2):
    context = {
        'num1' : num1,
        'num2' : num2,
        'multification' : num1 * num2
    }
    return render(request, 'multification.html', context)

def gugudan(request, big, small):
    result = []
    if big < small :
        big, small = small, big
    for num in range(1,small+1):
        result.append(big*num)
    context = {
        'result' : result
    }
    return render(request, 'gugudan.html', context)

def dtl(request):
    my_list = ['짜장면', '차돌짬뽕', '탕수육', '콩국수']
    empty_list = []
    my_string = "Life is short, You need Python"
    today = datetime.now()
    context = {
        'my_list' : my_list,
        'empty_list' : empty_list,
        'my_string' : my_string,
        'today' : today
    }
    return render(request, 'dtl.html', context)

def forif(request):
    my_list = [100, 50, 30, 20, 10]
    my_string = '간단한 문자열'
    data_a = '첫번째 데이터'
    data_b = '두번째 데이터'
    data_a, data_b = data_b, data_a
    context = {
        'my_list' : my_list,
        'my_string' : my_string,
        'data_a' : data_a,
        'data_b' : data_b
    }
    return render(request, 'forif.html', context)