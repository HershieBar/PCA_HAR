# PCA Human Activity Recognition

## Introduction

Principal Component Analysis (PCA) is a statistical procedure that transforms a set of observations of possibly correlated variables into a set of values of linearly uncorrelated variables called principal components.This technique is widely used in the reduction of high feature datasets, which then can be used for making predictive models. It is particularly useful in processing data where multicollinearity may be a problem, or before machine learning applications to enhance performance and reduce computational costs. With this we will explore how to use and interpret the reduced dataset produced by PCA using the Human Activity Recognition Using Smartphone dataeset.The HAR dataset contains time and frequency domain variables extracted from smartphone sensor signals (accelerometer and gyroscope) while subjects performed activities like walking, sitting, standing, etc. This dataset is often used for building models that can recognize human activities based on sensor data.   

## Data Manipulation 

There were 2 features that were discarded/changed. The feature that was discarded was the volunteer number since there was no characteristics that was provided about the person, so nothing can be concluded from the data about the motion under different personal characteristics such as height, weight, age, and other factors that can vary in an individuals movement, as these were not given. Further we are not intersted in individual variances of the above recorded activity and only want to see patterns in the motion of said activities. The other feature that was changed was Activity, which was a qualitative measurement, which was converted into numerical values (Standing = 1, Sitting = 2, etc) to code the data.

## PCA Methodology 

As mentioned before PCA is an algorithm that reduces the dimensionality (Features) of a dataset. Our goal using this algorithm is to find the eigenvalues that result in the most variance in the data and the resulting eigenvectors will be our Principal Components. And with these Principal Components, it'll capture the most important features of the dataset. To find these eigenvalues, we must first standarize the dataset (Set mean = 0 and standard deviation = 1) to ensure each data point is uniformly scaled as features that have high ranges of values will dominate over lower ranges of values, resulting in biased Principal Components. We then create a Covariance Matrix with our centered data and find the eigenvalues of that matrix. After that, we determine the eigen-outliers and create our Principal Component graphs.



[View Histo_MP.html](path/to/Histo_MP.html)

These are the resulting eigenvalues of our covariance matrix segmented into bins. Graphically we can see that there are 6 eigen-outliers in this graph, however, we do not know if all of these values are truely signals to the data. To verify if these values are in fact are PCs, we will use the Marchenko-Pastur Distribution, which will produce a asymtopical behavior that allows us to interpret which of eigenvalues are our signals and noise. 


[Marchenko-Pastur Distribution](Histo_MP.html)

#### Marchenko-Pastur Distribution Analysis

This Marchenko-Pastur Distribution shown in red fits decently to our histogram and this tells us enough about which eigenvalues are noise and signals. First off we can conclude that the eigen-outliers are 2.82904448, 2.93798858, 3.53668428, 8.43312561, 9.27615181, 118.320105 as they are outside the upper bound of the distribution and they have the greatest magnitude, meaning that these eigenvalues are our Prinicipal Components. On top of that they account for 77.37% of the explained variance in the dataset. And from this distribution we can conclude that anything under the distribution tells us that these eigenvalues are noise and contribute no signal to the actual data. The eigenvalues below the lower bound of the Marcenko Distribution can be principal components, however, because these values are very small, meaning that they have a weak signal-to-noise ratio, as there could be information associated with these eigenvalues about the data; it is a small contribution to the overall variance/infomration to the dataset. And not including these eigenvalues would not significantly influnece our data reduction. Lets look at the top 3 eigenvalues (8.43312561, 9.27615181, 118.320105) to understand what features are influencing the data the most. 

## Principal Components

Here is a list of the top 5 linear combinations that make up each PC, where largest magnitude shows what influences the Principal Component the most.

| Principal Component 1                | Principal Component 2                    | Principal Component 3                     |
|--------------------------------------|------------------------------------------|-------------------------------------------|
| tGravityAcc-energy()-X: 0.34954      | Activity: 0.30260                        | Activity: 0.23134                         |
| Activity: -0.30638                   | tBodyGyroMag-entropy(): 0.13315          | fBodyAccJerk-entropy()-X: 0.12193         |
| tGravityAcc-mean(): 0.25527          | fBodyAcc-kurtosis()-X: 0.13230           | fBodyAccJerk-entropy()-Y: 0.11898         |
| angle(X,gravityMean): -0.25275       | fBodyAcc-skewness()-Z: 0.12814           | tBodyAccJerkMag-entropy(): 0.11719        |
| tGravityAcc-max()-X: 0.25181         | tGravityAcc-energy()-X: -0.12433         | fBodyAcc-entropy()-X: 0.11711             |

### PC 1

