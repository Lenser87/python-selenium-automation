# Created by Lenser at 4/7/2024
Feature: Verifying test


  Scenario: Verifying the "Your cart is empty” message is shown
    Given Open Target main page
    When Clicking on Cart icon
    Then Verifying actual text is shown