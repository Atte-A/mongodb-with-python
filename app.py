import os
from bson import ObjectId
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
client = MongoClient(MONGODB_URI)

db = client["runningshoe"]

print("\n*** Welcome to your personal running shoe manager ***")

def list_shoes():

  models = db.models.find()

  for model in models:
   brand = db.brands.find_one({"_id": model["brand_id"]})
   print(brand["name"], model["name"])

def list_brands():

  brands = db.brands.find()

  for brand in brands:
    print(brand["name"])

def add_shoe():
  brand_name = input("Brand: ")
  model_name = input("Model: ")
  rating = float(input("Rating (0-10): "))
  rotation = bool(input("Is this shoe in your current rotation (True/False): "))

  brand = db.brands.find_one({"name": brand_name})

# Lisää tähän vielä tarkempaa brandin määrittelyä
  if not brand:
    brand_id = db.brands.insert_one({"name": brand_name}).inserted_id
  else:
    brand_id = brand["_id"]

  db.models.insert_one({
    "brand_id": brand_id,
    "name": model_name,
    "rating": rating,
    "on_rotation": rotation
  })

  print(f"\n{brand_name} {model_name} added into collection!")

def add_brand():
  brands = db.brands.find()

  brand_name = input("Brand: ")

  brand = db.brands.find_one({"name": brand_name})
  if brand in brands:
    print(f"{brand_name} already exists in the database")
    return

  ceo = input("CEO: ")
  established_year = int(input("Established year: "))
  website = input("Website: ")
  hq_city = input("In which city is their HQ? ")
  hq_country = input("In which country is their HQ? ")
  active = bool(input(f"Is the {brand_name} still active company (True/False)? "))

  db.brands.insert_one({"name": brand_name, "ceo": ceo, "established_year": established_year, "website": website, "headquarters": {"city": hq_city, "country": hq_country}, "active": active })

  print(f"\n{brand_name} added to database!")

def update_shoe():
  print("Shoe is updated!")

def delete_shoe():
  print("Shoe is deleted!")

def print_commands():
  print("\nCommands:")
  print("\n1. List shoes")
  print("2. Add shoes")
  print("3. Update shoes")
  print("4. Delete shoes")
  print("5. List brands")
  print("6. Add a brand")
  print("7. Update a brand")
  print("8. Delete a brand")
  print("9. Quit")

print_commands()

while True:
  command = input("\nType in the command number: ")

  if command == "1":
    list_shoes()
  elif command == "2":
    add_shoe()
  elif command == "3":
    update_shoe()
  elif command == "4":
    delete_shoe()
  elif command == "5":
    list_brands()
  elif command == "6":
    add_brand()
  elif command == "7":
    update_brand()
  elif command == "8":
    delete_brand()
  elif command == "9":
    break
  else:
    print("Unknown command")

print("\nSee you around!")