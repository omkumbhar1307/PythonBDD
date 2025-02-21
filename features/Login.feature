@Regression
Feature: Verify Login Page of OpenMRS

  @Sanity
  Scenario: Login with invalid credentials
    Given User is on Login page of OpenMRS
    When User enters invalid user name
    Then User will see invalid username password error message