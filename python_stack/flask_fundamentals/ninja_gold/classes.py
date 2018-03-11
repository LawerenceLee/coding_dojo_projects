import datetime
from random import randrange


class Activity(object):
    def __init__(self):
        self.text_color = "green"
        self.date_time = datetime.datetime.now()


class Farm(Activity):
    def __init__(self):
        super(Farm, self).__init__()
        self.gold_earned = randrange(10, 21)
        self.date_time = self.date_time.strftime("%Y/%m/%d %I:%M%p")
        self.activity_str = "Earned {} golds from the Farm! ({})".format(
            self.gold_earned, self.date_time)


class Cave(Activity):
    def __init__(self):
        super(Cave, self).__init__()
        self.gold_earned = randrange(5, 10)
        self.date_time = self.date_time.strftime("%Y/%m/%d %I:%M%p")
        self.activity_str = "Earned {} golds from the Cave! ({})".format(
            self.gold_earned, self.date_time)


class House(Activity):
    def __init__(self):
        super(House, self).__init__()
        self.gold_earned = randrange(2, 5)
        self.date_time = self.date_time.strftime("%Y/%m/%d %I:%M%p")
        self.activity_str = "Earned {} golds from the House! ({})".format(
            self.gold_earned, self.date_time)


class Casino(Activity):
    def __init__(self):
        super(Casino, self).__init__()

        self.gold_earned = randrange(-50, 50)
        self.date_time = self.date_time.strftime("%Y/%m/%d %I:%M%p")
        if self.gold_earned > 0:
            self.earned_lost = ('earned', 'WOW')
        else:
            self.earned_lost = ('lost', 'Ouch')
            self.text_color = "red"

        self.activity_str = "Entered a casino and {} {} golds... {}.. ({})".format(
                self.earned_lost[0],
                abs(self.gold_earned),
                self.earned_lost[1],
                self.date_time
            )


if __name__ == "__main__":
    a = Activity()
    print(a.__dict__)
    print("")
    b = Farm()
    print(b.__dict__)
    print("")
    c = Cave()
    print(c.__dict__)
    print("")
    d = House()
    print(d.__dict__)
    print("")
    e = Casino()
    print(e.__dict__)
