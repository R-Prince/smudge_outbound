from django.shortcuts import render


def index(request):
    # A view to return dashboard
    return render(request, 'dashboard/index.html')
