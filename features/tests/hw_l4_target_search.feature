# Created by Lenser at 4/12/2024
Feature: Search tests

  Scenario: User can search for a coffee
    Given Open Target main page
    When Search for coffee
    Then Verify search result are shown for coffee
    Then Verify that URL has coffee


  Scenario Outline: User can search for a product
    Given Open Target main page
    When Search for <item>
    Then Verify search result are shown for <expected_item>
    Examples:
    |item      |expected_item|
    |coffee    |coffee       |
    |tea       |tea          |
    |car       |car          |

