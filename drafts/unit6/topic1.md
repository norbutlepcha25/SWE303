6.1 Software Quality Concepts
Understanding the fundamental principles and economic aspects of software quality provides the foundation for effective quality management.

> **Software Quality** is the degree to which a software product satisfies stated and implied needs when used under specified conditions. It is not merely the absence of defects but the presence of valuable characteristics.

**PMBOK Relation:** This is the foundation of the **Project Quality Management Knowledge Area**. The PMBOK Guide defines quality as "the degree to which a set of inherent characteristics fulfills requirements." It emphasizes that project quality management aims to ensure both that the project fulfills its stated requirements (conformance to requirements) and that it meets the needs and expectations of its stakeholders (fitness for use).

Quality in the context of project management refers to the degree in which a project fulfills its objectives and meets or exceeds the needs and expectations of its stakeholders.

**Why quality is of paramount importance ?**

1.  **Quality directly impacts customer satisfaction.**

    When a project delivers high quality results, it not only meets but often exceeds customer expectations. Satisfied customers are more likely to form long time partnerships with organizations, leading to repeat business and positive referrals.

2.  **Effective quality management helps in cost control.**

    By identifying and addressing quality issues early in the project life cycle, organizations can avoid
    costly rework and corrections. This results in reduced project costs and improved profitability.

3.  **Quality management plays a crucial role in risk mitigation.**

    Identifying and addressing quality related risks and issues in a proactive manner prevents them from
    escalating into significant problems. This, in turn safeguards the project schedule, budget, and overall success.

4.  **Organizations that consistently deliver high quality projects gain a competitive edge in the market.**

    Quality becomes a differentiator that attracts discerning customers and sets the organization apart
    from competitors.

These principles serve as a framework for ensuring that quality is integrated into every aspect of project

1. Clear and well-defined quality.
   Objectives are the foundation of effective project quality management. These objectives should be
   specific, measurable, achievable, relevant, and time bound. They must align with the project's overall
   goals and stakeholders expectations.Clear objectives provide a roadmap for quality planning,  
    execution and monitoring.

2. The active involvement of stakeholders is instrumental in shaping the quality management process.
   Stakeholders, including customers and users, project sponsors and team members have unique perspectives and expectations regarding quality. Engaging stakeholders and quality planning and decision making ensures that their requirements are considered, leading to greater satisfaction.

3. One of the core principles of quality management is the emphasis on prevention over inspection.
   Instead of relying solely on post production, inspection and corrective actions. Project quality management advocates for identifying and addressing issues at their root causes. This proactive approach not only reduces the likelihood of defects, but also minimizes the associated costs and disruptions.

4. Quality management is an iterative and continuous process.
   Projects are dynamic and the business environment evolves over time. To remain competitive and meet changing expectations, organizations must embrace a culture of continuous improvement. This entails regularly reviewing and enhancing quality management processes and practices.

These best practices are a collection of proven methods and techniques that enhance the likelihood of
achieving and maintaining high quality standards throughout the project's life cycle.

1.  **Quality planning**

    - The initial step in project quality management.
    - It involves the development of a comprehensive quality management plan that outlines how quality will
      be achieved and maintained throughout the project.
    - The Quality Management Plan defines quality objectives, standards, processes, responsibilities and the methods for monitoring and controlling quality.
    - It serves as a crucial reference document for the project team and stakeholders.

2.  **Quality assurance**

    - encompasses the processes and activities that ensure project work complies with the defined quality standards and requirements.
    - It focuses on prevention, aiming to prevent defects and issues from occurring in the first place.
    - Key components of quality assurance include process audits, peer reviews, and process improvements.
    - It also involves the establishment of quality checkpoints and milestones to monitor progress.

3.  **Quality control**

    - is the ongoing process of monitoring and measuring project performance to identify variances from the quality plan.
    - It involves inspection, testing and verification activities to ensure that the project's deliverables meets the specified quality criteria.
    - When deviations from quality standards are identified, corrective actions are taken promptly to bring the project back on track.

