*** Settings ***
Library    robot-kafka-library.py   
 
*** Test Cases ***
Demo how to call python consumer function
    ${MSG} =     Consumer  10.138.38.65:9092   foobar
    log    ${MSG}
    Log to console   ${MSG}