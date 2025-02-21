import time

from selenium import webdriver
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from fuzzywuzzy import fuzz

from utils.excelreader import ExcelReader

TESTDATA_FILE_PATH = "ChatbotTestData1.xlsx"
driver= webdriver.Chrome()

@given("User is on Login page of OpenMRS")
def test_given_step(self):

    excel = ExcelReader(TESTDATA_FILE_PATH, "TestData")
    print("Cell A2:", excel.get_cell_value(2, 1))  # Fetch A2 value
    print("Cell B2:", excel.get_cell_value(2, 2))  # Fetch B2 value
    prompt1 = excel.get_cell_value(2, 1)

    driver.get("https://julius.ai/ai-chatbot")
    time.sleep(3)
    driver.find_element(By.XPATH, "//textarea[@placeholder = 'Send a message...']").send_keys(prompt1)
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[@type = 'submit']").click()
    time.sleep(10)

    # Wait until the main element is present
    response_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "// p[text() = 'Describe the concept of quantum entanglement.']//following :: div[@class='flex flex-col flex-1 w-full']"))
    )

   # actualResponse = driver.find_element(By.XPATH, "// p[normalize - space() = 'Describe the concept of quantum entanglement.']// following[1]").text
    actualResponse = response_element.text

    normalizedactualResponse = normalize_text(actualResponse)

    time.sleep(3)

    print("WE GOT THE RESPONSE =======>"+normalizedactualResponse)
    expectedResponse = excel.get_cell_value(2, 2)
    normalizedexpectedResponse = normalize_text(expectedResponse)

    similarity_score = fuzz.ratio(normalizedactualResponse, normalizedexpectedResponse)

    print("=======================================")

    print("The Similarity Score is ",similarity_score)

    print("=======================================")

    assert similarity_score > 30, f"Unexpected response: {normalizedactualResponse}"

    print("✅ Test Passed: Responses match well!")

    print("Given Step Completed")

    time.sleep(3)


@when("User enters invalid user name")
def test_when_step(self):

    print("When Step Completed")


@then("User will see invalid username password error message")
def test_then_step(self):
    print("Then Step Completed")


def normalize_text(text):
    """Remove extra spaces, convert to lowercase, and strip whitespace."""
    return " ".join(text.lower().strip().split())

