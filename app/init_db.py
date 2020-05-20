import requests

from pymongo import MongoClient, errors


def get_users():
    count_users_to_fetch = 100
    url = 'https://randomuser.me/api/?gender=male&results=' + str(count_users_to_fetch)

    try:
        response = requests.get(url)
    except requests.exceptions.RequestException:
        print('Oops... Something wrong happened on the server https://randomuser.me/')
    else:
        if response.status_code != 200:
            raise Exception(f'Response status code is not 200. It is {response.status_code}')

        data = response.json()

        return data['results']


def insert_data_to_db(data):
    try:
        db = MongoClient('mongodb://mongodb:27017')['test_db']

        user_collection = db['users']

        user_collection.drop()

        user_collection.insert_many(data)
    except errors.PyMongoError as e:
        raise Exception('Something wrong happened during inserting users into database')


if __name__ == '__main__':
    users = get_users()
    insert_data_to_db(users)
