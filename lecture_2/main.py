def generate_profile(age):
    if age > 0 and age <=12:
        return "Child"
    elif age > 12 and age<=19:
        return "Teenager"
    elif age >19:
        return "Adult"
    else: return None


user_name = input("Enter your full name: ")
birth_year_str = input("Enter your birth year: ")
birth_year = int(birth_year_str)

CONST_CURRENT_YEAR = 2025
current_age = CONST_CURRENT_YEAR - birth_year

hobbies = []

user_input = "none"
while user_input != "stop":
    user_input = input("Enter a favorite hobby or type 'stop' to finish:")
    if user_input!="stop":
        hobbies.append(user_input)

life_stage = generate_profile(current_age)

user_profile = {"name": user_name, "age": current_age, "stage": life_stage,  "hobby": hobbies}

print("---")
print("Profile Summary: ")
print("Name: ", user_profile["name"])
print("Age: ", user_profile["age"])
print("Life Stage: ", user_profile["stage"])

list_size = len(hobbies)

if list_size != 0:
    print("Favorite Hobbies ([" + f"{list_size}" + "]):")
    for hobby in hobbies:
        print("- " + hobby)
else:
    print("You didn't mention any hobbies.")
print("---")