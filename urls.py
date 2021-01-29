from django.conf.urls import url
from .views import *

urlpatterns= [
    url(r'^$', index,name = 'index'),

    url(r'^display_smartphone$', display_smartphone, name = "display_smartphone"),
    url(r'^display_laptop$', display_laptop, name = "display_laptop"),

    url(r'^add_smartphone$', add_smartphone,name = "add_smartphone"),
    url(r'^add_laptop$', add_laptop,name = "add_laptop"),

    url(r'^edit_smartphone/(?P<pk>\d+)$', edit_smartphone, name="edit_smartphone"),
    url(r'^edit_laptop/(?P<pk>\d+)$',edit_laptop, name = "edit_laptop"),

    url(r'^delete_smartphone(?P<pk>\d+)$',delete_smartphone,name = "delete_smartphone"),
    url(r'^delete_laptop(?P<pk>\d+)$',delete_laptop,name = "delete_laptop")



]