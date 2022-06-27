from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.http import HttpResponse

from .models import Article

# Create your views here.
def index(request):
    value1 = 0
    value2 = 0
    context = {'parameter1': value1, 'parameter2': value2}
    return render(request, 'home/index.html', context)
