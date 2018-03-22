# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Description(models.Model):
    desc = models.TextField()

    def __str__(self):
        return "{}".format(self.desc)


class Course(models.Model):
    name = models.CharField(max_length=255)
    desc = models.ForeignKey(Description, related_name="course")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Course Name: {}".format(self.name)


class Comment(models.Model):
    content = models.TextField()
    course = models.ForeignKey(Course, related_name="comments")

    def __str__(self):
        return "Comment: {}, Course: {}".format(self.content, self.course)
