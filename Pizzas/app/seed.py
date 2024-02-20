# from random import choice, choices, sample, randint
import random
import faker

from models import Restaurant,Restaurant_pizza,Pizza, db

fake = faker.Faker()

from app  import app

with app.app_context():
    print("++++++++++++++++++++++++++++++++++++++")
    print("Deleting data...")
    Pizza.query.delete()
    Restaurant_pizza.query.delete()
    Restaurant.query.delete()

    print("++++++++++++++++++++++++++++++++++++")
    print("Creating data...")
    for n in range(20):
        fake_name=  fake.name()
        address= fake.address()

        # Create a restaurant
        restaurant1 = Restaurant(name=fake_name ,address=address)
        # Add the restaurant to database
        db.session.add(restaurant1)
        db.session.commit()

    #random.sample(ingredients, k=3) to select 3 random ingredients instead of potentially selecting the same pizza twice.

    pizzas= ["Peperoni", "Chicken tika", "Mushroom" , "Hawaiian", "Beef", "Barbeque Chicken"]
    sample_ingredients= ["Pepperoni","Onion","Mushroom","Green Pepper","Red Pepper","Olives","Bacon","Chicken","Vegetables"]
    # other_pizza = choices(sample_ingredients , k=3)
    # random_ingedients= ','.join(str(ing) for ing in other_pizza)

    fake_pizzas= []

    for x in range(len(pizzas)):
        other_pizza = random.choices(sample_ingredients , k=3)
        random_ingedients= ','.join(str(ing) for ing in other_pizza)
        fake_pizza= Pizza(name= random.choice(pizzas), ingredients= random_ingedients)
        fake_pizzas.append(fake_pizza)

    print(fake_pizzas)
    db.session.add_all(fake_pizzas)
    db.session.commit()

    for record in range(20):
        rnd_rest=random.choice([x.id for x in Restaurant.query.all()])
        rnd_pizza= random.choice([p.id for p in  Pizza.query.all()])
        db.session.add(Restaurant_pizza(restaurant_id=rnd_rest, pizza_id=rnd_pizza, price= random.randint(1,30)))
        db.session.commit()

    print("++++++++++++++++++++++++++++++++++++")
    print("Finished creating data...")
