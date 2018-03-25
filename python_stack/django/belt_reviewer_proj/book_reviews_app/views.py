# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from models import Author, Book, Review, User
from book_review_validation import BookReviewValidation


def reviews_main(request):
    reviews = Review.objects.all().order_by("created_at")[:3]
    books = Book.objects.all()
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
        return redirect("/books")
    else:
        return render(
            request, "book_reviews_app/user_detail.html",
            {"user": user}
        )


def add_review(request):
    authors = Author.objects.all()
    return render(
        request, "book_reviews_app/add_review.html", {"authors": authors}
    )


def process_review(request):
    if not request.POST['review']:
        messages.error(request, "Review may not be empty")
        return redirect("/books/{}".format(request.POST['book_id']))
    else:
        Review.objects.create(
            content=request.POST['review'],
            rating=request.POST['rating'],
            user=User.objects.get(id=request.session['user_id']),
            book=Book.objects.get(id=request.POST['book_id']),
        ).save()
        return redirect("/books/{}".format(request.POST['book_id']))


def process_book_and_review(request):
    form = BookReviewValidation(request.POST)
    if form.errors:
        for error in form.errors:
            messages.error(request, error)
        return redirect("/books/add")
    else:
        author_tuple = Author.objects.get_or_create(
            name=form.posted_author,
        )
        book_tuple = Book.objects.get_or_create(
            title=request.POST['title'],
        )
        if author_tuple[0] not in book_tuple[0].authors.all():
            book_tuple[0].authors.add(author_tuple[0].id)
        Review.objects.create(
            content=request.POST['review'],
            rating=request.POST['rating'],
            user=User.objects.get(id=request.session['user_id']),
            book=book_tuple[0],
        ).save()
        return redirect("/books/{}".format(book_tuple[0].id))


def delete_review(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        messages.error(request, "You cannot delete a review that does not exist")
    
    if review.user.id == request.session['user_id']:
        review.delete()
        messages.success(request, "Successfully Deleted Review")
    else:
        messages.error(request, "You do not have permission to delete that review")

    return redirect("/books")
