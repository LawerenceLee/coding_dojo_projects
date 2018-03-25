# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from log_reg_app.models import User


class Author(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "ID: {}, Author Name: {}".format(self.id, self.name)


class Book(models.Model):
    title = models.CharField(max_length=255)
    authors = models.ManyToManyField(Author, related_name="books")
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        author_str = ""
        for author in self.authors.all():
            author_str += author.name + " "
        return "Title: {}, Authors: {}".format(self.title, author_str)

    def __str__(self):
        author_str = ""
        for author in self.authors.all():
            author_str += author.name + " "
        return "ID: {}\nTitle: {}\nAuthors: {}".format(
            self.id, self.title, author_str
        )

    def author_str(self):
        author_str = ""
        for author in self.authors.all():
            author_str += author.name + " "
        return author_str


class Review(models.Model):
    content = models.TextField()
    rating = models.IntegerField()
    user = models.ForeignKey(User, related_name="reviews")
    book = models.ForeignKey(Book, related_name="reviews")
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "ID: {}, Book Title: {}, Rating: {}, User: {}, Content: {}\
        ".format(
            self.id, self.book.title, self.rating,
            self.user.first_name, self.content
        )

    def __str__(self):
        return "ID: {}\nBook Title: {}\nRating: {}\nUser: {}\nContent: {}\
        ".format(
            self.id, self.book.title, self.rating,
            self.user.first_name, self.content
        )
