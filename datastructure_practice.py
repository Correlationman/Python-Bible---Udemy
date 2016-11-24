"""
Created on Tue Nov 16 14:04:47 2016
From Umedy course: The Python Bible™
Section 7: Data structures
"""
#Lists
# Can have any data type inside
our_list=[27,46.9,-5,"A","True",True]
print(type(our_list))
print(our_list[0])
print(our_list[0:3])
#Nested list
our_list=[1,2,[3,4,5],6,7,8]
print(our_list[2:])
print(our_list[2][0])

our_table=[[1,2,3],[4,5,6],[7,8,9]]
print(our_table[0])
print(our_table[1][0], our_table[2][1])
print(our_table[2][:2])
# Recognition
print(2 in our_table)
print([1,2,3] in our_table)
# Remove a known content from List by method remove() or delete an index by function del
our_table[0].remove(2)
print(our_table)
del our_table[0][1:]
print(our_table)
# Add a known content to List by method append()
our_table[0].append(2)
print(our_table)
our_table[0].append(3)
print(our_table)

print(our_table+[1])
our_table=our_table[0]+[1]
print(our_table)
# Add a known index to List by method insert()
our_table=[5,12,31,49,72]
print(our_table)
our_table.insert(2,100)
print(our_table)


#Tuples
our_tuple=1,2,3,'A','B','C'
print(our_tuple)
# Tuples cannot be changed unlike Lists
A=[1,2,3]
print(type(A))
A=tuple(A)
print(A,type(A))

#Dictionary{keys:values}
students={}
students={"Alice":25,"Bob":27,"Clair":17}
print(students)
print(students["Bob"])
print(students.keys())
print(students.values())
# To change any of keys or values, convert the dictionary keys() and values() to List
a=list(students.keys())
print(a[:],a[1:],a[:1])
b=list(students.values())
print(b[:],b[1:],b[:1])
c=students.items()
print(c)
print(type(c))
# Multiple values for each key in a List
students={"Alice":["ID1",25,"A"],"Bob":["ID2",27,"B"],"Clair":["ID3",17,"C"]}
print(students["Clair"])
print(students["Clair"][0])
print(students["Clair"][1:])
# Give each key a dictionary
students={"Alice":{"id":"ID001","age":25,"grade":"A"},"Bob":{"id":"ID002","age":27,"grade":"B"},"Clair":{"id":"ID003","age":17,"grade":"C"}}
print(students["Clair"])
print(students["Clair"]["age"],students["Alice"]["grade"])



















