import re
import os

# VULNERABILITY 1: Hardcoded Secret (Leaked API Key)
# Security Pulse Monitor will detect this and warn the developer
AWS_SECRET_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE12345" 
DB_CONNECTION_STRING = "mongodb://admin:supersecret123@cluster0.mongodb.net/test"

def validate_email(email_input):
    # VULNERABILITY 2: Catastrophic Regex (ReDoS)
    # This regex is highly inefficient and can crash the background engine if not fixed
    dangerous_pattern = re.compile(r"^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$")
    
    if dangerous_pattern.match(email_input):
        return True
    return False

def connect_services():
    print(f"Connecting to database using: {AWS_SECRET_ACCESS_KEY}")

if __name__ == "__main__":
    connect_services()
    # Testing with a potentially dangerous string
    validate_email("test.user.name.with.many.dots@example.com")