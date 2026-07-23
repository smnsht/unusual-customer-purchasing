# Abstract
This project investigates unusual customer purchasing behavior in UK online retail transactions. Using an invoice-level dataset that combines each transaction's own features with aggregated customer-level behavior, I discover and characterize behavioral segments, then identify the transactions and customers that do not fit well into any of them — without assuming in advance what "normal" shopping looks like. Cancellation behavior and order total are treated as the main axes of interest. This is not a predictive-modelling exercise, and clustering itself is a means to that end rather than the goal.


## 1. Introduction

Understanding unusual customer behavior has significant commercial value: it may help businesses identify high-value customers, customer segments associated with frequent cancellations, and emerging changes in purchasing patterns, supporting retention, marketing, and operational decision-making.

The dataset used for this project is `online_retail_II.csv` from Kaggle: a transaction-level log of online retail orders spanning December 2009 to December 2011, with roughly 1.07 million line-item rows across 43 countries. I will use only UK-related transactions, because they constitute 94.7% of all transactions; there are dozens of other countries, but the data outside the UK is insufficient to draw safe inferences about them.

About a quarter of the UK rows have no associated `Customer ID` — these are guest/unregistered purchases, and they are dropped, since customer-level behavior cannot be attributed to them. After restricting to UK transactions with a known customer, roughly 741,000 transaction rows remain, aggregating to about 40,500 invoices from roughly 5,400 distinct customers.

The unit of analysis is the individual invoice, described by both transaction-level features and aggregated customer-level features. A customer may therefore contribute typical invoices to a segment while a few of their extreme invoices are flagged as outliers — their routine behavior clusters normally, while individual atypical transactions stand apart.

In this work I will **not** try to build a regression model to assess the chance of a customer cancelling an order, or to predict the shopping basket for a given customer, **nor** merely to split transactions into clusters as an end in itself.

In this project I want to discover and characterize behavioral segments, then identify transactions and customers **that do not** fit well into any segment, without predefined knowledge of what is "normal" shopping, and trace those outliers back to the customers who produced them. I recognize cancellation behaviour and order total as the main axes of interest.
For instance, if we discover 3 well-defined clusters, we will try to answer the question: "Which transactions and customers do not fit any of those groups?"


## 2. Related Work

