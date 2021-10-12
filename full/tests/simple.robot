

*** Settings ***
# Import Selenium but remove run_on_failure (Screenshots are useless in headless)
Library           SeleniumLibrary    10    10    run_on_failure=Nothing

# Global libraries
Library           BuiltIn

# Our little library (set the option  headless tp true)
Library           ChromeHeadlessS1.py     headless=True

Suite Teardown    Close Browser

*** Variables ***
${DOWNLOAD_DIR}    ${CURDIR}/downloads


*** Keywords ***
# This is our magic keyword to set up chrome using our library
Open Chrome
    [Arguments]     ${url}

    # Call our library to setup the options
    ${options} =    get chrome options      download_dir=${DOWNLOAD_DIR}
    
    # Call the Selenium Open browser but add our custom config
    Open Browser    ${url}    browser=chrome    desired_capabilities=${options}

    # Setting the window size is important for the test to run correctly
    Set Window Size     1920    1080

*** Test Cases ***
# Our modest test case
Visit Delia
    Open Chrome  https://www.delia.tech/

