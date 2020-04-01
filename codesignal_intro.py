# codesignal level1 n2
def centuryFromYear(year):
    return (year - 1) // 100 + 1
# tests
print('century from hear 1905: ',centuryFromYear(1905)) # expected 20
print('century from hear 1700: ',centuryFromYear(1700)) # expected 17

#  codesignal level1 n3
def checkPalindrome(inputString):
    length = len(inputString)
    mid = length // 2
    return inputString[:mid-1:-1] == inputString[:mid] if length%2 == 0 else inputString[:mid] == inputString[:mid:-1]
# tests
print('checkPalindrome: "aabaa", expected True is: ',checkPalindrome("aabaa"))
print('checkPalindrome: "abac",  expected False is: ',checkPalindrome("abac"))
print('checkPalindrome: "a", expected True is: ',checkPalindrome("a"))
print('checkPalindrome: "abacaba", expected True is: ',checkPalindrome("abacaba"))

# codesignal level2 n1
def adjacentElementsProduct(inputArray):
    result = 0
    temp = 0
    for i in range(len(inputArray)):
        if i == 0:
            continue
        temp = inputArray[i-1] * inputArray[i]
        if result == 0:
            result = temp
        else :
            result = temp if temp > result else result
    return result
# tests
print('max of two multiplied members in list: [3, 6, -2, -5, 7, 3] is 21 = ',adjacentElementsProduct([3, 6, -2, -5, 7, 3]))
print('max of two multiplied members in list: [5, 1, 2, 3, 1, 4] is 6 = ',adjacentElementsProduct([5, 1, 2, 3, 1, 4]))

# codesignal level2 n2 - polygon shape area calculator
def shapeArea(n):
    return (n * n) + ((n - 1) * (n - 1))
# tests
print('polygon area of 2 squares is 5 = ',shapeArea(2))
print('polygon area of 7000 squares is 97986001 = ',shapeArea(7000))

# codesignal level2 n3 - find missing numbers count if list becomes sorted
def makeArrayConsecutive2(statues):
    full = list( range( min(statues), max(statues) ) )
    result = []
    for i in range( 0, len(full) ):
        if full[i] not in statues:
            result.append( full[i] )
    return len( result )
# tests
print('missing numbers count in list [6, 2, 3, 8] is 3 = ',makeArrayConsecutive2([6, 2, 3, 8]))
print('missing numbers count in list [6, 2, 10, 3, 15, 8] is 8 = ',makeArrayConsecutive2([6, 2, 10, 3, 15, 8]))

# codesignal level2 n4 - is it possible to get increasing sequence by removing only 1 member
def almostIncreasingSequence(sequence):
    j = first_bad_pair(sequence)
    if j == -1:
        return True  # List is increasing
    if first_bad_pair(sequence[j - 1:j] + sequence[j + 1:]) == -1:
        return True  # Deleting earlier element makes increasing
    if first_bad_pair(sequence[j:j + 1] + sequence[j + 2:]) == -1:
        return True  # Deleting later element makes increasing
    return False
# additional function for l2 n2 - almostIncreasingSequence
def first_bad_pair(sequence):
    for i in range(len(sequence) - 1):
        if sequence[i] >= sequence[i + 1]:
            return i
    return -1
# tests
print('almostIncreasingSequence of [1, 3, 2, 1] is false = ',almostIncreasingSequence([1, 3, 2, 1]))
print('almostIncreasingSequence of [123, -17, -5, 1, 2, 3, 12, 43, 45] is true = ',almostIncreasingSequence([123, -17, -5, 1, 2, 3, 12, 43, 45]))

# codesignal level2 n5 - matrix of ghosts
def matrixElementsSum(matrix):
    result = 0
    ignore = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > 0 and j not in ignore:
                result += matrix[i][j]
            elif matrix[i][j] == 0 and j not in ignore:
                ignore.append(j)
    return result
# tests
print('matrix of ghosts [[0,1,1,2],[0,5,0,0],[2,0,3,3]] sum is 9 = ',matrixElementsSum([[0,1,1,2],[0,5,0,0],[2,0,3,3]]))
print('matrix of ghosts [[4,0,1],[10,7,0],[0,0,0],[9,1,2]] sum is 15 = ',matrixElementsSum([[4,0,1],[10,7,0],[0,0,0],[9,1,2]]))

# codesignal level3 n1 - find longest string in list and how many have same length
def allLongestStrings(inputArray):
    result = []
    longest = max(inputArray, key=len)
    length = len(longest)
    for i in inputArray:
        if len(i) == length:
            result.append(i)
    return result
