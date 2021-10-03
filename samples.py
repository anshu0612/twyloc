from twyloc.locator import get_user_location

if __name__ == "__main__":
    dummy_tweet_obj_with_cor = {
        'coordinates': {
            'coordinates': [10, 10]
        },
        'place': None,
        'user': {
            'location': 'I am in Singapore',
            'description': 'I am in California',
        }
    }

    print('Sample 1: {}'.format(get_user_location(
        dummy_tweet_obj_with_cor, 'twyloc')))

    dummy_tweet_obj_with_place = {
        'coordinates': None,
        'place': {
            'country_code': 'SG',
            'full_name': 'Pasir panjang',
        },
        'user': {
            'location': 'I am in Singapore',
            'description': 'I am in California',
        }
    }

    print('Sample 2: {}'.format(get_user_location(
        dummy_tweet_obj_with_place, 'twyloc')))

    dummy_tweet_obj_with_user_location = {
        'coordinates': None,
        'place': None,
        'user': {
            'location': 'I am in Singapore',
            'description': 'I am in California',
        }
    }

    print('Sample 3: {}'.format(get_user_location(
        dummy_tweet_obj_with_user_location, 'twyloc')))

    dummy_tweet_obj_with_user_description = {
        'coordinates': None,
        'place': None,
        'user': {
            'location': 'I am in',
            'description': 'I am in California',
        }
    }

    print('Sample 4: {}'.format(get_user_location(
        dummy_tweet_obj_with_user_description, 'twyloc')))

    dummy_tweet_obj_with_no_geo_found = {
        'coordinates': None,
        'place': None,
        'user': {
            'location': 'Heart of the nation',
            'description': 'I am in <3',
        }
    }

    print('Sample 5: {}'.format(get_user_location(
        dummy_tweet_obj_with_no_geo_found, 'twyloc')))
