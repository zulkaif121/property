# API Documentation

This document describes the available REST API endpoints for the property management system. All endpoints follow standard REST conventions and return JSON data.

---

## Properties

**Endpoint:** `/api/properties/`

### Methods
- `GET /api/properties/` — List all properties
- `POST /api/properties/` — Create a new property
- `GET /api/properties/{id}/` — Retrieve a property
- `PUT /api/properties/{id}/` — Update a property
- `DELETE /api/properties/{id}/` — Delete a property

### Example Request (POST)
```json
{
  "title": "Luxury Villa",
  "description": "A beautiful villa by the sea.",
  "address": "123 Beach Road",
  "price": 500000,
  "currency": "USD",
  "room_booking": true,
  "total_rooms": 5,
  "room_price": 100,
  "is_available": true,
  "available_from": "2025-07-01",
  "available_to": "2025-08-01",
  "guests": 10,
  "pet_friendly": true,
  "children": 2,
  "location": {"lat": 40.7128, "lng": -74.0060},
  "overview": {"bedrooms": 5, "bathrooms": 3, "sqft": 3500},
  "features": {"cctv": true, "parking": true, "gym": false}
}
```

### Example Response (GET)
```json
{
  "id": 1,
  "title": "Luxury Villa",
  "description": "A beautiful villa by the sea.",
  "address": "123 Beach Road",
  "price": 500000,
  "currency": "USD",
  "room_booking": true,
  "total_rooms": 5,
  "room_price": 100,
  "is_available": true,
  "available_from": "2025-07-01",
  "available_to": "2025-08-01",
  "guests": 10,
  "pet_friendly": true,
  "children": 2,
  "location": {"lat": 40.7128, "lng": -74.0060},
  "overview": {"bedrooms": 5, "bathrooms": 3, "sqft": 3500},
  "features": {"cctv": true, "parking": true, "gym": false},
  "created_at": "2025-07-11T10:00:00Z",
  "updated_at": "2025-07-11T10:00:00Z",
  "images": [],
  "agents": [],
  "reviews": [],
  "bookings": []
}
```

---

## Property Images

**Endpoint:** `/api/images/`

### Methods
- `GET /api/images/` — List all images
- `POST /api/images/` — Upload a new image
- `GET /api/images/{id}/` — Retrieve an image
- `PUT /api/images/{id}/` — Update image info
- `DELETE /api/images/{id}/` — Delete an image

### Example Request (POST)
```json
{
  "image": "base64_or_url",
  "caption": "Front view",
  "uploaded_at": "2025-07-11T10:00:00Z"
}
```

### Example Response (GET)
```json
{
  "id": 1,
  "image": "url_to_image",
  "caption": "Front view",
  "uploaded_at": "2025-07-11T10:00:00Z"
}
```

---

## Property Agents

**Endpoint:** `/api/agents/`

### Methods
- `GET /api/agents/` — List all agents
- `POST /api/agents/` — Create a new agent
- `GET /api/agents/{id}/` — Retrieve an agent
- `PUT /api/agents/{id}/` — Update agent info
- `DELETE /api/agents/{id}/` — Delete an agent

### Example Request (POST)
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "phone": "+1234567890",
  "properties": [1, 2],
  "created_at": "2025-07-11T10:00:00Z",
  "updated_at": "2025-07-11T10:00:00Z"
}
```

### Example Response (GET)
```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com",
  "phone": "+1234567890",
  "properties": [1, 2],
  "created_at": "2025-07-11T10:00:00Z",
  "updated_at": "2025-07-11T10:00:00Z"
}
```

---

## Property Reviews

**Endpoint:** `/api/reviews/`

### Methods
- `GET /api/reviews/` — List all reviews
- `POST /api/reviews/` — Create a new review
- `GET /api/reviews/{id}/` — Retrieve a review
- `PUT /api/reviews/{id}/` — Update a review
- `DELETE /api/reviews/{id}/` — Delete a review

### Example Request (POST)
```json
{
  "property": 1,
  "user_name": "Jane Smith",
  "rating": 5,
  "comment": "Amazing place!",
  "created_at": "2025-07-11T10:00:00Z",
  "updated_at": "2025-07-11T10:00:00Z"
}
```

### Example Response (GET)
```json
{
  "id": 1,
  "property": 1,
  "user_name": "Jane Smith",
  "rating": 5,
  "comment": "Amazing place!",
  "created_at": "2025-07-11T10:00:00Z",
  "updated_at": "2025-07-11T10:00:00Z"
}
```

---

## Payment Methods

**Endpoint:** `/api/payments/`

### Methods
- `GET /api/payments/` — List all active payment methods
- `GET /api/payments/{id}/` — Retrieve a payment method

### Example Response (GET)
```json
{
  "id": 1,
  "name": "Credit Card",
  "description": "Pay using credit card.",
  "is_active": true,
  "created_at": "2025-07-11T10:00:00Z",
  "updated_at": "2025-07-11T10:00:00Z"
}
```

---

## Bookings

**Endpoint:** `/api/bookings/`

### Methods
- `GET /api/bookings/` — List all bookings
- `POST /api/bookings/` — Create a new booking
- `GET /api/bookings/{id}/` — Retrieve a booking
- `PUT /api/bookings/{id}/` — Update a booking
- `DELETE /api/bookings/{id}/` — Delete a booking

### Example Request (POST)
```json
{
  "property": 1,
  "user_name": "Alice Brown",
  "user_email": "alice@example.com",
  "user_phone": "+1234567890",
  "guests": 4,
  "check_in_date": "2025-07-15",
  "check_out_date": "2025-07-20"
}
```

### Example Response (GET)
```json
{
  "id": 1,
  "property": 1,
  "user_name": "Alice Brown",
  "user_email": "alice@example.com",
  "user_phone": "+1234567890",
  "guests": 4,
  "check_in_date": "2025-07-15",
  "check_out_date": "2025-07-20"
}
```

---

## Accounts

**Endpoint:** `/api/users/`

### Methods
- `GET /api/users/` — List all users
- `POST /api/users/` — Register a new user
- `GET /api/users/{id}/` — Retrieve a user
- `PUT /api/users/{id}/` — Update a user
- `DELETE /api/users/{id}/` — Delete a user

### Example Request (POST)
```json
{
  "username": "newuser",
  "email": "newuser@example.com",
  "password": "securepassword",
  "phone_number": "+1234567890",
  "address": "456 Main St",
  "full_name": "New User"
}
```

### Example Response (GET)
```json
{
  "username": "newuser",
  "email": "newuser@example.com",
  "phone_number": "+1234567890",
  "address": "456 Main St",
  "full_name": "New User"
}
```

---

**Endpoint:** `/api/login/`

### Method
- `POST /api/login/` — Authenticate user and return token

### Example Request
```json
{
  "username": "newuser",
  "password": "securepassword"
}
```

### Example Response
```json
{
  "token": "your_auth_token"
}
```

---

**Endpoint:** `/api/profile/`

### Method
- `GET /api/profile/` — Get current authenticated user's profile

### Example Response
```json
{
  "username": "newuser",
  "email": "newuser@example.com",
  "phone_number": "+1234567890",
  "address": "456 Main St",
  "full_name": "New User"
}
```

---

## Notes
- All endpoints return JSON.
- Authentication may be required for some endpoints.
- Dates should be in ISO 8601 format.

---
