from django.urls import path
from app8 import views
urlpatterns=[
    path('',views.index,name='index'),
    path('contact',views.contact,name='contact'),
    path('gallery',views.gallery,name='gallery'),
    path('viewsdata',views.viewsdata,name='viewsdata'),

]