from django.shortcuts import render

# Cate your views here
def testando (request):
    return render(request, 'Aplicativo/teste.html')

def boot (request):
    return render (request, 'Aplicativo/base.html')
