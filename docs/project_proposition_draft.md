# About section
This is a project about discovering unusual customer purchasing behavior based on shopping transactions.
The dataset used for this project is 'online_retail_II.csv' from Kaggle. I will use only UK-related transactions, because they constitute 94.7% of all transactions.
There are dozens of other countries, but the data outside the UK is insufficient to draw safe inferences about them.

The unit of analysis is the individual invoice, described by both transaction-level features and aggregated customer-level features. A customer may therefore contribute typical invoices to a segment while a few of their extreme invoices are flagged as outliers — their routine behavior clusters normally, while individual atypical transactions stand apart.

In this work I will **not** try to build a regression model to assess the chance of a customer cancelling an order, or to predict the shopping basket for a given customer, **nor** merely to split transactions into clusters as an end in itself.

In this project I want to discover and characterize behavioral segments, then identify transactions and customers **that do not** fit well into any segment, without predefined knowledge of what is "normal" shopping. I recognize cancellation behaviour and order total as the main axes of interest.
For instance, if we discover 3 well-defined clusters, we will try to answer the question: "Which transactions and customers do not fit any of those groups?"


## Objective
Identify and characterize purchasing behavior that differs substantially from the behavior observed in the major segments, and trace those outliers back to the customers who produced them.


## Business value
These questions have significant commercial value. Understanding unusual customer behavior may help businesses identify high-value customers, customer segments associated with frequent cancellations, and emerging changes in purchasing patterns. Such insights could support retention, marketing, and operational decision-making.


## Proposed work
In order to fulfill the objective, my plan is to build the analysis dataset in two stages. First, I will filter out non-UK transactions and guest transactions (those without a CustomerID). Then I will construct a customer-level table of engineered features derived from the available data:
- timing patterns: day of week and hour of shopping, average number of shopping trips per month
- spending patterns: global average, min, max, and std of transaction total amount
- product patterns: global average, min, max, and std of products purchased, and most frequently purchased products
- order cancellation patterns: percentage of cancelled transactions

I will then join this customer-level feature table back onto the invoice-level records, so that each invoice is described by both its own transaction-level features and its customer's aggregated behavior. This joined, invoice-level dataset is the unit of analysis for clustering and outlier detection.

Note on feasibility: one may ask whether there is enough data. As a rough estimate, the number of engineered features is ~50, spread across hundreds of thousands of invoices from approximately 6,000 identifiable customers. Given this feature space and sample size, the data appears sufficient for clustering and outlier analysis.

Once the dataset is prepared, we will first explore segmentation using the engineered behavioral features. The resulting groups will be used to characterize common patterns of behavior. We will then identify transactions and customers whose behavior differs significantly from the majority or from the identified segments. Particular attention will be given to spending, purchase composition, and cancellation behavior.