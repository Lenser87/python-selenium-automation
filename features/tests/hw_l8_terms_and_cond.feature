# Created by Lenser at 5/3/2024
Feature: Verifying test

  Scenario: User can open and close Terms and Conditions from sign in page
    Given Open Target main page
    When Clicking on Sign in
    When Store original window
    When Click on Target terms and conditions link
    When Switch to the newly opened window
    Then Verify Terms and Conditions page is opened
    Then User can close new window
    Then Switch back to original page
