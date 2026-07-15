# Project Journal

## 2026-07-11

### Course Understanding

Reviewed project lectures and proposal-review lectures.

Key insight:

Project evaluation emphasizes:

- clarity,
- feasibility,
- value,
- evaluation planning,
- analytical reasoning.

Not necessarily novelty or research contribution.

---

### Dataset Investigation

Explored multiple candidate datasets.

Candidates considered:

- Online Retail II
- NASA IMS Bearings
- SWaT

Decision:

Proceed with Online Retail II.

Reasoning:

- Dataset immediately available.
- Strong fit with course scope.
- Easier to explain and evaluate.
- Lower preprocessing burden.
- High probability of successful completion.

NASA IMS Bearings was considered highly interesting but likely too large in scope for the course timeline.

---

### Initial EDA Findings

Observations:

- Majority of transactions are UK-based.
- Large number of guest customers with missing customer IDs.
- Strong temporal patterns visible across hours, days, and months.
- Product popularity distribution appears highly skewed.
- Cancellation information is available through invoice identifiers.

Decision:

Restrict analysis to UK transactions.

---

### Current Project Direction

Working Project Idea:

Discovering and Characterizing Unusual Customer Purchasing Behavior in Online Retail Transactions.

Primary Objective:

Identify customers whose purchasing behavior differs significantly from the majority of customers.

Potential dimensions:

- cancellation behavior,
- spending behavior,
- purchasing patterns.

Secondary Objective:

Explore whether meaningful behavioral changes can be detected within a customer's purchase history over time.

Business Motivation:

Understanding unusual customer behavior may help businesses identify high-value customers, segments associated with frequent cancellations, and emerging changes in purchasing patterns.

---

### Open Questions

1. What customer-level features should be created?
2. How should customer behavior be represented?
3. What anomaly types should be considered most important?
4. What evaluation strategy best fits the project?