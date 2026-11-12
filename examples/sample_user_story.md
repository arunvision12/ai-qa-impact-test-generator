## Story: Enforce Minimum Annual Revenue Before Lead Conversion
**As a** Sales Representative,  
**I want** the system to validate that `Annual Revenue` is populated and greater than $10,000 before converting a Qualified Lead into an Opportunity,  
**So that** downstream pipeline forecasting remains accurate.

### Acceptance Criteria
1. Standard Sales Rep users cannot convert a Lead if `Annual Revenue` is null or <= $10,000; an inline validation message must appear.
2. Sales Operations Admin users retain override permission to convert Leads regardless of `Annual Revenue`.
3. Upon successful conversion, an Opportunity record is created via API with `Stage = Prospecting` and `Amount` mapped from `Annual Revenue`.
### Blast Radius Report
- **Primary Module:** Lead Management UI & Lead Conversion Modal
- **Downstream Impacts:** Opportunity Creation Trigger/Flow, Pipeline Forecast Reports, `/api/v1/leads/{id}/convert` endpoint
- **High-Risk Regression Areas:** Bulk lead conversion, API-level bypass of UI validation rules, permission-set overrides

### Generated Test Scenarios
| Test ID | Category | User Role | Scenario | Expected Result |
| :--- | :--- | :--- | :--- | :--- |
| TC-01 | Positive | Sales Rep | Convert Lead with `Annual Revenue = 50000` | Conversion succeeds; Opportunity created with `Stage = Prospecting` & `Amount = 50000` |
| TC-02 | Negative | Sales Rep | Attempt conversion with `Annual Revenue = null` | Blocked with inline error; no Opportunity record inserted in DB |
| TC-03 | Boundary | Sales Rep | Attempt conversion with `Annual Revenue = 10000` | Blocked (strictly `> 10000` required) |
| TC-04 | Permission | Sales Ops Admin | Convert Lead with `Annual Revenue = 5000` | Override allowed; Lead converts cleanly |
| TC-05 | API Negative | Sales Rep Token | `POST /api/v1/leads/{id}/convert` with revenue `5000` | Returns `422 Unprocessable Entity` with validation error payload |
