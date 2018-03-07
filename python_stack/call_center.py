import datetime


class Call:
    def __init__(self, uid, name, number, time, reason):
        self.uid = uid
        self.name = name
        self.number = number
        self.time = datetime.datetime.strptime(time, "%I:%M%p")
        self.reason = reason

    def display(self):
        time = self.time.strftime("%I:%M%p")
        print("ID: {}, Caller: {}, Number: {}, Time: {}, Reason: {}".format(
            self.uid, self.name, self.number, time, self.reason,
        ))


callone = Call(1, "Charlie", "301-124-3364", "04:00pm", "Needs tech support")
calltwo = Call(
    2, "Miss Mary", "230-434-3433", "05:50pm", "question about account")
print("")


class CallCenter():
    def __init__(self, calls_lst):
        self.calls_lst = calls_lst
        self.queue_size = len(calls_lst)

    def add(self, call):
        self.calls_lst.append(call)
        self.queue_size += 1

    def remove(self):
        self.calls_lst.pop(0)
        self.queue_size -= 1
    
    def remove_by_number(self, number):
        for call in self.calls_lst:
            if call.number == number:
                self.calls_lst.remove(call)
        self.queue_size -= 1

    def info(self):
        for call in self.calls_lst:
            time = call.time.strftime("%I:%M%p")
            print("NAME: {}, NUMBER: {}, TIME: {}".format(
                call.name, call.number, time))
        print("Current Queue: {}".format(self.queue_size))

    def sort_calls(self):
        self.calls_lst = sorted(
            self.calls_lst, key=lambda call: call.time)
        self.info()


callcenter = CallCenter([callone, calltwo])
callcenter.info()
print("")
callcenter.add(Call(3, "SlackJaw", "125-242-1243", "05:55pm", "car trouble"))
callcenter.info()
print("")
callcenter.remove()
callcenter.info()
print("")
callcenter.remove_by_number("125-242-1243")
callcenter.info()
print("")
callcenter.add(Call(5, "Jakson", "232-241-2195", "01:00pm", "tractor trouble"))
callcenter.add(
    Call(32, "Jakie", "234-135-2353", "5:00am", "Locked keys in car"))
callcenter.info()
print("")
callcenter.sort_calls()