import numpy as np
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris  # Example dataset

# Load your dataset or use a sample dataset (e.g., Iris dataset)
# Replace the next two lines with your own dataset loading code
data = load_iris()
X = data.data
y = data.target

# Normalize the data (optional but recommended for PCA)
X_normalized = (X - np.mean(X, axis=0)) / np.std(X, axis=0)

# Specify the number of components (dimensions) you want after PCA
n_components = 2  # Set to the desired number of dimensions

# Create PCA instance
pca = PCA(n_components=n_components)

# Fit the PCA model to the data and transform the data
X_pca = pca.fit_transform(X_normalized)

# Print the explained variance ratio for each principal component
print("Explained Variance Ratio:", pca.explained_variance_ratio_)

# Print the cumulative explained variance
print("Cumulative Explained Variance:", np.sum(pca.explained_variance_ratio_))

# You can now use X_pca as your reduced-dimensional dataset
print("Original Shape:", X.shape)
print("Reduced Shape:", X_pca.shape)
