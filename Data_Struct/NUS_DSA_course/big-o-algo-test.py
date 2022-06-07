i = 1
j = 0
n = 20
count = 0
while j < n:
    if i % n == 0:
        j += 1
        count+= 1
    i += 1
    
print("For n = ", n, "count is: ", count)