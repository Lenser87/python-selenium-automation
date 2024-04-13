# Created by Lenser at 4/13/2024
Feature: add tests

  Scenario: User can add a coffee
    Given Open Target main page
    When Search for coffee
    When Add coffee
    Then Verify coffee in the cart