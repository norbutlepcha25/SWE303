# 3.1 Time management

Time management involves the processes required to manage the timely completion of the project, focusing on activity definition, sequencing, duration estimating, and schedule development.

## 3.1.1 Activity definition and sequencing

## 3.1.1.1 Identifying project activities from the WBS

The process of decomposing Work Breakdown Structure (WBS) work packages into smaller, more manageable activities for estimation and scheduling.

Key Input: WBS and WBS Dictionary

Technique: Decomposition

Output: Activity List

PMBOK Reference: Process 6.2 - Define Activities

Software Context: Activities might include "Develop User Authentication Module," "Write Unit Tests for Payment API," or "Conduct Security Penetration Testing."

## 3.1.1.2 Creating network diagrams: Activity-On-Arrow(AOA) and Activity-On-Node(AON)

Activity-On-Node (AON)/Precedence Diagramming Method (PDM):

Description: Nodes represent activities, and arrows show dependencies (Most common in software projects)

Dependency Types: Finish-to-Start (FS), Start-to-Start (SS), Finish-to-Finish (FF), Start-to-Finish (SF)

Activity-On-Arrow (AOA)/Arrow Diagramming Method (ADM):

Description: Arrows represent activities, and nodes represent events (milestones)

PMBOK Reference: Process 6.3 - Sequence Activities

## 3.1.1.3 Determining dependencies between activities

Mandatory Dependencies (Hard Logic): Inherent in the nature of the work (e.g., test after coding)

Discretionary Dependencies (Soft Logic): Based on best practices or preferred sequence

External Dependencies: Relationships to non-project activities (e.g., delivery of third-party components)

Resource Dependencies: Based on availability of specific resources

## 3.1.2 Estimating activity durations

Analogous Estimating (Top-Down):

Description: Uses historical data from similar projects

When to Use: Early phases, when limited information available

Accuracy: Low to medium (-25% to +75%)

Parametric Estimating:

Description: Uses statistical relationship between historical data and other variables

Software Example: Cost per function point, story points based on velocity

Three-Point Estimating (PERT):

Formula: (Optimistic + 4×Most Likely + Pessimistic) ÷ 6

Benefit: Accounts for uncertainty and risk

PMBOK Reference: Process 6.4 - Estimate Activity Durations

## 3.1.2.1 Estimation techniques: analogous, parametric, and three-point

## 3.1.2.2 Dealing with estimation uncertainty in software projects

Use of Contingency Time: Adding buffers for known uncertainties

Progressive Elaboration: Refining estimates as more information becomes available

Reference Class Forecasting: Using data from completed similar projects

Agile Approach: Using velocity and iterative planning to improve accuracy over time

## 3.1.2.3 Using historical data for more accurate estimates

Organizational Process Assets: Past project records, lessons learned

Metrics: Team velocity, defect rates, productivity measures

Tools: Estimation databases, project management software historical data

## 3.1.3 Developing and optimizing the project schedule

## 3.1.3.1 Critical Path Method (CPM)

Definition: The sequence of activities that represents the longest path through the project, determining the shortest possible duration

Key Terms:

Critical Path: Longest duration path with zero float

Float/Slack: Amount of time an activity can be delayed without delaying project

Forward/Backward Pass: Calculation methods for determining early/late start and finish dates

PMBOK Reference: Process 6.5 - Develop Schedule

## 3.1.3.2 Resource leveling and fast tracking

Resource Leveling:

Purpose: Address resource over-allocation by adjusting schedule

Effect: Often extends project duration

Fast Tracking:

Description: Performing activities in parallel that would normally be sequential

Risk: Increases rework risk

Crashing: Adding resources to critical path activities to shorten duration (increases cost)

## 3.1.3.3 Using Gantt charts for schedule visualization

Purpose: Bar chart showing activities against calendar timeline

Benefits: Visual progress tracking, easy to understand for stakeholders

Tools: Microsoft Project, Jira, Asana, Monday.com

Modern Usage: Often integrated with agile boards and burn-down charts

## reference

## Test Your self
