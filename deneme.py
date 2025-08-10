import os
from dotenv import load_dotenv
# Load variables from .env file
load_dotenv()
# Access the variables

api_key = os.getenv("API_KEY")
password = os.getenv("DB_PASSWORD")
print(f"Your API key is: {api_key}")
print(f"Password is: {password}")
