# --- theory ---
# recursion factorial
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
# tests
print("5! is", factorial(5))
print("10! is", factorial(10))

# recursion countdown
def count_down(start):
    if start <= 0:
        print(start)
    else:
        print(start)
        count_down(start - 1)
# tests
count_down(5)

# recusrion fibonacci
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
# tests
print("fib(5) is", fib(5))
print("fib(10) is", fib(10))

# recursion exponent
def exponent_calc(base, expo):
    if expo == 0:
        return 1
    else:
        return base * exponent_calc(base, expo-1)
# test
print('recursion exponent: ',exponent_calc(5, 3)) #print: 125

# bubble sort
def sort_with_bubbles(lst):
    #Set swap_occurred to True to guarantee the loop runs once
    swap_occurred = True

    #Run the loop as long as a swap occurred the previous time
    while swap_occurred:

        #Start off assuming a swap did not occur
        swap_occurred = False

        #For every item in the list except the last one...
        for i in range(len(lst) - 1):

            #If the item should swap with the next item...
            if lst[i] > lst[i + 1]:

                #Then, swap them! But these lines aren't
                #quite right: fix this code!
                temp = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = temp

                #One more line is needed here; add it!
                swap_occurred = True

    return lst
# tests
print('buble sort',sort_with_bubbles([5, 3, 1, 2, 4])) # print: [1, 2, 3, 4, 5]

# selection sort
def sort_with_select(a_list):

    #For each index in the list...
    for i in range(len(a_list)):

        #Assume first that current item is already correct...
        minIndex = i

        #For each index from i to the end...
        for j in range(i + 1, len(a_list)):

            #Complete the reasoning of this conditional to
            #complete the algorithm! Remember, the goal is
            #to find the lowest item in the list between
            #index i and the end of the list, and store its
            #index in the variable minIndex.
            #
            #Write your code here!
            if (a_list[minIndex] > a_list[j]):
                minIndex = j

        #Save the current minimum value since we're about
        #to delete it
        minValue = a_list[minIndex]

        #Delete the minimum value from its current index
        del a_list[minIndex]

        #Insert the minimum value at its new index
        a_list.insert(i, minValue)

    #Return the resultant list
    return a_list
# tests
print('selection sort',sort_with_select([5, 3, 1, 2, 4])) # print: [1, 2, 3, 4, 5]

# merge sort
def mergesort(lst):
    #Then, what does it do? mergesort should recursively run mergesort on the left and right sides of lst until
    #it's given a list only one item. So, if lst has only one item, we should just return that one-item list.
    if len(lst) <= 1:
        return lst
    #Otherwise, we should call mergesort separately on the left and right sides. Since each successive call to
    #mergesort sends half as many items, we're guaranteed to eventually send it a list with only one item, at
    #which point we'll stop calling mergesort again.
    else:
        #Floor division on the length of the list will find us the index of the middle value.
        midpoint = len(lst) // 2
        #lst[:midpoint] will get the left side of the list based on list slicing syntax. So, we want
        #to sort the left side of the list alone and assign the result to the new smaller list left.
        left = mergesort(lst[:midpoint])
        #And same for the right side.
        right = mergesort(lst[midpoint:])
        #So, left and right now hold sorted lists of each half of the original list. They might
        #each have only one item, or they could each have several items.
        #Now we want to compare the first items in each list one-by-one, adding the smaller to our new
        #result list until one list is completely empty.
        newlist = []
        while len(left) and len(right) > 0:
            #If the first number in left is lower, add it to the new list and remove it from left
            if left[0] < right[0]:
                newlist.append(left[0])
                del left[0]
            #Otherwise, add the first number from right to the new list and remove it from right
            else:
                newlist.append(right[0])
                del right[0]
        #When the while loop above is done, it means one of the two lists is empty. Because both
        #lists were sorted, we can now add the remainder of each list to the new list. The empty list
        #will have no items to add, and the non-empty list will add its items in order.
        newlist.extend(left)
        newlist.extend(right)
        #newlist is now the sorted version of lst! So, we can return it. If this was a recursive call
        #to mergesort, then this sends a sorted half-list up the ladder. If this was the original
        #call, then this is the final sorted list.
        return newlist
#Let's try it out!
print('merge sort',mergesort([2, 5, 3, 8, 6, 9, 1, 4, 7]))