1. [Customer Segmentation & Retention Strategy using Transactional Data](https://www.kaggle.com/code/sachinegunjal/customer-segmentation-retention-analysis) - An end-to-end segmentation and retention pipeline on transactional data, identifying high-value and high-risk customer segments and quantifying churn risk via interpretable models. Unlike this project, its segments are the end product, optimized for retention decisions - not a baseline against which to surface behavior that fits no segment.

2. [Online Retail: Cohort Analysis and Other Stories](https://www.kaggle.com/code/olgaluzhetska/online-retail-cohort-analysis-and-other-stories) - Uses the same Online Retail II dataset for descriptive sales analytics: data cleaning, most/least expensive products, sales broken down by country/product/customer, cohort-based retention and average-quantity analysis, and sales trends over time. Unlike this project, it stays descriptive (cohorts and aggregate trends) rather than modelling behavioral segments or flagging customers/transactions that deviate from them.

3. [Customer Segmentation by Enhanced RFM (RFMT)](https://www.kaggle.com/code/adarshcgowda/new-rfmt-model-for-segmentation-1st-in-kaggle) - Extends the traditional RFM (Recency, Frequency, Monetary) model with a fourth dimension, Inter-Purchase Time (T), to capture each customer's dynamic purchasing cycle before segmenting. This project draws on similar timing/frequency signals as engineered features, but segmentation is not the end goal - it is the baseline used to identify customers and invoices that do not fit any RFM(T)-style segment.

4. [Recommendation Systems](https://www.kaggle.com/code/mehmettuzcu/recommendation-systems) - Product recommendations via Association Rule Learning and Collaborative Filtering. Addresses a different question (what a given user/product is likely to want next) rather than characterizing behavioral segments or identifying customers/transactions that deviate from them.


**How this work differs from the existing work:**

There is plenty of work related to retail data. It can largely be divided into three main categories: customer segmentation, prediction tasks (e.g., customer churn, likelihood of cancellation), and recommendation systems.

I chose to do something distinct - something with a deeper affinity to the "Data Mining" discipline itself: intentionally avoiding pure classification, regression, and clustering as an end goal, and instead focusing on discovering unknown patterns and analyzing the data.

## 3. Proposed work

In order to fulfill the objective, my plan is to build the analysis dataset in two stages. First, I will filter out non-UK transactions and guest transactions (those without a CustomerID). Then I will construct a customer-level table of engineered features derived from the available data:
- timing patterns: day of week and hour of shopping, average number of shopping trips per month
- spending patterns: global average, min, max, and std of transaction total amount
- product patterns: global average, min, max, and std of products purchased, and most frequently purchased products
- order cancellation patterns: percentage of cancelled transactions

I will then join this customer-level feature table back onto the invoice-level records, so that each invoice is described by both its own transaction-level features and its customer's aggregated behavior. This joined, invoice-level dataset is the unit of analysis for clustering and outlier detection.

Note on feasibility: one may ask whether there is enough data. As a rough estimate, the number of engineered features is ~50, spread across roughly 40,500 invoices from approximately 5,400 identifiable customers. Given this feature space and sample size, the data appears sufficient for clustering and outlier analysis.

Once the dataset is prepared, we will first explore segmentation using the engineered behavioral features. The resulting groups will be used to characterize common patterns of behavior. We will then identify transactions and customers whose behavior differs significantly from the majority or from the identified segments. Particular attention will be given to spending, purchase composition, and cancellation behavior.

## 4. Evaluation

### 4.1 Evaluation of clustering

We will build a baseline clustering model using KMeans, and use DBSCAN as the working model. For both KMeans and DBSCAN, two distance metrics will be employed:
euclidean and cosine. The planned number of engineered features is ~50. It is hard to predict upfront whether euclidean or cosine distance will yield better clustering, so both will be evaluated.

Note on cosine distance: DBSCAN natively supports cosine as a distance metric. KMeans does not - "cosine KMeans" is approximated by L2-normalizing the feature vectors first and then running standard (euclidean) KMeans on the unit vectors, since euclidean distance between unit vectors ranks the same as cosine distance.

Clustering will be evaluated by silhouette score, stability of the clustering, and interpretability of the obtained clusters and outliers. Important to understand: 
**silhouette score alone** is not supposed to define the model; it is only used in conjunction with the parameters mentioned above. Silhouette score measures how well 
each data point fits into its assigned cluster compared to other clusters. For our research it can mark the direction of optimization, not the best model.
As a strategy, we are looking for a clustering that:
- is stable (does not change strongly as a result of hyper-parameter changes)
- yields 2-3 clusters (it seems not feasible to interpret more than that)
- has a manageable amount of outliers relative to inliers (outliers are the main target of our research)
- produces both outliers and inliers that are interpretable

The KMeans baseline model is not expected to perform best - we will use it as a "quick and cheap" way to do a brief clustering and just obtain a first impression of 
how the data converges into clusters. It's worth mentioning that this algorithm can't serve our research on its own - **it does not produce outliers**, each point is assigned to a cluster.

DBSCAN, in contrast, can produce outliers, and is expected to serve as the "working horse" of our research.

### 4.2 Evaluation of dis-similarity

After obtaining clusters and outliers we have to interpret the results - answer the question "how does cluster A differ from cluster B?", and/or "how are outliers different 
from inliers?". In order to do that, we will compare the two datasets feature by feature, and take the most "different" ones - this will define the answer. But how do we assess
"how different dataset A and dataset B are for a given feature, compared to another feature"? We can look at abs(mean_A(feature) - mean_B(feature)), but absolute numbers alone won't tell us the "size" of how different they are.
If the feature is annual sum of invoices, this mean difference might be of the magnitude of hundreds, and at the same time it could represent only a small difference relative to that feature's natural spread. At the same time,
another feature might be percentage of cancelled transactions - then the mean difference might be less than 1, and at the same time signify a big difference between populations. 

In order to compare "how different" the two datasets are across features measured on very different scales, we will use Cohen's d.

In order to interpret the outliers and clusters, we will take the top 5-10 features with a Cohen's d greater than 0.8 - those will define the population.


## 5. Timeline

- **Week 1:** EDA, preprocessing, and feature engineering
- **Week 2:** Unusual purchasing behavior analysis
- **Week 3:** Report preparation


## 6. Discussion

This section will be updated once all analyses and results have been collected and documented.

## 7. Conclusion

This section will be updated once all analyses and results have been collected and documented.


## 8. References

1. Jolliffe, I. T. (2002). *Principal Component Analysis* (2nd ed.). Springer.
2. [ISLR2, Ch12_Unsupervised_Learning.pdf](https://hastie.su.domains/ISLR2/Slides/Ch12_Unsupervised_Learning.pdf)
3. [scikit-learn.org, silhouette_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_score.html)
4. MacQueen, J. (1967). Some methods for classification and analysis of multivariate observations.
5. scikit-learn User Guide: DBSCAN and parameter sensitivity. https://scikit-learn.org/stable/modules/clustering.html#dbscan
6. Ester, M., Kriegel, H.-P., Sander, J., Xu, X. (1996). *A Density-Based Algorithm for Discovering Clusters in Large Spatial Databases with Noise*.
7. Schubert, E., Sander, J., Ester, M., Kriegel, H.-P., Xu, X. (2017). *DBSCAN Revisited, Revisited: Why and How You Should (Still) Use DBSCAN*.
8. [scikit-learn DBSCAN documentation](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html)
9. Cohen, J. (1988). *Statistical Power Analysis for the Behavioral Sciences* (2nd ed.). Lawrence Erlbaum.
10. Li, Z., Zhu, Y., & van Leeuwen, M. (2023). A Survey on Explainable Anomaly Detection. *ACM Transactions on Knowledge Discovery from Data*. arXiv:2210.06959.
