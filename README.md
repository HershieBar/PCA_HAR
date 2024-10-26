# PCA Human Activity Recognition

This project applies **Principal Component Analysis (PCA)** to the Human Activity Recognition Using Smartphones (HAR) dataset, which contains data from smartphone sensors (accelerometer and gyroscope) capturing activities like walking, sitting, and standing. The goal is to reduce the dataset's dimensionality, preserving the most meaningful features for accurate human activity recognition.

### Project Overview
- **Dataset:** HAR data with time and frequency features extracted from smartphone sensors.
- **PCA Process:** 
  - **Data Standardization** to avoid bias in principal components.
  - **Covariance Matrix Creation** to identify eigenvalues indicating variance.
  - **Marchenko-Pastur Distribution** to separate signal from noise.
- **Results:** Six principal components account for 77.37% of the data variance. Testing with Logistic Regression achieved a 95.9% accuracy, with 82.5% faster processing than using the full dataset.

### Conclusion
PCA effectively reduced the HAR dataset’s dimensions from 563 features to six primary components, enhancing computational efficiency without significant information loss. The reduced dataset is suitable for training machine learning models, minimizing overfitting risk while maintaining robust predictive accuracy.


https://hershiebar.github.io/PCA_HAR/
