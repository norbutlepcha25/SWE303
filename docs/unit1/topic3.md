# 1.3 Project management methodologies

While the previous unit (SDLC Models) focused on the development process, this unit focuses on the management process. A methodology is a system of practices, techniques, procedures, and rules used by those who work in a discipline. We explore two primary paradigms: the comprehensive, process-oriented standard of PMBOK and the scalable, enterprise-level Agile frameworks.

Understanding these methodologies is crucial for a Project Manager to establish the "rules of the game" for a project or an entire organization. The choice between a process-centric approach and a lean-agile approach, or a blend of both, fundamentally shapes governance, reporting, team structure, and ultimately, project success.

## 1.3.1 PMBOK (Project Management Body of Knowledge)

The PMBOK Guide, published by the Project Management Institute (PMI), is not a methodology per se, but a standards framework that describes established norms, methods, processes, and practices for project management. It is a comprehensive body of knowledge that can be tailored to create a methodology.

## 1.3.1.1 Overview of PMBOK processes

The PMBOK Guide structures project management through a set of processes grouped into two dimensions: Process Groups and Knowledge Areas.

Process Groups represent the chronological flow of a project (Initiating, Planning, Executing, Monitoring & Controlling, Closing).

Knowledge Areas represent the specialist domains of project management (Integration, Scope, Schedule, Cost, Quality, etc.).

Each process is defined by its:

Inputs: Documents, plans, or information required to start the process.

Tools & Techniques: Mechanisms applied to the inputs.

Outputs: Documents, products, or decisions resulting from the process.

For example, the "Develop Schedule" process (in the Schedule Management Knowledge Area) takes inputs like the WBS and activity list, uses techniques like the Critical Path Method (CPM), and produces the Project Schedule as an output.

## 1.3.1.2 Tailoring PMBOK for software projects

Blindly applying all PMBOK processes can lead to excessive bureaucracy in software projects. Tailoring is the deliberate adaptation of the project management approach, governance, and processes to make them more suitable for the given environment.

How to Tailor PMBOK for Software:

Emphasize Certain Knowledge Areas:

Scope & Requirements Management: Use Agile artifacts (User Stories, Backlogs) instead of, or in addition to, a formal SRS.

Quality Management: Integrate agile technical practices like Test-Driven Development (TDD), Continuous Integration, and automated testing into the quality processes.

Risk Management: Incorporate risk review into sprint retrospectives and daily stand-ups.

Stakeholder Management: Leverage agile ceremonies like Sprint Reviews and Demo for continuous engagement.

Simplify Documentation: Replace lengthy documents with "working software." A product backlog can serve as the living scope document. A burndown chart can be a key performance report.

Adapt Process Groups to an Iterative Cycle: The five process groups are still relevant but are applied iteratively within each sprint or development cycle, not just once for the entire project.

## 1.3.1.3 PMBOK process groups and their interactions

The five Process Groups are not one-time phases; they are overlapping sets of activities that occur at varying levels of intensity throughout the project.

Initiating Process Group: Defines and authorizes the project or a project phase. Key Output: Project Charter.

Planning Process Group: Establishes the project scope, refines objectives, and defines the course of action. Key Output: Project Management Plan.

Executing Process Group: Completes the work defined in the project management plan. Key Output: Deliverables.

Monitoring and Controlling Process Group: Tracks, reviews, and regulates the progress and performance of the project; identifies changes required. Key Output: Change Requests, Performance Reports.

Closing Process Group: Formalizes completion and closes the project or phase. Key Output: Final Product, Lessons Learned.

Interactions: These groups are iterative and interconnected. For example, during Execution (Process Group 3), the results of the work may necessitate a change request. This triggers Monitoring & Controlling (Process Group 4) to evaluate the change, which then loops back into replanning (Process Group 2) if the change is approved, before returning to execution.

## 1.3.2 Agile project management frameworks

While Scrum and Kanban manage work at the team level, large enterprises require frameworks to coordinate Agile practices across multiple teams, portfolios, and the entire organization. These are known as Scaled Agile Frameworks.

## 1.3.2.1 Scaled Agile Framework (SAFe): levels and core values

SAFe is a knowledge base of integrated patterns for achieving enterprise-scale Lean-Agile development. It provides a structured approach to scaling agile across the organization.

Core Values:

Alignment: Ensuring all teams are working towards a common mission.

Built-in Quality: Ensuring every increment reflects quality standards.

Transparency: Making progress, status, and issues visible at all levels.

Program Execution: Focusing on the working, integrated systems that deliver value.

Four Configurations (Levels):

Essential SAFe: The basic building block, consisting of:

Team Level: 5-12 Agile Teams using Scrum/Kanban/XP.

Program Level: Teams are organized into an Agile Release Train (ART), a long-lived team of teams that plans, commits, and executes together in a series of Program Increments (PIs).

Large Solution SAFe: For building large and complex solutions that require multiple ARTs and suppliers.

Portfolio SAFe: Aligns strategy with execution by organizing development around the flow of value via one or more Value Streams.

Full SAFe: The most comprehensive configuration, encompassing all other levels.

## 1.3.2.2 Large-Scale Scrum (LeSS): principles and rules

LeSS is a framework for scaling Scrum to multiple teams, built on the principles of simplicity, empiricism, and whole-product focus. It aims to extend Scrum with minimal additional rules.

Principles:

Empirical Process Control: Transparency, Inspection, and Adaptation at scale.

Lean Thinking: Focus on eliminating waste and maximizing value delivery.

Systems Thinking: Focusing on the entire system and product, not just individual team output.

Whole-Product Focus: All teams share one single Product Backlog and one Potentially Shippable Product Increment at the end of each sprint.

Two Frameworks:

LeSS: For 2-8 teams. Involves one Product Owner, one Product Backlog, and one Sprint across all teams with a common Sprint Review and Retrospective.

LeSS Huge: For 8+ teams. Adds the role of Area Product Owner to help manage requirement areas within a single, massive product backlog.

## 1.3.2.3 Disciplined Agile Delivery (DAD): phases and decision points

DAD is a hybrid, process-decision framework that provides a foundation for scaling agile. It shows how all other agile, lean, and traditional practices fit together in a tailorable, learning-oriented lifecycle.

A Hybrid Approach: DAD explicitly incorporates strategies from Scrum, XP, Kanban, Lean, and traditional PMBOK, guiding teams to choose the right approach for their context.

Three Phases (Goal-Driven, not Prescriptive):

Inception (Phase 1): Goals include securing initial funding, forming the team, establishing a shared vision, and aligning with stakeholder goals. It addresses the "fuzzy front end" that many pure agile methods gloss over.

Construction (Phase 2): Goals include producing a consumable solution, achieving high quality, and engaging stakeholders. This is the iterative and incremental development phase, similar to Scrum Sprints.

Transition (Phase 3): Goals include ensuring the solution is usable and viable, and deploying the solution into production.

Decision Points: The core of DAD is its focus on making conscious choices about your Way of Working (WoW). It provides guidance on decisions such as: How formal should our architecture be? How should we model? How should we test? This makes DAD a process toolkit rather than a single methodology.

## Test Yourself

## Reference
