Feature: Polls
    In order to vote for polls
    As a visitor
    I want to browse all polls' questions

    Scenario: Browse polls' questions
        Given some questions are in the database
        When I visit the home page
        Then I should see a list of polls questions