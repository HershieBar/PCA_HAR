import numpy as np
import pandas as pd
import time
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

#Stores file data
features_file = "features.txt"
datafile = "ModifiedTrain.csv"
test_data = "test.csv"
df_test = pd.read_csv(test_data)
df_train = pd.read_csv(datafile)

features = pd.read_csv(features_file, sep = " ", header= None)


N = len(df_train)
gamma = df_train.shape[1] / df_train.shape[0]

a = (1 - np.sqrt(gamma))**2
b = (1 + np.sqrt(gamma))**2
p = df_train.shape[0]*gamma
pi = np.pi

#Stores columns as arrays in array
feature_names = features[1].values  
npdata_features = df_train.loc[:, feature_names].to_numpy()

#Centering data
data_features_mean = np.mean(npdata_features, axis=0)
std = np.std(npdata_features)
centered_features = (npdata_features - data_features_mean)/std

# N >> m, Covariance Matrix
cov_matrix = (centered_features.T @ centered_features) / (N-1)

#Eigenvalues of Covariance Matrix
eigen_vals, eigen_vecs = np.linalg.eigh(cov_matrix)



# Marchenko-Pastur density function 
def marchenko_pastur_pdf(x, gamma, a, b):
    return np.sqrt((b - x) * (x - a)) / (2 * pi * gamma * x)






sorted_indices = np.argsort(eigen_vals)[::-1]
sorted_eigen_vals = eigen_vals[sorted_indices]
sorted_eigen_vecs = eigen_vecs[:, sorted_indices]


outlier_eigenvalues = np.array([2.82904448e+00, 2.93798858e+00, 3.53668428e+00, 8.43312561e+00, 9.27615181e+00,  1.18320105e+02])

outlier_indices = [np.where(np.isclose(sorted_eigen_vals, val))[0][0] for val in outlier_eigenvalues]
principal_components = sorted_eigen_vecs[:, outlier_indices]
projected_data = np.dot(centered_features, principal_components)


total_variance = np.sum(eigen_vals)
selected_variance = np.sum(outlier_eigenvalues)

# Calculate the proportion of the total variance explained by selected components
explained_variance_ratio = selected_variance / total_variance

print(f"Explained Variance Ratio: {explained_variance_ratio}")


df_test_features = df_test.loc[:, feature_names].to_numpy()
centered_test_features = (df_test_features - data_features_mean) / std

projected_test_data = np.dot(centered_test_features, principal_components)
X_test = projected_test_data
y_test = df_test['Activity']




# Predict on test data
# Original Datset
start_time_original = time.time()
model_original = LogisticRegression(max_iter=2000)
model_original.fit(df_train.drop(['Activity'], axis=1), df_train['Activity'])
y_pred_original = model_original.predict(df_test_features)
print("Accuracy:", accuracy_score(y_test, y_pred_original))
print("Classification Report:\n", classification_report(y_test, y_pred_original))
end_time_original = time.time()
duration_original = end_time_original - start_time_original
print(duration_original)

# Reduced Dataset
start_time_reduced = time.time()
model_reduced = LogisticRegression(max_iter = 2000)
model_reduced.fit(projected_data, df_train['Activity']) 
y_pred_reduced = model_reduced.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred_reduced))
print("Classification Report:\n", classification_report(y_test, y_pred_reduced))
end_time_reduced = time.time()
duration_reduced = end_time_reduced - start_time_reduced
print(duration_reduced)


print((duration_original-duration_reduced)/duration_original)