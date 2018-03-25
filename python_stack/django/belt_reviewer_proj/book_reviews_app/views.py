# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages

from models import Author, Book, Review, User


def reviews_main(request):
    reviews = Review.objects.all().order_by("created_at")[:3]
    books = Book.objects.all()
    print(books)
    return render(
        request, 'book_reviews_app/reviews_main.html',
        {"books": books, "reviews": reviews},
    )


def book_detail(request, id):
    try:
        book = Book.objects.get(id=id)
    except Book.DoesNotExist:
        messages.error(request, "The book requested does not exist")
        return redirect("/books")
    return render(
        request, "book_reviews_app/book_detail.html",
        {"book": book}
    )


def user_detail(request, id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        messages.error(request, "That user does not exist")
    else:
        return render(
            request, "book_reviews_app/user_detail.html",
            {"user": user}
        )

# delete view for reviews
# if review.user.id == request.session.user_id then delete