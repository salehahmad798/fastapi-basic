from fastapi import FastAPI 
from mockData import products

app = FastAPI()



@app.get("/")
def home():
    return "welcome to the fastapi.. "

@app.get("/contact")
def contact():
    return "you can contact us any time"    

@app.get("/products")
def get_products():
    return products

# Path parameters
# A path parameter is embedded directly in the URL. 
# You declare it with {} in the route string, and FastAPI automatically passes it to your function:

# @app.get("/products/{product_id}")
# def get_product(product_id: int):
#     return {"product_id": product_id}
    


    # Calling /products/42 → product_id = 42
# Calling /products/ → 404 (the parameter is required — the URL pattern won't match)
# FastAPI also does type conversion — if you type-hint int, it converts "42" to 42 and returns a validation error if it's not a valid integer.



# Query parameters
# A query parameter comes after the ? in the URL. Any function parameter that is not in the route string is automatically treated as a query parameter by FastAPI:
# python@app.get("/products")
# def get_products(sort: str = "name", limit: int = 10):
#     return {"sort": sort, "limit": limit}

# /products → sort="name", limit=10 (defaults)
# /products?sort=price → sort="price", limit=10
# /products?sort=price&limit=5 → sort="price", limit=5

# To make a query parameter required (no default), just remove the default value:
# pythondef get_products(sort: str):   # now sort is required

# Using both together
# python@app.get("/products/{product_id}/reviews")
# def get_reviews(product_id: int, page: int = 1, limit: int = 5):
#     # product_id  → path param  (required)
#     # page, limit → query params (optional)
#     return {"product": product_id, "page": page, "limit": limit}
# Calling /products/42/reviews?page=2&limit=20 gives you all three values cleanly.




# 1. Basic integer ID
# @app.get("/products/{product_id}")
# def get_product(product_id: int): # /products/42
# 2. String slug
# @app.get("/categories/{category_name}")
# def get_category(category_name: str): # /categories/laptops
# 3. Multiple parameters
# @app.get("/users/{user_id}/orders/{order_id}")
# def get_order(user_id: int, order_id: int):
# # /users/5/orders/99
# 4. Enum (restrict allowed values)
# class Role(str, Enum):
# admin = "admin"; user = "user"
# @app.get("/roles/{role}")
# def get_role(role: Role): # /roles/admin only
# 5. Catch-all path (includes slashes)
# @app.get("/files/{file_path:path}")
# def get_file(file_path: str):
# # /files/docs/report/2024.pdf

# 1. Basic integer ID — FastAPI auto-converts and validates the type:
# python@app.get("/products/{product_id}")
# def get_product(product_id: int):
#     return {"id": product_id}
# # GET /products/42   → works
# # GET /products/abc  → 422 Unprocessable Entity (not an int)
# 2. String slug — captures any string segment:
# python@app.get("/categories/{category_name}")
# def get_category(category_name: str):
#     return {"category": category_name}
# # GET /categories/laptops → {"category": "laptops"}
# 3. Multiple parameters — order in the URL matches the function params:
# python@app.get("/users/{user_id}/orders/{order_id}")
# def get_order(user_id: int, order_id: int):
#     return {"user": user_id, "order": order_id}
# # GET /users/5/orders/99 → {"user": 5, "order": 99}
# 4. Enum — restricts what values are accepted, great for roles, statuses, categories:
# pythonfrom enum import Enum

# class Role(str, Enum):
#     admin = "admin"
#     user  = "user"
#     guest = "guest"

# @app.get("/roles/{role}")
# def get_role(role: Role):
#     return {"role": role}
# # GET /roles/admin  → works
# # GET /roles/hacker → 422 error
# 5. Catch-all path — the :path converter lets the parameter contain / slashes, useful for file paths or nested slugs:
# python@app.get("/files/{file_path:path}")
# def get_file(file_path: str):
#     return {"path": file_path}
# # GET /files/docs/report/2024.pdf → {"path": "docs/report/2024.pdf"}
# A key thing to remember: route order matters in FastAPI. If you have /products/featured and /products/{product_id}, put the fixed route first — otherwise "featured" will be captured as the product_id:
# python@app.get("/products/featured")   # must come FIRST
# def get_featured(): ...

# @app.get("/products/{product_id}")
# def get_product(product_id: int): 
