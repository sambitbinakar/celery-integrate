from django.shortcuts import render,redirect
from .models import Huddle
from django.contrib import messages
from .forms import itemform
from .utilities import notify_users
# Create your views here.

def index(request):
    return render(request,'index.html')


def huddle(request):
    key =request.GET.get('key','')
    user = request.GET.get('user','')
    huddle,created  = Huddle.objects.get_or_create(key=key)

    if created:
        messages.success(request, 'The  Huddle was created successfully')


    if request.method == 'POST':
        form = itemform(request.POST)

        if form.is_valid():
            item = form.save(commit=False)
            item.huddle = huddle
            item.save()
            notify_users(huddle,item.user)

            return redirect (f'/huddle/?user={user}&key={key}')


    return render (request,'huddle.html',{'user':user,'huddle':huddle })