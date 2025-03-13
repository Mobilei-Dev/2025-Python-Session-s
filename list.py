my_list=[10,20,30,40]

print(my_list)
my_list.insert(1,15)#inserts 15 on index 1
print(my_list)
my_list.extend([50,60,70])#extends the values listed
print(my_list)
my_list.remove(70)#removes 70 from the list

my_list.sort()#sorts in ascending order
print(my_list)

index_30 = my_list.index(30)
print(index_30)
