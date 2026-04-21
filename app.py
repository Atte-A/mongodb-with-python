import os
from bson import ObjectId
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
client = MongoClient(MONGODB_URI)

db = client["runningshoe"]

print("\n*** Welcome to your personal running shoe manager ***")

# CRUD operations for SHOES collection
def list_shoes():

  models_count = db.models.count_documents({})

  if models_count == 0:
    print("No shoe models in the database!")
    return
  
  models = db.models.find()

  for model in models:
   brand = db.brands.find_one({"_id": model["brand_id"]})
   print(brand["name"], model["name"])

def add_shoe():
  brand_name = input("Brand: ").strip()
  name_key = brand_name.lower()
  # check if the brand exists
  brand = db.brands.find_one({"name_key": name_key})

  # add_brand if does not exist
  if not brand:
    print(f"Brand '{brand_name}' not found. Let's add it first.")
    brand = add_brand()

  model_name = input("Model: ").strip()
  model_key = model_name.lower()

  rating = float(input("Rating (0-10): "))
  rotation = input("Is this shoe in your current rotation? (true/false): ").lower() == "true"

  db.models.insert_one({
    "brand_id": brand["_id"],
    "name": model_name,
    "name_key": model_key,
    "rating": rating,
    "on_rotation": rotation
  })

  print(f"\n'{brand_name} {model_name}' added into collection!")

def update_shoe():
  updated_shoe = input("Which shoe model you want to update? ").strip()

  shoe = db.models.find_one({"name_key": updated_shoe.lower()})

  if not shoe:
    print(f"No shoe found with name '{updated_shoe}'")
    return
  rating = float(input("Rating (0-10): "))
  rotation = input("Is this shoe in your current rotation? (true/false): ").lower() == "true"

  db.models.update_one(
    {"_id": shoe["_id"]},
    {
      "$set": {
        "rating": rating,
        "on_rotation": rotation
      }
    }
  )

  brand = db.brands.find_one({"_id": shoe["brand_id"]})

  print(f"'{brand['name']} {shoe['name']}' is updated!")

def delete_shoe():
  deleted_shoe = input("Shoe model to delete: ")

  shoe = db.models.find_one({"name": deleted_shoe})

  if not shoe:
    print(f"No shoe model found with name '{deleted_shoe}'")
    return

  brand = db.brands.find_one({"_id": shoe["brand_id"]})
  brand_name = brand["name"]

  db.models.delete_one({"_id": shoe["_id"]})

  print(f"'{brand_name} {deleted_shoe}' is deleted!")

# CRUD operations for BRANDS collections
def list_brands():

  brands_count = db.brands.count_documents({})

  if brands_count == 0:
    print("No brands in the database!")
    return

  brands = db.brands.find()

  for brand in brands:
    print(f"{brand['name']}, {brand['headquarters']['country']}")

def add_brand():
  brand_name = input("Brand: ").strip()

  name_key = brand_name.lower()

  # check if existing
  existing_brand = db.brands.find_one({"name_key": name_key})

  if existing_brand:
    print(f"{brand_name} already exists in the database")
    return

  ceo = input("CEO: ")
  established_year = int(input("Established year: "))
  website = input("Website: ")
  hq_city = input("In which city is their HQ? ")
  hq_country = input("In which country is their HQ? ")
  active = input(f"Is {brand_name} still an active company (true/false)? ").lower() == "true"

  result = db.brands.insert_one({
    "name": brand_name,
    "name_key": name_key,
    "ceo": ceo,
    "established_year": established_year,
    "website": website,
    "headquarters": {
        "city": hq_city,
        "country": hq_country
    },
    "active": active
  })

  brand = db.brands.find_one({"_id": result.inserted_id})

  print(f"\n'{brand_name}' added to database!")
  return brand

def update_brand():
  updated_brand = input("Which brand you want to update? ").strip()

  brand = db.brands.find_one({"name_key": updated_brand.lower()})

  if not brand:
    print(f"'{brand}' is not found")
    return
  
  ceo = input(f"CEO of the '{brand['name']}'? ")
  hq_city = input("In which city is their HQ? ")
  hq_country = input("In which country is their HQ? ")
  active = input(f"Is {brand['name']} still an active company (true/false)? ").lower() == "true"

  db.brands.update_one(
    {"_id": brand["_id"]},
    {
      "$set": {
        "ceo": ceo,
        "headquarters":
        {
          "city": hq_city,
          "country": hq_country
        },
        "active": active
      }
    }
  )

  print(f"'{brand['name']}' is updated!")

def delete_brand():
  deleted_brand = input("Brand to delete: ")

  brand = db.brands.find_one({"name": deleted_brand})

  if not brand:
    print(f"No brand found with name '{deleted_brand}'")
    return

  model_exists = db.models.find_one({"brand_id": brand["_id"]})

  if model_exists:
    print(f"Cannot delete '{deleted_brand}' – shoe models still reference it")
    return

  result = db.brands.delete_one({"_id": brand["_id"]})

  if result.deleted_count == 1:
    print(f"'{deleted_brand}' is deleted!")

# Commands to run the application
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