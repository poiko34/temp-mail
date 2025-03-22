from mailtm import Email

def listener(message):
    """Function to handle incoming messages"""
    print("\nSubject: " + message['subject'])
    print("Content: " + (message['text'] if message['text'] else message['html']))

# Create an object for working with mail
test = Email()

# Print the domain
print("\nDomain: " + test.domain)

# Input the username for email registration
user = str(input("Enter user name: "))

# Try to register a new email
try:
    test.register(username=user)
except Exception as e:
    print(f"\nError: {e}")
    print("\nUsername already exists or error occurred!")

# Print the email address
print("\nEmail Address: " + str(test.address))

# Start listening for incoming emails
test.start(listener, interval=1)

print("\nWaiting for new emails...")