print("environment.py LOADED!")  # Debugging print

from selenium import webdriver

def before_all(context):
    print("before_all: Starting the Test Execution...")
    #context.driver = webdriver.Chrome()

def after_all(context):
    print("after_all: Test Execution Completed. Closing Browser...")
    #context.driver.quit()

def before_scenario(context, scenario):
    print(f"before_scenario: Starting Scenario: {scenario.name}")

def after_scenario(context, scenario):
    print(f"after_scenario: Completed Scenario: {scenario.name}")

def before_step(context, step):
    print(f"before_step: Running Step: {step.name}")

def after_step(context, step):
    print(f"after_step: Completed Step: {step.name}")
