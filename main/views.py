from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Nazwa Arifah Ikhsan',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)
