import requests
from bs4 import BeautifulSoup

# Ingredient class to manage user input and check recipes
class Ingredient:
    def __init__(self, ingredients):
        # Ingredients will be stored as a list of lowercase strings
        self.ingredients = [ingredient.strip().lower() for ingredient in ingredients]

    # Method to check if all ingredients are found in the recipe content
    def check_in_recipe(self, recipe_content):
        recipe_content_lower = recipe_content.lower()
        # Using str.find() to check if each ingredient is present
        return all(recipe_content_lower.find(ingredient) != -1 for ingredient in self.ingredients)

# Soup class to manage web content fetching and recipe parsing
class Soup:
    def __init__(self, base_url):
        self.base_url = base_url

    # Method to fetch the HTML links from the base URL
    def fetch_links(self):
        response = requests.get(self.base_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        links = soup.find_all('a')
        return links

    # Method to fetch the content of each recipe page
    def fetch_recipe_content(self, link):
        full_url = self.base_url + link.get('href')
        recipe_response = requests.get(full_url)
        recipe_soup = BeautifulSoup(recipe_response.content, 'html.parser')
        return full_url, recipe_soup.get_text(separator='\n').strip()

# Main program
def main():
    # Base URL of the recipes page
    base_url = "https://codingnomads.github.io/recipes/"

    # Taking user input for ingredients
    user_ingredients = input("Enter ingredients separated by commas: ").split(",")

    # Creating instances of Ingredient and Soup classes
    ingredient_checker = Ingredient(user_ingredients)
    soup_scraper = Soup(base_url)

    # Fetching the HTML links from the base URL
    recipe_links = soup_scraper.fetch_links()

    # Looping through the recipe links and checking each one
    for link in recipe_links:
        href = link.get('href')
        if href:
            # Fetch the recipe content
            recipe_url, recipe_content = soup_scraper.fetch_recipe_content(link)

            # Check if the recipe contains the user's ingredients
            if ingredient_checker.check_in_recipe(recipe_content):
                print(f"\nRecipe found at: {recipe_url}")
                print(recipe_content)
                print("="*292)

if __name__ == "__main__":
    main()