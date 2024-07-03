# Keylogger Project

## Description

This project is a simple keylogger implemented in Python using the `pynput` library. The keylogger captures all keystrokes made by the user and saves them to a log file (`log.txt`). Additionally, it includes functionality to periodically send the updated log file to a specified email address.

This software is a form of malware. Keyloggers can be used to monitor and record user activity, potentially leading to unauthorized access to sensitive information such as passwords, credit card numbers, and personal messages. 
## Requirements

- Python 3.x
- `pynput` library
- `smtplib` library (for sending emails)

You can install the required libraries using pip:

```bash
pip install pynput
