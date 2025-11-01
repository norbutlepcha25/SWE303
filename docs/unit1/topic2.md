# 1.2 Software Development Life Cycle Model

This unit explores the various process frameworks, or Software Development Life Cycle (SDLC) models, that provide a structured approach for planning, designing, building, testing, and delivering software. The choice of an SDLC model is a fundamental strategic decision that defines the project's workflow, pace, and adaptability to change. No single model is universally superior; each offers a distinct set of advantages and trade-offs, making it suitable for specific project contexts.

The unit progresses from highly structured, predictive models to adaptive, flexible frameworks, reflecting the evolution of software project management in response to the need for speed and responsiveness. Understanding these models is crucial for a Project Manager to select the right lifecycle approach based on project requirements, stakeholder expectations, and the nature of the product being developed.

## 1.2.1 Waterfall model

The Waterfall model is a sequential (or linear) lifecycle model where project activities are broken down into distinct, non-overlapping phases. The output of one phase serves as the input for the next, with little to no iteration or going back. It is a predictive model, relying on extensive upfront planning and a fixed scope.

### 1.2.1.1 Phases of the waterfall model

The phases are strictly sequential and typically include:

Requirements Gathering and Analysis: All possible system requirements are captured in a detailed Software Requirements Specification (SRS) document.

System Design: The requirements are used to architect the system. This includes high-level (system architecture) and low-level (detailed module design) design documents.

Implementation (Coding): The design is translated into code in small programs called units. This is the software development phase.

Integration and Testing: All units are integrated and tested as a complete system to ensure all requirements are met. This is where most defects are identified.

Deployment of System (Deployment): The finished product is delivered to the customer and deployed in the production environment.

Operations and Maintenance: The system is used and maintained, including fixing undiscovered bugs and potentially releasing updates.

### 1.2.1.2 Advantages and disadvantages

Advantages Disadvantages
Simple and Easy to Understand: Phases are logical and easy for management and stakeholders to grasp. Inflexible to Change: It is difficult and expensive to go back and change requirements once a phase is complete.
Clear Milestones and Deliverables: Each phase has well-defined outputs, making progress easy to track. Late Delivery of Working Software: The customer does not see a working product until very late in the lifecycle.
Well-Suited for Stable Requirements: Works well when requirements are well-understood and unlikely to change. High Risk and Uncertainty: Major risks (e.g., misunderstood requirements, technical feasibility) are often discovered only during testing.
Easier Management and Control: The structured nature makes it easier to manage tasks, budgets, and schedules. Testing is a Bottleneck: Testing is relegated to the end, leading to potential schedule overruns if many defects are found.

### 1.2.1.3 Suitable scenarios for waterfall model usage

Projects with Stable, Well-Defined Requirements: Where requirements are clear, fixed, and unlikely to change (e.g., government contracts, regulatory systems).

Short and Simple Projects: Where the project scope is small and the technology is well-understood.

Projects with Strict Regulatory Compliance: Where each phase requires formal documentation and sign-off (e.g., medical, aviation, or nuclear software).

When the Technology and Tools are Stable and Familiar.

## 1.2.2 Iterative and incremental models

These models develop a system through repeated cycles (iterative) and in smaller portions at a time (incremental), allowing developers to learn from earlier cycles and build upon them. The goal is to break down the project into smaller, more manageable segments.

### 1.2.2.1 Spiral model: phases and risk-driven approach

The Spiral Model, developed by Barry Boehm, combines the iterative nature of prototyping with the controlled and systematic aspects of the Waterfall model. It is risk-driven.

Each loop of the spiral represents a phase and consists of four quadrants:

Objective Setting: Define the objectives, alternatives, and constraints for that iteration.

Risk Assessment and Reduction: Identify and analyze risks. Perform activities (like prototyping) to resolve the highest-priority risks.

Development and Validation: Develop and test the deliverables for that iteration using a suitable SDLC model (e.g., Waterfall for that segment).

Planning: Review the results of the iteration and plan for the next iteration.

### 1.2.2.2 Rational Unified Process (RUP): phases and disciplines

RUP is a comprehensive iterative framework that provides a disciplined approach to assigning tasks and responsibilities within a development organization.

Dynamic Structure (Phases - Managed across the project timeline):

Inception: Establish the business case and scope.

