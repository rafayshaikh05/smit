#String Method Assignment

#Return a capitalized version of the string.
print("test 1".capitalize())

#Return a version of the string suitable for caseless comparisons.
print("TEST2".casefold())

#Return a version of the string suitable for caseless comparisons.

print("ben".center(12, "-"))
#Return a centered string of length width.

print("banana".count("a"))
#Return the number of non-overlapping occurrences of substring sub in string S[start:end].


print("name".encode())
#Return the number of non-overlapping occurrences of substring sub in string S[start:end].


print("apple.py".endswith(".py"))
#Return True if the string ends with the specified suffix, False otherwise.


print("ben\tparker".expandtabs(6))
#Return a copy where all tab characters are expanded using spaces.


print("hello".find("e"))
#Return the lowest index in S where substring sub is found, such that sub is contained within S[start:end].


print("he is a good {}".format("player"))
#The format() method formats the specified value(s) and insert them inside the string's placeholder.


print("test: {test}".format_map({"test":10}))
#Return a formatted version of the string, using substitutions from mapping.

print("111020202".index("02"))
#Return the lowest index in S where substring sub is found, such that sub is contained within S[start:end].


print("abcdefg1234".isalnum())
#Return True if the string is an alpha-numeric string, False otherwise.


print("aplha".isalpha())
#Return True if the string is an alphabetic string, False otherwise.


print("abc".isascii())      
#Return True if all characters in the string are ASCII, False otherwise.

print("123".isdecimal())            
#Return True if the string is a decimal string, False otherwise.


print("123".isdigit()) 
#Return True if the string is a digit string, False otherwise.

print("var_1".isidentifier())       
#Return True if the string is a valid Python identifier, False otherwise.

print("hello".islower())            
#Return True if the string is a lowercase string, False otherwise.

print("123".isnumeric())            
#Return True if the string is a numeric string, False otherwise.

print("abc".isprintable())          
#Return True if all characters in the string are printable, False otherwise.


print("   ".isspace())              
#Return True if the string is a whitespace string, False otherwise.


print("Hello World".istitle())      
#Return True if the string is a title-cased string, False otherwise.


print("HELLO".isupper())
#Return True if the string is an uppercase string, False otherwise.


print("what".ljust(8, "-"))
#merge any number of strings.


print("ABCDEFG".lower())
#Return a copy of the string converted to lowercase.


print("    hey men wyd..".lstrip())
#Return a copy of the string with leading whitespace removed.


table = str.maketrans("joe-silvberg","joe-goldberg")
#Return a translation table 


print("joe-silvberg".translate(table))
#Replace each character in the string using the given translation table.

print("bat:man".partition(":"))
#Partition the string into three parts using the given separator.

print("JustTwo".removeprefix("Just"))
#Return a str with the given prefix string removed if present.

print("bonono".replace("o","a"))
#Return a copy with all occurrences of substring old replaced by new.

print("burayd".rfind("d"))
#Return the highest index in S where substring sub is found, such that sub is contained within S[start:end].

print("haider".rindex("i"))
#Return the highest index in S where substring sub is found, such that sub is contained within S[start:end].

print("huh".rjust(6, "."))
#Return a right-justified string of length width.

print("bat:woman".rpartition(":"))
#Partition the string into three parts using the given separator.

print("hey,hi,hello".rsplit(",", 1))
#Return a list of the substrings in the string, using sep as the separator string.

print("yeah     ".rstrip())
#Return a copy of the string with trailing whitespace removed.

print("abc,cba,bac,cab".split(",")) 
#Return a list of the substrings in the string, using sep as the separator string.

print("abc\nbca\ncab".splitlines())
#Return a list of the lines in the string, breaking at line boundaries.

print("burayd.exe".startswith("bu"))
#Return True if the string starts with the specified prefix, False otherwise.

print("   nonu  ".strip())
#Return a copy of the string with leading and trailing whitespace removed

print("abcDEFghiJKL".swapcase())
#Convert uppercase characters to lowercase and lowercase characters to uppercase.

print("burayd khan".title())
#Return a version of the string where each word is titlecased.

table = str.maketrans("idr", "854")
#Return a translation table usable for str.translate().

print("haider".translate(table))
#Replace each character in the string using the given translation table.

print("rafay".upper())
#Return a copy of the string converted to uppercase.

print("10101010".zfill(12))
#Pad a numeric string with zeros on the left, to fill a field of the given width.
