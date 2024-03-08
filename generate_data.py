from dataclasses import dataclass
from typing import List
from datetime import datetime


import faker

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

    for i in range(500):
        restaurant = RestaurantReview(
            id=i,
            restaurant_name=fake.company(),  # Assuming restaurant names are like company names
            reviewer_name=fake.name(),
            reviewer_text=fake.text(max_nb_chars=200),  # Generate fake review texts up to 200 characters
            rating=fake.random_element(elements=(1, 2, 3, 4, 5)),  # Assuming ratings are integers from 1 to 5
            date_of_visit=fake.date_between(start_date=start_date, end_date=end_date),
            location=fake.city()
        )
        restaurants.append(restaurant)

    return restaurants

    # # For the 1% of random students, set the average mark to None
    # for student in fake.random_elements(elements=students, length=int(len(students) * 0.01)):
    #     student.average_mark = None
    #
    # return students
def save_restaurants_to_csv(restaurants: List[RestaurantReview]):
    with open('students.csv', 'w') as f:
        f.write('id,first_name,last_name,birth_date,average_mark,count_of_lessons_absent,count_of_lessons_sick,gender,city\n')

        for student in students:
            f.write(f'{student.id},{student.first_name},{student.last_name},{student.birth_date},{student.average_mark},{student.count_of_lessons_absent},{student.count_of_lessons_sick},{student.gender},{student.city}\n')


def save_restaurants_to_csv(restaurants: List[RestaurantReview]):
    with open('restaurants_reviews.csv', 'w', newline='', encoding='utf-8') as f:
        f.write('id,restaurant_name,reviewer_name,reviewer_text,rating,date_of_visit,location\n')

        # Write the restaurant review data
        for restaurant in restaurants:
            f.write(f'{restaurant.id},{restaurant.restaurant_name},{restaurant.reviewer_name},"{restaurant.reviewer_text}",{restaurant.rating},{restaurant.date_of_visit},{restaurant.location}\n')

if __name__ == '__main__':
    restaurants = generate_restaurant_reviews()
    save_restaurants_to_csv(restaurants)