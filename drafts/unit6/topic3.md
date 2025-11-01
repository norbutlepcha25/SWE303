6.3 Quality Assurance and Control
The application of planned, systematic quality activities to ensure quality requirements are met and verified.

6.3.1 Quality Assurance Activities and Tools
6.3.1.1 Process Audits and Peer Reviews
Process Audits: Independent examination to verify process compliance

Internal Audits: Conducted by organization's own staff

External Audits: Conducted by customers or certification bodies

Follow-up: Corrective actions for identified non-conformities

Peer Reviews: Systematic examination of work products by peers

Effectiveness: Most efficient method for early defect detection

Types: Code reviews, design reviews, requirement reviews, test case reviews

6.3.1.2 Static Code Analysis Tools
Purpose: Automated analysis of source code without execution

Types of Analysis:

Code Quality: Complexity, adherence to standards, best practices

Security Vulnerabilities: SQL injection, buffer overflows, authentication issues

Performance Issues: Inefficient algorithms, resource leaks

Maintainability: Duplicate code, high complexity, poor structure

Tools: SonarQube, Checkmarx, Fortify, ESLint, PMD, FindBugs

6.3.1.3 Continuous Integration and Continuous Delivery (CI/CD)
Continuous Integration: Frequent code integration with automated builds and tests

Benefits: Early defect detection, reduced integration problems

Tools: Jenkins, GitLab CI, GitHub Actions, Azure DevOps

Continuous Delivery: Automated deployment to various environments

Benefits: Faster feedback, reduced deployment risk

Quality Gates: Automated checks before promotion to next environment

Infrastructure as Code: Automated environment provisioning for consistent testing

6.3.2 Testing Strategies and Methodologies
6.3.2.1 Unit, Integration, and System Testing
Unit Testing: Testing individual components or modules

Scope: Single function, class, or module

Techniques: White-box testing, boundary value analysis, equivalence partitioning

Tools: JUnit, NUnit, Jest, PHPUnit

Integration Testing: Testing interactions between components

Approaches: Big-bang, top-down, bottom-up, sandwich

Focus: Interfaces, data flow, API interactions

Tools: Postman, SoapUI, RestAssured

System Testing: Testing complete, integrated system

Scope: End-to-end functionality, system characteristics

Types: Functional, performance, security, usability, compatibility testing

6.3.2.2 User Acceptance Testing (UAT)
Purpose: Validate that system meets business requirements and is ready for use

Participants: End users, business stakeholders, product owners

Environment: Production-like environment with realistic data

Criteria: Business requirements fulfillment, usability, workflow support

Outcome: Formal sign-off for production deployment

6.3.2.3 Performance Acceptance Metrics
Response Time Requirements:

Critical Operations: Sub-second response (e.g., login, search)

Standard Operations: 2-5 second response (e.g., data entry, reports)

Background Processes: Defined SLAs for completion time

Throughput Requirements:

Concurrent Users: Maximum number of simultaneous users

Transaction Volume: Peak transactions per second/minute/hour

Data Processing: Volume of data processed in time periods

Resource Utilization Limits:

CPU Utilization: Typically <70-80% under peak load

Memory Usage: Within allocated limits, no memory leaks

Network/Disk I/O: Within infrastructure capacity

Scalability Metrics:

Load Testing: Performance under expected peak loads

Stress Testing: Behavior beyond normal operational capacity

Endurance Testing: Performance over extended periods
