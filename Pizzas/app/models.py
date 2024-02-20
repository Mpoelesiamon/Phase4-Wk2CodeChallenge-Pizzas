from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

db = SQLAlchemy()

class Restaurant(db.Model,  SerializerMixin):
    __tablename__ = 'restaurants'

    serialize_rules= ('-restaurants_pizzas.restaurant',)

    id = db.Column(db.Integer, primary_key=True)
    name=  db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(256))
    
    restaurant_pizzas=  db.relationship('Restaurant_pizza', backref='restaurant')

    # def serialize(self):
    #     return {"id": self.id , "name": self.name, "address": self.address}
    
    def __repr__(self):
        return f"Restaurant {self.name} Address: {self.address}"

class Pizza(db.Model,  SerializerMixin):
    __tablename__= 'pizzas'
    
    serialize_rules= ('-restaurants_pizzas.pizza',)

    id=  db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    ingredients= db.Column(db.String(), nullable=False)
    created_at=  db.Column(db.DateTime, server_default=db.func.now())
    updated_at=  db.Column(db.DateTime, onupdate=db.func.now())
    
    restaurant_pizzas=  db.relationship('Restaurant_pizza', backref='pizza')

    # def serialize(self):
    #     return {"id": self.id , "name": self.name, "ingredients": self.ingredients}
    
    def __repr__(self):
        return f"Pizza {self.name}"
    
class Restaurant_pizza(db.Model, SerializerMixin):
    __tablename__='restaurant_pizzas'

    serialize_rules= ('-pizza.restaurant_pizzas', '-restaurant.restaurant_pizzas')
    
    id=  db.Column(db.Integer, primary_key=True)
    pizza_id= db.Column(db.Integer, db.ForeignKey('pizzas.id'), nullable=False)
    restaurant_id= db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)
    price= db.Column(db.Integer, nullable=False)
    created_at=  db.Column(db.DateTime, server_default=db.func.now())
    updated_at=  db.Column(db.DateTime, onupdate=db.func.now())

    @validates('price')
    def validate_price(self, key, value):
        if value is None and value==range(1,30):
            raise ValueError ("Price must be between 1 and 30")
        return  value 
    
    # def serialize(self):
    #     return {"id": self.id , "pizza": self.pizza_id, "restaurant": {self.restaurant_id} ,"price": self.price}

    def __repr__(self):
         return f'Pizza: {self.pizza_id}, Price: Ksh{self.price}'
    
     
# add any models you may need. 