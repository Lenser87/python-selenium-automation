# Created by Lenser at 5/13/2024
Feature: Tests for Help pages

  Scenario: User can select Help topic Partner Programs
    Given Open Help page for Returns
    Then Verify Returns page has opened
    When Select Help topic Partner Programs
    Then Verify Ulta Beauty at Target page has opened


  Scenario: User can select Help topic Delivery & Pickup
    Given Open Help page for Returns
    Then Verify Returns page has opened
    When Select Help topic Delivery & Pickup
    Then Verify Drive Up & Order Pickup page has opened