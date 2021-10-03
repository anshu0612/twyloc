
from twyloc.locator_utils import TweetUserLocatorUtils
from twyloc.constants import ALPHA2_TO_COUNTRY, COUNTRY_APLHA_2_TO_3


def get_user_location(tweet, app_agent_name):
    '''
    Args:
        tweet: Object from twitter API - Tweet
        api_agent_name: Specify your app name required by Geocoder library - str
    Return:
        {
            'country': country - str,
            'country_code': {
                'alpha2': aplha2 code of the country - str,
                'alpha3': aplha3 code of the country - str,
            },
            'locator_type': 'Coordinates' | 'Place' | 'Location' | 'Description' - str,
            'address': location address - str
        }
    '''

    tw = TweetUserLocatorUtils(app_agent_name)
    locator_type = None
    location_info = None
    u = tweet['user']

    try:
        if tweet['coordinates']:  # gps coordinates
            location_info = tw.get_location_from_coordinates(tweet['coordinates']['coordinates'][0],
                                                             tweet['coordinates']['coordinates'][1])
            locator_type = 'Coordinates'
        elif 'place' in tweet and tweet['place']:  # user specified place
            p = tweet['place']
            location_info = p['country_code'], p['full_name']
            locator_type = 'Place'
        elif 'location' in u and u['location']:
            # Nullable. User-defined location for the account's profile.
            # Example: "Delhi, India"
            location_info = tw.get_location_from_text(u['location'])
            locator_type = 'Location'

        if not location_info and 'description' in u and u['description']:
            # Nullable. A user's description of the account
            # Example: "Given I am at pasir panjang, I gotta be at peace"
            location_info = tw.get_location_from_text(u['description'])
            locator_type = 'Description'

    except Exception as e:
        print(Exception)

    geo_data = {
        "error": "Sorry could not locate the user."
    }

    if location_info:
        geo_data = {
            'country': ALPHA2_TO_COUNTRY[location_info[0]],
            'country_code': {
                'alpha2': location_info[0],
                'alpha3': COUNTRY_APLHA_2_TO_3[location_info[0]],
            },
            'locator_type': locator_type,
            'address': location_info[1]
        }

    return geo_data
