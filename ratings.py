"""Restaurant rating lister."""


# put your code here

def restaurant_ratings(text):

    file = open(text)

    ratings = {}

    for line in file:
        line = line.rstrip()
        restaurants = line.split(":")

        for restaurant in restaurants:
            ratings[restaurants[0]] = restaurants[1]

    for restaurant in sorted(ratings):
        print(f"{restaurant} is rated at {ratings[restaurant]}")



restaurant_ratings("scores.txt")