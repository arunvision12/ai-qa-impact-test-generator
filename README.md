# AI-Powered QA Impact Analysis & Automated Test Scenario Generator

An AI-assisted QA engineering workflow using **Kiro** and **Playwright (Python)** to parse Agile user stories, map dependency blast radiuses across enterprise web/CRM modules, and generate structured functional, negative, and API test scenarios.

## Problem Statement
In fast-paced Agile sprints, manual user story breakdown and regression scope estimation often miss downstream dependencies (such as role-based permissions, validation rules, and API payload regressions) while consuming significant test design time.

## Solution Architecture
1. **User Story & Acceptance Criteria Parsing:** Structured prompt engineering guides Kiro to extract actors, permissions, state transitions, and boundary conditions.
2. **Blast Radius Mapping:** Identifies directly modified modules, upstream/downstream integrations, and high-risk regression zones.
3. **Multi-Layer Test Matrix Generation:** Produces a Requirement Traceability Matrix (RTM) covering positive, negative, boundary, and role-based scenarios.
4. **Automated Test Scaffolding & Stabilization:** Generates runnable Playwright UI and API validation scripts with resilient locators and explicit state assertions.

## Tech Stack
- **AI Workflow:** Kiro (Agentic AI IDE & Spec-Driven Prompting)
- **Automation & Validation:** Python, Playwright, Pytest, REST API / SQL Assertions
- **Test Management:** Markdown / CSV RTM Exports (Jira-compatible)

## Repository Contents
- `prompts/qa_impact_and_test_gen_prompt.md` — Reusable spec prompt for impact analysis and test generation.
- `examples/sample_user_story.md` — Anonymized enterprise CRM user story input.
- `examples/generated_test_matrix.md` — AI-generated blast radius report and test matrix output.
- `automation/test_lead_conversion_flow.py` — Sample Playwright test suite generated and stabilized from the test matrix.

## Key Outcomes
- Standardized edge-case and permission-boundary coverage across sprint stories.
- Accelerated test design and flaky locator stabilization during regression cycles.
