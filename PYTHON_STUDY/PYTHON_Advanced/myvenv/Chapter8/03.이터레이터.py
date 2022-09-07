# 1. 이터러블 객체 (iterable object)
# 문자열, 리스트, 튜플, 딕셔너리, ranege 객체

# for i in "123":
#     print(i)

# for i in [10, 20, 30]:
#     print(i)

iter_obj = [10, 20, 30].__iter__()

print(iter_obj)
# <list_iterator object at 0x000002649F5C7100>
print(dir(iter_obj))
# ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__length_hint__', '__lt__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__']

print(iter_obj.__next__()) # 10
print(iter_obj.__next__()) # 20
print(iter_obj.__next__()) # 30
print(iter_obj.__next__()) # StopIteration
