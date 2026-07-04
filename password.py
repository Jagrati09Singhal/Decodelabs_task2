import string
import secrets
import math

# Input Validation
while True:
    try:
        length = int(input("Enter password length (minimum 15): "))

        if length < 15:
            print("Password must be at least 15 characters long.")
        else:
            break
    except ValueError:
        print("Please enter a valid integer.")

# Character Pool
characters = (
    string.ascii_letters +
    string.digits +
    string.punctuation
)

# Secure Password Generation
password = ''.join(secrets.choice(characters) for _ in range(length))

# Entropy Calculation
entropy = length * math.log2(len(characters))

# Output
print("\nGenerated Password:")
print(password)

print(f"\nPassword Length : {length}")
print(f"Character Pool  : {len(characters)}")
print(f"Entropy         : {entropy:.2f} bits")

# Security Rating
if entropy >= 128:
    print("Security Level  : Very Strong")
elif entropy >= 80:
    print("Security Level  : Strong")
else:
    print("Security Level  : Moderate")