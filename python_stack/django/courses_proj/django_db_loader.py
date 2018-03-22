import os

from django.core.wsgi import get_wsgi_application

# project_name_settings = "<project_name's>.settings"
# project_name_settings = "dojo_ninjas_main.settings"
project_name_settings = "courses_main.settings"

os.environ.setdefault("DJANGO_SETTINGS_MODULE", project_name_settings)
application = get_wsgi_application()

# Example: from <location of models.py in relation to manage.py> import <model names>
from apps.course_app.models import Description, Course, Comment


descriptions = ["Learn to throw ninja stars...",
                "Learn to spread your wings...",
                "Learning the magic behind CAFFINE...",
                "Learn to love, rather than hate thy neighbor"]

# for description in descriptions:
#     alpha = Description()
#     alpha.desc = description
#     alpha.save()

courses = ["How to be a Ninja", "How to fly", "How to get more energy in the bootcamp", "How to pair progarm more efficiently"]

counter = 0
for desc in Description.objects.all():
    beta = Course()
    beta.name = courses[counter]
    beta.desc = desc
    beta.save()
    counter += 1


for course in Course.objects.all():
    print(course)