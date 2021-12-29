import requests
import functools


class User:
    def __init__(self):
        self.data = None

    def get_data(self):
        data = requests.get("https://randomuser.me/api/").json()
        self.data = data
        return data

    def get_email(self):
        return self.get_data().get("results", {})[0].get("email")

    def get_full_name(self):
        user_info = self.get_data().get("results")[0].get("name")
        return functools.reduce(lambda a, b: a + " " + b, user_info.values())

    def is_living_on_northern_hemisphere(self):
        latitude = self.get_data().get("results")[0].get("location")\
            .get("coordinates").get("latitude")
        return float(latitude) > 0


smsm = User()
print(smsm.get_email())
print(smsm.get_full_name())
print(smsm.is_living_on_northern_hemisphere())
