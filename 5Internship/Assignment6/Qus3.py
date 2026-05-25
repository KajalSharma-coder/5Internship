# Random Joke API
import requests

url = "https://official-joke-api.appspot.com/random_joke"

response = requests.get(url)

data = response.json()

print("Random Joke")
print("-------------------")
print("Setup :", data["setup"])
print("Punchline :", data["punchline"])

#Currency Converter API
import requests

base_currency = input("Enter base currency (e.g. USD): ").upper()

url = f"https://open.er-api.com/v6/latest/{base_currency}"

response = requests.get(url)

data = response.json()

print("\n Currency Rates")
print("----------------------")

rates = data["rates"]

print("INR :", rates["INR"])
print("EUR :", rates["EUR"])
print("JPY :", rates["JPY"])


#Random User API
import requests

url = "https://randomuser.me/api/"

response = requests.get(url)

data = response.json()

user = data["results"][0]

print(" Random User Details")
print("---------------------------")

print("Name :", user["name"]["first"], user["name"]["last"])
print("Gender :", user["gender"])
print("Country :", user["location"]["country"])
print("Email :", user["email"])


