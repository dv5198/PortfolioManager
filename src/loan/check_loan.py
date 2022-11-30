
from csv import writer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn import metrics
import pandas as pd                       # for reading the files
import numpy as np                        # for creating multi-dimensional-array
import warnings                           # for ignoring the warnings
warnings.filterwarnings("ignore")


def models(user, gender, married, dependents, education, self_employed, applicant_income, coapplicant_income, loan_amount, loan_amount_term, credit_history, property_area):
   
   # # Import the Data Files
    vals = ["LP0001011", gender, married, dependents, education, self_employed, int(applicant_income),
            int(coapplicant_income), int(loan_amount), int(loan_amount_term), credit_history, property_area]

    with open("test.csv", "r") as f:
        lines = f.readlines()
        lines = lines[:-1]
        # print(lines)

    with open("test.csv", "w") as f:
        for line in lines:
            f.write(line)
            # print(f)

    with open('test.csv', 'a') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(vals)
        # print(writer_object)
        f_object.close()

    test = pd.read_csv('test.csv')
    print("Test =====>", test)
    train = pd.read_csv('train.csv')
    
    # print(test(-1))

    test_original = test.copy()
    train_original = train.copy()

    pd.set_option("display.max_rows", 400)
    pd.set_option("display.max_columns", 400)
    

    # Frequency Table for Gender and Loan Status

    Gender = pd.crosstab(train['Gender'], train['Loan_Status'])
    Married = pd.crosstab(train['Married'], train['Loan_Status'])
    Dependents = pd.crosstab(train['Dependents'], train['Loan_Status'])
    Education = pd.crosstab(train['Education'], train['Loan_Status'])
    Self_Employed = pd.crosstab(train['Self_Employed'], train['Loan_Status'])
    Credit_History = pd.crosstab(train['Credit_History'], train['Loan_Status'])
    Property_Area = pd.crosstab(train['Property_Area'], train['Loan_Status'])

    bins = [0, 2500, 4000, 6000, 8100]
    group = ['Low', 'Average', 'High', 'Very high']
    train['Income_bin'] = pd.cut(train['ApplicantIncome'], bins, labels=group)

    Income_bin = pd.crosstab(train['Income_bin'], train['Loan_Status'])

    # Doing the same for Coapplicant Income

    bins = [0, 1000, 3000, 42000]
    group = ['Low', 'Average', 'High']
    train['Coapplicant_Income_bin'] = pd.cut(
        train['CoapplicantIncome'], bins, labels=group)
    Coapplicant_Income_bin = pd.crosstab(
        train['Coapplicant_Income_bin'], train['Loan_Status'])

    # Combine the Applicant Income and Coapplicant Income and see the combined effect of Total Income on the Loan_Status.

    train['Total_Income'] = train['ApplicantIncome']+train['CoapplicantIncome']
    bins = [0, 2500, 4000, 6000, 81000]
    group = ['Low', 'Average', 'High', 'Very high']
    train['Total_Income_bin'] = pd.cut(
        train['Total_Income'], bins, labels=group)
    Total_Income_bin = pd.crosstab(
        train['Total_Income_bin'], train['Loan_Status'])

    bins = [0, 100, 200, 700]
    group = ['Low', 'Average', 'High']
    train['LoanAmount_bin'] = pd.cut(train['LoanAmount'], bins, labels=group)
    LoanAmount_bin = pd.crosstab(train['LoanAmount_bin'], train['Loan_Status'])

    # Change the 3+ in dependents variable to 3 to make it a numerical variable.We will also convert the target variable’s categories into 0 and 1

    train['Dependents'].replace('3+', 3, inplace=True)
    test['Dependents'].replace('3+', 3, inplace=True)

    # Convert the target variable 'Loan Status' categories into 0 and 1 for logistic regression

    train['Loan_Status'].replace('N', 0, inplace=True)
    train['Loan_Status'].replace('Y', 1, inplace=True)

    # # Correlation using Heatmaps

    matrix = train.corr()

    train = train.drop(['Income_bin', 'Coapplicant_Income_bin',
                       'LoanAmount_bin', 'Total_Income_bin', 'Total_Income'], axis=1)

    # # Handling the missing Data

    train.isnull().sum()

    #  replacing the null values with the mode of the respective columns.

    train['Gender'].fillna(train['Gender'].mode()[0], inplace=True)

    train['Married'].fillna(train['Married'].mode()[0], inplace=True)

    train['Dependents'].fillna(train['Dependents'].mode()[0], inplace=True)

    train['Self_Employed'].fillna(
        train['Self_Employed'].mode()[0], inplace=True)

    train['Credit_History'].fillna(
        train['Credit_History'].mode()[0], inplace=True)

    train['Loan_Amount_Term'].fillna(
        train['Loan_Amount_Term'].mode()[0], inplace=True)

    train['LoanAmount'].fillna(train['LoanAmount'].median(), inplace=True)

    test['Gender'].fillna(test['Gender'].mode()[0], inplace=True)

    test['Married'].fillna(test['Married'].mode()[0], inplace=True)

    test['Dependents'].fillna(test['Dependents'].mode()[0], inplace=True)

    test['Self_Employed'].fillna(test['Self_Employed'].mode()[0], inplace=True)

    test['Credit_History'].fillna(
        test['Credit_History'].mode()[0], inplace=True)

    test['Loan_Amount_Term'].fillna(
        test['Loan_Amount_Term'].mode()[0], inplace=True)

    test['LoanAmount'].fillna(test['LoanAmount'].median(), inplace=True)

    # There are many outliers in the LoanAmount.Doing the log transformation to make the distribution look normal.

    train['LoanAmount_log'] = np.log(train['LoanAmount'])
    test['LoanAmount_log'] = np.log(test['LoanAmount'])

    # # Model Building

    train = train.drop('Loan_ID', axis=1)
    test = test.drop('Loan_ID', axis=1)

    train = train.drop('Gender', axis=1)
    test = test.drop('Gender', axis=1)

    train = train.drop('Dependents', axis=1)
    test = test.drop('Dependents', axis=1)

    train = train.drop('Self_Employed', axis=1)
    test = test.drop('Self_Employed', axis=1)

    # Also dropping the Loan_Status column and storing it in another variable.

    x = train.drop('Loan_Status', axis=1)
    
    y = train['Loan_Status']

    # Creating Dummy Variable

    x = pd.get_dummies(x)
    train = pd.get_dummies(train)
    test = pd.get_dummies(test)
    # print(test.tail(1))
    
 # Applying Logistic Regression 
    x_train, x_cv, y_train, y_cv = train_test_split(
        x, y, train_size=0.75, random_state=101)

    model = LogisticRegression()
    model.fit(x_train, y_train)
    pred_test = model.predict(test)
    
    print(pred_test)
    return pred_test[-1]
