# Risk management

> **Project risk may be defined as the chance of certain occurrences adversely affecting project objectives, the degree of exposure to negative events, and their probable consequences.**

Risk management in software projects is the systematic approach of identifying, analyzing, and responding to risks to minimize their negative impact on project objectives. It ensures that uncertainties are proactively managed rather than reactively handled.

---

## 4.1 Types of Risk

1.  **Schedule Risks**:

    - Related to **_time and delivery planning._**
    - Caused by poor estimation, improper resource allocation, frequent scope expansion, and lack of tracking.
    - Consequence: Delays, missed deadlines, and possible project failure.

2.  **Budget Risks:**

    - **_Monetary risks_** from budget overruns and mismanagement.
    - Reasons: Wrong estimation, cost overruns, scope expansion, improper tracking, poor finance handling.
    - Consequence: Financial instability and project failure.

3.  **Operational Risks:**

    - Risks from **_daily project operations and poor process execution._**
    - Reasons: Insufficient resources, conflicts, poor planning, lack of communication, unclear roles, inadequate training.
    - Consequence: Inefficient project execution.

4.  **Technical Risks:**

    - Related to **_functionality and performance_** of software.
    - Reasons: Frequent requirement changes, outdated technology, high complexity, poor integration, lack of skilled staff.
    - Consequence: Software performance issues and delivery failure.

5.  **Programmatic Risks**

    - External, uncontrollable risks.
    - Reasons: Market changes, lack of funds, policy/regulation changes, contract loss.
    - Consequence: Project disruption from external factors.

6.  **Other Forms of Risks**

    - **Communication Risks**: Misunderstandings due to inadequate communication.
    - **Security Risks**: Vulnerabilities affecting privacy, reliability, or access.
    - **Quality Risks**: Product fails to meet user satisfaction or standards.
    - **Law & Compliance Risks**: Legal penalties or issues from ignoring regulations.
    - **Cost Risks**: Unexpected costs or financial mismanagement.
    - **Market Risks**: Shifts in trends, competitors, or customer demands.

    📝[Further reading and reference](https://www.geeksforgeeks.org/software-engineering/different-types-of-risks-in-software-project-development/)

## 4.1 Risk Identification Techniques

### 4.1.1 Brainstorming and Delphi Technique

- **Brainstorming**: A collaborative technique where the project team generates as many potential risks as possible without immediate criticism. Encourages creativity and broad participation.
- **Delphi Technique**: An expert-based approach where multiple rounds of anonymous questionnaires are distributed to experts. Feedback is refined until consensus is reached on the most critical risks.

### 4.1.1.2 SWOT Analysis for Risk Identification

- **Strengths, Weaknesses, Opportunities, Threats (SWOT)** is used to analyze internal and external project factors.
  - _Weaknesses_ and _Threats_ often reveal potential risks (e.g., lack of technical expertise, competitive threats).
  - Helps in balancing risks with opportunities.

### 4.1.1.3 Creating a Risk Breakdown Structure (RBS)

- Hierarchical representation of risks, similar to a Work Breakdown Structure (WBS).
- Categorizes risks into levels: e.g., **Technical → Performance → Security**.
- Helps ensure no major risk category is overlooked.

---

## 4.1.2 Qualitative and Quantitative Risk Analysis

### 4.1.2.1 Probability and Impact Matrix

- A grid-based tool for ranking risks.
- Probability (likelihood of occurrence) × Impact (effect on project objectives).
- Helps prioritize risks into categories such as **High**, **Medium**, or **Low**.

### 4.1.2.2 Expected Monetary Value (EMV) Analysis

- Quantifies risk by calculating:  
  **EMV = Probability × Impact (in monetary terms)**.
- Example: If there is a 40% chance of a server failure costing $50,000 → EMV = $20,000.
- Useful for budgeting risk reserves.

### 4.1.2.3 Decision Tree Analysis for Risk Evaluation

- Graphical tool that maps decision alternatives and possible outcomes.
- Uses probabilities and EMV at each branch to identify the most cost-effective decision.
- Useful for high-stake, uncertain choices.

---

## 4.1.3 Risk Response Planning

### 4.1.3.1 Risk Response Strategies

1. **Avoid** – Change project plan to eliminate risk (e.g., using proven technology instead of experimental).
2. **Transfer** – Shift responsibility to a third party (e.g., outsourcing, insurance).
3. **Mitigate** – Reduce probability or impact (e.g., conduct extra testing, hire experts).
4. **Accept** – Acknowledge risk and deal with consequences (passive or active acceptance).

### 4.1.3.2 Developing Contingency Plans

- Predefined actions to be executed if the risk occurs.
- Example: If a critical resource becomes unavailable, a backup vendor is already identified.

### 4.1.3.3 Creating Risk Response Ownership

- Assigning responsibility for monitoring and responding to specific risks.
- Ensures accountability and proactive management.

---

# 4.2 Common Risks in Software Projects

## 4.2.1 Technical Risks

### 4.2.1.1 Technology Obsolescence and Integration Challenges

- New technologies may become outdated before project completion.
- Integrating diverse tools, platforms, or APIs may lead to compatibility issues.

### 4.2.1.2 Performance and Scalability Risks

- System may fail to meet performance benchmarks (speed, responsiveness).
- Poor scalability planning can lead to bottlenecks as user demand grows.

### 4.2.1.3 Security Vulnerabilities and Data Protection

- Software may be exposed to cyberattacks, data breaches, or non-compliance with data protection regulations.
- Risks increase with weak encryption, poor authentication, or outdated libraries.

---

## 4.2.2 Schedule and Budget Risks

### 4.2.2.1 Scope Creep and Requirement Changes

- Continuous addition of features without formal approval leads to delays and cost overruns.
- Often caused by unclear initial requirements or stakeholder pressure.

### 4.2.2.2 Underestimation of Effort and Complexity

- Developers or managers underestimate the technical difficulty, leading to missed deadlines and budget overruns.
- Often results from lack of historical data or optimism bias.

### 4.2.2.3 Resource Availability and Skill Set Mismatches

- Lack of sufficient skilled personnel at the right time delays progress.
- Skills required may differ from the team’s expertise (e.g., cloud migration expertise missing).

---

## 4.2.3 Human Resource Risks

### 4.2.3.1 Team Conflicts and Communication Breakdowns

- Disagreements, cultural differences, or lack of effective communication can disrupt collaboration.
- Leads to reduced morale and project delays.

### 4.2.3.2 Loss of Key Personnel

- Departure of highly skilled team members (due to resignation, illness, etc.) can jeopardize project progress.
- Creates knowledge gaps and transition delays.

### 4.2.3.3 Productivity Variations Among Team Members

- Team members may differ in motivation, skills, or working styles.
- Uneven productivity affects overall project delivery.
- Can be managed through workload balancing, mentoring, and monitoring.

<!-- footnote -->

[^1] :

      https://www.geeksforgeeks.org/software-engineering/different-types-of-risks-in-software-project-development/
