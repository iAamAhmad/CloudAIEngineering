# CloudAIEngineering

# API Routes Documentation

## Overview

This document provides documentation for the two API routes developed using FastAPI and Poetry.

## Technologies Used

- FastAPI
- Poetry

## API Routes

### 1. Route 1

- **Endpoint**: `/route1`
- **Description**: This route handles [add a brief description of what this route does].
- **HTTP Method**: GET
- **Parameters**:
  - `param1`: [description of parameter 1]
  - `param2`: [description of parameter 2]
- **Response**:
  - Status Code: 200 OK
  - Content-Type: application/json
  - Body: 
    ```
    {
        "message": "Success",
        "data": [description of returned data]
    }
    ```

### 2. Route 2

- **Endpoint**: `/route2`
- **Description**: This route handles [add a brief description of what this route does].
- **HTTP Method**: POST
- **Request Body**:
  - `param1`: [description of parameter 1]
  - `param2`: [description of parameter 2]
- **Response**:
  - Status Code: 201 Created
  - Content-Type: application/json
  - Body: 
    ```
    {
        "message": "Resource created",
        "data": [description of created resource]
    }
    ```

## How to Use

1. Make sure you have Poetry installed in your development environment.
2. Clone the repository containing the FastAPI project.
3. Install dependencies using Poetry:

