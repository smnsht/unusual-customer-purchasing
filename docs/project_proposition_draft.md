# About section
This is a project about discovering unusual customer purchasing behavior based on shopping transactions.
The dataset used for this project is 'online_retail_II.csv' from Kaggle. I will use only UK-related transactions, because they constitute 94.7% of all transactions.
There are dozens of other countries, but the data outside the UK is insufficient to draw safe inferences about them.

The unit of analysis is the individual invoice, described by both transaction-level features and aggregated customer-level features. A customer may therefore contribute typical invoices to a segment while a few of their extreme invoices are flagged as outliers — their routine behavior clusters normally, while individual atypical transactions stand apart.

In this work I will **not** try to build a regression model to assess the chance of client X cancelling an order, or to predict the shopping basket for a given client, **nor** merely to split transactions into clusters as an end in itself.

In this project I want to discover and characterize behavioral segments, then identify transactions and customers **that do not** fit well into any segment, without predefined knowledge of what is "normal" shopping. However, I recognize cancellation behaviour and order total as the main axes of interest.
For instance, if we discover 3 well-defined clusters, we will try to answer the question: "Which transactions and customers do not fit any of those groups?"


## Primary Objective
Identify and characterize purchasing behavior that differs substantially from the behavior observed in the major segments, and trace those outliers back to the customers who produced them.

## Secondary Objective
Explore whether meaningful behavioral changes can be detected within a customer's purchasing history over time.
For example, a customer may exhibit a sudden increase in monthly spending or a significant shift in purchase composition.
While the dataset does not allow us to determine the reason for such changes, it does allow us to detect and characterize them.


## Business value
These questions have significant commercial value. Understanding unusual customer behavior may help businesses identify high-value customers, customer segments associated with frequent cancellations, and emerging changes in purchasing patterns. Such insights could support retention, marketing, and operational decision-making.


## Proposed work
In order to fullfill the primary objective my plan is to build new dataset, customer-centered. I will filter out non-UK transactions, and I will filter out
guiest transactions (transactions without CustomerID). This new dataset will contain enginered features, based on available data: 
- timing patterns: day of week and hours when shopping, shoppings agerage per month
- spending patterns: global average, min, max, and std of transactions total sum
- product patterns: global average, min, max and std of products purchased, most frequently purchased products
- order cancellation patterns: percentage of cancelled transactions

Note of feasibilty of anylisys: the question might arize if we have enouth data. Fast and rough evaluation: estimated number of engineered features ~ 50.
The dataset contains approximately 6,000 identifiable customers. Given the expected feature space, this appears sufficient for clustering and outlier analysis.


When the customer-centered dataset is prepared, we will first explore customer segmentation using engineered behavioral features.

The resulting customer groups will be used to characterize common patterns of behavior.

We will then identify customers whose behavior significantly differs from the majority of customers or from the identified customer segments.

Particular attention will be given to spending, purchase composition, timing patterns, and cancellation behavior.

In order to fullfill the secondary objective, we will need to analize customers behaviour on temporal axis: instead of global metrics we will employ monthly metrics.
This will allow to answer questions as:
- customer X suddenly tripples level of monthly expences
- customer Y suddenly changes his busket