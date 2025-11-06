<figure markdown="span">
    ![RBS](img/risk_mgt/4quatitativeanalysis.png){width="80%"}
    <figcaption>Quantitative Analysis: Input, tools and output</figcaption>
    <p align='right' style="font-size:0.8em"><i>Image Source: PMBOK 6th Edition, chapter 11</i></p>
</figure>

<!-- reference linked refence  -->
<figure markdown="span">
    ![RBS](img/risk_mgt/PImatrix.webp){width="60%"}
    <figcaption>Perform Qualitative analysis: Input, tools and output</figcaption>
    <p align='right' style="font-size:0.8em"><i>Image Source: <a href="https://www.rosemet.com/qualitative-risk-analysis/"> Project Management Training</a ></i></p>
</figure>

---

### ⚡ Efficiency Tip

making notes template

<!-- cp docs/template/template.md docs/unit1/topic3.md  -->

<span class="tooltip" data-tooltip="This is a styled tooltip">Hover over me</span>

<span class="tooltip-box">Sorting Algorithm
<span class="tooltip-content">
<strong>Definition:</strong> {{ project }}<br>
<em>Example:</em> Quicksort, Merge Sort.<br>
<a href="sorting.md">Read more →</a>
</span>
</span>
<button onclick="window.print()">🖨️ Print PDF</button>

<!-- Table -->

<style>
.table_component {
    overflow: auto;
    width: 100%;
}

.table_component table {
    border: 1px solid #000000;
    height: 100%;
    width: 100%;
    table-layout: fixed;
    border-collapse: collapse;
    border-spacing: 1px;
    text-align: left;
}

.table_component caption {
    caption-side: bottom;
    text-align: center;
}

.table_component th {
    border: 1px solid #000000;
    background-color: #0b5a8e;
    color: #ffffff;
    padding: 5px;
}

.table_component td {
    border: 1px solid #000000;
    padding: 5px;
}

.table_component tr:nth-child(even) td {
    background-color: #f07575;
    color: #000000;
}

.table_component tr:nth-child(odd) td {
    background-color: #ffffff;
    color: #000000;
}
</style>
<div class="table_component" role="region" tabindex="0">
<table>
    <caption>Table 1</caption>
    <thead>
        <tr>
            <th>Header 1</th>
            <th>Header 2</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td></td>
            <td></td>
        </tr>
    </tbody>
</table>
<div style="margin-top:8px">Made with <a href="https://www.htmltables.io/" target="_blank">HTML Tables</a></div>
</div>

<!-- size medium -->

{{ image_block("img/risk_mgt/PImatrix.webp", "RBS", "Perform Qualitative analysis: Input, tools and output", "Project Management Training", "https://www.rosemet.com/qualitative-risk-analysis/") }}

<!-- size: small -->

{{ image_block("img/example.webp", "Chart", "Risk comparison chart", "DataViz", "https://dataviz.com", size="small") }}

<!-- custome size -->

{{ image_block("img/custom.webp", "Custom", "Custom width example", "Docs", "https://example.com", width="75%") }}

<div class="custom-table-container">
  <table class="custom-table">
    <thead>
      <tr>
        <th>Area</th>
        <th>Advantage</th>
        <th>Disadvantage</th>
      </tr>
    </thead>
    <tbody>
      <tr>
      <td>Simple and Easy to Understand:</td>
        <td> Phases are logical and easy for management and stakeholders to grasp</td>
        <td>Inflexible to Change: It is difficult and expensive to go back and change requirements once a phase is complete</td>
      </tr>
      <tr>
      <td>Milestones and Deliverables</td>
        <td>Each phase has well-defined outputs, making progress easy to track.</td>
        <td>Late Delivery of Working Software: The customer does not see a working product until very late in the lifecycle</td>
      </tr>
      <tr>
      <td>Well-Suited for Stable Requirements</td>
        <td>Works well when requirements are well-understood and unlikely to change.</td>
        <td> Major risks (e.g., misunderstood requirements, technical feasibility) are often discovered only during testing.</td>
      </tr>
      <tr>
      <td>Easier Management and Control:</td>
        <td>The structured nature makes it easier to manage tasks, budgets, and schedules.</td>
        <td>Testing is a Bottleneck: Testing is relegated to the end, leading to potential schedule overruns if many defects are found.</td>
      </tr>
    </tbody>
  </table>
</div>
