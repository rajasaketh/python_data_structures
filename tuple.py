empty_tuple = ()
print(empty_tuple)

#Create tuple with one element
single_tuple = ('one',)
print(single_tuple)

single_tuple2 = 'one',
print(single_tuple2)

# Caution -Single element in paranthesis omitting the comma would not get a tuple
single_tuple3 = ('one')
print(type(single_tuple3))

#Create tuple with multiple elements
multiple_tuple = ('one', 'two', 'three')
print(multiple_tuple)

# Tuple unpacking
a, b, c = ('one', 'two', 'three')
print(a)
print(b)
print(c)

# The tuple() conversion makes tuples from other things - Generators ?
samp_list = ('apple','banana','orange')
samp_tuple = tuple(samp_list)
print(samp_tuple)

# Combining Tuples 
comb = ('one', 'two') + ('three',)
print(comb)


#Duplicate items
dupl = ('dice',) * 3
print(dupl)


#Comparisions works much like lists
t1  = (7,2,3)
t2 = (7,3)

print(t1 == t2)
print(t1 < t2)
print(t2 < t1)
print('')

#Iterate using a tuple
words = ('one','two','three')
for w in words:
    print(w)

