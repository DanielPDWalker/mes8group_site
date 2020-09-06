from django.shortcuts import render


def writing_home(request):
    context = {
        'title': 'Writing'
    }
    return render(request, 'writing/writing.html', context)

def writing_post(request):
    pass