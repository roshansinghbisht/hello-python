# Try comparison operators in this quiz! This code calculates the
# population densities of Rio de Janeiro and San Francisco.

sf_population, sf_area = 864816, 231.89
rio_population, rio_area = 6453682, 486.5

san_francisco_pop_density = sf_population/sf_area
rio_de_janeiro_pop_density = rio_population/rio_area

# Write code that prints True if San Francisco is denser than Rio,
# and False otherwise

print(san_francisco_pop_density > rio_de_janeiro_pop_density)


# The bool data type holds one of the values True or False, which are
# often encoded as 1 or 0, respectively.

# There are 6 comparison operators that are common to see in order to
# obtain a bool value:
# < : Less Than
# > : Greater Than
# <= : Less Than or Equal To
# >= : Greater Than or Equal To
# == : Equal to
# != : Not Equal to

# And there are 3 logical operators you need to be familiar with:
# and - Evaluates if all provided statements are True
# or - Evaluates if at least one of many statements is True
# not - Flips the Bool Value
