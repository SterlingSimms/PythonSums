
for count in range(1, 1000):
    if count % 2 == 1: #having a remainder of 1 to keep numbers odd
        print count

for count in range(5, 1000001): #added 1 to print up to 1,000,000
    if count % 5 == 0: #% 5 == 0 to increment by 5
        print count

sum = 0
a = [1, 2, 5, 10, 255, 3]
for element in a: #for loop to iterate through array
    sum += element #+= to add each index to var element
print sum


sum = 0
a = [1, 2, 5, 10, 255, 3]
for element in a:
    sum += element #using last problems code to build on.
    avg = sum/len(a) #using .len() to find average from the sum.
print avg


    


    
