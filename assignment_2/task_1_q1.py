# create list of cities
cities = ['Mumbai', 'Pune', 'Nagpur', 'Bengaluru', 'Chennai', 'Kolkata']

# print(type(cities))

# append the list of cities
cities.append('New Delhi')
print(cities)

# print the length of cities list
length = len(cities)
print('The length of list is {}'.format(length))
# remove the element at index 2
remove_city = cities.pop(2)

print('The index two city is : {}'.format(remove_city))
print('The updated list of cities :{}'.format(cities))