from unittest import TestCase
from user import User
from assertpy import assert_that


class TestUser(TestCase):
    def setUp(self) -> None:
        self.temp = User()

    def test_get_data_not_None(self):
        assert_that(self.temp.get_data()).is_not_none()

    def test_get_data_is_iterable(self):
        assert_that(self.temp.get_data()).is_iterable()

    def test_get_data_is_instance_of(self):
        assert_that(self.temp.get_data()).is_instance_of(dict)

    def test_get_data_length(self):
        assert_that(self.temp.get_data()).is_length(2)

    def test_get_data_keys(self):
        assert_that(self.temp.get_data()).contains_key("results", "info")

    def test_get_data_results_keys(self):
        assert_that(self.temp.get_data().get("results", {})[0]).contains_key("email", "name", "location")

    def test_get_email(self):
        assert_that(self.temp.get_email()).is_instance_of(str)

    def test_get_fullname(self):
        assert_that(self.temp.get_full_name().split(" ")).is_length(3)

    def test_is_living_on_northern_hemisphere(self):
        assert_that(self.temp.is_living_on_northern_hemisphere()).is_instance_of(bool)

    def tearDown(self) -> None:
        self.temp = None
