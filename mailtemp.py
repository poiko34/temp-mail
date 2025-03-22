import argparse
from mailtm import Email

def listener(message):
    """Function to handle incoming messages"""
    print("\nSubject: " + message['subject'])
    print("Content: " + (message['text'] if message['text'] else message['html']))

# Create an argument parser
parser = argparse.ArgumentParser(description="Script to register a mail and listen for incoming messages")

# Add the optional -n parameter for the username
parser.add_argument('-n', '--name', type=str, help="Username for email registration", default=None)

# Parse the arguments
args = parser.parse_args()

# Create an object for working with email
email_client = Email()

# Print the domain
print("\nDomain: " + email_client.domain)

# Get the username from the -n flag or leave it as None if not provided
username = args.name

# If the username is provided, try to register a new email
if username is not None:
    try:
        email_client.register(username=username)
    except Exception as e:
        print(f"\nError: {e}")
        print("\nUsername already exists or an error occurred!")
else:
    email_client.register()
    print("\nNo username provided.")

# Print the email address
print("\nEmail Address: " + str(email_client.address))

# Start listening for incoming emails
email_client.start(listener, interval=1)

print("\nWaiting for new emails...")
