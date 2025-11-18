def generate_profile(age):
    if age > 0 and age <=12:
        return "Child"
    elif age > 12 and age<=19:
        return "Teenager"
    elif age >19:
        return "Adult"
    else: return None