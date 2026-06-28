# 📊 Crime Patterns and Crime Risk Prediction in Boston

## Project Overview
This project analyzes open crime data from the City of Boston to uncover spatial, temporal, and behavioral patterns in criminal incidents, and extends the analysis with a machine learning pipeline for district-level crime risk prediction. 

The work is organized in two complementary parts: an exploratory and geospatial analysis of crime trends, and a predictive modeling notebook designed to estimate short-term high-risk patterns across Boston police districts. 

## Dataset
- **Source:** [City of Boston Open Data Portal](https://data.boston.gov/dataset/?organization=boston-police-department-org) 
- **Main attributes:** incident type, date and time, district, neighborhood, and geographic coordinates. 
- **Modeling input:** a cleaned dataset aggregated into a district-day structure for temporal forecasting. 

## Project Structure
This repository now includes both descriptive and predictive components: 

- **Data capture and cleaning:** collection, preprocessing, and standardization of the Boston crime dataset. 
- **Exploratory Data Analysis:** temporal trends, pandemic effects, crime type patterns, and neighborhood comparisons. 
- **Geospatial analysis:** crime concentration and crime density across Boston neighborhoods. 
- **Machine learning notebook:** district-level prediction of serious crime risk using time-based features and imbalanced classification methods. 

## Exploratory Analysis
The exploratory phase investigates how crime varies by day of the week, time of day, crime type, and neighborhood. It also examines how crime behavior changed before, during, and after the COVID-19 pandemic. 

### Main findings from the exploratory analysis
- General crime declined during the pandemic, while homicides increased. 
- Dorchester, Roxbury, and Jamaica Plain had the highest number of incidents overall. 
- When adjusting for area, the Leather District showed the highest crime density. 
- Downtown neighborhoods such as the Leather District, South End, Back Bay, Downtown, and Chinatown accounted for more than 46% of total crime density. 

## Predictive Modeling Notebook
The machine learning notebook reframes the problem as a **future risk prediction task**. Instead of modeling isolated incidents, it estimates whether a district is likely to enter a high-risk pattern in the near future based on historical serious crime activity. 

### Modeling approach
- The original data was aggregated at the **district-day** level. 
- Temporal features were engineered using past-only information, including lagged crime counts, 7/30/90-day rolling sums, trend indicators, and seasonal variables. 
- The target variable was defined as the number of serious crimes expected in the **next 7 days**, converted into a binary high-risk label. 
- The train-test split was performed chronologically to preserve the time structure of the problem. 
- Two models were compared: **Logistic Regression** and **Random Forest**. 
- Threshold tuning was applied with the precision-recall curve to improve evaluation under class imbalance. 

### Final modeling results
After threshold tuning, both models performed competitively on the district-level risk classification task. 

- **Logistic Regression:** threshold 0.5699, ROC AUC 0.9588, PR AUC 0.8621, precision 0.7155, recall 0.8495, F1-score 0.7767. 
- **Random Forest:** threshold 0.5192, ROC AUC 0.9599, PR AUC 0.8671, precision 0.7467, recall 0.8042, F1-score 0.7744. 

These results show that Random Forest achieved slightly stronger ranking and precision-based metrics, while Logistic Regression produced the highest recall for the positive class. 

### Model selection rationale
Because the main objective of the predictive notebook is to identify high-risk districts and minimize missed alerts, recall was treated as the most important metric in the final comparison. This makes the final model choice dependent on whether the priority is to maximize detection of risky districts or to achieve a slightly more balanced precision-recall trade-off. 

## Tools and Libraries
- **Python:** Pandas, NumPy 
- **Visualization:** Matplotlib, Seaborn, Plotly 
- **Geospatial analysis:** Geopy, GeoPandas 
- **Machine learning:** scikit-learn, Random Forest, Logistic Regression 
- **Notebook environment:** Jupyter Notebook 

## How to Run
1. Clone the repository. 
2. Install the required libraries. 

```bash
pip install pandas numpy matplotlib seaborn geopy geopandas plotly scikit-learn
```

3. Open the notebooks and run the cells in order. 
4. Use the exploratory notebook for descriptive and geospatial insights, and the machine learning notebook for district-level crime risk prediction. 

## Project Status
- ✅ Data capture and cleaning completed. 
- ✅ Exploratory Data Analysis completed. 
- ✅ Geospatial analysis completed. 
- ✅ Predictive modeling notebook completed. 
- 🔜 Future work: real-time dashboards, additional models, and integration of external variables such as weather or local events. 

## Contact
Feel free to connect: 
- [LinkedIn](https://www.linkedin.com/in/denise-ribeiro-potenza/)
- denisepotenza@gmail.com
