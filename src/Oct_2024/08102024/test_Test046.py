import pytest
import allure


@allure.title("Test Authentication")
@allure.description("This test attempts to log into the website using a login and a password. Fails if any error happens.")
@allure.tag("NewUI", "Essentials", "Authentication")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "John Doe")
@allure.link("https://dev.example.com/", name="Website")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")
@pytest.mark.smoke
def test_verify_sum():
    assert 1 + 1 == 2


@pytest.mark.smoke
def test_verify_sub():
    assert 2 - 1 == 2


@pytest.mark.smoke
def test_verify_div():
    assert 16 / 4 == 4


@pytest.mark.reg
def test_verify_mul():
    assert 2 * 2 == 4


@pytest.mark.skip(reason="Not completed,Skip it")
def test_verify_div1():
    assert 1 / 0 == 0
