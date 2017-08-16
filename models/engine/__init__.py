#!/usr/bin/python3
from models import base_model, amenity, city, place, review, state, user

PARAM = {}
CNC = {
    'BaseModel': base_model.BaseModel,
    'Amenity': amenity.Amenity,
    'City': city.City,
    'Place': place.Place,
    'Review': review.Review,
    'State': state.State,
    'User': user.User
}
