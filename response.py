import validators

mail = input("What's your email adress? ")

result = validators.email(mail)

if result is True:
    print("Valid")
else:
    print("Invalid")
