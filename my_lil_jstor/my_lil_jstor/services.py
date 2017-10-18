from django.core.serializers import serialize

from .models import ColoringBook
from .models import Comment


def get_coloring_book(primary_key):
    coloring_book = ColoringBook.objects.get(pk=primary_key)
    coloring_book_dict = {
        'id': coloring_book.id,
        'title': coloring_book.title,
        'description': coloring_book.description,
        'image_name': coloring_book.image_name,
        'pub_date': coloring_book.pub_date,
        'price': coloring_book.price,
        'likes': coloring_book.likes
    }

    return coloring_book_dict

def like_coloring_book(primary_key):
    coloring_book = ColoringBook.objects.get(pk=primary_key)
    coloring_book.likes = coloring_book.likes + 1
    print(coloring_book.likes)
    coloring_book.save()
    return coloring_book.likes

def get_books():
    coloring_books = ColoringBook.objects.all()
    books = []
    for coloring_book in coloring_books:
        coloring_book_dict = {
            'id': coloring_book.id,
            'title': coloring_book.title,
            'description': coloring_book.description,
            'image_name': coloring_book.image_name,
            'pub_date': coloring_book.pub_date,
            'price': coloring_book.price
        }
        books.append(coloring_book_dict)
    return books

def insert_coloring_book_comment(user, comment, bookId):
    comment = Comment(comment=comment, name=name, book=ColoringBook.objects.get(pk=bookId))
    comment.save()
    return {
        'user': comment.user,
        'comment': comment.comment
    }


def get_coloring_book_comments(bookId):
    if ((len(bookId) == 0) or (bookId is None)):
        comments = Comment.object.all()
    else:
        comments = Comment.objects.filter(book=bookId)
    comments2 = []
    for comment in comments:
        if(comment.rating != 0): 
            comments2.append({
            'user': comment.user,
            'comment': comment.comment,
            'rating': comment.rating
            })
        else:
            comments2.append({
            'user': comment.user,
            'comment': comment.comment,
            })
    return comments2

def change_coloring_book_price(primary_key, value):
    coloring_book = ColoringBook.objects.get(pk=primary_key)
    coloring_book.price = coloring_book.price - value
    coloring_book.save()
    return coloring_book.price
