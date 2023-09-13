# Simple CRUD API Documentation

This documentation outlines the requirements and usage guidelines for the Simple CRUD API.

## Table of Contents

- [Requirements](#requirements)
- [Standard Formats](#standard-formats)
  - [Create Person (POST /api/)](#create-person-post-api)
  - [Read Person (GET /api/)](#read-person-get-api)
  - [Read Single Person (GET /api/{id})](#read-single-person-get-apiid)
  - [Update Person (PUT /api/{id})](#update-person-put-apiid)
  - [Delete Person (DELETE /api/{id})](#delete-person-delete-apiid)
- [Sample Usage](#sample-usage)
  - [Create a New Person](#create-a-new-person)
  - [Read a Person's Details](#read-a-persons-details)
  - [Update a Person's Details](#update-a-persons-details)
  - [Delete a Person](#delete-a-person)

## Requirements

- Python 3.6 or higher
- Django 4 or higher

BASE URL: `https://hngx-stage-two-gxoe.onrender.com/api/`

## Standard Formats

Append the following to the base URL to access the API

For each endpoint, the API follows the following request and response formats:

### Create Person (POST /api)

- **Request:**
  - HTTP Method: POST
  - Endpoint: `/api/`
  - Request Body:
    ```
    json
    {
    	"name": "Tunde"
    }
    ```
- **Response:**
  - HTTP Status Code: 201 Created
  - Response Body:
    ```
    json
    {
    	"id": 1,
    	"name": "Tunde"
    }
    ```

### Read Person (GET /api)

- **Request:**

  - HTTP Method: GET
  - Endpoint: `/api/`

- **Response:**
  - HTTP Status Code: 200 OK
  - Response Body:
    ```
    json
    {
    	"id": 1,
    	"name": "Tunde"
    }
    ```

### Read Single Person (GET /api/{id})

- **Request:**

  - HTTP Method: GET
  - Endpoint: `/api/{id}`

- **Response:**
  - HTTP Status Code: 200 OK
  - Response Body:
    ```
    json
    {
    	"id": 1,
    	"name": "Tunde"
    }
    ```

### Update Person (PUT /api/{id})

- **Request:**

  - HTTP Method: PUT
  - Endpoint: `/api/{id}`
  - Request Body:
    ```
    json
    {
    	"name": "Daniel"
    }
    ```

- **Response:**
  - HTTP Status Code: 200 OK
  - Response Body:
    ```
    json
    {
    	"id": 1,
    	"name": "Daniel"
    }
    ```

### Delete Person (DELETE /api/{id})

- **Request:**

  - HTTP Method: DELETE
  - Endpoint: `/api/{id}`

- **Response:**
  - HTTP Status Code: 204 No Content

## Sample Usage

Below are some examples of how to use the API:

### Create a New Person

```shell
curl -X POST -H "Content-Type: application/json" -d '{
	"name": "Tunde"
}' https://hngx-stage-two-gxoe.onrender.com/api/

```

### Read a Person's Details

```shell
curl https://hngx-stage-two-gxoe.onrender.com/api/1
```

### Update a Person's Details

```shell
curl -X PUT -H "Content-Type: application/json" -d '{
	"name": 'Daniel"
} https://hngx-stage-two-gxoe.onrender.com/api/1
```

### Delete a Person

```shell
curl -X DELETE https://hngx-stage-two-gxoe.onrender.com/api/1
```