Elaboration: Plan the project, specify features, and baseline the architecture.

Construction: Build the product through a series of iterative developments.

Transition: Transition the product to the end users (deployment, beta testing).

Static Structure (Disciplines - Activities that occur within each phase):

Business Modeling, Requirements, Analysis & Design, Implementation, Test, Deployment.

Supporting Disciplines: Configuration & Change Management, Project Management, Environment.

### 1.2.2.3 Advantages of iterative development in software projects

Early Risk Mitigation: Major risks are identified and addressed in early iterations.

Early Visibility and Feedback: Stakeholders can see working software early and provide feedback, which is incorporated into subsequent iterations.

Manageable Complexity: The project is broken down into smaller, more manageable chunks.

Easier to Accommodate Change: The iterative nature allows for requirements to be refined and changed between cycles.

Continuous Improvement: Defects are identified and fixed early in the lifecycle, leading to higher quality.

## 1.2.3 Agile methodologies

Agile is a mindset and philosophy based on the values and principles expressed in the Agile Manifesto. It emphasizes individuals and interactions over processes and tools, working software over comprehensive documentation, customer collaboration over contract negotiation, and responding to change over following a plan.

### 1.2.3.1 Scrum: roles, artifacts, and events

Scrum is a lightweight framework for developing complex products, not a definitive methodology.

Roles:

Product Owner: Maximizes product value, manages the Product Backlog.

Scrum Master: Ensures the team follows Scrum practices, removes impediments (servant-leader).

Development Team: A cross-functional, self-organizing team of 5-9 people who do the work.

Artifacts:

Product Backlog: An ordered list of everything needed in the product.

Sprint Backlog: The set of Product Backlog items selected for the current Sprint, plus a plan for delivering them.

Increment: The sum of all completed Product Backlog items at the end of a Sprint.

Events (Ceremonies):

Sprint: A time-boxed iteration (usually 2-4 weeks) where a "Done" increment is created.

Sprint Planning: A plan is created for the work to be performed in the Sprint.

Daily Scrum: A 15-minute time-boxed event for the Development Team to synchronize.

Sprint Review: The team demonstrates the Increment to stakeholders and gathers feedback.

Sprint Retrospective: The team inspects itself and creates a plan for improvements.

### 1.2.3.2 Kanban: principles, practices, and board management

Kanban is a method for managing and improving work across human systems. It focuses on visualizing the workflow, limiting work in progress (WIP), and enhancing flow.

Principles:

Start with what you do now.

Agree to pursue incremental, evolutionary change.

Respect the current process, roles, and responsibilities.

Practices:

Visualize the Workflow (Kanban Board): Uses columns (e.g., To Do, In Progress, Done) and cards to represent work items.

Limit Work in Progress (WIP): Explicitly limits the number of items in any given column to prevent bottlenecks and improve flow.

Manage Flow: The movement of work items through the process is monitored and optimized for smoothness and speed.

Make Process Policies Explicit: The team defines when a work item can move from one column to the next.

Implement Feedback Loops: Regular meetings (e.g., daily stand-ups, replenishment meetings) are held.

Improve Collaboratively, Evolve Experimentally: The team uses the scientific method to implement improvements.

### 1.2.3.3 Extreme Programming (XP): values, practices, and team dynamics

XP is an Agile methodology focused on technical excellence and customer satisfaction. It is most suitable for projects with dynamic or rapidly changing requirements.

Values:

Communication: Constant communication between developers and customers.

Simplicity: Design and code for the current needs, not future possibilities.

Feedback: Rapid feedback from the system (unit tests), customer (user stories), and team.

Courage: To refactor code, to throw away code, and to resist unrealistic demands.

Respect: For all team members.

Key Practices:

User Stories: For requirements capture.

Test-Driven Development (TDD): Write a failing test before writing the code.

Pair Programming: Two programmers work together at one workstation.

Continuous Integration: Integrate and test code multiple times a day.

Refactoring: Continuously improve the design of the code without changing its behavior.

Sustainable Pace: Work at a pace that can be sustained indefinitely, avoiding burnout.

On-Site Customer: A real customer is available full-time to answer questions.

## reference

## Quiz

{{ h5p_lumi_embed("quiz1","assets/h5p/quiz1/index.html", base_url="/SWE303") }}
