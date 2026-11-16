*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser

*** Test Cases ***

when counter value is set to 10 it's value becomes 10
    Go To  ${HOME_URL}
    Fill Text  input[name="number"]  10
    Click  button >> text=Aseta
    Get Text  body  *=  nappia painettu 10 kertaa
