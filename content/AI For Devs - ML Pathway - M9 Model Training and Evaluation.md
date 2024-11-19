# Model Training and Evaluation

## K-Fold Cross Validation
<iframe width="720" height="405" src="https://www.youtube.com/embed/TIgfjmp-4BA?si=1K3CkHT7KOZImNP0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

### Example of K-Fold in Python

#### admissions.csv

| StudentID | GRE_Score | GPA | College_Rating | Admission |
| --------- | --------- | --- | -------------- | --------- |
| 1         | 320       | 3.5 | 4              | 1         |
| 2         | 310       | 3.0 | 3              | 0         |
| 3         | 325       | 3.8 | 5              | 1         |
| 4         | 300       | 2.8 | 2              | 0         |
| 5         | 315       | 3.4 | 3              | 1         |
| 6         | 305       | 3.2 | 2              | 0         |
| ...       | ...       | ... | ...            | ...       |

- **StudentID**: A unique identifier for each student
- **GRE_Score**: The student’s GRE test score (out of 340)
- **GPA**: Undergraduate Grade Point Average (on a 4.0 scale)
- **College_Rating**: College prestige rating (1 = lowest, 5 = highest)
- **Admission**: Target variable (1 = Admitted, 0 = Not Admitted)

#### Example Code
```python
# Import necessary libraries
import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier

# Load the dataset
df = pd.read_csv('admissions.csv')

# Features and target
X = df[['GRE_Score', 'GPA', 'College_Rating']]
y = df['Admission']

# Define the model
model = RandomForestClassifier()

# Perform K-Fold Cross-Validation
scores = cross_val_score(model, X, y, cv=3, scoring='accuracy')  # 3 folds

# Print results
print("K-Fold Cross-Validation Results")
print(f"Fold Accuracies: {scores}")
print(f"Mean Accuracy: {scores.mean():.2f}")
```

## Learning and Validation Curves
<iframe width="720" height="405" src="https://www.youtube.com/embed/nt5DwCuYY5c?si=BcQEjOVOW5DytrOE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Handling Overfitting / Underfitting

**Overfitting**: High training accuracy, low test accuracy.

**Underfitting**: Low accuracy on both training and test data.

### Overfitting

Overfitting happens when your model performs well on training data but poorly on unseen data because it "memorizes" the training details rather than learning general patterns.

**Possible Solutions to Consider:**
- **Simplify the Model**: Use a less complex algorithm (e.g., reduce the depth of decision trees or use fewer layers in neural networks).
- **Regularization**: Apply L1 (Lasso) or L2 (Ridge) regularization to penalize overly complex models.
- **Reduce Features**: Remove irrelevant or redundant features via feature selection.
- **Increase Training Data**: Gather more varied data to help the model generalize better.
- **Tune Hyperparameters with Cross-Validation**: Tune hyperparameters using techniques like K-Fold Cross-Validation to find the best model settings.

### Underfitting

Underfitting happens when your model performs poorly on both training and unseen data because it’s too simple to capture the underlying patterns.

**Possible Solutions to Consider:**
- **Increase Model Complexity**: Use an algorithm capable of modeling more complex relationships in the data (such as moving from linear regression to random forests or from random forests to neural networks, depending on the problem type).
- **Add Features**: Include more informative features that help the model learn better patterns.
- **Train Longer**: Increase the number of training epochs for models like neural networks to better fit the data.

The goal is to find the sweet spot where the model is neither overfitting nor underfitting by carefully tuning complexity, hyperparameters, and features.

### Back [[AI For Devs - ML Pathway]]