4.  Ensuring that team members possess the necessary skills and knowledge to meet quality standards is a critical aspect of project quality management. Continuous training and skill development programs should be in place to equip team members with the competencies required to deliver high quality work.
    Training should cover both technical skills and soft skills such as communication and problem solving.

5.  Data and metrics play a pivotal role in quality management.
    Project teams should collect and analyze relevant data to make informed decisions about quality.
    By tracking performance metrics, organizations can identify trends, patterns, and areas for improvement.
    Data driven decision making enhances the organization's ability to proactively address quality issues.

6.1.1 Defining Software Quality
6.1.1.1 ISO/IEC 25010 Software Quality Model

The ISO/IEC 25000 series, known as SQuaRE (Systems and software Quality Requirements and Evaluation), is a set of international standards focused on the quality of systems and software products.

The ISO/IEC 25010 standard provides a comprehensive and modern framework for evaluating software product quality, replacing the older ISO 9126. It breaks down quality into two main models:

1.  **Product Quality Model (8 Characteristics):** The inherent properties of the software itself.
2.  **Quality in Use Model (5 Characteristics):** The outcome of interacting with the software in a specific context.

**Key Product Quality Characteristics:**

1.  **Functional Suitability:**

    - How well the software provides functions that meet stated and implied needs.
    - to meet the stated and implied needs of the user
    - Completeness, correctness, and appropriateness of functions.
    - example: An online banking app correctly performs fund transfers, shows accurate account balances, and generates transaction histories without errors.

2.  **Performance Efficiency:**

    - How efficiently the software uses resources (e.g., time, memory).
    - perfrom the functions within specified time and throughput parameters and be efficient in the use of resources under specified conditions
    - Time behavior, resource utilization, and capacity under defined conditions.
    - Example: A video streaming platform loads and plays videos quickly without buffering, even during high user traffic.The system maintains quick response even with many users rather then the app freezing when more than 100 users are online.

3.  **Compatibility:**

    - Ability to work with other systems or software.
    - exchange information with other products and/or perform its required functions while sharing the same common environment and resources.
    - Interoperability and coexistence with other systems or software.
    - Example: A document editing app can open and save files in Microsoft Word (.docx) and Google Docs formats which runs smoothly on Windows, macOS, and Linux rather than only running on Windows and crashes when opening .docx files from other software.

4.  **Usability:**

    - Ease of use and learnability for users.
    - Degree to which the software is easy to use and learn, and protects users from errors
    - Learnability, accessibility, and user interface quality.
    - Example: A food delivery app with a clean interface where users can easily find restaurants, add items, and track delivery rather than requiring too many steps or has confusing navigation.

5.  **Reliability:**

    - Ability to perform consistently under stated conditions.
    - perform a specified function, under specified condition for a specifed amount of time
    - availability, fault tolerance, and recoverability after failures
    - Example: A hospital management system runs 24/7 without crashing, ensuring patient data is always accessible, continuouly running correctly during high usage period rather than a system frequently crashing when saving patient data.

6.  **Security:** Can it protect data and resist attacks?

    - Ability to protect information and data.
    - protect information and data so the person or other products have a degree of access appropriate to their types and level of authorization
    - Confidentiality, integrity, authenticity, accountability, and non-repudiation.
    - Example: An e-commerce website encrypts user passwords and uses two-factor authentication for login with user data encrypted and protected from breaches rather than storing passwords in plain text, making it vulnerable to hacking.

7.  **Maintainability:** How easy is it to modify?

    - Ease of modification and maintenance.
    - easily modified by the intended modifers for efficiency and effectiveness
    - Modularity, reusability, analyzability, and modifiability of code.
    - Example: A university portal system where developers can quickly update course details or fix bugs without affecting other modules. Uses modular code and proper documentation.

8.  **Portability:**

    - Ease of transferring software from one environment to another.
    - to adapt to the change in its requirement, context of use, or system environment
    - Installability, adaptability, and replaceability across platforms.
    - Example: A mobile game that runs smoothly on both Android and iOS devices and adapts automatically to screen sizes and OS versions rather than running only on andriods

