from food_search import food_search

def main():
    api_key = 'AIzaSyA6PlZk4J8p6s8Nfm_p1nX58Lk6gOyMYX0'
    food_places = {}

    food = food_search(api_key, food_places)

    food.search()
    
if __name__ == "__main__":
    main()

