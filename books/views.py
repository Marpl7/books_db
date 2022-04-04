from django.shortcuts import render
from django.core.paginator import Paginator
from books.models import Book


def books_view(request):
    template = 'books/books_list.html'

    books = Book.objects.order_by('pub_date')
    context = {

        'books': books
    }
    return render(request, template, context)


def book_view(request, pub_date):
    template = 'books/book_view.html'

    books = Book.objects.filter(pub_date=pub_date)
    dates = sorted([str(book.pub_date) for book in Book.objects.all()])

    paginator = Paginator(dates, 1)
    page_number = int(request.GET.get('page', dates.index(pub_date) + 1))
    page = paginator.get_page(page_number)
    next_date = pub_date
    previous_date = pub_date

    if page.has_next():
        next_date = paginator.page(page.next_page_number()).object_list[0]
    elif page.has_previous():
        previous_date = paginator.page(page.previous_page_number()).object_list[0]

    context = {
        'previous_date': previous_date,
        'next_date': next_date,
        'books': books,
        'page': page



    }
    return render(request, template, context)