Current Standard: Replaces ISO 9126, providing comprehensive quality characteristics

Product Quality Model (8 Characteristics):

Functional Suitability: Completeness, correctness, appropriateness

Performance Efficiency: Time behavior, resource utilization, capacity

Compatibility: Co-existence, interoperability

Usability: Appropriateness, recognizability, learnability, operability

Reliability: Maturity, availability, fault tolerance, recoverability

Security: Confidentiality, integrity, non-repudiation, accountability

Maintainability: Modularity, reusability, analyzability, modifiability, testability

Portability: Adaptability, installability, replaceability

6.1.1.2 Internal vs. External Quality Attributes
Internal Quality Attributes: Measurable during development, not directly visible to users

Examples: Code complexity, coupling, cohesion, test coverage, documentation quality

Importance: Predict external quality, affect maintainability and evolution

External Quality Attributes: Observable during operation by end-users

Examples: Response time, availability, ease of use, functional correctness

Measurement: Through testing, monitoring, and user feedback

When evaluating the quality of a product, service, or process, its precise features or characteristics are referred to as its attributes. This is a critical distinction for when and how quality is measured.

- **Internal Quality Attributes:**

       Internal quality attributes are properties of the software product that are observable or measurable inside the development environment or codebase, before execution (or without actual end-user observation). They relate to code, architecture, and artifacts that developers and testers can inspect.

       - **Examples:** Code complexity (Cyclomatic Complexity), code duplication, comment density, adherence to coding standards, modularity.
       - **Measurement:** Static code analysis tools (e.g., SonarQube).

- **External Quality Attributes:**

       External quality attributes are properties that are measured when the software is executed in an environment or experienced by end-users. They reflect the runtime behaviour and user-observed characteristics.

       - **Examples:** Response time, ease of use, crash frequency, feature correctness.
       - **Measurement:** Testing (functional, performance, usability).

**Relationship:** High internal quality (clean, well-structured code) is a prerequisite for achieving and sustaining high external quality (a stable, fast application).

6.1.1.3 User Satisfaction and Software Quality
Quality in Use (ISO 25010): Effectiveness, efficiency, satisfaction, freedom from risk, context coverage

User Experience (UX): Goes beyond functionality to include emotional response

Stakeholder Value: Quality defined by meeting or exceeding stakeholder expectations

Continuous Feedback: Incorporating user feedback into quality improvement cycles

User satisfaction is the ultimate, holistic measure of software quality, often captured by the **Net Promoter Score (NPS)** or user satisfaction surveys. It transcends technical metrics and is a function of:

- **Meeting Explicit Requirements:** The software functions as advertised.
- **Fulfilling Implied Needs:** It is intuitive, reliable, and performs well enough not to cause frustration.
- **Perceived Value:** The benefits outweigh the costs and effort of using it.

**Example:** A bug-free application with all required features (high conformance to requirements) may still receive low user satisfaction if it is slow and confusing to navigate (low fitness for use).

How to measure user satisfaction

1. Direct surveys
2. Behavioral metrics: retention rate, task completion rate, time-on-task, bounce rate, feature usage.
3. Support metrics: number of support tickets, time-to-resolution, sentiment in feedback.
4. Qualitative methods: interviews, contextual inquiry, usability testing with think-aloud protocol.

6.1.2 Quality Attributes and Metrics
6.1.2.1 Reliability and Maintainability Metrics
Reliability Metrics:

MTBF (Mean Time Between Failures): Average time between system failures

MTTR (Mean Time To Repair): Average time to restore service after failure

Availability: (MTBF / (MTBF + MTTR)) × 100%

Defect Density: Number of defects per size unit (KLOC, function points)

Maintainability Metrics:

Cyclomatic Complexity: Measures code complexity (McCabe metric)

Technical Debt: Quantifying shortcuts that require future rework

Code Churn: Frequency of code changes indicating instability

