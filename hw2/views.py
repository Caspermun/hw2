from django.shortcuts import render


def index(request):
    name = 'Anderson Stephens'
    return render(request, 'index.html', locals())

def index2(request):
    name = 'Ella Stanton'
    return render(request, 'index2.html', locals())

def index3(request):
    name = 'Lucy Spears'
    return render(request, 'index3.html', locals())

def index4(request):
    name = 'Livia Hopkins'
    return render(request, 'index4.html', locals())

def index5(request):
    name = 'Dexter Chen'
    return render(request, 'index5.html', locals())