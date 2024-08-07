from django.urls import path
from  . import views

urlpatterns=[
    path('',views.index,name="base"),
    path('huddle/',views.huddle,name='huddle'),
]