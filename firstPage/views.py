from django.shortcuts import render, redirect
from .forms import DataForm
from .models import Data

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-predictions')
    else:
        form = DataForm()
    context = {
        'form': form,
    }
    return render(request, 'dashboard/index.html', context)


def predictions(request):
    predicted_instance = Data.objects.all()
    context = {
        'predicted_instance': predicted_instance
    }
    return render(request, 'dashboard/predictions.html', context)
    
  