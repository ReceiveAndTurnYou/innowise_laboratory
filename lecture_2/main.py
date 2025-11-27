#calculate user life stage
def generate_profile(age):
    if age > 0 and age <=12:
        return "Child"
    elif age > 12 and age<=19:
        return "Teenager"
    elif age >19:
        return "Adult"
    else: return None

#output user profile
def output_profile(usr_profile):
    print("---")
    print("Profile Summary: ")
    print("Name: ", usr_profile["name"])
    print("Age: ", usr_profile["age"])
    print("Life Stage: ", usr_profile["stage"])
    list_size = len(hobbies)

    if list_size != 0:
        print("Favorite Hobbies ([" + f"{list_size}" + "]):")
        for hobby in hobbies:
            print("- " + hobby)
    else:
        print("You didn't mention any hobbies.")
    print("---")

# input username and birth age
user_name = input("Enter your full name: ")
birth_year_str = input("Enter your birth year: ")
birth_year = int(birth_year_str)

#input user age
CONST_CURRENT_YEAR = 2025
current_age = CONST_CURRENT_YEAR - birth_year

hobbies = [] # initialize hobbies list

user_input = "none"
while user_input != "stop":
    user_input = input("Enter a favorite hobby or type 'stop' to finish:")
    if user_input!="stop":
        hobbies.append(user_input)

life_stage = generate_profile(current_age)

user_profile = {"name": user_name, "age": current_age, "stage": life_stage,  "hobby": hobbies}

output_profile(user_profile)