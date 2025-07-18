import random 
def generate_random_number():
    return random.randint(1, 100)

print("Random number generated:", generate_random_number())
if(generate_random_number() >= 50):
    print("The number is greater than 50.")
else:
    print("The number is 50 or less.")