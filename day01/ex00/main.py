from recipe import Recipe
from book import Book
from book import error_check

if __name__ == "__main__":
    test = Recipe("fergre", 2, 1, ["gregre"], "gerger", "starter")
    book = Book("book", "19/09/2019", 19, {'starter': {'salade', 'pain'}, 'lunch': {'sandwich', 'crepe'}, 'dessert' : {'creme', 'banane flambee'}})
    error_check(book)
