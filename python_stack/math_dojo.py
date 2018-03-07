
# class MathDojo():
#     result = 0

#     def add(self, *args):
#         self.result += sum(args)
#         return self

#     def subtract(self, *args):
#         self.result -= sum(args)
#         return self


# md = MathDojo()
# print(md.add(2).add(2,5).subtract(3,2).result)


class MathDojo():
    result = 0

    def add(self, *args):
        for arg in args:
            if isinstance(arg, int) or isinstance(arg, float):
                self.result += arg
            elif isinstance(arg, list) or isinstance(arg, tuple):
                self.result += sum(arg)
        return self

    def subtract(self, *args):
        for arg in args:
            if isinstance(arg, int) or isinstance(arg, float):
                self.result -= arg
            elif isinstance(arg, list) or isinstance(arg, tuple):
                self.result -= sum(arg)
        return self


md = MathDojo()
print(md.add([1], 3, 4, (50)).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2, 3], [1.1, 2.3], (4, 5)).result)