# linear search
def linear(a_list, num):

    for i in range(len(a_list)):
        print(i)
        if a_list[i] == num:
            return i
    return False
# test
a_list = [5, 1, 3, 6, 7, 3, 1, 6, 7, 8, 3, 6]
print('linear search for index of nr: 6 is: ',linear(a_list, 6)) # print: 3

# binary search
def binary_search(searchList, searchTerm):
    #First, the list must be sorted.
    searchList.sort()
    #Now, each iteration of the loop, we want to narrow down the part of the list to look at. So, we need to
    #keep track of the range we've narrowed down to so far. Initially, that will be the entire list, from
    #the first index to the last.
    min = 0
    max = len(searchList) - 1
    #Now, we want to loop as long as our range has any numbers left to investigate. As long as there is
    #more than one number between minimum and maximum, we're not done searching.
    while min <= max:
        #We want to check the middle item of the current range, which is the average of the
        #current minimum and maximum index. For example, if min was 5 and max was 15, our
        #middle number would be at index 5. We'll use floor division because indices must be integers.
        currentMiddle = (min + max) // 2
        #If the term in the middle is the term we're looking for, we're done!
        if searchList[currentMiddle] == searchTerm:
            return True
        #If not, we want to check if the term we're looking for should come earlier or later.
        #If the term we're looking for is less than the current middle, then search the first
        #half of the list:
        elif searchTerm < searchList[currentMiddle]:
            max = currentMiddle - 1
        #If the term we're looking for is greater than the current middle, search the second
        #half of the list:
        else:
            min = currentMiddle + 1
        #Each iteration of the loop, one of three things happens: the term is found, max
        #shrinks, or min grows. Eventually, either the term will be found, or min will be
        #equal to max.
    #If the search term was found, this line will never be reached because the return statement
    #will end the function. So, if we get this far, then the search term was not found, and
    #we can return False.
    return False
#Let's try it out!
intlist = [12, 64, 23, 3, 57, 19, 1, 17, 51, 62]
print("23 is in intlist:", binary_search(intlist, 23))
print("50 is in intlist:", binary_search(intlist, 50))
#Want to see something else interesting? Because of the way Python handles types, this exact same
#function works for any sortable data type. Check it out with strings:
strlist = ["David", "Joshua", "Marguerite", "Jackie"]
print("David is in strlist:", binary_search(strlist, "David"))
print("Lucy is in strlist:", binary_search(strlist, "Lucy"))
#Or with dates!
from datetime import date
datelist = [date(1885, 10, 13), date(2014, 11, 29), date(2016, 11, 26)]
print("10/13/1885 is in datelist:", binary_search(datelist, date(1885, 10, 13)))
print("11/28/2015 is in datelist:", binary_search(datelist, date(2015, 11, 28)))

# range iterates with one index value at a time for long list
for i in range(6):
    print(i)

# looping over collection fast
colors = ['red', 'green', 'blue', 'yellow']

for color in colors:
    print(color)

# loop collection backwards
for color in reversed(colors):
    print(color)

# looping collection and indexes at same time
for i, color in enumerate(colors):
    print(i, '-->', colors[i])

# looping over two collections at once
names = ['petras', 'jonis', 'simas', 'domas']

# izip creates indexes
for name, color in izip(names, colors):
    print(name, '-->', color)

# looping and sorted
for color in sorted(colors):
    print(color)

# looping over sorted reversed list
for color in sorted(colors, reverse=True):
    print(color)

# custom sort order
print sorted(colors,key=len)

# call function until sentinel value (second parameter)
blocks = []
for block in iter(partial(f.read, 32), ''):
    blocks.append(block)

# multiple exit in for loop
def find(seq, target):
    for i, value in enumerate(seq):
        if value == target:
            break
    else:
        return -1
    return i

# looping over dictionary keys
dict_names = {'mike': 23, 'dan': 50, 'rose': 45, 'bel': 16}

for k in dict_names:
    print(k)

# ---- https://www.youtube.com/watch?v=OSGv2VnC0go
# makes new list of keys
for k in dict_names.keys():
    if k.startswith('m'):
        del(dict_names[k])
# or:
dict_names = {k : dict_names[k] for k in dict_names if not k.startswith('m')}

