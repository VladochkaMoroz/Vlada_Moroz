Feature: Test om OrangeHRM

  Scenario: Time shifting normal-flow
    Given initialized driver
    When successful login
     And go to work shifts page
     And add new record
     And set work hours
     And save record
    Then new work shift appeared
     And remove added record
     And check if record is removed
     And close page