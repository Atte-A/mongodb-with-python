# 👟 Running Shoe Manager (CLI + MongoDB)

A simple command-line application for managing running shoes using Python and MongoDB.  

This project was built as part of a coursework assignment to practice CRUD operations, database design, and basic CLI application structure.

## 📌 Features  
### Shoes
- Add new running shoes  
- View all shoes with brand, rating, and rotation status  
- Update shoe rating and rotation status  
- Delete shoes
  
### Brands
- Add new shoe brands
- View all brands with company details
- Update brand information
- Delete brands (only if no shoes are linked)

## 🛠️ Tech Stack
- Python3
- MongoDB (Atlas)
- PyMongo
- python-dotenv

## 🗄️ Database Structure

### Brands collection

| Field                  | Type     | Description                        |
| ---------------------- | -------- | ---------------------------------- |
| `_id`                  | ObjectId | Unique identifier (auto-generated) |
| `name`                 | string   | Brand name                         |
| `name_key`             | string   | Lowercase version for searching    |
| `ceo`                  | string   | CEO name                           |
| `established_year`     | int      | Year the company was founded       |
| `website`              | string   | Official website URL               |
| `headquarters.city`    | string   | Headquarters city                  |
| `headquarters.country` | string   | Headquarters country               |
| `active`               | boolean  | Whether the company is active      |

### Models collection

| Field         | Type     | Description                         |
| ------------- | -------- | ----------------------------------- |
| `_id`         | ObjectId | Unique identifier (auto-generated)  |
| `brand_id`    | ObjectId | Reference to a brand (`brands._id`) |
| `name`        | string   | Shoe model name                     |
| `name_key`    | string   | Lowercase version for searching     |
| `rating`      | float    | Rating between 0–10                 |
| `on_rotation` | boolean  | Whether the shoe is in rotation     |

## 🚀 How to run the project
1. Clone the repository
```
git clone https://github.com/Atte-A/mongodb-with-python.git
cd mongodb-with-python
```
2. Create virtual environment
```
python -m venv venv
source venv/bin/activate
```
3. Install dependencies
```
pip install pymongo python-dotenv
```
4. Create `.env`file
```
MONGODB_URI = your_mongodb_connection_string
```
5. Run the application
```
python app.py
```

## ☁️ MongoDB Atlas
This project uses MongoDB Atlas, which is a cloud-hosted MongoDB database service. It allows you to run MongoDB without installing it locally and provides managed features like scaling, security, and backups.

To use this project, you need to:
- Create a free MongoDB Atlas account
- Create a cluster
- Get your connection string
- Paste it into `.env`file

## 📚 What I learned
- MongoDB CRUD operations
- Working with references between collections
- Structuring a Python CLI application
- Basic data validation and input handling
- Using MongoDB Atlas as a cloud database

## 👤 Author
Atte Ampuja [GitHub](https://www.github.com/Atte-A) | [LinkedIn](https://www.linkedin.com/in/atteampuja/)

## 📄 License
This project is for educational purposes only.