tGravityAcc-energy()-X: This feature has the highest positive loading and represents the energy of the gravity acceleration signal in the X-direction. The fact that this feature dominates PC1 suggests that this linear combination captures variations in the acceleration due to gravity, which is likely to differ across activities like standing, sitting, or lying down. <br><br>

Activity: Because the activity feature is negative, it suggests that as the movements of the subject becomes more dynamic (Standing &#8594; Sitting &#8594; Laying, etc), there will be an inverse relationship between the positive features of the linear combinations of PC 1. For example, the feature 'tGravityAcc-energy()-X' will tend to decrease, as the type of activity increases.<br><br>

tGravityAcc-mean()-X: This represents the average gravity acceleration in the X-direction. Similar to the energy, this suggests that PC1 is influenced by how the orientation of the device (and by extension, the user's body) changes with different activities.<br><br>

angle(X,gravityMean): The angle between the X-axis and the gravity vector has an influence on PC1 with a negative loading, indicating that changes in this angle are important in differentiating between activities.<br><br>

tGravityAcc-max()-X: This feature tells us the maximum value of gravity acceleration in the X-direction and the static and transitional aspects of the user's orientation relative to gravity.

### PC 2

Activity: This feature appears again with a positive loading this time, and it's top feature that influences the PC the most. <br><br>

tBodyGyroMag-entropy(): The entropy of the gyroscope magnitude reflects the complexity or randomness of the gyroscope signal. A higher value could indicate more complex body motion, possibly associated with dynamic activities like walking or even laying down.<br><br>

fBodyAcc-kurtosis()-X: This measures the 'tailedness' of the frequency domain signal from body acceleration in the X-direction. It's interesting that PC2 relates to both frequency (fBodyAcc) and time (tBodyGyro) domain features, suggesting a blend of dynamic movement and signal properties.<br><br>

fBodyAcc-skewness()-Z: This represents the asymmetry of the body acceleration frequency distribution in the Z-direction. Skewness can indicate the directionality of movement, which might differentiate activities such as walking upstairs vs downstairs.<br><br>

tGravityAcc-energy()-X: The negative loading of gravity acceleration energy in the X-direction, which contrasts with its positive contribution in PC1, suggesting that PC2 may capture different aspects of motion or orientation changes.

### PC 3

Activity: Yet again, 'Activity' appears with positive loading and it being a top feature of PC 3. <br><br>

fBodyAccJerk-entropy()-X and fBodyAccJerk-entropy()-Y: The entropy of body linear acceleration (jerk signals) in both X and Y directions suggests that PC3 may be capturing the irregularity and complexof motion changes, as jerk signals are indicative of sudden movements which differ between activities.<br><br>

tBodyAccJerkMag-entropy(): This is the entropy of the magnitude of body acceleration jerk, which further supports the notion that PC3 is capturing the nuances of transient, possibly abrupt movements.<br><br>

fBodyAcc-entropy()-X: This feature measures the randomness in the frequency domain of the body acceleration signal in the X-direction, implying that PC3 is sensitive to both sudden movements and the structured patterns in the frequency domain.

## Principal Component Plots

### PC 1 vs PC 2

Distinct clustering of activities observed, with PC1 capturing gravitational features and PC2 capturing entropy and complexity of movements.

### PC 1 vs PC 3

Clustering of dynamic and static activities observed, with PC3 capturing jerk signal entropy and PC1 indicating gravity acceleration in X-direction.

### PC 2 vs PC 3

Clear separation of dynamic vs. static activities, with PC2 capturing body gyroscope movements and PC3 capturing jerk signal-related transient movements.

## Testing

To assess the efficacy of the condensed training set, I used Logistic Regression to evaluate its accuracy in predicting activities based on new sensory data, relative to our original dataset. Impressively, this dimensionally reduced dataset not only surpassed the original with an accuracy of 95.9% compared to 95.5%, but it also demonstrated a substantial increase in computational efficiency, running 82.5% faster   

## Conclusion

The application of Principal Component Analysis (PCA) significantly reduced the dimensionality of the original 563 features in the Human Activity Recognition Using Smartphones dataset. Resulting in only six principal components with eigenvalues of [2.82, 2.93, 3.53, 8.433, 9.27, 118.32]. These eigenvalues stand out from the noise in the dataset. This reduction highlights the dataset's intrinsic patterns by capturing the majority of the variance with fewer dimensions, thus enhancing analytical efficiency without significant loss of information. These principal components, which primarily encapsulate variations in gravity-affected movements, rotational motion, and the complexity of jerk movements among different activities, allows for a condensed understanding of human activity patterns. The dimension-reduced data can be applied to other machine learning models as it improves model training times and mitigating the risk of overfitting.
