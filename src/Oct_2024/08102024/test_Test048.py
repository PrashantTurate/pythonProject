import pytest
import allure
import requests


@allure.title("Test#1 GET Request - Restful-booker project#1")
@allure.description("TC#1 --> Verify GET request with ID")
@allure.tag("regression", "P0", "smoke")
@allure.label("owner", "Prashant Turate")
@allure.testcase("TC#1")
@pytest.mark.smoke
def test_get_single_request_id_positive():
    url = "https://restful-booker.herokuapp.com/booking/2"
    response_Data = requests.get(url)
    print(response_Data.text)
    print("================================================================")
    print(response_Data.headers)
    print("================================================================")
    print(response_Data.json())
    assert response_Data.status_code == 200


@allure.title("Test#2 GET Request - Restful-booker project#1")
@allure.description("TC#2 --> Verify GET request with ID")
@allure.tag("regression", "P0", "smoke")
@allure.label("owner", "Prashant Turate")
@allure.testcase("TC#2")
@pytest.mark.smoke
def test_get_single_request_id_negative_1():
    url = "https://restful-booker.herokuapp.com/booking/-2"
    response_Data = requests.get(url)
    print(response_Data.text)
    assert response_Data.status_code == 404


@allure.title("Test#3 GET Request - Restful-booker project#1")
@allure.description("TC#3 --> Verify GET request with ID")
@allure.tag("regression", "P0", "smoke")
@allure.label("owner", "Prashant Turate")
@allure.testcase("TC#3")
@pytest.mark.smoke
def test_get_single_request_id_negative_2():
    url = "https://restful-booker.herokuapp.com/booking/invalid"
    response_Data = requests.get(url)
    print(response_Data.text)
    assert response_Data.status_code == 404


@allure.title("Test#4 GET Request - Restful-booker project#1")
@allure.description("TC#4 --> Verify GET request with ID")
@allure.tag("regression", "P0", "smoke")
@allure.label("owner", "Prashant Turate")
@allure.testcase("TC#4")
@pytest.mark.smoke
def test_get_single_request_id_negative_3():
    url = "https://restful-booker.herokuapp.com/booking/@#$%^"
    response_Data = requests.get(url)
    print(response_Data.text)
    assert response_Data.status_code == 404