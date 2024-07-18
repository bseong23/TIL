import requests
from pprint import pprint 

black_list = [
    'Hoeger LLC',
    'Keebler LLC',
    'Yost and Sons',
    'Johns Group',
    'Romaguera-Crona',
]

def censorship(company, name):
    for i in range(len(black_list)):
        if company == black_list[i]:
            print(f'{company} 소속의 {name} 은/는 등록할 수 없습니다.')
            return False

    print('이상 없습니다.')
    return True

def create_user(user_list):
    censored_user_list = {}
    for i in range(len(user_list)):
        user_name = user_list[i]['name']
        user_company = user_list[i]['company']
        if censorship(user_company, user_name) == True:
            censored_user_list[user_company] = [f'{user_name}']
    return censored_user_list


dummy_data = []

for i in range(1, 11):
    API_URL = f'https://jsonplaceholder.typicode.com/users/{i}'
    response = requests.get(API_URL)
    parsed_data = response.json()
    info = {}
    if -80 < float(parsed_data['address']['geo']['lat']) < 80 and -80 < float(parsed_data['address']['geo']['lng']) < 80:
        info['company'] = parsed_data['company']['name']
        info['lat'] = parsed_data['address']['geo']['lat']
        info['lng'] = parsed_data['address']['geo']['lng']
        info['name'] = parsed_data['name']
        dummy_data.append(info)



print(create_user(dummy_data))
