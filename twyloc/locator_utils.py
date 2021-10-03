
import re
import spacy

from geopy.geocoders import Nominatim
'''
    More info: https://geopy.readthedocs.io/en/stable/#geopy.location.Location.address
'''


class TweetUserLocatorUtils():
    def __init__(self, locator_user_agent='random_user') -> None:
        self.locator = Nominatim(user_agent=locator_user_agent)
        self.nlp = spacy.load('en')

    def get_location_from_text(self, text):
        '''
        Args:
            text - Noisy location/description text - str      
        Return:
            (country_code, address) - Tuple(str, str) 
        '''

        # 1. Remove numbers and set to lowercase
        # 2. Spacy to find GPE entity -- place # performs better than nltk
        # 3. Use geocoder to find the lat, long
        # 3. Use lat, long to find country_code and address
        location_desc = re.sub(r'\d+', '', text).lower()
        location_desc = self.nlp(location_desc)
        for ent in location_desc.ents:
            if ent.label_ == "GPE":
                try:
                    loc = self.locator.geocode(ent.text)
                    '''
                     Sample response: 
                    '''
                    if loc:
                        # For consistency in country naming, calling the API to get the country and country code
                        # Eg: Germany can also be named Deutschland
                        return self.get_location_from_coordinates(loc.raw['lon'], loc.raw['lat'])
                except Exception as e:
                    print("Error locating: ", e)
        return None

    def get_location_from_coordinates(self, lng, lat):
        '''
        Args:
            longitude - float
            latitude - float

        Return:
            (country_code, address) - Tuple(str, str) 
        '''
        try:
            coordinates = str(lat) + "," + str(lng)
            location = self.locator.reverse(coordinates)
            '''
            Sample response: 
            '''
            country_code = location.raw['address']['country_code'].upper()
            return (country_code, location.address)
        except Exception as e:
            print("Error locating: ", e)
        return None
