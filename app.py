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

def add_shoe():
  brand_name = input("Brand: ")
  model_name = input("Model: ")
  rating = float(input("Rating (0-10): "))
  rotation = bool(input("Is this shoe in your current rotation (True/False): "))

  brand = db.brands.find_one({"name": brand_name})

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

  print(f"\n{brand_name} {model_name} added!")

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
  print("5. Quit")

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
    break
  else:
    print("Unknown command")

print("\nSee you around!")