# SmartBuy AI — Intelligent E-Commerce Platform

SmartBuy AI is a full-stack e-commerce web application built with Django, designed to simulate real-world platforms like Amazon and Flipkart. It integrates user authentication, product management, order processing, and a behavior-driven recommendation system to deliver a personalized shopping experience.

---

## Overview

This project demonstrates the design and development of a scalable e-commerce system with a focus on user behavior tracking and intelligent product recommendations. It combines backend engineering, frontend design, and basic machine learning logic into a single cohesive product.

---

## Key Features

### Authentication System

* Secure user registration and login
* Custom user model support
* Dynamic navigation based on authentication state

### Product Management

* Product listing and detail pages
* Image handling and category organization
* Structured data models for scalability

### Recommendation Engine

* Tracks user interactions:

  * Product views
  * Cart actions
  * Purchases
* Generates personalized product suggestions
* Avoids already viewed products
* Uses weighted scoring logic for ranking

### Cart and Order System

* Add to cart functionality
* Checkout process
* Order history tracking per user

### Review System

* User-generated product reviews
* Basic fake/spam review detection logic

### Search and Filtering

* Real-time product search
* Category-based filtering

### Chatbot Integration

* FAQ chatbot for handling common user queries

### Frontend Experience

* Responsive layout
* Clean and modern UI
* Interactive components for better user engagement

---

## Technology Stack

**Backend**

* Python
* Django

**Frontend**

* HTML
* CSS (Tailwind CSS)
* JavaScript

**Database**

* SQLite (development)

**Additional Components**

* Custom recommendation engine (behavior-based logic)

---

## Project Structure

```
smartbuy_ai/
│
├── accounts/         # Authentication and user management
├── products/         # Product models and views
├── cart/             # Cart functionality
├── orders/           # Order processing
├── reviews/          # Review system
├── chatbot/          # FAQ chatbot
├── recommendations/  # Recommendation engine
│
├── templates/        # HTML templates
├── static/           # CSS and JavaScript
├── media/            # Uploaded images
│
└── manage.py
```

---

## Installation and Setup

### 1. Clone the Repository

```
git clone https://github.com/rivubiswas/smartbuy-ai.git
cd smartbuy-ai
```

### 2. Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Apply Migrations

```
python manage.py migrate
```

### 5. Run Development Server

```
python manage.py runserver
```

---

## Future Improvements

* Advanced recommendation system (collaborative filtering)
* Integration with cloud storage for media (AWS S3 or Cloudinary)
* Payment gateway integration
* Admin analytics dashboard
* Performance optimization and caching

---

## Key Highlights

* Designed with modular architecture for scalability
* Implements behavior-based recommendation logic
* Covers end-to-end e-commerce workflow
* Combines full-stack development with applied ML concepts

---

## Impact

* Built a complete end-to-end e-commerce system simulating real-world platforms like Amazon, covering authentication, product management, cart, and order workflows.

* Implemented a behavior-based recommendation engine that personalizes product suggestions using user activity (views, cart actions, purchases), improving user engagement compared to static listings.

* Designed a modular and scalable architecture, separating concerns across multiple Django apps (accounts, products, orders, recommendations), making the system maintainable and extensible.

* Integrated multiple components (authentication, AI logic, chatbot, reviews) into a single cohesive application, demonstrating full-stack development capability.

* Focused on user experience with a responsive UI and dynamic features, improving usability and interaction flow.

* Showcases practical understanding of how real-world systems track user behavior and use data-driven logic to enhance product discovery.

---

## Author

Rivu Biswas

---

## License

This project is for educational and portfolio purposes.
