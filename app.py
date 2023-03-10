from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@localhost/restoran'
db = SQLAlchemy(app)

class Ingredient(db.Model):
    __tablename__ = 'ingredients'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now(), onupdate=db.func.now())

class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now(), onupdate=db.func.now())
    
#Ingredients
@app.route('/ingredients', methods=['GET'])
def get_ingredients():
    ingredients = Ingredient.query.all()
    return jsonify({'ingredients': [i.name for i in ingredients]})

@app.route('/ingredients/<int:id>', methods=['GET'])
def get_ingredient(id):
    ingredient = Ingredient.query.get(id)
    if not ingredient:
        return jsonify({'message': 'Ingredient not found'}), 404
    return jsonify({'ingredient': ingredient.name})

@app.route('/ingredients', methods=['POST'])
def create_ingredient():
    name = request.json.get('name')
    if not name:
        return jsonify({'message': 'Name is required'}), 400
    ingredient = Ingredient(name=name)
    db.session.add(ingredient)
    db.session.commit()
    return jsonify({'message': 'Ingredient created', 'ingredient': ingredient.name})

@app.route('/ingredients/<int:id>', methods=['PUT'])
def update_ingredient(id):
    ingredient = Ingredient.query.get(id)
    if not ingredient:
        return jsonify({'message': 'Ingredient not found'}), 404
    name = request.json.get('name')
    if not name:
        return jsonify({'message': 'Name is required'}), 400
    ingredient.name = name
    db.session.commit()
    return jsonify({'message': 'Ingredient updated', 'ingredient': ingredient.name})
  
@app.route('/ingredients/<int:id>', methods=['DELETE'])
def delete_ingredient(id):
  ingredient = Ingredient.query.get(id)
  db.session.delete(ingredient)
  db.session.commit()
  return jsonify({'message': 'Ingredient deleted'})

#Categories
@app.route('/categories', methods=['GET'])
def get_categories():
    categories = Category.query.all()
    return jsonify({'categories': [c.name for c in categories]})

@app.route('/categories/<int:id>', methods=['GET'])
def get_categories(id):
    categories = Category.query.get(id)
    if not categories:
        return jsonify({'message': 'Category not found'}), 404
    return jsonify({'category': category.name})

@app.route('/categories', methods=['POST'])
def create_category():
    name = request.json.get('name')
    if not name:
        return jsonify({'message': 'Name is required'}), 400
    category = Category(name=name)
    db.session.add(category)
    db.session.commit()
    return jsonify({'message': 'Category created', 'category': category.name})

@app.route('/categories/<int:id>', methods=['PUT'])
def update_category(id):
    category= Category.query.get(id)
    if not category:
        return jsonify({'message': 'Category not found'}), 404
    name = request.json.get('name')
    if not name:
        return jsonify({'message': 'Name is required'}), 400
    category.name = name
    db.session.commit()
    return jsonify({'message': 'Category updated', 'category': category.name})
  
@app.route('/categories/<int:id>', methods=['DELETE'])
def delete_category(id):
  category = Category.query.get(id)
  db.session.delete(category)
  db.session.commit()
  return jsonify({'message': 'Category deleted'})

#Recipe
