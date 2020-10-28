# robot-kafka-library
### robot framework extension test kafka message queue system

https://pypi.org/project/robot-kafka-library/

## How to Use
> pip install robot-kafka-library

Import into project file : example.robot

```
Library    RobotKafkaLibrary.Producer
Library    RobotKafkaLibrary.Consumer
 
*** Test Cases ***
Test producer topic test publish message1
    ${RESULT} =     Publish  {broker-ip}:{port}   {topic}   {message}
    log    ${RESULT}
    Log to console   ${RESULT}

Test consumer topic test publish message1
    ${MSG} =     Subscribe  {broker-ip}:{port}   {topic}   {option-timeout}
    log    ${MSG}
    Log to console   ${MSG}
    ```
