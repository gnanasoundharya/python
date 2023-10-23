*** Settings ***
Library    SeleniumLibrary

*** Keywords ***
logintest
    Input Text    xpath://input[@name='username']   Admin
    ${username}    Set Variable    xpath://input[@name='username']    
    
    Element Should Be Visible    ${username}
    Element Should Be Enabled    ${username}
    Sleep    3
    Clear Element Text    ${username}

    Input Text    xpath://input[@name='password']      admin123
    Click Button   //button[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']    
