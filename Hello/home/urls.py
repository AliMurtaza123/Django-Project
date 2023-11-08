from django.contrib import admin
from django.urls import path
from home import views
admin.site.site_header = "Ali Murtaza Admin"
admin.site.site_title = "Ali Murtaza Admin Portal"
admin.site.index_title = "Welcome to Ali Murtaza Researcher Portal"
urlpatterns = [
   path('',views.index, name='home'),
   path('about',views.about, name='about'),
   path('services',views.services, name='services'),
   path('contact',views.contact, name='contact'),

]
