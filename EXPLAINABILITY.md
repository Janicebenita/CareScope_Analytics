# CareScope Operations Assistant: Explainability

## Decision and reasoning

The intended decision is which simulated hospital operations signal should be brought to a human reviewer's attention and why. The reasoning may compare patient load, appointment activity, bed occupancy, staff availability, or resource utilization with the values and thresholds represented in CareScope, while keeping simulated forecasts separate from current mock observations. The existing repository is a frontend dashboard; a reproducible agent execution path must still be implemented and demonstrated before claiming that these reviews run autonomously.

## Inputs and data sources

Inputs are a user's operational review request and the local typed mock data contained in the CareScope Analytics frontend. The available data describes fictional patients, clinicians, appointments, diagnostics, departments, forecasts, beds, oxygen, ventilators, blood-bank inventory, ambulances, and activity records. No external API, database, authentication service, electronic health record, or live hospital system supplies the information.

## Limits and known constraints

The primary limitation is that all people, clinical records, forecasts, laboratory values, and operational metrics are fictional demonstration data. Forecasts are simulated rather than validated predictive models, and threshold indicators cannot establish patient risk, clinical urgency, or the correct allocation of real resources. CareScope is not a medical device and must not be used for diagnosis, treatment, triage, or real clinical operations. Any future use with real data would require security, privacy, validation, governance, access control, and authorized human oversight.
