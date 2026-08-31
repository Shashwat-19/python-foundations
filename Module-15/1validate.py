email = input("Please enter your email address: ").strip()
# # very basic validation to check if the email address contains "@gmail.com"
# if "@gmail.com" in email and "." in email:
#     print("Valid email address.")
# else:
#     print("Invalid email address.")

# username, domain = email.split("@")
# if (username) and ("." in domain):
#     print("Valid email address.")
# else:
#     print("Invalid email address.")


username, domain = email.split("@")
if (username) and domain.endswith(".edu"):
    print("Valid email address.")
else:
    print("Invalid email address.")