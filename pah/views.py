from django.shortcuts import render


# View Pah SKU and pricing
def pah(request):
    return render(request, 'pah/pah.html')
