import webbrowser

class Ingredient:
    def __init__(self, name, amount=""):
        self.name = name
        self.amount = amount

    def __str__(self):
        return f"{self.amount} {self.name}" if self.amount else self.name


class Spice:
    def __init__(self, name, amount=""):
        self.name = name
        self.amount = amount

    def __str__(self):
        return f"{self.amount} {self.name}" if self.amount else self.name

class Soup:
    def __init__(self, *ingredients):
        self.ingredients = ingredients

    def cook(self):
        # Generate a search query using the ingredient names
        ingredient_names = [ingredient.name for ingredient in self.ingredients]
        search_query = " ".join(ingredient_names) + " soup recipe"

        # Open a web browser with the search query
        url = f"https://www.google.com/search?q={search_query.replace(' ', '+')}"
        webbrowser.open(url)

        return f"Searching for: {search_query}"

    def __str__(self):
        ingredients_list = ", ".join([str(ingredient) for ingredient in self.ingredients])
        return f"Soup with: {ingredients_list}"


if __name__ == '__main__':
    # Create some ingredients and spices
    carrot = Ingredient("carrot", "2")
    onion = Ingredient("onion", "1 large")
    garlic = Spice("garlic", "3 cloves")
    pepper = Spice("pepper", "1 tsp")

    # Make a soup with those ingredients
    my_soup = Soup(carrot, onion, garlic, pepper)

    # Display the ingredients in the soup
    print(my_soup)

    # Cook the soup (open a search result for the recipe)
    print(my_soup.cook())