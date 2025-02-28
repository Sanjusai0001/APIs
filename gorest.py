import pytest
import requests
import json
import string
import random


base_url = "https://gorest.co.in"

auth_token = "Bearer e4b8e1f593dc4a731a153c5ec8cc9b8bbb583ae964ce650a741113091b4e2ac6"

def random_email_generator():
    domain = "gmail.com"
    email_length = 10
    random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(email_length))
    email = random_string + "@" + domain
    return email

# GET

def get_request():
    url = base_url + "/public/v2/users/"
    header = { "Authorization" : auth_token }
    response = requests.get(url, headers=header)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json response body: \n", json_str)
    print(".........GET USER IS DONE........\n" )


# POST
def post_request():
    url = base_url + "/public/v2/users"
    print("post url: " + url)
    header = { "Authorization" : auth_token}
    data = {
    "name": "sanjusai",
    "email": random_email_generator(),
    "gender": "male",
    "status": "inactive"
    }
    response = requests.post(url, json = data, headers=header)
    assert response.status_code == 201
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json respone body : ", json_str)
    user_id = json_data["id"]
    print("user_id ==> ", user_id)
    assert "name" in json_data
    assert json_data["name"] == "sanjusai"
    print(".........POST/CREATE USER IS DONE........\n" )
    return user_id


# PUT
def put_request(user_id):
    url = base_url + f"/public/v2/users/{user_id}"
    print("put url: " + url)
    header = { "Authorization" : auth_token}
    data = {
    "name": "sanjusai pro",
    "email": random_email_generator(),
    "gender": "male",
    "status": "inactive"
    }
    response = requests.put(url, json=data, headers=header)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json response body: ", json_str)
    assert json_data["id"] == user_id
    assert json_data["name"] == "sanjusai pro"
    print(".........PUT USER IS DONE........\n" )



# DELETE

def delete_request(user_id):
    url = base_url + f"/public/v2/users/{user_id}"
    print("delete url: " + url)
    header = { "Authorization" : auth_token}
    response = requests.delete(url, headers=header)
    assert response.status_code == 204
    print(".........DELETE USER IS DONE........" )
    print("=" * 40)

# calling methods
get_request()
user_id = post_request()
put_request(user_id)
delete_request(user_id)


# user_id = test_get_request()
# test_post_request(user_id)
# test_put_request(user_id)
# test_delete_request(user_id)