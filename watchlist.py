import json

# Initialize the watchlist as a list of dictionaries
watchlist = []

def add_movie():
    """Adds a new movie to the watchlist with a default unwatched status."""
    title = input("\nEnter the movie title: ").strip()
    if title:
        # Check if movie already exists
        if any(movie['title'].lower() == title.lower() for movie in watchlist):
            print(f"'{title}' is already in your watchlist!")
        else:
            watchlist.append({"title": title, "watched": False})
            print(f" Added '{title}' to your watchlist.")
    else:
        print(" Movie title cannot be empty.")

def show_movies():
    """Displays all movies with their current watched/unwatched status."""
    if not watchlist:
        print("\nYour watchlist is currently empty.")
        return

    print("\n--- Your Movie Watchlist ---")
    for index, movie in enumerate(watchlist, start=1):
        status = "Watched" if movie["watched"] else "⏳ Unwatched"
        print(f"{index}. {movie['title']} [{status}]")

def mark_watched():
    """Marks a selected movie as watched."""
    if not watchlist:
        print("\n No movies to mark as watched.")
        return

    show_movies()
    try:
        choice = int(input("\nEnter the number of the movie you watched: "))
        if 1 <= choice <= len(watchlist):
            watchlist[choice - 1]["watched"] = True
            print(f" Awesome! Marked '{watchlist[choice - 1]['title']}' as Watched.")
        else:
            print(" Invalid number selection.")
    except ValueError:
        print(" Please enter a valid number.")

def remove_movie():
    """Removes a movie from the watchlist."""
    if not watchlist:
        print("\n No movies to remove.")
        return

    show_movies()
    try:
        choice = int(input("\nEnter the number of the movie to remove: "))
        if 1 <= choice <= len(watchlist):
            removed = watchlist.pop(choice - 1)
            print(f" Removed '{removed['title']}' from your list.")
        else:
            print(" Invalid number selection.")
    except ValueError:
        print("Please enter a valid number.")

def main_menu():
    """Runs the main continuous menu loop for the application."""
    while True:
        print("\n=============================")
        print("  MOVIE WATCHLIST MENU  ")
        print("=============================")
        print("1. Add a Movie")
        print("2. Show Movie List")
        print("3. Mark a Movie as Watched")
        print("4. Remove a Movie")
        print("5. Exit")
        
        choice = input("\nChoose an option (1-5): ").strip()
        
        if choice == "1":
            add_movie()
        elif choice == "2":
            show_movies()
        elif choice == "3":
            mark_watched()
        elif choice == "4":
            remove_movie()
        elif choice == "5":
            print("\n Goodbye! Happy watching!")
            break
        else:
            print(" Invalid choice. Please select from 1 to 5.")

# Run the project from start to finish
if __name__ == "__main__":
    main_menu()
