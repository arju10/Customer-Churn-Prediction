# Customer-Churn-Prediction

**Dataset Columns**
The dataset comprises the following columns:

**CustomerID:** A unique identifier assigned to each customer.
**Name:** The name of the customer.
**Age:** The age of the customer.
**Gender:** The gender of the customer, categorized as male or female.
**Location:** The geographical location associated with the customer.
**Subscription_Length_Months:** The length of the customer's subscription in months.
**Monthly_Bill:** The monthly bill amount associated with the customer's subscription.
**Total_Usage_GB:** The total usage in gigabytes (GB) by the customer.
**Churn:** The target variable indicating whether the customer has churned (1) or not (0).

**Sample Data Entry**
Here is a sample data entry from the dataset:

**Age:** 63
**Gender:** 1
**Location:** 3
**Subscription_Length_Months:** 17
**Monthly_Bill:** 73.36
**Total_Usage_GB:** 236


**Data Preprocessing**
Upon loading the dataset named "customer_churn_large_dataset.xlsx," I performed an initial assessment of its characteristics using the .info() and .describe() methods. Identifying and handling missing data is crucial, and I accomplished this by using .isnull().sum() to identify the extent of missing values. To ensure data quality, I calculated the Interquartile Range (IQR) and removed any outliers.

Feature Engineering
Categorical variables like "Gender" and "Location" were encoded into numerical values using LabelEncoder. This transformation enables the integration of categorical data into machine learning models.

**Model Building**
I divided the data into training and testing sets using train_test_split. Standardization of features was carried out with StandardScaler to ensure uniform scaling. I then trained and evaluated three machine learning models:

**Logistic Regression:** A baseline model known for its interpretability.
**Random Forest Classifier:** A versatile ensemble model capable of handling non-linear relationships.
**Neural Network (MLPClassifier):** A deep learning model for capturing intricate patterns.
Performance metrics such as accuracy, precision, recall, and F1-score were calculated for each model using established metrics from the scikit-learn library.

**Best Model Selection**
The model with the highest F1-score was identified as the best model. The F1-score is particularly relevant for imbalanced datasets like ours, as it balances precision and recall.

**Model Deployment with Flask**
To make the model accessible and usable, I deployed it using the Flask web framework. Users can input customer data through a user-friendly web form, and the deployed model predicts whether a customer will churn or not. The Flask app processes the input, invokes the model, and displays the prediction results on the web page.
