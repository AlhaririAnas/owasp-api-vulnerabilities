# Insecure API for Educational Purposes  

This project is a deliberately insecure API designed to demonstrate common security vulnerabilities outlined in the OWASP API Top 10. The API should **only** be used for learning purposes and must **never** be deployed in a production environment.

---

## **Table of Contents**  
1. [Features and Purpose](#features-and-purpose)  
2. [How It Works](#how-it-works)  
3. [Setup Instructions](#setup-instructions)  
4. [Available Endpoints](#available-endpoints)  
5. [Examples of Usage](#examples-of-usage)  
6. [Warnings and Notes](#warnings-and-notes)  

---

## **Features and Purpose**  

This API simulates the following vulnerabilities:  
- **Unrestricted Resource Consumption**: A resource-intensive endpoint with no rate limits.  
- **Server Side Request Forgery (SSRF)**: An endpoint that accepts and executes unvalidated external requests.  
- **Security Misconfiguration**: An endpoint exposing sensitive data like default admin credentials.  
- **Unsafe Consumption of APIs**: An endpoint that blindly trusts and processes user inputs.  

---

## **How It Works**  

The API has been built using **Python** and the **Flask** framework. Each route demonstrates a specific vulnerability for testing or educational purposes:  
1. It handles HTTP requests and responds with JSON.  
2. It includes endpoints to simulate unsafe API behaviors.  
3. It highlights why such practices can lead to potential breaches.

---

## **Setup Instructions**  

### **1. Prerequisites**  
Ensure you have the following installed:  
- Python 3.8 or higher  
- `pip` (Python's package manager)  

### **2. Install Dependencies**  
Clone this repository or download the code, then run:  
```bash
pip install flask requests
```

### **3. Run the Application**  
Execute the API server by running:  
```bash
python app.py
```
The API will be accessible at `http://127.0.0.1:5000/`.

---

## **Available Endpoints**  

### **1. `/` (Home)**  
- **Method**: `GET`  
- **Description**: Displays a welcome message.  
- **Example Response**:  
  ```json
  {"message": "Welcome to the Insecure API for educational purposes!"}
  ```

### **2. `/heavy` (Unrestricted Resource Consumption)**  
- **Method**: `GET`  
- **Description**: Simulates a resource-intensive process by creating a large list.  
- **Example Response**:  
  ```json
  {"message": "Processed a large request", "data_size": 1000000}
  ```

### **3. `/proxy` (Server Side Request Forgery - SSRF)**  
- **Method**: `GET`  
- **Parameters**:  
  - `url` (Query Parameter): The URL to be fetched by the server.  
- **Description**: Fetches the contents of the provided URL without validation.  
- **Example Request**:  
  ```bash
  curl "http://127.0.0.1:5000/proxy?url=http://example.com"
  ```
- **Example Response**:  
  ```json
  {"proxied_response": "<html><head>Example...</html>"}
  ```

### **4. `/admin` (Security Misconfiguration)**  
- **Method**: `GET`  
- **Description**: Exposes default admin credentials.  
- **Example Response**:  
  ```json
  {"message": "Admin area accessed", "default_password": "admin123"}
  ```

### **5. `/external` (Unsafe Consumption of APIs)**  
- **Method**: `POST`  
- **Body**: JSON with a `name` field.  
- **Description**: Echoes user input directly in the response.  
- **Example Request**:  
  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"name": "Alice"}' http://127.0.0.1:5000/external
  ```
- **Example Response**:  
  ```json
  {"unsafe_response": "Hello, Alice!"}
  ```

---

## **Examples of Usage**  

### 1. **Simulating Resource Exhaustion**  
Run a `GET` request to `/heavy`. Observe how it processes a computationally intensive task, which could slow down the server.  

### 2. **Testing SSRF**  
Use `/proxy` with a malicious or internal URL (e.g., `http://127.0.0.1:5000/admin`) to demonstrate how this could expose sensitive data.  

### 3. **Exposing Default Credentials**  
Visit `/admin` to view hardcoded admin passwords, simulating poor security practices.  

### 4. **Trusting Malicious Inputs**  
Send a crafted JSON payload to `/external` to demonstrate the risks of blindly trusting user input.
