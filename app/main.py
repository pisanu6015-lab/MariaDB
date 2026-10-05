from app.repositories.pet_repository import get_all_pets

def main():
    print("🐾 Happy Paws Pet Hotel")
    print("------------------------")
    # Get all pets from the repository
    pets = get_all_pets()
    # Display each pet
    for pet in pets:
        print(pet)

if __name__ == "__main__":
    main()