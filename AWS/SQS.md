SQS oldest offering
Fully managed, used for decoupling applications

Attributes:
Unlimited throughput, unlimited number of messages in queue
Short-lived: 4 days, maximum of 14 days
Low latency (<10 ms)
Limit of 256KB per message sent

Can have duplicate messages
Can have out of order messages


Producers -> SQS <-> Consumer

Produced to SQS using SDK (Send message API)

Consumers - runs on EC2, servers, or Lambda