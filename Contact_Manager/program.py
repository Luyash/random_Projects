 
def search_contact():
    found_contact = []
    query = input("Enter name which you want to search---> ")
    with open("contact.txt", "r") as f:
        lines = f.readlines()
        contact_detail = {}
        for i in range(0, len(lines), 3):  # -->takes 3 lines from txt file

            if (i+2 < len(lines)):  # -->ensures the no. of lines in txt file is divisible by 3

                name_line = lines[i].strip()  # -->this gives name line
                address_line = lines[i+1].strip()
                numnber_line = lines[i+2].strip()
                if name_line.startswith("Name:") and query.lower() in name_line.lower():
                    act_name = name_line.split(':', 1)
                    act_address = address_line.split(':', 1)
                    act_number = numnber_line.split(':', 1)
                    contact_detail["Name"] = act_name[1].strip()
                    contact_detail["Address"] = act_address[1].strip()
                    contact_detail["Number"] = act_number[1].strip()
                    found_contact.append(contact_detail)
        if contact_detail:
            print(f"\n✅ Found {len(found_contact)} contact(s):")
            print("------Displaying the contacts------\n")
            for contact in found_contact:
                print(
                    f"{contact['Name']}\n{contact['Address']}\n{contact['Number']}")
        else:
            print(f"❌ No contact found matching '{query}'.")


def add_contact():
    print("\n [ADD NEW CONTACT] ")

    with open("contact.txt", "a") as f:
        name = input("Enter Full Name--> ")
        address = input("Enter Address--> ")
        number = input("Enter Number--> ")
        info = {
            "Name": name,
            "Address": address,
            "Number": number
        }
        f.write(
            f"Name: {name}\nAddress: {address}\nNumber: {number}\n")
        print("\n---Are you sure this is correct informantion?---")
        print("Press 1 for CORRECT INFORMATION")
        print("Press 2 for INCORRECT INFORMATION")
        query = int(input("----->"))
    f.close()
    if (query == 1):
        print("-------Contact saved SUCCESSFULLY-------")
    elif (query == 2):
        with open("contact.txt", "r") as f:
            old_list = f.readlines()
            new_contact = []
            i = 0
            while i < len(old_list):
                if (old_list[i].startswith("Name:") and name.lower().strip() in old_list[i].lower().strip()):
                    i += 3
                else:
                    new_contact.append(old_list[i])
                    i += 1
        with open("contact.txt", "w") as f:
            f.writelines(new_contact)
        add_contact()


def view_contact():
    with open("contact.txt", "r") as f:
        data = f.read()
        print(data)
    f.close()
    print()
    print("-----THIS IS WHOLE LIST-----")


def delete_contact():
    query = input("Enter name of person to delete contact --> ")
    with open("contact.txt", "r") as f:
        lines = f.readlines()
        new_line = []
        i = 0
        while i < len(lines):
            if lines[i].startswith("Name: ") and query.lower() in lines[i].lower():
                i += 3
            else:
                new_line.append(lines[i])
                i += 1
        with open("contact.txt", "w") as f:
            f.writelines(new_line)
            f.close()
        if new_line == lines:
            print("\n--No Contact found with that name--")
        else:
            print("\n-----Contact deleted successfully-----")


while True:
    print("-----PRESS 1-5 TO PERFORM TASK-----")
    print("1. ADD new Contact")
    print("2. View all Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit and save")
    try:
        number = int(input("\n---> "))
        if (number == 1):
            print()
            add_contact()
        elif (number == 2):
            print()
            view_contact()
        elif (number == 3):
            print()
            search_contact()
        elif (number == 4):
            print()
            delete_contact()
        elif (number == 5):
            print()
            print("=======Saved and exited Successfully!!!=======")
            break
        else:
            print("\n---Please enter number from 1-5---")
    except ValueError:
        print("====Please enter a NUMBER from 1 to 5====")
