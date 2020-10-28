*** Settings ***
Library    RobotKafkaLibrary.Producer
Library    RobotKafkaLibrary.Consumer
 
*** Test Cases ***
Test producer topic test publish message1
    ${MSG} =     Publish  10.138.38.65:9092   topicTest   message1
    log    ${MSG}
    Log to console   ${MSG}

Test consumer topic test subscribe message1
    ${MSG} =     Subscribe  10.138.38.65:9092   topicTest
    log    ${MSG}
    Log to console   ${MSG}
