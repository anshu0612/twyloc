# twyloc 📍
Twyloc is useful to locate a tweet's user.


--------------------------------------------------------------------------------

## Sample responses from twyloc
```bash
    # using coordinates
    {   
        'country': 'Singapore',
        'country_code': {
            'alpha2': 'SG',
            'alpha3': 'SGP'
            }, 
        'locator_type': 'Location',
        'address': 'Drongo Trail, Bishan, Singapore, Central, 578774 Singapore'
    }
    
    # using user-defined location 
    {
        'country': 'Nigeria', 
        'country_code': {
            'alpha2': 'NG',
            'alpha3': 'NGA'
        },
        'locator_type': 'Coordinates',
        'address': 'Mun-Munsal, Bauchi, Nigeria'
    }

    # failure 
    {
        'error': 'Sorry could not locate the user.'
    }

```

## How does it locate a user? 

It searches out for any of the following information in a tweet object:
<!-- toc -->
- Coordinate:  Nullable else twyloc uses latitude, longitude information to fetch the location details
- Place: Nullable else provides a user's location
- User-defined location: (1) NLP to process any place entity in the text (2) [Geocoder library](https://geocoder.readthedocs.io/) to fetch the location 
- User-defined description: (1) NLP to process any place entity in the text (2) Geocoder library to fetch the location 
<!-- tocstop -->

## Sample Usage
```bash
from twyloc.locator import get_user_location
get_user_location(tweet, app_agent_name)
```

**Arguments**

| Argument | Description 
| ---- | --- | 
| tweet | [Tweet object](https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/object-model/tweet) |
| app_agent_name | Give a random name -- required by the geopy library |


## Todos
1. Duh!! The document can be made a lot better 
2. Add some twyloc stats on performance

## Contributions
If you find any bug or have anything to contribute, feel free to create a pull request or report an issue.  

## License
MIT license, as found in the [LICENSE](LICENSE) file.
