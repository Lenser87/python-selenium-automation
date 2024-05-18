# Created by Lenser at 5/17/2024
Feature: Verifying test for password

  Scenario: Verifying the “We can't find your account.” message is shown if we use incorrect credentials
    Given Open Target main page
    When Clicking on Sign in
    When Input incorrect email and password
    When Click login button
    Then Verify the “We can't find your account.” message is shown