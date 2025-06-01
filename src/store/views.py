from django.shortcuts import render



def office(request):
    ctx = {}

    return render(request, 'office.html', ctx)
