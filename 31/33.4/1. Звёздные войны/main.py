import requests
import json

my_req = requests.get('https://swapi.dev/api/people/3/')
if my_req.status_code == 200:
    json_dict = json.loads(my_req.text)
    json_dict['name'] = 'New name'
    with open('change_name.json', 'w') as file:
        json.dump(json_dict, file, indent=4)

    res_homeworld = requests.get(json_dict['homeworld'])
    print(res_homeworld.text)