#looping over dictionary keys and values
# .items() create new big list iteritems() return iterator
for k, v in dict_names.iteritems():
    print(k,'-->',v)

# construct dictionary from two lists. First for keys, second for values
d = dict(izip(names, colors))
# construct a dictionary from one list to have keys 0,1,2...
d = dict(enumerate(names))

# count list members to dictionary results
colors = ['red', 'green', 'red', 'blue', 'green', 'red']
d = {}
for color in colors:
    if color not in d:
        d[color] = 0
    d[color] += 1
# better way:
d = {}
for color in colors:
    d[color] = d.get(color, 0) + 1
# or :
d = defaultdict(int)
for color in colors:
    d[color] += 1

# grouping with dictionaries
# traditional way
d = {}
for name in names:
    key = len(name)
    if key not in d:
        d[key] = []
    d[key].append(name)
# other way
d = {}
for name in names:
    key = len(name)
    d.setdefault(key, []).append(name)
# best way
d = defaultdict(list)
for name in names:
    key = len(name)
    d[key].append(name)

# popitem atomic
while dict_names:
    key, value = dict_names.popitem()
    print(key, '-->', value)

# linking dictionaries
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args([])
command_line_args = {k:v for k,v in
                    vars(namespace).items() if v}
# copy dictionary - standard way
d = dict_names.copy()
d.update(os.environ)
d.update(command_line_args)

# pythonic way
d = ChainMap(command_line_args, os.environ, dict_names)

# named arguments
twitter_search('@obama', False, 20, True) # bad, unknown arguments
twitter_search('@obama', retweets=False, numtweets=20, popular=True) # good

# without named tuples
doctest.testmod()
(0, 4) # output
# with named tuples: better
TestResults = namedtuple('TestResults', ['failed', 'attempted'])
doctest.testmod()
TestResults(failed=0, attempted=4) # output

# unpacking sequences
# other programming language:
p = '[raymond', 'hettinger', 0x30, 'python@example.com']
fname = p[0]
lname = p[1]
age = p[2]
email = p[3]
# pythonic way:
fname, lname, age, email = p

# updating multiple state variables
# other langages:
def fibonacci(n):
    x = 0
    y = 1
    for i in range(n):
        print x
        t = y
        y = x + y
        x = t
# pythonic way:
def fibonacci(n):
    x, y = 0, 1
    for i in range(n):
        print x
        x, y = y, x + y
# np way:
tmp_x = x + dx * t
tmp_y = y + dy * t
tmp_dx = influence(m, x, y, dx, dy, partial='x')
tmp_dy = influence(m, x, y, dx, dy, partial='y')
x = tmp_x
y = tmp_y
dx = tmp_dx
dy = tmp_dy
# p way first executes code from right side, then left side:
x, y, dx, dy = (x + dx * t,
                y + dy * t,
                influence(m, x, y, dx, dy, partial='x'),
                influence(m, x, y, dx, dy, partial='y'))

# concatenating strings
# wrong:
c = colors[0]
for color in colors[1:]:
    c += ', ' + color
print(c)
# pythonic way:
print ', '.join(colors)

# updating sequences of very long size
# wrong:
del colors[0] # or
colors.pop(0) # or
colors.insert(0, 'black')
# pythonic way:
c = deque(colors) # and then del, pop ir insert

# decorators. Routing function with cache
# bad! not reusable
def web_lookup(url, saved={}):
    if url in saved:
        return saved[url]
    page = urllib.urlopen(url).read()
    saved[url] = page
    return page
# pythonic router:
@cache
def web_lookup(url):
    return urllib.urlopen(url).read()
# cache function in other file
def cache(func):
    saved = {}
    @wraps(func)
    def newfunc(*args):
        if args in saved:
            return newfunc(*args)
        result = func(*args)
        saved[args] = result
        return result
    return newfunc

# temporary context
# bad
old_context = getcontext().copy()
getcontext().prec() = 50
print Decimal(355) / Decimal(113)
setcontext(old_context)
# pythonic:
with localcontext(Context(prec=50)):
    print Decimal(355) / Decimal(113)

# traditional way of open / close files
f = open('data.txt')
try:
    data = f.read()
finally:
    f.close()
# pythonic:
with open('data.txt') as f:
    data = f.read()

