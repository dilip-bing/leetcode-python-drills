# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

# Given s = "hello world", get the last 5 characters using slicing.
s = "hello world"
print(s[-5:])
print(s[-0:])
print(s[-44:])
print(s[1:10:2])
dilip = s[-2:]
print(dilip)

# Given lst = [10, 20, 30, 40, 50], reverse it using slicing (no .reverse(), no reversed()).
st = [10, 20, 30, 40, 50]
print(st[::-1])


# s = "abcdef" → every 2nd char starting index 1
d = "abcdef"
print(d[1::2])

#swap
x =5
y = 10
x,y = y,x
print (x)
print (y)

# lst = [1,2,3,4,5] → delete first two elements in place via slice
ts = [1,2,3,4,5]
del ts[:2]
print (ts)
