import os

from django.core.wsgi import get_wsgi_application

project_name_settings = "dojo_ninjas_main.settings"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", project_name_settings)
application = get_wsgi_application()

from apps.likes_books.models import Users, Books


users = [['Jimmy', "Crouch", "barty_couch@gmail.com"], ["Jelly", "Bean", "jb@gmail.com"], ['JAckdon', "brown", "jackB@gmail.com"]]

# for usr in users:
#     user = Users()
#     user.first_name = usr[0]
#     user.last_name = usr[1]
#     user.email = usr[2]
#     user.save()

user1 = Users.objects.get(first_name="Jimmy")
user2 = Users.objects.get(first_name="Jelly")
user3 = Users.objects.get(first_name="JAckdon")

books = [
    ["Harry Potter and the Philosopher's Stone", " It is the first novel in the Harry Potter series and Rowling's debut novel, first published in 1997 by Bloomsbury.", user1, user1],
    ["Harry Potter and the Chamber of Secrets", "The plot follows Harry's second year at Hogwarts School of Witchcraft and Wizardry, during which a series of messages on the walls of the school's corridors warn that the 'Chamber of Secrets' has been opened and that the 'heir of Slytherin' would kill all pupils who do not come from all-magical families.", user1, user1],
    ["Harry Potter and the Prisoner of Azkaban", "The book follows Harry Potter, a young wizard, in his third year at Hogwarts School of Witchcraft and Wizardry. Along with friends Ronald Weasley and Hermione Granger, Harry investigates Sirius Black, an escaped prisoner from Azkaban who they believe is one of Lord Voldemort's old allies.", user2, user2],
    ["Harry Potter and the Goblet of Fire", "It follows Harry Potter, a wizard in his fourth year at Hogwarts School of Witchcraft and Wizardry and the mystery surrounding the entry of Harry's name into the Triwizard Tournament, in which he is forced to compete.", user2, user2],
    ["Harry Potter and the Order of the Phoenix", " It follows Harry Potter's struggles through his fifth year at Hogwarts School of Witchcraft and Wizardry, including the surreptitious return of the antagonist Lord Voldemort, O.W.L. exams, and an obstructive Ministry of Magic.", user3, user3],
    ["Harry Potter and the Half-Blood Prince", "Set during protagonist Harry Potter's sixth year at Hogwarts, the novel explores the past of Harry's nemesis, Lord Voldemort, and Harry's preparations for the final battle against Voldemort alongside his headmaster and mentor Albus Dumbledore.", user3, user3],
]

# for book in books:
#     a_book = Books()
#     a_book.name = book[0]
#     a_book.desc = book[1]
#     a_book.uploader = book[2]
#     a_book.save()
    # a_book.liked_users = book[3]

# for book in Books.objects.all():
#     book.liked_users.add(user3)

# book1 = Books.objects.get(name=books[0][0])
# book2 = Books.objects.get(name=books[1][0])
# book3 = Books.objects.get(name=books[2][0])
# book4 = Books.objects.get(name=books[3][0])
# book5 = Books.objects.get(name=books[4][0])
# book6 = Books.objects.get(name=books[5][0])

# book1.liked_users.add(user1)
# book6.liked_users.add(user1)

# book1.liked_users.add(user2)
# book3.liked_users.add(user2)