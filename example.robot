*** Settings ***
Library    RobotKafkaLibrary.py   
 
*** Test Cases ***
Test producer topic test publish message1
    ${MSG} =     Producer  10.138.38.65:9092   topicTest   message1
    log    ${MSG}
    Log to console   ${MSG}

Test consumer topic test publish message1
    ${MSG} =     Consumer  10.138.38.65:9092   topicTest
    log    ${MSG}
    Log to console   ${MSG}