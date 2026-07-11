# About section


In my project I want to focus on identifying "out of line" shopping behaviour, without predefined knowledge of what is "normal" shopping. 
However, behavior is defined by 2 axis: order cancellation and total shopping experience. I will not try to build regression to assess 
chances of client X to cancel an order, but will try to identify attributes of group(s) of customers who behave not like the others on mentioned 2 axes.
With regard to transaction amount, the point of interest is high value (large sales).

Another point of interest - detect changes in shopping behaviour within given customer. For instance, customer X permanently increasing level of monthly expences.  
Based on my dataset I can't infer the reason for change - but I can attempt to detect the change.

## Primary Objective
Identify customer groups and individual customers whose purchasing behavior differs significantly from the majority of customers.

## Secondary Objective
Explore whether meaningful behavioral changes can be detected within a customer's purchasing history over time.

## Data 
Dataset used for this project is a dataset from Kaggle 'online_retail_II.csv'. I will use only UK-related transactions, because they constitute 94.7% of all transactions.
There are dozens of other countries, but the data outside of UK is insufficient to infer safely about them.

## Business value
Those questions have significant commercial significance. Understanding unusual customer behavior may help businesses identify high-value customers, customer segments associated with frequent cancellations, and emerging changes in purchasing patterns. Such insights could support retention, marketing, and operational decision making.
