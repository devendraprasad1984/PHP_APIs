"""
There is a horizontal row of  cubes. The length of each cube is given. You need to create a new vertical pile of cubes. The new pile should follow these directions: if  is on top of  then .

When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time. Print "Yes" if it is possible to stack the cubes. Otherwise, print "No". Do not print the quotation marks.

Input Format

The first line contains a single integer , the number of test cases.
For each test case, there are  lines.
The first line of each test case contains , the number of cubes.
The second line contains  space separated integers, denoting the sideLengths of each cube in that order.

Constraints



Output Format

For each test case, output a single line containing either "Yes" or "No" without the quotes.

Sample Input

2
6
4 3 2 1 3 4
3
1 3 2
Sample Output

Yes
No
Explanation

In the first test case, pick in this order: left - , right - , left - , right - , left - , right - .
In the second test case, no order gives an appropriate arrangement of vertical cubes.  will always come after either  or .
"""



# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

# for _ in range(int(input())):
#     n,l=int(input()), list(map(int,input().split()))
#     dq=deque(l)
#     left,right=dq.popleft(),dq.pop()
#     check=[]
#     if n%2!=0:
#         print("No")
#     else:
#         for x in range(n//2):
#             if right>=left:
#                 check.append(True)
#         print("Yes" if all(check) else print("No"))


for _ in range(int(input())):
    n = input()
    d = deque()
    d.extend( list(input().split()) )
    for i in range(int(n)):
        try:
            if d[0] < d[1] and d[-1] < d[-2]:
                print("No")
                break
            else:
                d.pop()
                d.popleft()
        except IndexError:
            print("Yes")
            break
