class Mammal:
    def Walk(self):
        print("walk")


class Dog(Mammal):
   def Bark(self):
       print("Bark")


class Cat(Mammal):
    def Speak(self):
        print("sdkm")


c=Cat()
c.Speak()

# Constructor
# class Person:
#     def __init__(self,name):
#         self.name=name
#
#     def Talk(self):
#         print(f"Hi, I am {self.name}")
#
# p=Person("Jay")
# p.Talk()














# class A:
#    def Vehicle(self):
#        print("Defender")
# class B(A):
#     def Vehicle(self):
#         print("This is class B")
#
# class C(A):
#     def Vehicle(self):
#         print("this is class C")
# class D(B,C):
#     pass
#
#
# obj=D()
# obj.Vehicle()
# print(D.mro())















# class A:
#     def Vehicle(self):
#         print("This is Vehicle")
# class B (A):
#     def RangeRover(self):
#         print("This is RangeRover")
# class C(A):
#     def Bugati(self):
#         print("This is Bugati")
# class D(C,B,A):
#     def Bugati(self):
#         print("this is Lambo")
#
#
#     # def Vehicle(self):
#     #     print("this is D")
#
#
# obj=D()
# obj.RangeRover()
#
#
#
#
#
