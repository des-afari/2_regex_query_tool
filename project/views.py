from django.shortcuts import render
from .forms import RegexForm

def index(request):
    regex_form = RegexForm()

    payload = {
        'regex_form': regex_form
    }

    return render(request, 'index.html', payload)