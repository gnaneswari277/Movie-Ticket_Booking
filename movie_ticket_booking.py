# Movie Ticket Booking System

bookings = []

movies = {
    "1": {"name": "Avengers", "price": 200},
    "2": {"name": "Inception", "price": 180},
    "3": {"name": "Interstellar", "price": 220},
    "4": {"name": "Leo", "price": 160}
}


def display_movies():
    print("\n===== AVAILABLE MOVIES =====")

    for key, movie in movies.items():
        print(f"{key}. {movie['name']} - ₹{movie['price']}")


def book_ticket():
    print("\n===== BOOK MOVIE TICKET =====")

    display_movies()

    movie_choice = input("\nEnter movie number: ")

    if movie_choice not in movies:
        print("Invalid movie choice.")
        return

    movie = movies[movie_choice]

    name = input("Enter customer name: ")
    tickets = int(input("Enter number of tickets: "))

    total = movie["price"] * tickets

    booking = {
        "Customer": name,
        "Movie": movie["name"],
        "Tickets": tickets,
        "Total": total
    }

    bookings.append(booking)

    print("\nTicket booked successfully! ✅")
    print("Movie :", movie["name"])
    print("Tickets :", tickets)
    print("Total Amount : ₹", total)


def view_bookings():
    print("\n===== ALL BOOKINGS =====")

    if not bookings:
        print("No bookings found.")
        return

    for i, booking in enumerate(bookings, start=1):
        print(f"\nBooking {i}")
        print("Customer :", booking["Customer"])
        print("Movie    :", booking["Movie"])
        print("Tickets  :", booking["Tickets"])
        print("Total    : ₹", booking["Total"])


def search_booking():
    print("\n===== SEARCH BOOKING =====")

    name = input("Enter customer name: ")

    found = False

    for booking in bookings:
        if booking["Customer"].lower() == name.lower():
            print("\nBooking Found ✅")
            print("Customer :", booking["Customer"])
            print("Movie    :", booking["Movie"])
            print("Tickets  :", booking["Tickets"])
            print("Total    : ₹", booking["Total"])
            found = True

    if not found:
        print("No booking found.")


def cancel_booking():
    print("\n===== CANCEL BOOKING =====")

    name = input("Enter customer name: ")

    for booking in bookings:
        if booking["Customer"].lower() == name.lower():
            bookings.remove(booking)
            print("Booking cancelled successfully. ✅")
            return

    print("No booking found.")


def main():
    while True:
        print("\n================================")
        print("     MOVIE TICKET BOOKING")
        print("================================")
        print("1. Display Movies")
        print("2. Book Ticket")
        print("3. View Bookings")
        print("4. Search Booking")
        print("5. Cancel Booking")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            display_movies()

        elif choice == "2":
            book_ticket()

        elif choice == "3":
            view_bookings()

        elif choice == "4":
            search_booking()

        elif choice == "5":
            cancel_booking()

        elif choice == "6":
            print("\nThank you for using the Movie Ticket Booking System!")
            break

        else:
            print("Invalid choice. Please try again.")


main();