# tests
print('all longest strings of ["aba","aa","ad","vcd","aba"] is ["aba","vcd","aba"] = ',allLongestStrings(["aba","aa","ad","vcd","aba"]))
print('all longest strings of ["abc","eeee","abcd","dcd"] is ["eeee","abcd"] = ',allLongestStrings(["abc","eeee","abcd","dcd"]))

# codesignal level3 n2
def commonCharacterCount(s1, s2):
    result = 0
    ignore = []
    for i in s1:
        for j in range(len(s2)):
            if i == s2[j] and j not in ignore:
                ignore.append(j)
                result += 1
                break
    return result
# tests
print('commonCharacterCount of "aabcc" and "adcaa" is 3 = ',commonCharacterCount("aabcc","adcaa"))
print('commonCharacterCount of "zzzz" and "zzzzzzz" is 4 = ',commonCharacterCount("zzzz","zzzzzzz"))
print('commonCharacterCount of "abca" and "xyzbac" is 3 = ',commonCharacterCount("abca","xyzbac"))

# codesignal level3 n3 - lottery win when one half of matrix sum is equal to other half
def isLucky(n):
    half = len(list(n)) // 2
    sum1 = 0
    sum2 = 0
    for i in n[:half]:
        sum1 += int(i)
    for j in n[half:]:
        sum2 += int(j)
    return sum1 == sum2
# tests
print('the ticket with "134008" is lucky: true = ',isLucky('134008'))
print('the ticket with "239017" is lucky: false = ',isLucky('239017'))

# codesignal level3 n4 - sort low to high humans ignoring trees
def sortByHeight(a):
    new = []
    tmp = []
    for v in a:
        if v != -1:
            tmp.append(v)
    tmp.sort()
    z = 0
    for j,x in enumerate(a):
        if x == -1:
            new.insert(j, x)
        else:
            new.insert(j, tmp[z])
            z += 1
    return new

# tests
print('sorted: ',sortByHeight([-1, 150, 190, 170, -1, -1, 160, 180]))
print('sorted: ',sortByHeight([23, 54, -1, 43, 1, -1, -1, 77, -1, -1, -1, 3]))

# codesignal level3 n5 - invert string in parentheses
def reverseInParentheses(inputString):
    stack = []
    for x in inputString:
        if x == ")":
            tmp = ""
            while stack[-1] != "(":
                tmp += stack.pop()
            stack.pop() # pop the (
            for item in tmp:
                stack.append(item)
        else:
            stack.append(x)

    return "".join(stack)

# tests "(bar)"
print('==========\n1) inverted: ',reverseInParentheses("(bar)")) # expected "rab"
print('==========\n2) inverted: ',reverseInParentheses("foo(bar)baz")) # expected "foorabbaz"
print('==========\n3) inverted: ',reverseInParentheses("foo(bar)baz(blim)")) # expected "foorabbazmilb"
print('==========\n4) inverted: ',reverseInParentheses("foo(bar(baz))blim"))  # expected "foobazrabblim"

# codesignal level4 n1 - alternating sums
def alternatingSums(a):
    return [sum(a[::2]), sum(a[1::2])]

# tests
print('==========\n1) inverted: ',alternatingSums([50, 60, 60, 45, 70])) # expected [180, 105]
print('==========\n2) inverted: ',alternatingSums([100, 50])) # expected [100, 50]
print('==========\n3) inverted: ',alternatingSums([100, 50, 10, 20, 30, 40])) # expected [140, 110]

# codesignal level4 n2 - alternating sums
def addBorder(picture):
    output = []
    border = ""
    for i in range(0,len(picture[0])+2):
        border += "*"
    output.append(border)
    for i in range(0,len(picture)):
        output.append("*"+picture[i]+"*")

    output.append(border)

    return output

# tests
print('==========\n1) bordered: ',addBorder(["abc","ded"])) # expected
print('==========\n2) bordered: ',addBorder(["a"])) # expected

# codesignal level4 n3 - similar when swapping at least 2 array members
def areSimilar(a, b):
    if a == b: return True 
    not_same = []
    tmp = b
    for i,v in enumerate(a):
        # when more than 2 elements values do not match 
        if len(not_same) > 2: return False #  result is false
        # when value of same index in both lists do not match
        if v != b[i]: not_same.append(i) # remember the value that did not matched
    if len(not_same) == 2:
        tmp[not_same[1]], tmp[not_same[0]] = b[not_same[0]], b[not_same[1]]
        print(f"a: {a}, b: {b}, tmp: {tmp}, not_same: {not_same}")
        return True if tmp == a else False
    return False
