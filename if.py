is_male=False
is_tall=True

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are male but short")
elif not(is_male) and is_tall:
    print("You are not male but tall")
else:
    print("you are neither male nor tall")