# make a lock
lock = treading.Lock()
# old way
lock.acquire()
try:
    print('Critical section 1')
    print('Critical section 2')
finally:
    lock.release()
# new way
with lock:
    print('Critical section 1')
    print('Critical section 2')

# factor out temporary context
try:
    os.remove('somefile.tmp')
except OSError:
    pass
# better:
with ignored(OSError): # vvvv uses function below vvvvvvv
    os.remove('somefile.tmp')

# context manager: ignored()
@contextmanager
def ignored(*exceptions):
    try:
        yield
    except exceptions:
        pass

# factor out temporary contexts
with open('help.txt', 'w') as f:
    oldstdout = sys.stdout
    sys.stdout = f
    try:
        help(pow)
    finally:
        sys.stdout = oldstdout
# better:
with open('help.txt', 'w') as f:
    with redirect_stdout(f): # vvvv function below vvvvv
        help(pow)
# context manager: redirect_stdout()
@contextmanager
def redirect_stdout(fileobj):
    oldstdout = sys.stdout
    sys.stdout = fileobj
    try:
        yield fileobj
    finally:
        sys.stdout = oldstdout

# write code as sentence of business logic, its easier to understand.
# bad:
result = []
for i in range(10):
    s = i ** 2
    result.append(s)
print sum(result)
# good: (generator expressions)
print sum(i**2 for i in range(10))

# class developement toolkit: https://www.youtube.com/watch?v=HTLu2DFOdTg
# architecture - problem -> solution
# start with documentation, first class with comments and no code
import math

class Circle(object):  # new style class inheriting from Object
    'advanced chat robot'
    version = '0.1' # class variable, dont use float, use string for 'version'

    # flyweight design pattern suppresses
    __slots__ = ['diameter'] # the instance dictionary
    # slots cannot be inherited, so inheriting gets rid of it

    def __init__(self, radius): # init isnt a constructor,
        self.radius = radius  # set required instance variable

    # use imported modules and parameters for better self addapting code
    def area(self):
        # return math.pi * self.radius ** 2.0 # changed by client request
        p = self.__perimeter()
        r = p / math.pi / 2.0
        return math.pi * r ** 2.0

    def perimeter(self):
        return 2.0 * math.pi * self.radius

     # make a copy in case subclass overwrites it
    __perimeter = perimeter # but if the client will copy it too...
    # double underscore used to in case 'to be only you, not children'

    @classmethod  # alternative constructor
    def from_bbd(cls, bbd):
        # using different parameter name 'cls',
        # to separate instances when subclassing
        'Construct a circle from a bounding box diagonal'
        radius = bbd / 2.0 / math.sqrt(2.0)
        return Circle(radius)

    # as it has nothing to do with instance parameters,
    # convert this method to static. Attach functions to classes
    @staticmethod
    def angle_to_grade(angle):
        'Convert angle in degree to a percentage grade'
        return math.tan(math.radians(angle)) * 100.0

    @property  # convert dotted access to method calls
    def radius(self):
        'Radius of a circle'
        return self.diameter / 2.0

    @radius.setter
    def radius(self, radius):
        self.diameter = radius * 2.0

# lean startup filosofy says do not throw too mutch stuff into classes
# when you still dont know is it will be needed.
# Start with minimum vialable product,
# more you throuw in less agile you get. Ship it!

# Tutorial
print('Circuituous version', Circle.version)
c = Circle(10)
print('A circle of radius', c.radius)
print('has an area of', c.area())

# first customer: academia students
from random import random, seed

seed(8675309)
print('using circuituous(tm) version', Circle.version)
n = 10
circles = [Circle(random()) for i in range(n)]
print('The average area of', n, 'random circles')
avg = sum([c.area() for c in circles]) / n
print('is %.1f' % avg)

# second customer: rubber sheet company
cuts = [0.1, 0.7, 0.8]
circles = [Circle(r) for r in cuts]
for c in circles:
    print('A circles with a radius of', c.radius)
    print('has a perimeter of', c.perimeter())
    print('and a cold area of', c.area())
    c.radius *= 1.1
    print('and warm area of', c.area())

