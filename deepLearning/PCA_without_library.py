import numpy as np

def pca(X, num_components):
    # Step 1: Normalize the data
    X_normalized = (X - np.mean(X, axis=0)) / np.std(X, axis=0)

    # Step 2: Compute the covariance matrix
    covariance_matrix = np.cov(X_normalized, rowvar=False)

    # Step 3: Compute the eigenvectors and eigenvalues
    eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)

    # Step 4: Sort eigenvalues and corresponding eigenvectors in descending order
    sorted_indices = np.argsort(eigenvalues)[::-1]
    eigenvalues = eigenvalues[sorted_indices]
    eigenvectors = eigenvectors[:, sorted_indices]

    # Step 5: Select the top 'num_components' eigenvectors
    top_eigenvectors = eigenvectors[:, :num_components]

    # Step 6: Project the data onto the reduced-dimensional space
    reduced_data = np.dot(X_normalized, top_eigenvectors)

    return reduced_data

# Example usage:
# Replace the next two lines with your own dataset loading code
data = np.random.rand(100, 5)  # Example random dataset
num_components = 2  # Set to the desired number of dimensions

# Apply PCA
reduced_data = pca(data, num_components)

# Print the shape of the original and reduced data
print("Original Shape:", data.shape)
print("Reduced Shape:", reduced_data.shape)
