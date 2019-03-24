from django.shortcuts import render, redirect
from .models import books, authors




def index(request):
    context = {
        "all_books" : books.objects.all()
    }
    #all_books = books.objects.all()
    return render(request, "books_authors_app/index.html",context)

# Create your views here.

def process(request):
    
    data = {
        "title": request.POST['title'],
        "desc": request.POST['desc']
    }

    new_book = books.objects.create(title = request.POST['title'], desc = request.POST['desc'])
    new_book.save()
    return redirect("/")

def specific_book(request, book_id):

    newly_created_book = books.objects.get(id= book_id)

    context = {
        "id"        :   newly_created_book.id,
        "title"     :   newly_created_book.title,
        "desc"      :   newly_created_book.desc, 
        "select_book" : newly_created_book,
        "authors"   :   newly_created_book.books_authors.all(),
        "all_authors":  authors.objects.all(),
        "none_authors" :authors.objects.all().exclude()
    }
    print("*"*100)
    print(authors)
    print("%"*100)

    #more optomized way of creating a dictionary
    # context = {
    #     "newly_created_book": books.objects.get(id= book_id),
    # }
    return render(request, "books_authors_app/books.html", context)


def author(request):
    # newly_created_book = books.objects.get(id= book_id)

    context = {
        "all_authors" : authors.objects.all(),
        "all_books"   : books.objects.all(),
    }

    return render(request, "books_authors_app/authors.html", context)

def process_author(request):
    data = {
        "first_name": request.POST['f_name'],
        "last_name": request.POST['l_name'],
        "notes": request.POST['notes'],
    }
    new_author = authors.objects.create(first_name = request.POST['f_name'], last_name = request.POST['l_name'], notes = request.POST['notes'])
    new_author.save()
    return redirect("/authors")

def specific_author(request, author_id):
    
    newly_created_author = authors.objects.get(id= author_id)

    context = {
        "id": newly_created_author.id,
        "first_name": newly_created_author.first_name,
        "last_name": newly_created_author.last_name,
        "notes": newly_created_author.notes,
        "all_books"   : books.objects.all(),
        "title"     :   books.objects.get(id = author_id),
        "books"   :   newly_created_author.books.all(),




        
    }
    return render(request, "books_authors_app/authorspage.html",context)

def addauthor(request,book_id):
    # y = request.POST['source']
    thisbook= books.objects.get(id=book_id)
    newauthor= authors.objects.get(id=request.POST['newauthor'])
    newauthor.books.add(thisbook)
    print("*"*100)
    print (id)
    print("*"*100)

    # source.authors.add(newauthor)
    # return redirect('/books/'+y)
    # new_author = authors.objects.get(id = request.POST['id'])
    # newauthor.books_authors.add(book_id)
    # thisbook = books.objects.get(id = book_id)
    # thisbook.authors.add(newauthor)
    # thisbook.objects.add(authors)


    # newauthor.objects.all()

    return redirect("/books/"+ str(book_id))


def addbook(request, author_id):
    
    
    newly_created_author = authors.objects.get(id= author_id)
    newbook= books.objects.get(id=request.POST['newbook'])
    # newauthor=authors.objects.get(id = author_id)
    # authors.objects.get(id=request.POST['newauthor'])
    # newbook.books.add(newly_created_author)
    newbook.books_authors.add(newly_created_author)
    # authors.newbook.add(newly_created_author)
    # newly_created_author.books.add(newbook)

    return redirect("/authors/"+ str(author_id))


 
