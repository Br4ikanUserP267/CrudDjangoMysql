from django.urls import path
from . import views
from  django.conf import settings
from django.contrib.staticfiles.urls import static

#user can enter and have acesss to the views
urlpatterns = [
        #principal 
        path('',views.start, name = 'start'),
        path('we', views.we,  name='we'),
        path('books', views.books, name = 'books'),
        path('books/create', views.create, name = 'create'),
        path('books/edit', views.edit, name = 'edit'),
        path('delete/<int:id>', views.delete, name = 'delete'),
         path('books/edit/<int:id>', views.edit, name = 'edit'),
       
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)