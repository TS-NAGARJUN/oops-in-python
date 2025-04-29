# overload means same name of methods but take up different parameters
# in python we can not create two methods with same name and same parameters
# but we can create two methods with same name and different parameters
class A:
    def show(self, a):
        print("in a show")


class B(A):
    def show(self, a, b):
        print("in b show")


b1 = B()
b1.show(10,20)
# Python does not support method overloading by redefining methods with the same name its gets overriden.
