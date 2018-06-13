# NSAG COMP3321 String Formatting Exercises

# Part 1
# Print 10 lines from an ASCII chart starting at decimal 63
# Ensure that the columns line up, and the appropriate values are shown

# <YOUR CODE HERE>
	
# Expected Output:
# Octal     Decimal     Hex       Bin    Char
# -------------------------------------------
#  0o77          63      3f    111111       ?
# 0o100          64      40   1000000       @
# 0o101          65      41   1000001       A
# 0o102          66      42   1000010       B
# 0o103          67      43   1000011       C
# 0o104          68      44   1000100       D
# 0o105          69      45   1000101       E
# 0o106          70      46   1000110       F
# 0o107          71      47   1000111       G
# 0o110          72      48   1001000       H	

# Part 2
# Given the strings below, print 'abracadabra' using a format string
a = 'abra'
b = 'cad'
# "{0}{1}{0}".format(a,b)

# Part 3
# Print only the 1st, 3rd, and 5th items from the list
my_list = ['1st', '2nd', '3rd', '4th', '5th']
# '{l[0]} {l[2]} {l[4]}'.format(l=my_list)

# Part 4 *Challenge*
# Print the decimal value of a given IP address using a format command
# Keep it in 1 line
ip = "192.168.0.1"
# <YOUR CODE HERE> REMEMBER ONLY 1 LINE
