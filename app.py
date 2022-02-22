# cmd + s -> save the file
# ctrl + alt + n -> run code
# This function does this and that funciton does that
'''This is docstring
big
multiline string'''
"""This is another one"""

# print('Ok, let\'s go!')

# ----- Variables --------------------------------------------------

# -*-*- String -----------------------------------------------------

# my_story = "A Thousand Splendid Suns"
# print(my_story)

# -*-*- Number -----------------------------------------------------

# my_grade = 85
# print(my_grade)

# -*-*- Boolean ----------------------------------------------------

# am_i_young = True
# print(am_i_young)

# ----- Variable names ---------------------------------------------

# 1. - Variable names must make sense
# movie_rating = 8.5

# 2. - Python convention is to use lowercase letters
# my_name = "Ivan Pavlovitch"

# 3. - Python is snake case
# user_info = "Online"

# 4. - Variable name must start with a letter or _
# 15street - error
# go_for_a_walk()

# 5. - Following the pep8 standards
# to_do = 'Buy Coffee'

# ------------------------------------------------------------
# ---------------**## Data Types part 1 ##**------------------

"""
--Data Type--          --Class--                 --Value--
integers               -> int                     -> 45
floating point numbers  -> float                    -> 4.5
booleans               -> bool                    -> True/False
strings                -> str                     -> "Muslim Helalee"
list                   -> list                    -> [1, 2, 3]
dictionary             -> dict                    -> {"user_name": "awesome50", "user_id": 56}
tuple                  -> tuple                   -> (10, 20, 30)
set                    -> set                     -> {"cat", 99}
"""

# *-*-*-*-*--------------- Numbers **************************
# Integer
age = 38
print(age)
print(type(age))

# Floats
grade = 8.9
print(grade)
print(type(grade))

# *-*-*-*-*--------------- Booleans **************************
alarm = True
offline = False
print(alarm, offline)
print(type(alarm))
print(type(offline))

# *-*-*-*-*--------------- Strings **************************
# Immutable
movie_name = "The good, bad and ugly"
print(movie_name)
print(type(movie_name))

# *-*-*-*-*--------------- List ********************************
# Ordered
mixed = [1, 2, 3.2, 5.4, True, "Muslim Helalee", [1, 2, 3]]
# print(mixed)
# print(type(mixed))

# *-*-*-*-*--------------- Dictionary **************************
# unordered
user_info = {"user_name": "awesome50", "user_id": 56}
# print(user_info)
# print(type(user_info))

# *-*-*-*-*--------------- Tuple *******************************
# Immutable
# ordered
mixed_tuple = (1, 2, 3.2, 5.4, True, "Muslim Helalee", [1, 2, 3])
# print(mixed_tuple)
# print(type(mixed_tuple))


# *-*-*-*-*--------------- Set *********************************
# unordered
mixed_set = {1, 2, 3.2, 5.4, "Python", "Muslim Helalee", 101}
print(mixed_set)
print(type(mixed_set))

# ------------------------------------------------------------
# -----------------**## String Methods ##**-------------------

# 1- len()
address = "Afghanistan"
# print(len(address))

# 2- [] Notation
# print(address[0])
# print(address[7])
# print(address[-1])
# print(address[-4])

# 3- [] Notation
# print(address[0:4])
# print(address[-7:-1])
# print(address[0:])
# print(address[:9])
# print(address[:])

# 4- Concatenation ->>>> Formatted Strings
# country = "USA"
# city = "NYC"
# full_address = city + ", " + country
# full_address = f"{city}, {country}"
# print(full_address)

# 5- upper()
# print(address.upper())

# 6- lower()
# print(city.lower())

# 7- title()
# print("---------------", full_address.title(), "---------------")

# 8- strip()
job = "       Programmer   "
# print(job)
# print(job.strip())
# print(job.lstrip())
# print(job.rstrip())

# 9- find()
# print(address.find("n"))
# print(address.find("i"))

# 10- replace()
# print(address.replace("f", "Z"))

# 11- in operator
# print("ne" in address)
# print("ni" in address)

# 12- not operator
# print("ne" not in address)
# print("ne" not in address)
# print("ni" not in address)
