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

    return rating


ratings_dict = restaurant_ratings("scores.txt")


def sorted_ratings(dict):
    for restaurant in sorted(dict):
        print(f"{restaurant} is rated at {dict[restaurant]}")

sorted_ratings(ratings_dict)


def new_recommendations(old_dicts):
    new_dicts = old_dicts

    new_restaurant = input("Please enter restaurant name: ")
    new_rating = input("Please enter restaurant score: ")

    new_dicts[new_restaurant] = new_rating

restaurant_ratings("scores.txt")