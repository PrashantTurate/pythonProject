import pytest
import allure


@allure.title("TC#1-Verify Addition")
@allure.description("This is a smoke test case which verify 1 + 1 equal to 2")
@pytest.mark.smoke
def test_verify_sum():
    assert 1 + 1 == 2


@allure.title("TC#2-Verify Subtraction")
@allure.description("This is a smoke test case which verify 2 - 1 equal to 1")
@pytest.mark.smoke
def test_verify_sub():
    assert 2 - 1 == 2


@allure.title("TC#3-Verify Divison")
@allure.description("This is a smoke test case which verify 16 / 4 equal to 4")
@pytest.mark.smoke
def test_verify_div():
    assert 16 / 4 == 4

@allure.title("TC#4-Verify Multiplication")
@allure.description("This is a regression test case which verify 2 * 2 equal to 4")
@pytest.mark.reg
def test_verify_mul():
    assert 2 * 2 == 4

