from django.shortcuts import render

def terms(request):
    if request.method == 'GET':
        return render(request, 'terms.html')
