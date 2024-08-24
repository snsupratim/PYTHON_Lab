# Input the email address
email_address = input("Enter an email address: ")

# Split the email address at the "@" symbol
parts = email_address.split('@')

# Check if the email address is in the correct format
if len(parts) == 2:
    # Extract and print the company name
    company_name = parts[1].split('.')[0]
    print(company_name)
else:
    print("Invalid email address format")
