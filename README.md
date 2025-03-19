# Flask API on Vercel

This is a simple Flask API that provides CRUD operations for managing users. The API is deployed on **Vercel** and supports the following endpoints:

- **Create a user** (`POST /users`)
- **Get all users** (`GET /users`)
- **Get a specific user** (`GET /users/<user_id>`)
- **Update a user** (`PUT /users/<user_id>`)
- **Delete a user** (`DELETE /users/<user_id>`)

---

## Features
- **Lightweight & Fast:** Built with Flask.
- **RESTful API:** Provides endpoints for user management.
- **Easy Deployment:** Deployed on **Vercel**.
- **Serverless Execution:** Runs as a serverless function.

---

## Project Structure
```
/flask-app
  ├── api/
  │   ├── index.py  # Flask API Code
  ├── requirements.txt
  ├── vercel.json
  ├── README.md
```

---

## Prerequisites
Ensure you have the following installed:

- **Python 3.x**
- **pip** (Python package manager)
- **Vercel CLI** (for deployment)

Install **Vercel CLI** if not installed:
```sh
npm install -g vercel
```

---

## Setup Instructions

### **1. Clone the Repository**
```sh
git clone <repository-url>
cd flask-app
```

### **2. Install Dependencies**
```sh
pip install -r requirements.txt
```

### **3. Run Locally**
```sh
python api/index.py
```
- The API should now be running on `http://127.0.0.1:5000/`

---

## Deployment on Vercel

### **1. Create `vercel.json` (if not already created)**
Ensure this file exists in the root directory:
```json
{
  "version": 2,
  "builds": [
    {
      "src": "api/index.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "/api/index.py"
    }
  ]
}
```

### **2. Deploy on Vercel**
Login to **Vercel**:
```sh
vercel login
```
Deploy the app:
```sh
vercel
```
Follow the prompts, and Vercel will deploy your **Flask API**.

---

## API Endpoints

### **1. Create a User**
- **Endpoint:** `POST /users`
- **Request Body:**
  ```json
  {
    "name": "Alice",
    "email": "alice@example.com",
    "age": 25
  }
  ```
- **Response:**
  ```json
  {
    "id": 1,
    "name": "Alice",
    "email": "alice@example.com",
    "age": 25
  }
  ```

### **2. Get All Users**
- **Endpoint:** `GET /users`
- **Response:**
  ```json
  [
    {
      "id": 1,
      "name": "Alice",
      "email": "alice@example.com",
      "age": 25
    }
  ]
  ```

### **3. Get a Specific User**
- **Endpoint:** `GET /users/<user_id>`
- **Response:**
  ```json
  {
    "id": 1,
    "name": "Alice",
    "email": "alice@example.com",
    "age": 25
  }
  ```

### **4. Update a User**
- **Endpoint:** `PUT /users/<user_id>`
- **Request Body:**
  ```json
  {
    "name": "Alice Updated"
  }
  ```
- **Response:**
  ```json
  {
    "id": 1,
    "name": "Alice Updated",
    "email": "alice@example.com",
    "age": 25
  }
  ```

### **5. Delete a User**
- **Endpoint:** `DELETE /users/<user_id>`
- **Response:**
  ```json
  {
    "message": "User deleted"
  }
  ```

---

## Testing the API with `curl`

### **Create User**
```sh
curl -X POST "https://your-project.vercel.app/users" -H "Content-Type: application/json" -d '{"name": "Alice", "email": "alice@example.com", "age": 25}'
```

### **Get All Users**
```sh
curl "https://your-project.vercel.app/users"
```

### **Update User**
```sh
curl -X PUT "https://your-project.vercel.app/users/1" -H "Content-Type: application/json" -d '{"name": "Alice Updated"}'
```

### **Delete User**
```sh
curl -X DELETE "https://your-project.vercel.app/users/1"
```

---

## Conclusion
Your **Flask API** is now deployed on **Vercel** and accessible via the provided URL. 🚀

Feel free to contribute or modify the project! 🎉

