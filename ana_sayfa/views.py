from django.shortcuts import render

def ana_sayfa(request):
    return render(request, 'ana_sayfa/ana_sayfa.html')
