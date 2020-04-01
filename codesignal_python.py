# --- PYTHON ---

# 5)
def countBits(n):
    return n.bit_length()
# tests
print('=======\n1) bits: ', countBits(50)) # expected 6
print('=======\n2) bits: ', countBits(1000000000)) # expected 30

# 6)
def modulus(n):
    if float(n).is_integer():
        return n % 2
    else:
        return -1
# tests
print('=======\n1) expected modulus of 15 is 1 = ', modulus(15))
print('=======\n2) expected modulus of 232.2423 is -1 = ', modulus(232.2423))

# 7)
def simpleSort(arr):

    n = len(arr)

    for i in range(n):
        j = 0
        stop = n - i
        while j < stop - 1:
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j += 1
    return arr
# tests
print('=======\n1) sorted arr [2, 4, 1, 5] = ', simpleSort([2, 4, 1, 5]))
print('=======\n2) sorted arr [3, 6, 1, 5, 3, 6] = ', simpleSort([3, 6, 1, 5, 3, 6]))

# 8)
def baseConversion(n, x):
    return hex(int(n, x))[2:]
# tests
print('=========\n1) base convert of "1302", 5 expected "ca" =', baseConversion('1302', 5))
print('=========\n2) base convert of "1010100101", 2 expected "2a5" =', baseConversion('1010100101', 2))

# 9)
def mexFunction(s, upperBound):
    found = -1
    for i in range(upperBound):
        if not i in s:
            found = i
            break
    else:
        return upperBound

    return found
# tests
print('=========\n1) mex of [0, 4, 2, 3, 1, 7] and upper 10 is 5 =', mexFunction([0, 4, 2, 3, 1, 7] , 10))
print('=========\n2) mex of [] and upper 15 is 0 =', mexFunction([], 15))

# 10)
def listBeautifier(a):
    res = a[:]
    while res and res[0] != res[-1]:
        first, *res, last = res
    return res
# tests
print('=========\n1) beautified list of [3, 4, 2, 4, 38, 4, 5, 3, 2] is [4, 38, 4] =', listBeautifier([3, 4, 2, 4, 38, 4, 5, 3, 2]))
print('=========\n2) beautified list of [1, 4, -5] is [4] =', listBeautifier([1, 4, -5]))

# 11)
def fixMessage(message):
    return message.capitalize()
# tests
print('=========\n1) capitalize:', fixMessage("you'll NEVER believe what that 'FrIeNd' of mine did!!1"))
print('=========\n2) capitalize:', fixMessage("LOL you've GOT to hear this one XDD"))

# 12)
def catWalk(code):
    return " ".join(code.split())
# tests
print('=========\n1) catWalk spaces:', catWalk("def      m   e  gaDifficu     ltFun        ction(x):"))
print('=========\n2) catWalk spaces:', catWalk("      for      i      in         ra   nge(x,   29):"))

# 13)
def convertTabs(code, x):
    return (x*' ').join(code.split('\t'))
# tests
print('=========\n1) convertTabs:', convertTabs("\treturn False", 4))
print('=========\n2) convertTabss:', convertTabs("def add(x, y)\f\treturn x + y", 8))

# 14)
import textwrap
def feedbackReview(feedback, size):
    return textwrap.wrap(feedback, size)
# tests
print('=========\n1) feedbackReview:', feedbackReview("This is an example feedback", 8))
print('=========\n2) feedbackReview:', feedbackReview("Dude, do you even review these feedbacks?", 16))

# 15)
def isWordPalindrome(word):
    return word == word[::-1]
# tests
print('=========\n1) isWordPalindrome expected true =', isWordPalindrome("aibohphobia"))
print('=========\n2) isWordPalindrome expected false =', isWordPalindrome("hehehehehe"))

# 16)
def permutationCipher(password, key):
    table = password.maketrans("abcdefghijklmnopqrstuvwxyz",key)
    return password.translate(table)
# tests
print('=========\n1) permutationCipher converted password "hzlsgdadrs" =', permutationCipher("iamthebest","zabcdefghijklmnopqrstuvwxy"))
print('=========\n2) permutationCipher converted password "tvyfjaumezovtij" =', permutationCipher("codesignalrocks","ebtyfkudagizxmvcnojqwlsrhp"))

# 17)
def competitiveEating(t, width, precision):
    # return '{:^{}}'.format(round(t, precision),width)
    return '{1:.{0}f}'.format(precision, round(t, precision)).center(width)
# tests
print('=========\n1) competitiveEating: "   3.14   " =', competitiveEating(3.1415, 10, 2))
print('=========\n2) competitiveEating: "    30    " =', competitiveEating(29.8245, 10, 0))
print('=========\n3) competitiveEating: "    837.2847200     " =', competitiveEating(837.28472, 20, 7))

# 18)
import re
def newStyleFormatting(s):
    return "%".join([re.sub("%([bcdeEfFgGnosxX])","{}", S) for S in s.split("%%")])
# tests
print('=========\n1) newStyleFormatting: {}%  =', newStyleFormatting("We expect the %f%% growth this week"))
print('=========\n2) newStyleFormatting: {}%  =', newStyleFormatting("%d%d%%-growth in products is expected quite soon"))

# 20)
def getCommit(commit):
    return ''.join(c for c in commit if c not in set('0?!+'))
# tests
print('=========\n1) getCommit: someCommIdhsSt =', getCommit("0??+0+!!someCommIdhsSt"))
print('=========\n2) getCommit: "" =', getCommit("?????!+0"))

# 22)
def listsConcatenation(lst1, lst2):
    res = lst1
    res.extend(lst2)
    return res
# tests
print('=========\n1) listsConcatenation: [2, 2, 1, 10, 11] =', listsConcatenation([2, 2, 1],[10, 11]))
print('=========\n2) listsConcatenation: [5, 3, -2, 0] =', listsConcatenation([],[5, 3, -2, 0]))

# 23)
def twoTeams(students):
    return sum(students[::2]) - sum(students[1::2])
# tests
print('=========\n1) twoTeams: sum subtraction is 11 =', twoTeams([1, 11, 13, 6, 14]))
print('=========\n2) twoTeams: sum subtraction is -1 =', twoTeams([3, 4]))
print('=========\n3) twoTeams: sum subtraction is -38 =', twoTeams([23, 72, 54, 4, 88, 91, 8, 44]))


# 24)
def removeTasks(k, toDo):
    del toDo[k-1::k]
    return toDo
# tests
print('=========\n1) result [1237, 2847, 2947, 1, 374827, 22] \nis',
    removeTasks(3, [1237, 2847, 27485, 2947, 1, 247, 374827, 22]))
print('=========\n2) result [] =\nis',
    removeTasks(1, [1237, 2847, 27485, 2947, 1, 247, 374827, 22]))
print('=========\n3) result [1237] =\nis',
    removeTasks(10, [1237]))

# 25) print text with all list
def printList(lst):
    return f"This is your list: {lst}"
# tests
print('=========\n1) This is your list: [1, 2, 3, 4, 5] \n=', printList([1, 2, 3, 4, 5]))
print('=========\n2) This is your list: [71] \n=',printList([71]))