# third customer: national tire chain
class Tire(Circle):
    'tires are circles with a corrected perimeter'
    # no init found, so it calls Circle class init
    # when parent gets call'ed that action is 'extending'
    # if parent isnt call'ed at all it is 'overwriting'
    def perimeter(self):
        'circumference corrected for the rubber'
        return Circle.perimeter(self) * 1.25

t = Tire(22)
print('A tire of radius', t.radius)
print('has an inner area of', t.area())
print('and an odometer corrected perimeter of', t.perimeter())

# next customer: national graphics company
c = Circle(b.from_bbd(25.1))
print('A circle with a bbd of 25.1')
print('haas a radius of', c.radius)
print('an an area of', c.area())

# new customer request: add a function
# but it is only in plain 2D geometry, not 3D
# converted to static method

# new customer government request: ISO-11110
# dont mix perimeter and radius

# new government request: ISO-2220
# do not let access radius parameter

# Academic request: many circles
n = 10000000
seed(8675309)
print('Using Circuituous(tm) version', Circle.version)
circles = [Circle(random()) for i in range(n)]
print('The average area of', n, 'random circles')
avg = sum([c.area() for c in circles]) / n
print('is %.1f' avg)
# use flyweight desing pattern: use slots

# Raymond Hetinger - super considered super
# https://www.youtube.com/watch?v=EiOglTERPEo
# any other language - super: calls parent class
# inheritance have diamond structure
# inheritance - dad can i use a car?
# multiple inheritance - dad can i use a car? - no. mom an i use a car?
# Python super call parent, but not your parents.
# mra - methodic resolution algorythm: call next in line
class Adam(object): pass
class Eve(object): pass
class Ramon(Adam, Eve): pass
class Gayle(Adam, Eve): pass
class Raymond(Ramon, Gayle): pass
class Dennis(Adam, Eve): pass
class Sharon(Adam, Eve): pass
class Rachel(Dennis, Sharon): pass
class Matthew(Raymond, Rachel): pass
help(Matthew)

# pizza example
class DoughFactory(object):
    def get_dough(self):
        return 'insecticide treated wheat dough'

class Pizza(DoughFactory):
    def order_pizza(self, *toppings):
        print('Getting dough')
        dough = super().get_dough() # DoughFactory.get_dough() # <-- DRY principle here
        print(f"Making pie with {dough}")
        for topping in toppings:
            print(f"Adding: {topping}")
# if __name__ == '__main__':
#     Pizza().order_pizza('Pepperoni', 'Bell Pepper')

class OrganicDoughFactory(DoughFactory):
    def get_dough(self):
        return 'pure untreated wheat dough'

# initializing OrganicDoughFactory, then Pizza
class OrganicPizza(Pizza, OrganicDoughFactory): pass
if __name__ == '__main__':
    OrganicPizza().order_pizza('Pepperoni', 'Bell Pepper')

# Robot example
class Robot(object):
    'Sophisticated class that moves a real robot'
    # don't wear down real robots by running tests!
    def fetch(self, tool):
        print('Physical Movement! Fetching')
    def move_forward(self, tool):
        print('Physical Movement! Moving forward.')
    def move_backward(self, tool):
        print('Physical Movement! Moving backward.')
    def replace(self, tool):
        print('Physical Movement! Replacing.')

class CleaningRobot(Robot):
    'Custom robot that can clean with a given tool'
    def clean(self, tool, times=10):
        super().fetch(tool)
        for i in range(times):
            super().move_forward(tool)
            super().move_backward(tool)
        super().replace(tool)
if __name__ == '__main__':
    t = CleaningRobot()
    t.clean('broom')

# proper class usage:
# in parent provide a toolkit
# in a child excercises that toolkit in some way
# write tests, do not wear robot actually
class MockBot(Robot):
    'Simulate a real robot by merely recording tasks'
    def __init__(self):
        self.tasks = []
    def fetch(self, tool):
        self.tasks.append(f'fetching {tool}')
    def move_forward(self, tool):
        self.tasks.append(f'foward {tool}')
    def move_backward(self, tool):
        self.tasks.append(f'backward {tool}')
    def replace(self, tool):
        self.tasks.append(f'replace {tool}')
# this class makes sure MockBot is initialized instead of original Robot
class MockedCleaningRobot(CleaningRobot, MockBot):
    'Inject a mock bot into the robot dependency'

