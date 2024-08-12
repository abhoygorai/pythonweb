from django.shortcuts import render
from .forms import AddForm

def add_numbers_view(request):
    result = None
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            num1 = form.cleaned_data['num1']
            num2 = form.cleaned_data['num2']
            result = num1 + num2
    else:
        form = AddForm()

    return render(request, 'calculator/add.html', {'form': form, 'result': result})
