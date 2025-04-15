from django.shortcuts import render


def power(request):
    if request.method == 'POST':
        I = int(request.POST.get('Intensity'))
        R = int(request.POST.get('Resistance'))
        P = (I**2)*R
        return render(request, 'power.html', {'output': P})
    return render(request, 'power.html')
