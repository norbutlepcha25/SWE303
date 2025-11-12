# 2.3 Scope definition and management

Project Scope Management, as defined by the PMBOK Guide, includes the processes required to ensure that a project includes all the work required, and only the work required, to complete the project successfully. For software projects, this is a critical discipline to prevent scope creep—the uncontrolled expansion of a project's scope without adjustments to time, cost, or resources—which is a primary cause of project failure.

## 2.3.1 Creating the project scope statement

The Project Scope Statement is the detailed description of the project and its major deliverables. It provides a common understanding of the project scope among stakeholders and serves as a baseline for future project decisions.

## 2.3.1.1 Defining product scope vs. project scope

Product Scope: The features and functions that characterize a software product, service, or result. It describes the "what" – the deliverable's attributes and capabilities.

Example: "The mobile application shall allow users to check their account balance, transfer funds between accounts, and deposit checks via the device's camera."

Project Scope: The work performed to deliver the software product with the specified features and functions. It describes the "how" – the activities required.

Example: "The project scope includes front-end and back-end development, API integration with the core banking system, user acceptance testing, and deployment to the Apple App Store and Google Play Store."

Key Distinction: The product scope is measured against the product requirements and SRS, while the project scope is measured against the project plan.

## 2.3.1.2 Techniques for defining project boundaries

Expert Judgment: Leveraging the knowledge of individuals or groups with specialized training or experience in software development and domain knowledge.

Product Analysis: Translating high-level product descriptions into tangible deliverables. For software, this includes decomposing high-level features from the SRS into lower-level, manageable components.

Alternatives Analysis: Evaluating different approaches (e.g., build vs. buy, different tech stacks) to perform the project work.

Explicitly Stating Inclusions and Exclusions: Clearly defining what is not included in the project is as critical as defining what is included. This prevents assumptions and manages stakeholder expectations.

Example: "In-scope: Development of the core mobile banking application. Out-of-scope: Integration with third-party investment platforms or development of a web-based admin console."

## 2.3.1.3 Documenting assumptions and constraints

Assumptions: Factors that are considered to be true, real, or certain for planning purposes, without proof or demonstration. They represent a potential risk if proven false.

Example: "It is assumed that the required banking API will be available for testing by Phase 2." "It is assumed that key subject matter experts will be available 15 hours per week."

Constraints: Limiting factors that restrict the team's options. The classic "Triple Constraint" of scope, time, and cost are primary examples.

Example: "The project must be completed before the end of the fiscal year (December 31st)." "The project budget is fixed at $500,000." "The solution must comply with PCI-DSS security standards."

## 2.3.2 Developing the Work Breakdown Structure (WBS)

The WBS is a key project deliverable that hierarchically decomposes the total scope of work into manageable components called work packages. It is a foundational tool for cost estimating, scheduling, resource planning, and risk management.

## 2.3.2.1 WBS creation techniques: top-down and bottom-up

Top-Down Approach: Starts with the final project deliverable and systematically subdivides it into smaller, more manageable components. This is the most common technique.

Process: Project -> Major Deliverables -> Sub-deliverables -> Work Packages.

Advantage: Provides a high-level view early on and is efficient for projects where the overall scope is well-understood.

Bottom-Up Approach: Involves identifying as many specific tasks as possible and then grouping them into higher-level categories and deliverables.

Advantage: Can be more accurate and comprehensive, as it leverages the team's detailed knowledge.

Disadvantage: Can be time-consuming and risks missing high-level elements; often used for novel or highly complex projects where the full scope is unclear at the start.

The 100% Rule: The most important principle in WBS creation. The WBS must include 100% of the work defined by the project scope and only the work required by the project scope.

## 2.3.2.2 WBS dictionary and its importance

The WBS Dictionary is a document that provides detailed deliverable, activity, and scheduling information about each component in the WBS, particularly the work packages.

Contents for each work package:

Code of Account Identifier: A unique identifier from the WBS.

Description of Work: A detailed narrative of the work to be performed.

Assumptions and Constraints: Specific to the work package.

Responsible Organization/Resource: The team or individual assigned.

List of Schedule Milestones: Key start and end dates.

Associated Activities: The tasks required to complete the work package.

Resources Required: People, equipment, materials.

Cost Estimates: The budget for the work package.

