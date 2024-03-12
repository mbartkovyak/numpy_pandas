from dataclasses import dataclass
from typing import List
from datetime import datetime


import faker, random

# Use the faker library to generate a dataset for "Restaurant Reviews." Each entry in the dataset should include the following fields:
#
# Restaurant Name
# Reviewer Name
# Review Text
# Rating (1 to 5)
# Date of Visit (within the last two years)
# Location (City)


# Set polish locale
fake = faker.Faker('pl_PL')

@dataclass
class RestaurantReview:
    id: int
    restaurant_name: str
    reviewer_name: str
    reviewer_text: str
    rating: float
    date_of_visit: datetime
    location: str

def generate_restaurant_reviews() -> List[RestaurantReview]:
    restaurants = []
    start_date = datetime.strptime("2020-01-01", "%Y-%m-%d").date()
    end_date = datetime.strptime("2023-12-31", "%Y-%m-%d").date()

    # Decide on the number of unique names, locations, etc.
    unique_restaurant_names = 100  # For example, 100 unique restaurant names
    unique_reviewer_names = 30  # For example, 300 unique reviewer names
    unique_locations = 50  # For example, 50 unique locations

    # Generate unique names and locations
    restaurant_names = [fake.company() for _ in range(unique_restaurant_names)]
    reviewer_names = [fake.name() for _ in range(unique_reviewer_names)]
    locations = [fake.city() for _ in range(unique_locations)]

    restaurants = []
    for i in range(500):
        restaurant = RestaurantReview(
            id=i,
            restaurant_name=random.choice(restaurant_names),  # Randomly reuse restaurant names
            reviewer_name=random.choice(reviewer_names),  # Randomly reuse reviewer names
            reviewer_text=fake.text(max_nb_chars=200),  # Generate fake review texts up to 200 characters
            rating=fake.random_element(elements=(1, 2, 3, 4, 5)),  # Assuming ratings are integers from 1 to 5
            date_of_visit=fake.date_between(start_date=start_date, end_date=end_date),
            location=random.choice(locations)  # Randomly reuse locations
        )
        restaurants.append(restaurant)

    for restaurant in fake.random_elements(elements=restaurants, length=int(len(restaurants) * 0.01), unique=True):
        restaurant.rating = None

    return restaurants

def save_restaurants_to_csv(restaurants: List[RestaurantReview]):
    with open('restaurants_reviews.csv', 'w', newline='', encoding='utf-8') as f:
        f.write('id,restaurant_name,reviewer_name,reviewer_text,rating,date_of_visit,location\n')

        # Write the restaurant review data
        for restaurant in restaurants:
            f.write(f'{restaurant.id},{restaurant.restaurant_name},{restaurant.reviewer_name},"{restaurant.reviewer_text}",{restaurant.rating},{restaurant.date_of_visit},{restaurant.location}\n')

if __name__ == '__main__':
    restaurants = generate_restaurant_reviews()
    save_restaurants_to_csv(restaurants)

