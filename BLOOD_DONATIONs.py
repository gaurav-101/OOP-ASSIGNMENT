print("\n---------------------------------------++ WELCOME TO XYZ BLOOD DONATION BLOOD SERVICES ++-----------------------------------------\n")
#It is assumed that there is only one admin
#password of the admin for logging in into the application
admin_password = "cba321"

#The users which are already signed in
users = ['Rani', 'Ramesh', 'Mahesh', 'Suresh', 'Anup', 'Sushila', 'Pooja', 'Manav']

#Passwords of the signed in users index-wise
user_passwords = ['zyx987', 'R@m123', 'M@h567', 'sur123', 'lmnop', 'ila@sush', 'P#2o', 'M@n101']

#Areas of the cty are divided into 6 parts: City side East(E), West(W), North(N), South(S), North-East(N-E), South-West(S-W)
#so the location of registered users is stored in this list index-wise
user_location = ['S', 'W', 'N-E', 'W', 'E', 'S-W', 'N', 'N-E']

#There are 4 types of blood groups: A,B, AB, O each has two subtypes: A+, A-, B+, B-, O+, O-, AB+, AB-
# The Blood group of registered users are there in list index-wise
user_group = ['O-', 'AB+', 'A-', 'B+', 'O+', 'B-', 'A+', 'AB-']

#we are assuming that Ramesh and Manav have given the request to admin
user_request = [users[1], users[7]]

#assuming that admin sent request to Anup, Pooja
admin_request = [users[4], users[6]]

#Blood banks in this have code names as BB-1, BB-2 etc. below is the dictionary with blood bank names and it's location
blood_banks = {'BB1': 'N', 'BB2': 'E', 'BB3': 'W', 'BB4': 'W', 'BB5': 'N-E', 'BB6': 'N-E', 'BB7': 'S', 'BB8': 'S', 'BB9': 'S-W', 'BB10': 'N'}

#asking the application user that he is blood donation admin or user 
ask = int(input("Please specify, you are a User or an Admin: \nPRESS '1' for Admin \nPRESS '2' for User(The one who can donate or accept blood)\n"))
if ask == 1:
    ad_pass=input("\nEnter admin password: ")
    if ad_pass == admin_password:
        print("Admin Succesfully logged in")
        print("------WELCOME! Admin------\n")
        print("What you want to know: \n\n1. Details of blood banks\n2. Details of the users\n3. Add hoptals to this program\n4. Check for any request of blood doner\n5. Send request to user\n")
        x = int(input("Enter the choice from above: \n"))
        if x == 1:
            print("added blood banks in this city: ", blood_banks.keys())
            print("Location of these blood banks: ", blood_banks.values())
        elif x == 2:
            print("There are 8 signed in users")
            for i in range(8):
                print(i+1, "th user")
                print("**name of user: ", users[i])
                print("**location in which user live: ", user_location[i])
                print("**blood group of user: ", user_group[i])
                print("------------------------------")
        elif x == 3:
            print("Hospitals which are not part of blood bank program: H-1(S)\nH-2(W)\nH-3(N)\nH-4(S-W)")
            y = int(input("Which one you want to enter: "))
            if y == 1:
                blood_banks.update({'H-1': 'S'})
                print("Hospital added")
            elif y == 2:
                blood_banks.update({'H-2': 'W'})
                print("Hospital added")
            elif y == 3:
                blood_banks.update({'H-3': 'N'})
                print("Hospital added")
            elif y == 4:
                blood_banks.update({'H-4': 'S-W'})
                print("Hospital added")
            else:
                print("Invalid input")
        elif x == 4:
            print("There are two requests by", len(user_request), "users: ", user_request)
            z=input("Do you want to accept the request('y' or 'n'): ")
            if z == 'y':
                a=int(input("whose request you want to accept(press 1,2 and press 3 for accepting all): "))
                if a == 1:
                    print("Request accepted of ", users[1])
                elif a == 2:
                    print("Request accepted of ", users[7])
                elif a == 3:
                    print("All requests got accepted")
                else:
                    print("Wrong input, request not accepted")
            else:
                print("Request not accepted")
        elif x == 5:
            print("Send request to which user: ")
            print(users)
            req_user=input("Enter user name: ")
            if req_user in users:
                if req_user != users[4] and req_user != users[6]:
                    admin_request.append(req_user)
                    print("Request sent")
                else:
                    print("Request already sent previously")
            else:
                print("Request not sent, entered user is not regitered")
        else:
            print("Incorrect input")
    else:
        print("Wrong password")
elif ask == 2:
    user_options = int(input("\n1_User login \n2_New user sign in \n"))
    if user_options == 1:
        us_name=input("Enter User name: ")
        if us_name in users:
            print("User found")
            us_pass=input("Enter your password: ")
            if us_pass == user_passwords[users.index(us_name)]:
                print("User succesfully logged in\n")
                print("What you want to do: \n\n1. Request for blood of particular group\n2. Check total no. of users\n3. Check for requests given to you by admin\n")
                b=int(input("Choose a choice from above: "))
                if b==1:
                    group=input("Which blood group you want: ")
                    if group not in user_group:
                        print("invalid blood group")
                    else:
                        print("User with this blood group is present")
                        #The user name will be added in the user request list
                        if us_name != users[1] and us_name != users[7]:
                            user_request.append(us_name)
                            print("Request sent to admin succesfully")
                        else:
                            print("Request already sent")
                elif b==2:
                    #user can only know know number
                    print("Total number of users:", len(users))
                elif b==3:
                    if us_name != users[4] and us_name != users[6]:
                        print("you got no requests from admin")
                    else:
                        print("You got a request from the admin")
                        c=input("Do you want to accept the request('y' or 'n'): ")
                        if c == 'y':
                            print("Request accepted")
                        else:
                            print("Request not accepted")
                else:
                    print("wrong input")
            else:
                print("Wrong password")
        else:
            print("User not registered")
    elif user_options == 2:
        new_us_name=input("Enter user name: ")
        users.append(new_us_name)
        new_us_pass=input("Enter your password: ")
        user_passwords.append(new_us_pass)
        new_us_loc=input("Enter your location in this City: ")
        if new_us_loc in user_location:
            user_location.append(new_us_loc)
        else:
            print("Wrong city location")
            exit()
        new_us_grp=input("Enter your blood group: ")
        if new_us_grp in user_group:
            user_group.append(new_us_grp)
        else:
            print("Wrong blood group")
            exit()
        print("User signed in and logged in to the account")
        print("What you want to do: \n1_Request for blood of particular group\n2Check total no. of users\n3_Check for requests given to you by admin")
        b2=int(input("Choose a choice from above: "))
        if b2==1:
            group=input("Which blood group you want: ")
            if group not in user_group:
                print("invalid blood group")
            else:
                print("User with this blood group is present")
                user_request.append(new_us_name)
                print("Request sent to admin succesfully")
        elif b2==2:
            #user can only know know number
            print("Total number of users:", len(users))
        elif b2==3:
            #new user will not get any request from admin
            print("you got no requests from admin")
        else:
            print("wrong input")
    else:
        print("wrong input")
else:
    print("Wrong input")