# Weather Project

## Overview
This project is a Django-based web application that provides APIs to fetch weather data from an external API and save it to the database, and to retrieve the stored weather data.

## Features
- Fetch weather data for a specific city from the Weather API and save it to the database.
- Retrieve weather data from the database, with optional filtering by city.
- Token-based authentication for secure access to the APIs.

## Endpoints

### Obtain Token
- **URL:** `/api-token-auth/`
- **Method:** `POST`
- **Description:** Obtain an authentication token using username and password.
- **Request Body:**
  ```json
  {
    "username": "username",
    "password": "password"
  }
  ```
- **Response:**
  ```json
  {
    "token": "your_generated_token"
  }
  ```

### Fetch and Save Weather Data
- **URL:** `/fetch-weather_from_api/`
- **Method:** `GET`
- **Description:** Fetch weather data from the Weather API for a specified city and save it to the database.
- **Query Parameters:**
  - `city`: The name of the city to fetch weather data for.
- **Headers:**
  - `Authorization: Token your_generated_token`
- **Response:**
  ```json
  {
    "message": "Weather data fetched and saved successfully.",
    "status": "success",
    "data": {
      "id": 1,
      "city": "City Name",
      "temperature": 25.0,
      "description": "Clear sky",
      "timestamp": "2024-06-21T12:34:56Z"
    }
  }
  ```

### Get Weather Data from Database
- **URL:** `/weather_data_from_db/`
- **Method:** `GET`
- **Description:** Retrieve weather data from the database. If a city name is provided as a query parameter, return data for that city only.
- **Query Parameters:**
  - `city` (optional): The name of the city to filter weather data by.
- **Headers:**
  - `Authorization: Token your_generated_token`
- **Response:**
  ```json
  {
    "message": "Data retrieved successfully.",
    "status": "success",
    "data": [
      {
        "id": 1,
        "city": "City Name",
        "temperature": 25.0,
        "description": "Clear sky",
        "timestamp": "2024-06-21T12:34:56Z"
      }
    ]
  }
  ```
  If no data is available for the specified city:
  ```json
  {
    "message": "No data available for the specified city.",
    "status": "success",
    "data": []
  }
  ```

## Setup

1. **Clone the repository**:
   ```sh
   git clone https://github.com/uzma/weather_project.git
   cd weather_project
   ```

2. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

3. **Run migrations**:
   ```sh
   python manage.py migrate
   ```

4. **Create a superuser** (to access the admin panel):
   ```sh
   python manage.py createsuperuser
   ```

5. **Run the development server**:
   ```sh
   python manage.py runserver
   ```

## Usage

- **Obtain a token** by making a POST request to `/api-token-auth/` with your username and password.
- **Fetch and save weather data** by making a GET request to `/fetch-weather_from_api/` with the city name as a query parameter.
- **Retrieve weather data from the database** by making a GET request to `/weather_data_from_db/` with an optional city name as a query parameter.