Importance: It provides the necessary detail and clarity that the graphical WBS cannot, preventing ambiguity and ensuring everyone understands what each component entails.

## 2.3.2.3 Using WBS to improve project planning and control

Foundation for Planning:

Scheduling: Work packages can be decomposed into activities for the project schedule.

Cost Estimating & Budgeting: Costs can be reliably estimated at the work package level and rolled up to create the project budget.

Resource Allocation: Work packages can be assigned to individual team members or groups, clarifying accountability.

Enhanced Control:

Monitoring: Provides a framework for tracking progress against specific, tangible components.

Performance Measurement: Enables Earned Value Management (EVM) by providing a clear breakdown of planned value (PV).

Communication: Serves as a clear communication tool to show stakeholders how the project is structured.

## 2.3.3 Scope control and change management

Scope Control is the process of managing changes to the project scope baseline. An effective process is essential to contain scope creep while still allowing for necessary and valuable changes.

Scope control and change management ensure that a project stays aligned with its defined objectives despite **evolving requirements.** They involve monitoring project scope, **managing scope changes** systematically, and preventing uncontrolled scope creep.

!!! warning "Note"

    It's the project manager's job to ***limit the need for changes*** on one hand, and on the other to ***efficiently manage the changes*** in a way that the project could benefit.

Requirement change control is the formal process of handling modifications to agreed-upon requirements in a project. It ensures that changes are properly documented, evaluated, approved, and communicated, preventing uncontrolled scope creep and project disruptions.

## 2.3.3.1 Establishing a change control board

vA CCB is a formally constituted group of stakeholders responsible for reviewing, evaluating, approving, delaying, or rejecting changes to the project.

Membership: Typically includes the project sponsor, project manager, key customer representatives, and technical leads.

Role: The CCB ensures that each change is evaluated from a business and technical perspective and that approved changes are properly integrated and communicated. It is the ultimate authority on scope changes.

- **Responsibilities**:

  - Review change requests.
  - Assess alignment with project goals.
  - Balance project constraints (time, cost, quality).
  - Approve or reject changes formally.

## 2.3.3.2 Evaluating the impact of scope changes

Before a change is approved, a systematic Integrated Change Control process is followed to assess its impact on all aspects of the project. This analysis is critical for informed decision-making by the CCB.

Scope Impact: Does the change alter the scope statement, WBS, or WBS Dictionary?

Schedule Impact: How many additional days/weeks are required? Does it affect the critical path?

Cost Impact: What are the additional costs for labor, materials, licenses, etc.?

Quality Impact: Does it affect quality standards, testing scope, or performance criteria?

Resource Impact: Are new or different skills required? Is there an impact on resource allocation?

Risk Impact: Does it introduce new risks or mitigate existing ones?

Procurement Impact: Are new vendors or contracts required?

- **Tools used**: Impact analysis, cost-benefit analysis, risk assessment.
- **Outcome**: Informed decision-making that balances customer needs with project feasibility.

## 2.3.3.3 Implementing an effective change management process

A formal, documented process ensures changes are managed consistently and transparently.

Identify & Document Change: A stakeholder submits a formal Change Request (e.g., via a standardized form in a tool like Jira).

Perform Integrated Impact Analysis: The project manager, with input from the team, conducts the comprehensive analysis described above.

CCB Review & Decision: The CCB meets regularly to review the change request and its impact analysis, deciding to Approve, Reject, or Defer the change.

Update Project Documents: If approved, the project management plan, scope baseline (Scope Statement, WBS, WBS Dictionary), and other relevant documents are updated.

Communicate Decision: The decision and its rationale are formally communicated to all stakeholders.

Implement & Track Change: The project team implements the change, and the project manager ensures it is tracked to completion and that the project baselines reflect the new reality. All changes are logged in a Change Log.

- A well-defined **change management process** ensures that changes are documented, assessed, approved, and communicated.
- **Steps typically include**:

  1. **Change Request Submission** → Formal request logged with description and justification.
  2. **Impact Analysis** → Evaluation of cost, schedule, quality, and risks.
  3. **CCB Review and Decision** → Approve, reject, or defer the change.
  4. **Implementation Planning** → Update project plans, schedules, and resources.
  5. **Communication** → Notify stakeholders and ensure alignment.
  6. **Monitoring** → Track change implementation and its results.

- **Benefit**: Ensures transparency, accountability, and control over evolving requirements.
