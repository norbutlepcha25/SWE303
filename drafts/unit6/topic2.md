6.2 Quality Planning
Quality planning involves identifying which quality standards are relevant to the project and determining how to satisfy them.

6.2.1 Developing the Quality Management Plan
6.2.1.1 Defining Quality Policies and Objectives
Quality Policy: Organizational commitment to quality (e.g., "Zero critical defects in production")

Quality Objectives: Specific, measurable targets derived from quality policy

Examples: "Achieve 95% test coverage," "Reduce defect density by 20%," "Maintain 99.9% availability"

SMART Criteria: Specific, Measurable, Achievable, Relevant, Time-bound objectives

Alignment: Ensure objectives support project and organizational goals

6.2.1.2 Establishing Quality Assurance Processes
Process Definition: Standard procedures for development, testing, and deployment

Quality Gates: Checkpoints where deliverables must meet specific criteria to proceed

Standards Compliance: Ensuring adherence to coding standards, documentation standards

Continuous Improvement: Mechanisms for process refinement based on metrics and feedback

6.2.1.3 Defining Quality Control Procedures
Inspection Criteria: What will be checked and how

Testing Strategy: Types of testing, coverage requirements, entry/exit criteria

Acceptance Criteria: Conditions that must be met for deliverables to be accepted

Metrics Collection: What data will be collected and how it will be used

6.2.2 Selecting Appropriate Quality Standards
6.2.2.1 ISO 9001 for Software Development
Process Standard: Focuses on quality management systems rather than product quality

Key Principles: Customer focus, leadership, engagement of people, process approach, improvement

Certification: Independent verification of quality processes

Documentation Requirements: Quality manual, procedures, records

6.2.2.2 CMMI (Capability Maturity Model Integration) Levels
Level 1 - Initial: Processes unpredictable, poorly controlled, reactive

Level 2 - Managed: Projects planned, documented, performed, measured, controlled

Level 3 - Defined: Processes characterized, understood, described in standards

Level 4 - Quantitatively Managed: Processes measured and controlled using statistical techniques

Level 5 - Optimizing: Focus on continuous process improvement

6.2.2.3 Industry-specific Quality Standards
Medical: FDA 21 CFR Part 11, IEC 62304 (Medical Device Software)

Automotive: ISO 26262 (Functional Safety)

Aerospace: DO-178C (Software Considerations in Airborne Systems)

Financial: PCI DSS (Payment Card Industry Data Security Standard)

Government: Various security and quality standards based on criticality

6.2.3 Defining Quality Control Processes
6.2.3.1 Inspection and Review Techniques
Formal Inspections: Structured process with defined roles (moderator, author, reviewer)

Peer Reviews: Less formal technical reviews by colleagues

Walkthroughs: Author-led sessions to explain work product

Checklist-based Reviews: Using standardized checklists for consistency

Effectiveness: Typically find 60-90% of defects before testing

6.2.3.2 Static and Dynamic Testing Approaches
Static Testing: Examining software without executing it

Examples: Code reviews, requirement analysis, design analysis, static code analysis

Benefits: Early defect detection, lower cost of correction

Dynamic Testing: Executing software with test cases

Examples: Unit testing, integration testing, system testing, acceptance testing

Benefits: Validation of behavior, performance measurement

6.2.3.3 Automated Testing Strategies
Test Automation Pyramid:

Base: Large number of fast, inexpensive unit tests

Middle: Smaller number of integration tests

Top: Few end-to-end UI tests

Continuous Testing: Automated tests executed as part of CI/CD pipeline

Test Coverage Metrics: Code coverage, requirement coverage, risk coverage

Tools: Selenium, JUnit, TestNG, Cypress, Postman, SoapUI
