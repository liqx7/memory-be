from django.urls import path
from . import views

urlpatterns = [
    path('list/',views.list,name='list'),
    path('detail/<int:item_id>',views.detail,name='detail'),
    path('add/',views.add,name='add')
]
