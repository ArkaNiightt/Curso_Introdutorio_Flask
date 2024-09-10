from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ecommerce.db"

db = SQLAlchemy(app)

# Modelagem
# Produto (id, name, price, description)


class Product(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)


@app.route("/api/products/add", methods=["POST"])
def add_product():
    data = request.json
    if "name" in data and "price" in data:
        product = Product(
            name=data["name"],
            price=data["price"],
            description=data.get("description", ""),
        )
        db.session.add(product)
        db.session.commit()
        return jsonify({"message": "Product added sucessfully"})
    return jsonify({"message": "Invalid product data (name or price)"}), 400


@app.route("/api/products/delete/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    product = Product.query.get(product_id)
    if product:
        db.session.delete(product)
        db.session.commit()
        return jsonify({"message": "Product deleted sucessfully"})
    return jsonify({"message": "Product not found"}), 404


@app.route("/api/products/<int:product_id>", methods=["GET"])
def get_product_details(product_id):
    product = Product.query.get(product_id)
    if product:
        return jsonify(
            {
                "id": product.id,
                "name": product.name,
                "price": product.price,
                "description": product.description,
            }
        )
    return jsonify({"message": "Product not found"}), 404


@app.route("/api/products/update/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({"message": "Product not found"}), 404

    data = request.json

    if "name" in data:
        product.name = data["name"]

    if "price" in data:
        product.price = data["price"]

    if "description" in data:
        product.description = data["description"]

    db.session.commit()
    return jsonify({"message": "Product updated sucessfully"})


# Definir uma rota raiz (página inicial) e a função que será executada ao requisitar
@app.route("/")
def hello_world():
    return "Hello World"


# Iniciar app
if __name__ == "__main__":
    app.run(debug=True)
