############################################################################################################################################
# - The Concept of Tuples are closely related to Lists. However, unlike lists tuples are immutable
# - Tuples do not support all the methods or functions supported by the lists. In particlarm tuples do not suppot any methods that modify the contents of the tuple
#
#
###########################################################################################################################################

#An Empty tupls
empty_tuple = ()
print(empty_tuple)

#Create tuple with one element aka Singleton tuple
single_tuple = ('one',)
print(single_tuple)
print('------------------------------------------------------------')

single_tuple2 = 'one',
print(single_tuple2)
print('------------------------------------------------------------')

# Caution -Single element in paranthesis omitting the comma would not get a tuple
# The type resolves to str type
single_tuple3 = ('one')
print(type(single_tuple3))
print('------------------------------------------------------------')

#Create tuple with multiple elements
multiple_tuple = ('one', 'two', 'three')
print(multiple_tuple)
print('------------------------------------------------------------')

# Tuple unpacking
a, b, c = ('one', 'two', 'three')
print(a)
print(b)
print(c)
print('------------------------------------------------------------')

# The tuple() conversion makes tuples from other things - Generators ?
samp_list = ['apple','banana','orange']
samp_tuple = tuple(samp_list)
print(samp_tuple)
print('------------------------------------------------------------')
# Combining Tuples 
comb = ('one', 'two') + ('three',)
print(comb)
print('------------------------------------------------------------')

#Duplicate items
dupl = ('dice',) * 3
print(dupl)
print('------------------------------------------------------------')

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

print('------------------------------------------------------------')

# De-duplicating the lists using tuples
list_dup = ['tesla','toyota','honda','audi','bmw','tesla','nissan','toyota']
tup_dedup=tuple(list_dup)
print(tup_dedup)