class TestCleaningRobot(unittest.TestCase):
    def test_clean(self):
        t = MockedCleaningRobot()
        t. clean('mop')
        expected = (['fetching mop'] +
                    ['forward mop', 'backward mop'] * 10 +
                    ['replace mop'])

# if __name__ == '__main__':
unittest.main(argv=['first-arg-is-ignored'], exit=False) # exit=False

# other example
from __future__ import print_function
from collections import Counter, OrderedDict

class OrderedCounter(Counter, OrderedDict):
    'Counter that remembers the order elements are first seen'
    def __reduce__(self):
        return '%s(%r)' % (self.__class__.__name__,
                            OrderedDict(self))
    def __reduce__(self):
        return self.__class__, (OrderedDict(self),)

oc = OrderedCounter('abracadabra')
print(oc)
# linearisation algorithm: childer go before their parents -
# and parents stay in order
# ! cooperative multiple inheritance:
# I design tree of classes where everybody is cooperating:
# means everybody says: "next in line".
# - Use keyword arguments, because you dont know in advance
# what you are calling and you dont know what arguments their going to need,
# only they know which ones they need, but they dont know
# what they are calling in advance.
# - If class in not cooperative, wrap it in cooperative sub class wrapper
# in the end of the chain 'stopper' class is needed.

##### data clases
# data structure with named fields, type annotations, and default values
from dataclasses import dataclass, asdict, astuple, replace
'dataclass example'
@dataclass
class Color:
    hue: int
    saturation: float
    lightness: float = 0.5

c = Color(33, 1.0)
print(c)
print(c.hue, c.saturation, c.lightness)

print(replace(c, hue=120))
# print(c) # this prints hue=33

print(asdict(c))

print(astuple(c))

print(c.__annotations__)

from typing import NamedTuple
'tuples example'
class Color(NamedTuple):
    hue: int
    saturation: float
    lightness: float = 0.5

c = Color(33, 1.0)
print(c)
print(c.hue, c.saturation, c.lightness)
print(c._replace(hue=120))
print(c) # this prints hue=33

print(c._asdict())

print(tuple(c))

print(c.__annotations__)

hue, saturation, lightness = c # get individual values from tuple
print(hue, saturation, lightness)

#### data clases autogenerate code:
# __init__, __repr__, __eq__, __hash__,
# __dataclass_params__, __dataclass_fields__

#### Freezing and Ordering
# dataclasses are MUTABLE, but it can be set IMMUTABLE
# by 'freezing' them using 'frozen' parameter
# dataclasses are not ordered by default, but it can be done
# using 'order' parameter
from pprint import pprint

@dataclass(order=True, frozen=True)
class Color:
    hue: int
    saturation: float
    lightness: float = 0.5

colors = [Color(33, 1.0),
          Color(66, 0.75),
          Color(99, 0.5),
          Color(66, 0.75)]
# pprint(colors)
pprint(sorted(colors))
pprint(set(colors)) # set removes dublicates

## with multiple instances autogenerated code have:
# __lt__, __le__, __gt__, __ge__ - for stronger check, comparison
# __setattr__, __delattr__ for freezing, prevent delete and set attributes
# __hash__
from dataclasses import dataclass, field, fields
# from verbose_dataclasses import dataclass, field
from datetime import datetime
from pprint import pprint

@dataclass(order=True, unsafe_hash=True)
class Employee:
    emp_id: int = field()
    name: str = field()
    gender: str = field()
    salary: int = field(hash=False, repr=False, metadata={'units': 'bitcoin'})
    age: int = field(hash=False)
    viewed_by: list = field(default_factory=list, compare=False, repr=False)

    def access(self, viewer_id):
        self.viewed_by.append((viewer_id, datetime.now()))

e1 = Employee(emp_id='3536465054',
            name = 'Rachel Hettinger',
            gender = 'female',
            salary = 22,
            age = 0x30,)

e2 = Employee(emp_id='4054646353',
            name = 'Martin Murchison',
            gender = 'male',
            salary = 20,
            age = 0x30,)

e1.access('Roger Wastun')
e1.access('Shelly Summers')

pprint(e1.viewed_by)
pprint(sorted([e1, e2]))

assignments = {e1: 'gather requirements', e2: 'write tests'}
pprint(assignments)

pprint(fields(e1)[3])
