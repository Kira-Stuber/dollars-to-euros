convert = input("Would you like to convert US dollars to euros?: ")

while convert == "yes":
    dollar = float(input("Enter dollar amount to be converted: "))
    euros = dollar * .94540
    euros = str(euros)
    print("€" + euros)
    convert = input("Would you like to convert dollars to euros?: ")