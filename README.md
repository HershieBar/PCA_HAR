# PCA Human Activity Recognition

## Introduction

Principal Component Analysis (PCA) is a statistical procedure that transforms a set of observations of possibly correlated variables into a set of values of linearly uncorrelated variables called principal components. This technique is widely used in the reduction of high-feature datasets, which can then be used for making predictive models. It is particularly useful in processing data where multicollinearity may be a problem, or before machine learning applications to enhance performance and reduce computational costs. 

In this analysis, we explore how to use and interpret the reduced dataset produced by PCA using the Human Activity Recognition Using Smartphone dataset. This dataset contains time and frequency domain variables extracted from smartphone sensor signals (accelerometer and gyroscope) while subjects performed activities like walking, sitting, standing, etc. It is often used for building models that recognize human activities based on sensor data.

## Data Manipulation 

Two features were discarded or changed. The feature discarded was the volunteer number, as no characteristics about the person were provided. Therefore, no conclusions could be drawn about the motion under different personal characteristics such as height, weight, or age, which can vary in an individual's movement. We are not interested in individual variances of the recorded activities and want to see patterns in the motion of said activities. 

The other feature, *Activity*, was changed from a qualitative measurement to numerical values (Standing = 1, Sitting = 2, etc.) to code the data.

## PCA Methodology 

PCA is an algorithm that reduces the dimensionality (features) of a dataset. Our goal with this algorithm is to find the eigenvalues that result in the most variance in the data, with the resulting eigenvectors becoming our Principal Components (PCs). These PCs capture the most important features of the dataset. To find these eigenvalues:

1. Standardize the dataset (set mean = 0 and standard deviation = 1) to ensure each data point is uniformly scaled.
2. Create a Covariance Matrix with the centered data and find its eigenvalues.
3. Identify eigen-outliers and create our Principal Component graphs.

![Histogram of Eigenvalues](Histogram.html)

These are the resulting eigenvalues of our covariance matrix segmented into bins. Graphically, we see six eigen-outliers. To verify if these values are PCs, we use the Marchenko-Pastur Distribution, which produces asymptotic behavior to interpret which eigenvalues are signals and which are noise.

![Marchenko-Pastur Distribution](Histo_MP.html)

### Marchenko-Pastur Distribution Analysis

The Marchenko-Pastur Distribution (shown in red) fits decently with our histogram, indicating which eigenvalues are signals and which are noise. The eigen-outliers 2.829, 2.938, 3.537, 8.433, 9.276, and 118.32 stand out, accounting for 77.37% of the dataset's explained variance. This distribution helps us identify noise components, which contribute little to the dataset's overall variance.

## Principal Components

Here are the top 5 linear combinations that make up each PC, where the largest magnitudes show what influences the Principal Component the most.

| Principal Component 1                | Principal Component 2                    | Principal Component 3                     |
|--------------------------------------|------------------------------------------|-------------------------------------------|
| tGravityAcc-energy()-X: 0.34954      | Activity: 0.30260                        | Activity: 0.23134                         |
| Activity: -0.30638                   | tBodyGyroMag-entropy(): 0.13315          | fBodyAccJerk-entropy()-X: 0.12193        |
| tGravityAcc-mean(): 0.25527          | fBodyAcc-kurtosis()-X: 0.13230           | fBodyAccJerk-entropy()-Y: 0.11898         |
| angle(X,gravityMean): -0.25275       | fBodyAcc-skewness()-Z: 0.12814           | tBodyAccJerkMag-entropy(): 0.11719        |
| tGravityAcc-max()-X: 0.25181         | tGravityAcc-energy()-X: -0.12433         | fBodyAcc-entropy()-X: 0.11711             |

**PC 1** emphasizes gravitational features, reflecting static vs. dynamic activities.

**PC 2** captures gyroscope signal entropy, useful for distinguishing complex, dynamic activities.

**PC 3** captures the randomness in jerk signals, indicating sudden, irregular movement.

## Principal Component Plots

### PC 1 vs PC 2
We observe distinct activity clusters, with static movements like standing and sitting clustered along the PC1 axis, influenced by gravitational acceleration, while dynamic activities disperse along PC2.

### PC 1 vs PC 3
This clustering shows sudden movements in walking downstairs, captured well by jerk signals on PC3. Static activities cluster lower on PC3, indicating minimal jerk.

### PC 2 vs PC 3
Dynamic activities occupy higher values on both axes, reflecting complexity and irregularity in movement. PC2 emphasizes body gyroscope data, while PC3 captures jerk features.

## Testing

To assess the efficacy of the condensed training set, I used Logistic Regression to evaluate its accuracy in predicting activities based on new sensory data. The reduced dataset achieved an accuracy of 95.9%, outperforming the original dataset (95.5%) and running 82.5% faster.

## Conclusion

The application of PCA significantly reduced the original 563 features in the Human Activity Recognition Using Smartphones dataset to only six principal components. This reduction highlights intrinsic patterns, capturing the majority of the variance with fewer dimensions and enhancing analytical efficiency without significant information loss. These components, encapsulating gravity-related movement, rotational motion, and jerk complexity across activities, allow for a condensed understanding of human activity patterns. The reduced data is efficient for machine learning applications, improving training times and reducing overfitting risk.
