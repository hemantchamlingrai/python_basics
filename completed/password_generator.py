import random
import string

def generate_password(length=12, use_digits=True, use_punctuation=True):
    #Define character sets
    characters = string.ascii_letters #letters (both cases)
    if use_digits:
        characters += string.digits #Add digits (0-9)
    if use_punctuation:
        characters += string.punctuation #Add symbols (!@#$..)
    
    #Ensure password length is at least $ characters
    length = max(length, 4)
    
    #Generate password using secure randomization
    password = [
        random.SystemRandom().choice(string.ascii_lowercase),
        random.SystemRandom().choice(string.ascii_uppercase)
    ]
    
    #Add digits and punctuation if enabled
    if use_digits:
        password.append(random.SystemRandom().choice(string.digits))
    if use_punctuation:
        password.append(random.SystemRandom().choice(string.punctuation))
    
    #Fill remaining length with random characters
    remaining = length - len(password)
    for _ in range(remaining):
        password.append(random.SystemRandom().choice(characters))
    
    #Shuffle and convert to string
    random.SystemRandom().shuffle(password)
    return ''.join(password)

password = generate_password(
    length=16,
    use_digits=True,
    use_punctuation=True
)

print("Generate password:", password)