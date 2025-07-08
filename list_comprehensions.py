tuple_xx = ("hi",2,3,)
print(tuple_xx)
x= 1,
print(type(x))

tuple_mary=("germany",11.2,)
tuple_leila=("uk",12.2,)
tuple_rinat=("usa",23.4,)

# zz = type(tuple_rinat)

y  = tuple_mary[0] #DUMB YUSIF TUPILS ARE IMMUTABLE U CAN'T CHANGE THE PLACES OF VALUE, BUT U CAN MAKE NEW TUPLE USING IT
f = tuple_mary[1]

EMPTY_TUPLE=tuple([f,y,])
print(EMPTY_TUPLE[1])
# for i in tuple_mary:
#     EMPTY_TUPLE.append(-1)
#     print(EMPTY_TUPLE)

#dictionary
x_dictionary = {
    "name " : "yusif",
"age " : 13,
"city" : "new york"
}

print(x_dictionary)

met_museum = {"artist" : "Ryūryūkyo Shinsai","period":"19th century","date":1930}
print(met_museum)

list1 = ["a","b","c",1] #ordered
tuple1=  ("a","b","c",1,2,1,2,4) #ordered
set1 = set(tuple1) #sets are un-ordered
dict1 = {
    "value1":"a","value2":"b","value3":"c","value4":1
}
print(tuple1)
print(set1)

set1 = {'alma','nar','banana'}
set2=set(1,2,"nar","na")
print(set2)


#sets are for store uniqe values
my_fav={"apple","banana","kiwi"}
friends_fav={"orange","strawberry","kiwi","plum","banana"}

z = my_fav.intersection (friends_fav) #can use '&'
y = my_fav.union(friends_fav) # can use '|'

print(z)
print(y)
