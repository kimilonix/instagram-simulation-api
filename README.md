# instagram-simulation-api
Welcome to the Instagram Simulation API! This FastAPI project simulates basic functionalities of Instagram, allowing users to create accounts, post photos, and comment on the others post. This project is intended for educational purposes and to demonstrate the capabilities of FastAPI.

# Features

- User registration and authentication
- Create, comment, update, and delete operations for posts
- Simple in-memory database for demonstration purpose

# Installation

To get started with the Instagram Simulation API, follow these steps:

1. Clone the repository:

      git clone https://github.com/yourusername/instagram-simulation-api.git
   cd instagram-simulation-api
   

2. Create a virtual environment:

      python -m venv venv
   source venv/bin/activate 
   

3. Install the required packages:

      pip install -r requirements.txt
   

4. Run the application:

      uvicorn main:app --reload
   

   The API will be available at http://127.0.0.1:8000.

# Usage

Once the application is running, you can interact with the API using tools like Postman or cURL. You can also explore the interactive API documentation provided by FastAPI at http://127.0.0.1:8000/docs.
