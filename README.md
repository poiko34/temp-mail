# Temp Mail Script (Debian-Based Systems)

This is a Python-based script designed for **Debian-based systems** (such as Debian, Ubuntu, Kali Linux, etc.). It registers a temporary email address and listens for incoming emails.

## Features
- Register a temporary email address
- Listen for incoming emails
- Print the subject and content of received emails

## Prerequisites

Before running the script, ensure the following:

- **Debian-based OS** (Debian, Ubuntu, Kali, etc.)
- **Python 3** is installed on your system
- You have the necessary permissions to install packages and make system changes

## Installation

Follow these steps to install and set up the environment for the script:

### 1. Clone the repository (optional)

If you're using Git, you can clone the repository to your local machine:

```bash
git clone https://github.com/poiko34/temp-mail.git
cd temp-mail
```

### 2. Run the setup script

The `setup.sh` script will install necessary dependencies and set up the virtual environment for the project.

```bash
chmod +x setup.sh
./setup.sh
```

This script does the following:
- Installs Python virtual environment (`python3-venv`)
- Installs necessary Python packages
- Makes the `mail.py` script executable
- Creates a symbolic link to the script, allowing you to run it as a command

### 3. Running the Script

To run the script, simply use the `mail` command:

```bash
mail
```

The script will listen for incoming emails, print the subject, and display the content.

### 4. Usage

You can specify a username to register with the following command:

```bash
mail -n yourusername
```

If no username is specified, the script will **automatically generate a random username** by default.

## Compatibility

✅ Works on:
- **Debian**
- **Ubuntu**
- **Kali Linux**
- **Other Debian-based distributions**

❌ **Not tested on non-Debian systems.** If you use another distribution, you may need to adjust the installation process.