# tests
print('=========\n1) areSimilar is false =', areSimilar([1, 1, 4], [1, 2, 3]))
print('=========\n2) areSimilar is false =', areSimilar([1, 2, 2], [2, 1, 1]))
print('=========\n3) areSimilar false =', areSimilar([832, 998, 148, 570, 533, 561, 894, 147, 455, 279], [832, 570, 148, 998, 533, 561, 455, 147, 894, 279]))

# codesignal level4 n4 -
def arrayChange(inputArray):
    sum = 0
    q = inputArray[0]
    for i in inputArray[1:]:
        if i <= q:
            sum += q-i+1
            q = q+1
        else:
            q = i
    return sum

# tests
print('=========\n1) arrayChange is 3 =', arrayChange([1, 1, 1]))
print('=========\n2) arrayChange is 5 =', arrayChange([-1000, 0, -2, 0]))

# codesignal level4 n5 -
def palindromeRearranging(inputString):
    r = {}
    for v in inputString:
        if v not in r:
            r[v] = 1
        else:
            r[v] += 1
    count = [x for x in r if r[x] % 2]
    if len(count) > 1:
        return False
    else:
        return True
# tests
print('=========\n1) palindromeRearranging is true =', palindromeRearranging("aabb"))
print('=========\n2) palindromeRearranging is false =', palindromeRearranging("abca"))

# codesignal level5 n1 -
def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    return True if yourLeft == friendsLeft and yourRight == friendsRight or yourLeft == friendsRight and yourRight == friendsLeft else False
# tests
print('=========\n1) areEquallyStrong is true =', areEquallyStrong(10, 15, 15, 10))
print('=========\n2) areEquallyStrong is false =', areEquallyStrong(15, 10, 15, 9))

# codesignal level5 n2 -
def arrayMaximalAdjacentDifference(inputArray):
    diff = 0
    tmp = inputArray[0]
    for i in inputArray[1:]:
        if tmp > i and diff < tmp - i:
            diff = tmp - i
        if tmp < i and diff < i - tmp:
            diff = i - tmp
        tmp = i
    return diff
# tests
print('=========\n1) arrayMaximalAdjacentDifference is 2 =',
    arrayMaximalAdjacentDifference([10, 11, 13]))
print('=========\n2) arrayMaximalAdjacentDifference is 0 =',
    arrayMaximalAdjacentDifference([1, 1, 1, 1]))
print('=========\n3) arrayMaximalAdjacentDifference is 7 =',
    arrayMaximalAdjacentDifference([-1, 4, 10, 3, -2]))

# codesignal level5 n3 -
def isIPv4Address(inputString):
    splited = inputString.split('.')
    if len(splited) != 4:
        return False
    for x in splited:
        if x == '' or not x.isdigit() or int(x) < 0 or 255 < int(x):
            return False
    return True
# tests
print('=========\n1) isIPv4Address is true =', isIPv4Address("172.16.254.1"))
print('=========\n2) isIPv4Address is false =', isIPv4Address("172.316.254.1"))
print('=========\n3) isIPv4Address is false =', isIPv4Address(".254.255.0"))

# codesignal 22
def avoidObstacles(inputArray):
    for i in range(1, max(inputArray)):
        divs = any([x for x in inputArray if not x%i])
        if not divs:
            return i
    return max(inputArray) + 1
# tests
print(avoidObstacles([5, 3, 6, 7, 9]))
print(avoidObstacles([2, 3]))
print(avoidObstacles([1, 4, 10, 6, 2]))

# codesignal 23
def pixel(matrix,i,j):
    total = 0
    for x in range(i - 1, i + 2):
        for y in range(j - 1, j + 2):
            total += matrix[x][y]
    return total//9

def boxBlur(image):
    sol = []
    row = len(image)
    col = len(image[0])
    for i in range(1, row - 1):
        temp = []
        for j in range(1, col - 1):
            temp.append(pixel(image, i, j))
        sol.append(temp)
    
    return sol
# tests
print(boxBlur([[1,1,1], 
               [1,7,1], 
               [1,1,1]]), 'result should be: [[1]]')
print(boxBlur([[36,0,18,9], 
                [27,54,9,0], 
                [81,63,72,45]]), 'result should be: [[40,30]]')