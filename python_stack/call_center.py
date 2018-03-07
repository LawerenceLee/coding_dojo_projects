
class Call:
    def __init__(self, uid, name, number, time, reason):
        self.uid = uid
        self.name = name
        self.number = number
        self.time = time 
        self.reason = reason

    def display(self):
        print("ID: {}, Caller: {}, Number: {}, Time: {}, Reason: {}".format(
            self.uid, self.name, self.number, self.time, self.reason,
        ))


callone = Call(1, "Charlie", "301-124-3364", "4pm", "Needs tech support")
# callone.display()

calltwo = Call(2, "Miss Mary", "230-434-3433", "5:50pm", "question about account")
# calltwo.display()
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
            print("NAME: {}, NUMBER: {}".format(call.name, call.number))
        print("Current Queue: {}".format(self.queue_size))

callcenter = CallCenter([callone, calltwo])
callcenter.info()
print("")
callcenter.add(Call(3, "SlackJaw", "125-242-1243", "5:55pm", "car trouble"))
callcenter.info()
print("")
callcenter.remove()
callcenter.info()
print("")
callcenter.remove_by_number("125-242-1243")
callcenter.info()