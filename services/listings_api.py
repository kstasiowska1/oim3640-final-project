import os
import requests
from dotenv import load_dotenv

load_dotenv()

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")
RAPIDAPI_HOST = os.getenv("RAPIDAPI_HOST")

# This stores the latest search results so get_property_by_id can find them
cached_properties = []

def extract_image_url(property_data):
    """
    Try many possible image formats from the API.
    """
    possible_keys = [
        "primaryPhoto",
        "primary_photo",
        "thumbnail",
        "photo",
        "imgSrc",
        "image",
        "image_url"
    ]

    for key in possible_keys:
        value = property_data.get(key)

        if isinstance(value, str) and value.startswith("http"):
            return value

        if isinstance(value, dict):
            for subkey in ["href", "url", "src"]:
                subvalue = value.get(subkey)
                if isinstance(subvalue, str) and subvalue.startswith("http"):
                    return subvalue

    photos = property_data.get("photos")
    if isinstance(photos, list) and photos:
        first_photo = photos[0]

        if isinstance(first_photo, str) and first_photo.startswith("http"):
            return first_photo

        if isinstance(first_photo, dict):
            for subkey in ["href", "url", "src"]:
                subvalue = first_photo.get(subkey)
                if isinstance(subvalue, str) and subvalue.startswith("http"):
                    return subvalue

    return "https://via.placeholder.com/300x200?text=No+Image"

def extract_sqft(property_data):
    """
    Extract square footage from the API response.
    The API usually stores it as 'area' or 'livingArea'.
    """
    value = property_data.get("area")

    if value:
        return value

    value = property_data.get("livingArea")

    if value:
        return value

    hdp_data = property_data.get("hdpData", {})
    home_info = hdp_data.get("homeInfo", {})

    value = home_info.get("livingArea")

    if value:
        return value

    return None


def extract_price(property_data):
    value = property_data.get("price", 0)

    if isinstance(value, (int, float)):
        return value

    if isinstance(value, str):
        cleaned = value.replace("$", "").replace(",", "").strip()
        try:
            return float(cleaned)
        except ValueError:
            return 0

    return 0

    return "https://via.placeholder.com/300x200?text=No+Image"

def search_properties(location):
    """
    Search for properties using the RapidAPI real estate endpoint.
    Returns a clean list of property dictionaries for the app.
    """
    global cached_properties

    url = f"https://{RAPIDAPI_HOST}/search"

    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": RAPIDAPI_HOST
    }

    params = {
        "location": location
    }

    try:
        response = requests.get(url, headers=headers, params=params, timeout=15)
        response.raise_for_status()
        data = response.json()

        print("API RESPONSE:")
        print(data)

        raw_properties = data.get("data", [])

        cleaned_properties = []

        for i, property_data in enumerate(raw_properties, start=1):
                print("RAW PROPERTY:")
                print(property_data)
                break
            
        cleaned_property = {
            "id": i,
            "address": property_data.get("address", "No address available"),
            "price": extract_price(property_data),
            "beds": property_data.get("beds") or property_data.get("bedrooms") or 0,
            "baths": property_data.get("baths") or property_data.get("bathrooms") or 0,
            "sqft": extract_sqft(property_data),
            "image": extract_image_url(property_data)
        }
        cleaned_properties.append(cleaned_property)

        cached_properties = cleaned_properties
        return cleaned_properties

    except Exception as e:
        print(f"Error calling API: {e}")
        return []


def get_property_by_id(property_id):
    """
    Return one property from the latest cached search results.
    """
    for property_data in cached_properties:
        if property_data["id"] == property_id:
            return property_data
    return None