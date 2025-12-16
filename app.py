from flask import Flask, jsonify, request

app = Flask(__name__)

# Temporary in-memory database (We will replace this with PostgreSQL later)
inventory_data = [
    {"id": 1, "product": "Milk (1L)", "quantity": 50, "price": 1.50},
    {"id": 2, "product": "Cheese (200g)", "quantity": 20, "price": 3.00},
    {"id": 3, "product": "Butter (500g)", "quantity": 15, "price": 2.50}
]

# --- 1. HEALTH CHECK (Keeps your pipeline happy) ---
@app.route('/')
def home():
    return jsonify({"message": "Dairy Inventory System is Running!", "status": "success"}), 200

# --- 2. GET ALL INVENTORY ---
@app.route('/inventory', methods=['GET'])
def get_inventory():
    return jsonify(inventory_data), 200

# --- 3. ADD NEW ITEM ---
@app.route('/inventory', methods=['POST'])
def add_item():
    new_item = request.get_json()
    
    # Simple Validation
    if not new_item or 'product' not in new_item or 'quantity' not in new_item:
        return jsonify({"error": "Invalid data. Product and Quantity are required."}), 400

    # Simulate adding ID
    new_item['id'] = len(inventory_data) + 1
    inventory_data.append(new_item)
    
    return jsonify({"message": "Item added successfully", "item": new_item}), 201

if __name__ == '__main__':
    # 'debug=True' helps you see errors during development
    app.run(host='0.0.0.0', port=5000, debug=True)
