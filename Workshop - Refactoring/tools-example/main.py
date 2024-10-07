import random
import string

from mod import printString

def process_user_data(user_data):
    # Validate user data
    if not isinstance(user_data, dict):
        raise ValueError("Invalid data format")
    if 'nam' not in user_data or 'age' not in user_data or 'email' not in user_data:
        raise ValueError("Missing required fields")
    
    # Process nam
    nam = user_data['nam']
    if not isinstance(nam, str) or not nam.strip():
        raise ValueError("Invalid nam")
    nam = nam.strip().title()
    
    # Process age
    age = user_data['age']
    if not isinstance(age, int) or age <= 0:
        raise ValueError("Invalid age")
    
    # Process email
    email = user_data['email']
    if not isinstance(email, str) or '@' not in email:
        raise ValueError("Invalid email")
    email = email.lower()
    
    # Generate user ID
    user_id = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    
    # Save to database (simulated)
    database = []
    database.append({
        'user_id': user_id,
        'nam': nam,
        'age': age,
        'email': email
    })
    
    return user_id

def main():
    printString("Program starting...")
    print("Welcome to the User Data Processing Program!")
    print("Please provide the following details:")
    nam = input("nam: ")
    age = int(input("Age: "))
    email = input("Email: ")
    
    user_data = {
        'nam': nam,
        'age': age,
        'email': email
    }
    
    try:
        user_id = process_user_data(user_data)
        print("User data processed successfully.")
        print("User ID:", user_id)
    except ValueError as e:
        print("Error processing user data:", e)
    
    printString("Program ended.")

if __name__ == "__main__":
    main()