## Story: Enforce Minimum Annual Revenue Before Lead Conversion
**As a** Sales Representative,  
**I want** the system to validate that `Annual Revenue` is populated and greater than $10,000 before converting a Qualified Lead into an Opportunity,  
**So that** downstream pipeline forecasting remains accurate.

### Acceptance Criteria
1. Standard Sales Rep users cannot convert a Lead if `Annual Revenue` is null or <= $10,000; an inline validation message must appear.
2. Sales Operations Admin users retain override permission to convert Leads regardless of `Annual Revenue`.
3. Upon successful conversion, an Opportunity record is created via API with `Stage = Prospecting` and `Amount` mapped from `Annual Revenue`.
