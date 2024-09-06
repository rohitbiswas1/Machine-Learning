def recommend_pet_food(species, age):
    if species.lower() == "dog":
        if age < 2:
            return "Puppy food"
        elif 2 <= age <= 7:
            return "Adult dog food"
        else:
            return "Senior dog food"
    
    elif species.lower() == "cat":
        if age < 1:
            return "Kitten food"
        elif 1 <= age <= 5:
            return "Adult cat food"
        else:
            return "Senior cat food"
    
    else:
        return "Unknown species. Please enter either 'dog' or 'cat'."


species = input("Enter the species (dog/cat): ")
age = int(input("Enter the age of the pet in years: "))

food_recommendation = recommend_pet_food(species, age)
print(f"Recommended food: {food_recommendation}")
