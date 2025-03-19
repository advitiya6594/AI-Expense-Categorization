# AI-Expense-Categorization
# 🧠 AI-Powered Expense Categorization System 🚀

An intelligent bookkeeping assistant that uses **AI & Machine Learning** to automatically categorize financial transactions, reducing manual effort for accountants and finance teams.

---

## 📌 Overview

This system is designed to **automate expense categorization** by analyzing transaction descriptions using **Machine Learning (NLP)**. It integrates with **Plaid API** for real-time transaction data and provides a dashboard for visualization.

### ✨ Key Features
✅ **AI-Based Categorization:** Automatically classifies expenses using ML.  
✅ **Bank Statement Parsing:** Extracts transactions from **PDF/CSV** using **OCR & NLP**.  
✅ **Real-Time Dashboard:** Displays categorized expenses, trends, and analytics.  
✅ **API Integration:** Fetches live transaction data from **Plaid API**.  
✅ **Secure & Scalable:** Built with **FastAPI, PostgreSQL, AWS Lambda**.  
✅ **Automated Testing:** Implements **unit tests (Pytest, JUnit5)** for reliability.  

---
---

## 🛠️ Tech Stack

| **Category**       | **Technology** |
|-------------------|----------------|
| **Frontend**     | React.js, Next.js |
| **Backend**      | FastAPI (Python) |
| **Database**     | PostgreSQL, Firebase |
| **Machine Learning** | NLP (Scikit-Learn, TensorFlow) |
| **Cloud Services** | AWS Lambda, Plaid API |
| **Testing** | Pytest, JUnit5, Postman |
| **Security** | OAuth2, JWT Authentication |

---

## 📌 API Endpoints

### 🟢 Transaction API

| Method | Endpoint | Description |
|--------|---------|-------------|
| **POST** | `/categorize` | Categorizes a transaction using AI |
| **GET** | `/transactions` | Fetches all stored transactions |
| **POST** | `/transactions` | Adds a new transaction |

### 🔵 Authentication API

| Method | Endpoint | Description |
|--------|---------|-------------|
| **POST** | `/auth/signup` | Registers a new user |
| **POST** | `/auth/login` | Logs in a user and returns a JWT token |

---

## 💾 Database Schema

### 📝 Transaction Table

| Column | Type | Description |
|--------|------|-------------|
| `id` | INT (Primary Key) | Unique ID for each transaction |
| `description` | TEXT | Transaction details |
| `amount` | FLOAT | Transaction amount |
| `date` | DATE | Transaction date |
| `category` | TEXT | AI-predicted category |

---

## 🚀 Installation Guide

### 1️⃣ Prerequisites

Before running the project, ensure you have the following installed:
- **Python 3.9+**
- **Node.js & npm**
- **Docker (for containerized setup)**
- **AWS Account (for Lambda deployment)**

---


