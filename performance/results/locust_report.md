Performance Testing Report (Locust)
Objective
To test the load capacity and response time of the /add endpoint.

Test Configuration
Target Endpoint: POST /add
Tool Used: Locust
Environment: Local (Windows, Flask Dev Server)
Results Summary
Total Requests: [ض 50]
Requests Per Second (RPS):3,4
Failure Rate: 1%
Median Response Time:  [16 ]
Analysis & Bottlenecks
The endpoint performed efficiently under the simulated load.
No bottlenecks were observed during the test.
The server handled concurrent requests smoothly without dropping connections.
Conclusion
The /add endpoint is optimized and capable of handling the expected user load without performance degradation.



