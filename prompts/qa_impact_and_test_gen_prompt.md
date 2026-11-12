# QA Impact Analysis & Test Matrix Prompt Template

Analyze the provided User Story and Acceptance Criteria. Act as a Senior QA Architect and output:

1. **Blast Radius & Dependency Map:**
   - Primary module/object impacted
   - Downstream UI flows, automated workflows/triggers, and API endpoints at risk
   - Role/Permission matrix impacts

2. **Structured Test Scenario Matrix (Markdown Table):**
   - Columns: `Test ID` | `Category (Positive/Negative/Boundary/Security)` | `User Role` | `Preconditions` | `Steps` | `Expected UI & Backend Result`

3. **Automation Candidates:**
   - Highlight top P1 scenarios suitable for Playwright UI + API verification with resilient locator recommendations (`get_by_role`, `get_by_label`, `data-testid`).
