import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import PizzaForm from "./PizzaForm";

function Home() {
  const [{ data: restaurant, error, status }, setRestaurant] = useState({
    data: null,
    error: null,
    status: "pending",
  });
  const { id } = useParams();

  

  useEffect(() => {
    fetch(`/restaurants/${id}`).then((r) => {
      if (r.ok) {
        r.json().then((restaurant) =>
          setRestaurant({ data: restaurant, error: null, status: "resolved" })
        );
      } else {
        r.json().then((err) =>
          setRestaurant({ data: null, error: err.error, status: "rejected" })
        );
      }
    });
  }, [id]);

  console.log(restaurant)

  function handleAddPizza(newPizza) {
    setRestaurant({
      data: {
        ...restaurant,
        pizzas: [...restaurant.restaurant_pizzas, newPizza],
      },
      error: null,
      status: "resolved",
    });
    alert('Successifully saved')
    window.location.reload();
  }

  if (status === "pending") return <h1>Loading...</h1>;
  if (status === "rejected") return <h1>Error: {error.error}</h1>;

  return (
    <section className="container">
      <div className="card">
        <h1>{restaurant.name}</h1>
        <p>{restaurant.address}</p>
      </div>
      <div className="card">
        <h2>Pizza Menu</h2>
        {restaurant.restaurant_pizzas.map((pizza) => (
          <div key={pizza.id}>
            <h3>{pizza.pizza.name}</h3>
            <p>
              <em>{pizza.pizza.ingredients}</em>
            </p>
          </div>
        ))}
      </div>
      <div className="card">
        <h3>Add New Pizza</h3>
        <PizzaForm restaurantId={restaurant.id} onAddPizza={handleAddPizza} />
      </div>
    </section>
  );
}

export default Home;
