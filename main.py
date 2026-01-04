from selenium import webdriver
import pytest

def run_tests():
    # Initialize the WebDriver (for example, Chrome)
    driver = webdriver.Chrome(executable_path="./drivers/chromedriver")

    # Run the tests using pytest
    exit_code = pytest.main(["-q", "--tb=short", "tests"])

    # Clean up the driver after tests
    driver.quit()

    return exit_code

if __name__ == "__main__":
    exit_code = run_tests()
    if exit_code == 0:
        print("All tests passed successfully!")
    else:
        print("Some tests failed. Please check the logs.")
