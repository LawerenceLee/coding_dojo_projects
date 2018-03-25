from django.utils.datastructures import MultiValueDictKeyError

from models import Author, Book


class BookReviewValidation(object):

    def __init__(self, form):
        self.title = form['title']
        self.author = form['author']
        self.review = form['review']
        try:
            self.new_author = form['new_author']
        except MultiValueDictKeyError:
            self.new_author = None
        self.errors = []
        self.posted_author = None

        self.is_title_valid()
        self.is_author_valid()
        self.is_review_valid()

    def is_title_valid(self):
        if not self.title:
            self.errors.append(
                "Book Title cannot be empty"
            )
 
    def is_author_valid(self):
        if self.author and self.new_author:
            self.errors.append(
                "Must choose either add new author or select from the list"
            )
        elif not self.author and not self.new_author:
            self.errors.append(
                "Must choose either add new author or select from the list"
            )
        elif self.author:
            self.posted_author = self.author
        elif self.new_author:
            self.posted_author = self.new_author

    def is_review_valid(self):
        if not self.review:
            self.errors.append(
                "Review field may not empty"
            )


