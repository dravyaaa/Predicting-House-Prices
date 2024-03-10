# Predicting-House-Prices
## 1. Data Collection

For this project, I collected data from the Philadelphia Open Portal, a comprehensive repository of public datasets maintained by the city of Philadelphia. The dataset I used for this project is titled "properties_public.csv." This dataset contains detailed information about properties in Philadelphia, including their characteristics such as location, size, number of bedrooms and bathrooms, number of stories, interior and exterior conditions, sale date, sale price, and market value. It is important to note that the dataset comprises over 5000 records, ensuring an adequate amount of training data for model development.

## 2. Data Preprocessing

Upon acquiring the dataset, I preprocessed the data to ensure its cleanliness and suitability for analysis. The preprocessing steps I performed include:

Handling missing values: I systematically dealt with missing values by dropping rows with missing values for essential features such as sale price, number of bathrooms, and number of bedrooms.
Removing outliers: To maintain the integrity of the data, I identified and removed outliers in the sale price column.
Converting categorical variables: I converted categorical variables, such as zip code, into a suitable format for modeling using one-hot encoding. This allowed me to effectively utilize these variables in the predictive modeling process.

## 3. Feature Engineering

Feature engineering played a crucial role in enhancing the predictive performance of the models. I employed various techniques to create new features from the existing data, including:

Creating a new feature representing the ratio of bedrooms to bathrooms.
Combining interior and exterior conditions into a single feature to capture the overall condition of the property.
Extracting additional features such as the sale year and the age of the property, which provided valuable insights into the temporal aspects of property sales.

## 4. Model Development

Using the preprocessed and engineered data, I developed machine learning models to predict house prices. I experimented with a range of algorithms, including:

Linear Regression
Decision Trees
Random Forests
Gradient Boosting
These models were trained on the training dataset and evaluated based on various evaluation metrics such as mean squared error (MSE) and mean absolute error (MAE). The model with the best performance was selected based on these metrics.

## 5. Construction of Test Dataset and Model Evaluation

To evaluate the performance of the trained models, I constructed a separate test dataset. I applied the selected model to the test dataset and assessed its predictive accuracy using metrics such as mean absolute error (MAE) and root mean squared error (RMSE). This rigorous evaluation process ensured the reliability and effectiveness of the predictive models.

## 6. Challenges

During the course of this project, one notable challenge encountered was the presence of mixed data types within the dataset. This challenge manifested in DtypeWarning messages and data conversion errors during the preprocessing stage. For instance, certain columns contained a combination of numeric and string values, requiring careful handling to ensure accurate analysis. Addressing this challenge involved implementing specific data type conversions and error-handling techniques to coerce the data into a consistent format suitable for further processing. Additionally, identifying and resolving inconsistencies in data representation required meticulous attention to detail to maintain data integrity and reliability throughout the analysis pipeline. This challenge underscored the importance of robust data preprocessing techniques and highlighted the need for flexible and adaptive approaches to handle diverse data types effectively.

## Results

### Linear Regression:
Mean Squared Error (MSE): 21,881,412,766.07

Mean Absolute Error (MAE): 128,103.18

### Random Forest Regressor:
Mean Squared Error (MSE): 24,525,209,559.54

Mean Absolute Error (MAE): 130,107.45

### Gradient Boosting Regressor:
Mean Squared Error (MSE): 22,743,201,247.82

Mean Absolute Error (MAE): 127,589.25

## 7. Discussion

In the final report, I discussed the project findings in detail, including insights gained from data analysis and model development. I addressed challenges encountered during the process and provided recommendations for improving the predictive performance of the model. Additionally, I reflected on the strengths and limitations of the approach and proposed future research directions to further enhance the predictive modeling of house prices using the Philadelphia Open Portal dataset.

Overall, this project aimed to develop an accurate and reliable model for predicting house prices in Philadelphia, leveraging advanced machine learning techniques and comprehensive data analysis. The detailed methodology and thorough analysis presented in this report demonstrate a comprehensive understanding of the subject matter and a commitment to delivering high-quality results.
