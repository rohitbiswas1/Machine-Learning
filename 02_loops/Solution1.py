numbers=[1,-21,12,11,-23,2,22,2,2,44,22,3,-11]

psitive_number_count=0
for num in numbers:
    if num>0:
        psitive_number_count+=1

print("Final count of positive number is : " ,psitive_number_count)