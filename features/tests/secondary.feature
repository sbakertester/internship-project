
Feature: Tests for Secondary page


  Scenario: User can filter the Secondary deals by the “want to buy” option
    Given Open Reelly main page
    # Replace the email and password with your valid sign in credentials
    Given User is signed into page with email "sbakertester@outlook.com" and password "tester123"
    When Click on the Secondary tab on side menu
    Then Verify the right page opens
    When Clicks on Filters
    And Selects the Want to buy option
    And Clicks on Apply Filter button
    Then Verify all cards have the Want to buy tag