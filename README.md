# Customer-Churn-Prediction

![image](https://github.com/arju10/Customer-Churn-Prediction/assets/52301135/affdf037-6c87-42aa-b6e2-617fc9b18a75)

<br/>
<br/>

![image](https://github.com/arju10/Customer-Churn-Prediction/assets/52301135/4f0f9825-fa47-4b39-b62a-5dea03c2dfb4)


<hr/>
**Dataset Columns **
<br/>
The dataset comprises the following columns:<br/>

**CustomerID:** A unique identifier assigned to each customer. <br/>
**Name:** The name of the customer. <br/>
**Age:** The age of the customer.<br/>
**Gender:** The gender of the customer, categorized as male or female.<br/>
**Location:** The geographical location associated with the customer.<br/>
**Subscription_Length_Months:** The length of the customer's subscription in months.<br/>
**Monthly_Bill:** The monthly bill amount associated with the customer's subscription.<br/>
**Total_Usage_GB:** The total usage in gigabytes (GB) by the customer.<br/>
**Churn:** The target variable indicating whether the customer has churned (1) or not (0).<br/>

<hr/>

**Sample Data Entry** <br/>
Here is a sample data entry from the dataset:<br/>

**Age:** 63<br/>
**Gender:** 1<br/>
**Location:** 3<br/>
**Subscription_Length_Months:** 17<br/>
**Monthly_Bill:** 73.36<br/>
**Total_Usage_GB:** 236<br/>

<hr/>

**Data Preprocessing**<br/>
Upon loading the dataset named "customer_churn_large_dataset.xlsx," I performed an initial assessment of its characteristics using the .info() and .describe() methods. Identifying and handling missing data is crucial, and I accomplished this by using .isnull().sum() to identify the extent of missing values. To ensure data quality, I calculated the Interquartile Range (IQR) and removed any outliers.


<hr/>

**Feature Engineering** <br/>
Categorical variables like "Gender" and "Location" were encoded into numerical values using LabelEncoder. This transformation enables the integration of categorical data into machine learning models.

<hr/>

**Model Building**  <br/>
I divided the data into training and testing sets using train_test_split. Standardization of features was carried out with StandardScaler to ensure uniform scaling. I then trained and evaluated three machine learning models:

**Logistic Regression:** A baseline model known for its interpretability.  <br/>
**Random Forest Classifier:** A versatile ensemble model capable of handling non-linear relationships. <br/>
**Neural Network (MLPClassifier):** A deep learning model for capturing intricate patterns. <br/>
Performance metrics such as accuracy, precision, recall, and F1-score were calculated for each model using established metrics from the scikit-learn library. <br/>

<hr/>

**Best Model Selection** <br/>
The model with the highest F1-score was identified as the best model. The F1-score is particularly relevant for imbalanced datasets like ours, as it balances precision and recall. <br/>

<hr/>

**Model Deployment with Flask**  <br/>
To make the model accessible and usable, I deployed it using the Flask web framework. Users can input customer data through a user-friendly web form, and the deployed model predicts whether a customer will churn or not. The Flask app processes the input, invokes the model, and displays the prediction results on the web page.
