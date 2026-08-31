# import re
# email = input("Please enter your email address: ").strip()
# # re.search(pattern, string, flags = 0) method is used to search for a pattern in a string.
# if re.search("@", email):
#     print("Valid")
# else:
#     print("Invalid")

import re
email = input("Please enter your email address: ").strip()
if re.search("..*@..*", email):
    print("Valid")
else:
    print("Invalid")