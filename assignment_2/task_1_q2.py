country_capitals = {
    "United States": "Washington D.C.",
    "Canada": "Ottawa",
    "France": "Paris",
    "Spain": "Madrid",
    "Japan": "Tokyo",
    "India": "New Delhi",
}
print(type(country_capitals))

countries = country_capitals.keys()
print(countries)

# add the name of new country and capital
country_capitals["Australia"] = "Canberra"
print(country_capitals)

# length of the dictionary
print('The length of dictionary is:', len(country_capitals))

# remove an element from dictionary
remove_country = country_capitals.pop("Spain")
print('The updated dictionary is:', country_capitals)
