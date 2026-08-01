import random
import string

if __name__ == "__main__":
    length = int(input("Enter the desired password length: "))
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation

    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    random.shuffle(s)
    password = ''.join(s[:length])
    print("Generated password:", password)
    
