import pyairbnb
import json
from dotenv import load_dotenv
import os

load_dotenv()
HOTEL_ID = os.getenv("HOTEL_ID")

def scrape_reviews(hotel_id, filepath):
    # Define listing URL and proxy URL
    room_url = f"https://www.airbnb.com/rooms/{hotel_id}"# Listing URL
    proxy_url = ""  # Proxy URL (if needed)
    language = "fr"
    # Retrieve reviews for the specified listing
    reviews_data = pyairbnb.get_reviews(room_url, language, proxy_url)

    # Save the reviews data to a JSON file
    with open(filepath, 'w', encoding='utf-8') as f:
        try:
            reviews_json = json.dumps(reviews_data)
            f.write(reviews_json)  # Extract reviews and save them to a file
            print(f"Saved reviews to {filepath}!")
            return reviews_json
        except Exception as e:
            print("Error in saving reviews!.")
        

reviews = scrape_reviews(HOTEL_ID, "./inputs/hotel_reviews.json")
print(type(reviews))
