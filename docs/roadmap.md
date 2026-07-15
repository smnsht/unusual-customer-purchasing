### To avoid:

1. Customer segmentation with RFM + K-Means.
    - Why? Because thousands of people have done it already.

2. Basic sales forecasting.
    - Why? Becomes a standard prediction project.

### To do

1. Customer Anomaly Detection

- Question: Which customers exhibit unusual purchasing behavior?

Examples:

- sudden spending spikes
- unusual product combinations
- abrupt purchasing pattern changes
- reseller-like behavior

Techniques:

- Isolation Forest
- LOF
- DBSCAN
- Autoencoders



### Project Idea B — Temporal Cluster Evolution
Question:

How do customer segments evolve over time?

Most clustering projects create clusters once.
A more interesting question is:

cluster customers monthly
observe migration between clusters
identify transition patterns


### Project Idea C — Product Association + Anomaly Discovery
Question:

Which baskets violate established purchasing patterns?

Step 1:

discover frequent itemsets

Step 2:

identify baskets that look unusual

This combines:

pattern mining
knowledge discovery
anomaly detection


### Project Idea D — Unusual Customer Journey Detection
Question:

Can we discover rare but valuable customer trajectories?

Example:
New customer
→ small purchases
→ high-value purchases
→ wholesale behavior

vs
New customer
→ 1 purchase
→ disappear

This becomes sequential pattern mining.