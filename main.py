#Run the Gui class

phone_contact = {'1111111111': "Amal", '2222222222': "Mohammed", '3333333333': "Khadijah", '4444444444': "Abdullah",
                 '5555555555': "Rawan", '6666666666': "Amal", '7777777777': "Layla"}


def getName(number):  # Get name by the number
    return phone_contact.get(number)


def getContact(name: str):  # Get a contact
    found = False
    for key, value in phone_contact.items():
        if name.lower() == value.lower():
            print(f"name:{value} phone:{key}")
            found = True
    if found is False:
        print("the number is not found ")


def AddContact(phone: str, name: str):  # Add Contact
    phone_contact[phone] = name


def display():  # display the Phone Contact
    for num, names in phone_contact.items():
        print(f"name: {names}, phone: {num}")





# choice = 0
# while choice != -1:
#     user_choice = input(
#         "Enter the number:(1)-Search for a name by Phone | (2)-Add Contact | (3)-Display your Phone Contact | (4)-Search for contact  (-1)-Exit\n")
#
#     if user_choice == '1':  # use getName Function
#         phone_num = input("Enter the number (must be 10 digts)\n")
#         if len(phone_num) != 10:
#             print("This is invalid number\n")
#         else:
#             if phone_num is None:
#                 print("Sorry, the number is not found\n ")
#             else:
#                 print(f"The name of this Number {getName(phone_num)}\n")
#
#     elif user_choice == '2':  # use AddContact Function
#         phone = input("Enter the number to add\n")
#         name = input("Enter the name\n")
#         if getName(phone) is None and len(phone) == 10:  # check if the phone number does not exist and phone have 10 digits
#             AddContact(phone, name)
#             print("The contact have been added")
#     elif user_choice == '3':
#         display()
#     elif user_choice == '4':
#      name = input("Enter the name\n")
#      getContact(name)
#     elif user_choice == '-1':
#         print("Thank you")
#         exit()
#     else:
#         print("input wrong")
