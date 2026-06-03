# 🛠️ Python CRUD Server

A lightweight REST API server built with **FastAPI** and an in-memory store. Supports full Create, Read, Update, and Delete operations out of the box.

---

## 🚀 Quick Start

### 1. Install dependencies

```bash
pip install fastapi uvicorn
```

### 2. Run the server

```bash
uvicorn crud_server:app --reload
```

### 3. Open the interactive docs

Visit [http://localhost:8000/docs](http://localhost:8000/docs) for the Swagger UI.

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/items` | List all items |
| `GET` | `/items/{id}` | Get a single item |
| `POST` | `/items` | Create a new item |
| `PUT` | `/items/{id}` | Replace an item (full update) |
| `PATCH` | `/items/{id}` | Partially update an item |
| `DELETE` | `/items/{id}` | Delete an item |

---

## 📦 Item Schema

```json
{
  "name": "Widget",
  "description": "A nice widget",
  "price": 9.99,
  "in_stock": true
}
```

Responses include an auto-generated `id` field:

```json
{
  "id": "a1b2c3d4-...",
  "name": "Widget",
  "description": "A nice widget",
  "price": 9.99,
  "in_stock": true
}
```

---

## 🧪 Example Requests

**Create an item**
```bash
curl -X POST http://localhost:8000/items \
  -H "Content-Type: application/json" \
  -d '{"name": "Widget", "description": "A nice widget", "price": 9.99}'
```

**List all items**
```bash
curl http://localhost:8000/items
```

**Get one item**
```bash
curl http://localhost:8000/items/<id>
```

**Update an item**
```bash
curl -X PUT http://localhost:8000/items/<id> \
  -H "Content-Type: application/json" \
  -d '{"name": "Updated Widget", "price": 14.99, "in_stock": false}'
```

**Delete an item**
```bash
curl -X DELETE http://localhost:8000/items/<id>
```

---

## 🗂️ Project Structure

```
.
├── crud_server.py   # Main application
└── README.md
```

---

## 🔧 Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/) - modern, fast web framework
- [Pydantic](https://docs.pydantic.dev/) - data validation
- [Uvicorn](https://www.uvicorn.org/) - ASGI server

---

## 📌 Notes

- Data is stored **in memory** — it resets when the server restarts.
- To persist data, swap the `db` dict for SQLite, PostgreSQL, or any database of your choice.

---
