from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'todo_list'
urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path('toggle/<int:item_id>', views.toggle, name='toggle'),
    path('delete/<int:item_id>', views.delete, name='delete'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
