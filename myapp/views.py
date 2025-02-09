from django.shortcuts import render, redirect
from .models import AstronomicalObject
from .forms import AstronomicalObjectForm

def index(request):
    return render(request, 'myapp/index.html')

def object_list(request):
    objects = AstronomicalObject.objects.all()
    return render(request, 'myapp/object_list.html', {'objects': objects})

def object_create(request):
    if request.method == 'POST':
        form = AstronomicalObjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('object_list')
    else:
        form = AstronomicalObjectForm()
    return render(request, 'myapp/object_form.html', {'form': form})
