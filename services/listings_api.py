sample_properties = [
    {
        "id": 1,
        "address": "123 Main St, Boston, MA",
        "price": 350000,
        "beds": 3,
        "baths": 2,
        "sqft": 1450,
        "image": "https://via.placeholder.com/300x200?text=House+1"
    },
    {
        "id": 2,
        "address": "45 Oak Ave, Cambridge, MA",
        "price": 425000,
        "beds": 4,
        "baths": 3,
        "sqft": 1800,
        "image": "https://via.placeholder.com/300x200?text=House+2"
    },
    {
        "id": 3,
        "address": "78 River Rd, Somerville, MA",
        "price": 299000,
        "beds": 2,
        "baths": 1,
        "sqft": 1200,
        "image": "https://via.placeholder.com/300x200?text=House+3"
    }
]


def search_properties(location):
    """
    Return sample properties for now.
    Later this function will call the real API.
    """
    return sample_properties


def get_property_by_id(property_id):
    """
    Find one property by its id.
    """
    for property_data in sample_properties:
        if property_data["id"] == property_id:
            return property_data
    return None