- **Reliability:** The ability to operate without failure under stated conditions for a specified period.

  - **Metrics:**
    - **Mean Time To Failure(MTTF)** = Total operational time / Number of failures - Use when failures are non-repairable or initial time-to-failure is measured.
    - **Mean Time Between Failures (MTBF):** The average time between system breakdowns. (Higher is better).
    - **Mean Time To Repair (MTTR):** The average time required to fix a failure and restore service. (Lower is better).
    - **Defect Density:** Number of confirmed defects per size of software (e.g., per 1000 lines of code).

- **Maintainability:** The ease with which a software system can be modified to correct defects, improve performance, or adapt to a changed environment.
  - **Metrics:**
    - **Cyclomatic Complexity:** A measure of the logical complexity of the code (e.g., measured per function). Lower complexity is easier to test and maintain.
    - **Technical Debt:** Quantified effort (in developer-hours) required to fix code that is quick-and-dirty but not sustainable.
      6.1.2.2 Performance Efficiency and Security Metrics
      Performance Metrics:

Response Time: Time to complete specific operations

Throughput: Transactions processed per time unit

Resource Utilization: CPU, memory, network, disk usage

Scalability: Performance under increasing load

Security Metrics:

Vulnerability Density: Security flaws per size unit

Time to Patch: Average time to fix security vulnerabilities

Security Test Coverage: Percentage of security requirements tested

Penetration Test Results: Number and severity of vulnerabilities found

- **Performance Efficiency:**

  - **Metrics:**
    - **Response Time:** Time taken to complete a user transaction (e.g., page load < 3 seconds).
    - **Throughput:** Number of transactions processed per unit of time (e.g., 1000 requests/second).
    - **Resource Utilization:** CPU, memory, and network bandwidth consumed under load.

- **Security:**

  - **Metrics:**

    - **Number of Vulnerabilities:** Found by penetration testing or automated security scans (e.g., using OWASP ZAP).
    - **Time to Remediate Vulnerabilities:** Average time from discovery to fix for critical security flaws.
    - **Pass/Fail Security Compliance Checks:** Against standards like OWASP Top 10 or CIS Benchmarks.

    6.1.2.3 Usability and Portability Metrics
    Usability Metrics:

Task Success Rate: Percentage of correctly completed tasks

Time on Task: Time users take to complete specific tasks

Error Rate: Frequency of user errors

SUS (System Usability Scale): Standardized usability questionnaire

Portability Metrics:

Platform Independence: Effort required to port to different environments

Configuration Coverage: Percentage of supported configurations

Installation Time: Time and effort for deployment

**Usability:**

- **Metrics:**

  - **Task Success Rate:** Percentage of correctly completed tasks by test users.
  - **Time-on-Task:** Average time a user takes to complete a specific task.
  - **Error Rate:** Number of mistakes made by users during testing.
  - **System Usability Scale (SUS):** A standardized, reliable questionnaire for subjective usability assessment.

- **Portability:**
  - **Metrics:**
    - **Platform Independence:** Percentage of code that is platform-agnostic.
    - **Migration Effort:** Estimated person-hours required to port the system to a new environment (e.g., from on-premise to cloud).

---

6.1.3 Cost of Quality in Software Projects
6.1.3.1 Prevention Costs
Activities: Training, process improvement, tool acquisition, requirements analysis, design reviews

Goal: Prevent defects from being introduced

Examples: Code review processes, developer training, static analysis tools, prototyping

Economic Benefit: Highest return on investment in quality activities

6.1.3.2 Appraisal Costs
Activities: Testing, inspections, audits, quality assessments

Goal: Evaluate products to ensure quality standards are met

Examples: Test case development, automated testing, peer reviews, quality audits

Measurement: Cost of finding and identifying defects

6.1.3.3 Failure Costs (Internal and External)
Internal Failure Costs: Defects found before delivery to customers

Examples: Debugging, rework, retesting, scrap

Impact: Project delays, increased development costs

External Failure Costs: Defects found after delivery to customers

Examples: Technical support, warranty claims, patches, lost business, reputation damage

Impact: Highest cost multiplier (5-100x more expensive than prevention)

## reference

## Test Your self
