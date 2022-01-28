from django.shortcuts import render
from django.utils import timezone
from .models import Letter

# Create your views here.
def post_list(request):
    posts = Letter.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'anonymous_letters/post_list.html', {'posts': posts})