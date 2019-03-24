
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('process',views.process),
    path('books/<book_id>',views.specific_book),
    path('authors', views.author),
    path('processA', views.process_author),
    path('authors/<author_id>', views.specific_author),
    path('addauthor/<book_id>', views.addauthor),
    path('addbook/<author_id>', views.addbook)
]
