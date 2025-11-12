# 2.2 Requirements gathering processes

Requirements gathering is the foundational process of identifying, documenting, and managing the needs and constraints of stakeholders to define project and product scope. In software project management, this process directly determines whether the final product will meet business objectives. As defined by the PMBOK Guide and IEEE standards, effective requirements management is critical for controlling scope creep, mitigating risks, and establishing a basis for validation and verification.

## 2.2.1 Requirements elicitation techniques

Elicitation involves actively engaging with stakeholders to discover, extract, and define their needs. The choice of technique depends on stakeholder availability, project complexity, and the clarity of initial requirements.

## 2.2.1.1 Interviews and questionnaires

- **Interviews**: A direct, conversational technique for gathering detailed information from individuals or small groups.

      **Types of interview:**

      1.  Structured: Uses a pre-defined set of questions for consistency.
      2.  Unstructured: An open, conversational format to explore topics in depth.
      3.  Semi-structured: A blend, using a guide but allowing for follow-up questions.

!!! note ""

    Ideal for engaging subject matter experts (SMEs) and key stakeholders to understand complex processes and nuanced needs.

- **Questionnaires and Surveys:** A written technique for collecting data from a large, geographically dispersed group of stakeholders.

!!! note ""

    Efficient for validating requirements, gathering feedback on prototypes, or quantifying user preferences (e.g., feature prioritization surveys).

     Limitation: Lacks the depth of interviews and cannot probe immediate, unscripted responses.

## 2.2.1.2 Workshops and focus groups

Requirements Workshops (e.g., JAD Sessions): Facilitated meetings that bring together key cross-functional stakeholders (e.g., developers, testers, business analysts, end-users) to collaboratively define and refine requirements.

Key Feature: High-intensity, focused collaboration aimed at achieving consensus quickly.

Output: Often produces prioritized lists, draft models, and clarified requirements. Highly effective for building shared understanding and buy-in.

Focus Groups: A moderated discussion with a pre-selected group of users or stakeholders to gain insights into their expectations, perceptions, and attitudes.

Application: Useful for understanding user experience (UX) needs, exploring reactions to new concepts, or gathering feedback on a product's "look and feel."

## 2.2.1.3 Observation and document analysis

Observation (Job Shadowing): The process of watching users in their actual work environment to understand processes, workflows, and challenges that they may not articulate verbally.

Types:

Passive Observation: Watching without interrupting.

Active Observation: Asking questions while the user works.

Application: Uncovers unstated or tacit requirements, inefficiencies in current processes, and contextual factors affecting system use.

Document Analysis: Reviewing existing organizational artifacts to extract requirements and understand the business context.

Documents Reviewed: Business plans, market studies, existing system documentation, process flows, policy documents, and bug/issue logs from legacy systems.

Application: Provides historical context, identifies business rules, and is a low-cost method for gathering initial information.

## 2.2.2 Requirements analysis and specification

This process involves refining, decomposing, and formally documenting the elicited requirements to make them unambiguous, verifiable, and actionable for the development team.

## 2.2.2.1 Functional vs. non-functional requirements

**Functional Requirements:** Describe the behaviors or functions of the system—what the system must do. They define interactions between the system and its environment.

Examples: "The system shall allow users to reset their password." "The system shall generate a monthly sales report."

**Non-Functional Requirements (Quality Attributes):** Describe the quality constraints and performance criteria under which the system must operate—how well the system performs its functions. They are often critical to user satisfaction and system success.

Categories:

Performance: Response times, throughput (e.g., "The system shall support 1,000 concurrent users with a sub-2-second page load time.").

Security: Authentication, authorization, data protection (e.g., "All sensitive data shall be encrypted in transit and at rest.").

Usability: User interface simplicity, learnability.

Reliability/Availability: Uptime requirements (e.g., "System availability shall be 99.9% during business hours.").

Scalability & Maintainability: Ease of future modification and growth.

## 2.2.2.2 Use cases and user stories

Use Cases: A textual description of the interactions between an actor (a user or external system) and the system itself to achieve a specific goal.

Components: Actor, Primary Success Scenario, Alternate Paths, and Exception Paths.

Application: Excellent for detailing complex business processes and system interactions in a narrative form. Common in traditional/waterfall methodologies.

User Stories: An Agile requirements artifact that follows a simple, concise template: "As a [type of user], I want to [perform some action], so that I can [achieve some benefit/value]."

Key Feature: They are placeholders for a future conversation and are deliberately brief. Details are elaborated during backlog refinement sessions.

INVEST Criteria: Effective user stories should be Independent, Negotiable, Valuable, Estimable, Small, and Testable.

## 2.2.2.3 Creating a Software Requirements Specification (SRS)

The SRS is a comprehensive, formal document that serves as a complete description of the external behavior of the software system. It is the single source of truth for what will be built.

Purpose: Provides a basis for agreement between customers and developers; reduces development effort; serves as a basis for cost and schedule estimation; and provides a baseline for validation and verification (testing).

Key Contents (IEEE Std 830):

Introduction: Purpose, Scope, Definitions, References.

Overall Description: Product Perspective, Functions, User Characteristics, Constraints.

Specific Requirements: Detailed Functional Requirements, Non-Functional Requirements, External Interface Requirements (UI, Hardware, Software, Communications), and System Features.

## 2.2.3 Requirements validation and management

This ongoing process ensures that requirements remain correct, consistent, and actionable throughout the project lifecycle and that changes are controlled.

## 2.2.3.1 Requirements traceability matrix

The RTM is a grid that links product requirements from their origin to the deliverables that satisfy them, providing bi-directional traceability.

Purpose:

Ensures each requirement adds business value (links to business need).

Confirms all requirements are implemented (links to design/code).

Verifies all requirements are tested (links to test cases).

Facilitates impact analysis when changes occur.

Structure: Typically maps Requirements ID and Description to Business Objective, Design Document, Source Code Module, and Test Case ID.

## 2.2.3.2 Change control process for requirements

A formal process to manage changes to baselined requirements, preventing uncontrolled scope creep.

Change Request Submission: Any stakeholder submits a formal change request.

Impact Analysis: The project manager and team analyze the impact on scope, schedule, cost, quality, and risks.

Change Control Board (CCB) Review: A formally constituted group (sponsor, PM, key stakeholders) reviews the impact analysis and approves, rejects, or defers the change.

Implementation & Communication: If approved, the requirements documents (SRS, Backlog) and project baselines are updated. The decision is communicated to all stakeholders.

## 2.2.3.3 Tools for requirements management

Purpose-Built Tools:

Jira/Azure DevOps: Widely used for Agile projects to manage user stories, epics, and backlogs. Integrates well with development and testing workflows.

IBM DOORS NG: A powerful, enterprise-level tool for complex projects requiring rigorous traceability and compliance.

Modern Requirements: A solution that often integrates with Azure DevOps to provide enhanced SRS-like capabilities.

Modeling & Collaboration Tools:

Enterprise Architect, IBM Rational Rhapsody: For visual modeling (UML, BPMN) linked to requirements.

Confluence, SharePoint: Often used as a collaborative repository for SRS documents, meeting notes, and other requirement-related artifacts.

## reference

## Test Your self

```

```
