# 제너레이터
# 1. 이터레이터를 만드는 함수


def season_generator(*args):
    for arg in args:
        yield arg

g = season_generator('spring', 'summer', 'autumn', 'winter')

# print(g) # <generator object season_generator at 0x000001D1ECE47B50>

# print(dir(g)) 
# ['__class__', '__del__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__name__', '__ne__', '__new__', '__next__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'close', 'gi_code', 'gi_frame', 'gi_running', 'gi_yieldfrom', 'send', 'throw']

print(g.__next__()) # spring
print(g.__next__()) # summer
print(g.__next__()) # autumn
print(g.__next__()) # winter


def func():
    print("첫번째 작업 중...")
    yield 1

    print("두번째 작업 중...")
    yield 2

    print("세번째 작업 중...")
    yield 3 

ge = func()
data = ge.__next__()
print(data)
data = ge.__next__()
print(data)
data = ge.__next__()
print(data)