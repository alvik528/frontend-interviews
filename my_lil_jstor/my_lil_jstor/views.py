from django.shortcuts import render
from django.http import JsonResponse
from .services import get_coloring_book
from .services import get_books
from .services import like_coloring_book
from .services import insert_coloring_book_comment
from .services import get_coloring_book_comments
from .services import change_coloring_book_price

def coloring_books(request, book_id):
    coloring_book = get_coloring_book(book_id)
    comments = get_coloring_book_comments(book_id)
    context = {
        'book': coloring_book,
        'comments': comments
    }
    return render(request, 'coloring_book_view.html', context)


def home(request):
    book = get_coloring_book(3)
    context = {
        'book': book
    }

    return render(request, 'home.html', context)

def purchase(request, book_id):
    book = get_coloring_book(book_id)
    context = {
        'book': book
    }
    return render(request, 'purchase.html', context)

def browse(request):
    books = get_books()
    context = {
        'books': books
    }
    return render(request, 'browse.html', context)

def likeBook(request):
    print(request)
    bookid = request.POST.get('bookId')
    likes = like_coloring_book(request.POST.get('bookId'))
    '''change_coloring_book_price(request.POST.get('bookId'), 0.25)'''
    print("hellohellohleooasfsfdasf")
    return JsonResponse({
        'likes': likes
    })

def commentBook(request):
    comment = insert_coloring_book_comment(request.POST.get('name'), request.POST.get('comment'), request.POST.get('bookId'))
    '''change_coloring_book_price(request.POST.get('bookId'), 0.5)'''
    return JsonResponse({
        'comment': comment
    })
