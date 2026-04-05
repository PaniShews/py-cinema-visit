from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(movie: str,
                 customers: list,
                 hall_number: int,
                 cleaner: str
                 ) -> None:
    cust_list = []

    for cust in customers:
        customer_instances = Customer(
            name=cust["name"],
            food=cust["food"]
        )

        CinemaBar.sell_product(
            product=customer_instances.food,
            customer=customer_instances
        )
        cust_list.append(customer_instances)
    hall = CinemaHall(hall_number)
    cleaning_staff = Cleaner(cleaner)
    hall.movie_session(movie_name=movie,
                       customers=cust_list,
                       cleaning_staff=cleaning_staff)

    customers = [
        {"name": "Bob", "food": "Coca-cola"},
        {"name": "Alex", "food": "popcorn"}
    ]
    hall_number = 5
    cleaner_name = "Anna"
    movie = "Madagascar"
    cinema_visit(customers=customers, hall_number=hall_number, cleaner=cleaner_name, movie=movie)
    # Cinema bar sold Coca-cola to Bob.
    # Cinema bar sold popcorn to Alex.
    # "Madagascar" started in hall number 5.
    # Bob is watching "Madagascar".
    # Alex is watching "Madagascar".
    # "Madagascar" ended.
    # Cleaner Anna is cleaning hall number 5.