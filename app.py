from flask import Flask, render_template, jsonify
import random
from datetime import datetime, timedelta

app = Flask(__name__)

# --- Simulated Data ---

def generate_revenue(months=12):
    base = 42000
    data = []
    for i in range(months):
        date = datetime.now() - timedelta(days=30 * (months - 1 - i))
        value = base + random.randint(-8000, 18000) + (i * 1500)
        data.append({"month": date.strftime("%b"), "revenue": round(value, 2)})
    return data

def generate_orders():
    statuses = ["Delivered", "Processing", "Shipped", "Cancelled"]
    customers = ["Wanjiru K.", "Omar A.", "Fatima N.", "James M.", "Aisha L.",
                 "David O.", "Priya S.", "Carlos R.", "Yuki T.", "Leila H."]
    orders = []
    for i in range(20):
        date = datetime.now() - timedelta(days=random.randint(0, 30))
        orders.append({
            "id": f"#ORD-{1000 + i}",
            "customer": random.choice(customers),
            "amount": round(random.uniform(800, 25000), 2),
            "status": random.choice(statuses),
            "date": date.strftime("%d %b %Y"),
        })
    return sorted(orders, key=lambda x: x["id"], reverse=True)

def get_stats():
    return {
        "revenue": {"value": "KES 1,284,500", "change": "+14.2%", "up": True},
        "orders": {"value": "3,847", "change": "+8.1%", "up": True},
        "customers": {"value": "1,204", "change": "+22.5%", "up": True},
        "refunds": {"value": "KES 42,300", "change": "-3.4%", "up": False},
    }

def get_top_products():
    products = [
        {"name": "Premium Plan", "sales": 412, "revenue": 618000, "pct": 92},
        {"name": "Starter Pack", "sales": 289, "revenue": 289000, "pct": 68},
        {"name": "Add-on Bundle", "sales": 201, "revenue": 201000, "pct": 51},
        {"name": "Enterprise Seat", "sales": 87, "revenue": 174000, "pct": 34},
        {"name": "API Access", "sales": 63, "revenue": 63000, "pct": 18},
    ]
    return products

# --- Routes ---

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/stats")
def api_stats():
    return jsonify(get_stats())

@app.route("/api/revenue")
def api_revenue():
    return jsonify(generate_revenue())

@app.route("/api/orders")
def api_orders():
    return jsonify(generate_orders())

@app.route("/api/products")
def api_products():
    return jsonify(get_top_products())

if __name__ == "__main__":
    app.run(debug=True)
