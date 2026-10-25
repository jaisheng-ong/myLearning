
**Prediction Models**

| Common Prediction Models |    Use when  |
|---------------------------|---------------------------|
| `Mean/Median Baseline Models` | Just need a simple reference to see if a complex models is needed |
| `Rube-Based Models` | Limited Data (if else models)    |



*MAE & RMSE Formulas*
- *y* = actual value (from your data)
- *ŷ* (y-hat) = predicted value (from your model)

MAE = (1/n) × Σ |y - ŷ|  
→ "Average of absolute differences"

RMSE = √[(1/n) × Σ (y - ŷ)²]  
→ "Square root of average squared differences"  
→ Penalizes big errors more than MAE

*MAE*
- Lower MAE = Accurate Model
- Higher MAE = Predictions are farther from actual values on average

*How we get predicted value (ŷ) from a model:*
The model calculates ŷ based on what it learned from training data.

Examples:
- Mean baseline model: learns mean = 1157 → any new row gets ŷ = 1157
- Rule-based (segment) model: learns mean per segment → new row with "Makeup" gets ŷ = 1152
- Linear regression: ŷ = b₀ + b₁×feature₁ + b₂×feature₂ + ...
- Decision tree: follows rules like "if price > 50, predict X, else predict Y"

Flow:
1. Model learns patterns from training data
2. Give it new input (features)
3. It outputs ŷ (the prediction)
4. Compare ŷ to actual y to compute error (MAE, RMSE, etc.)

**Types of ML**

*Supervised Learning* 
- Have clear labels and let the machine learn from examples.
- Like feeding past sales and it learns the relationship between various factors and those outcomes. Then, when we give it new data, it can predict the outcome based on what it learned.

*Unsupervised Learning* - Data has no clear labels and uncategorized thus model identify and group the data into each categorizes itself.

*Reinforcement Learning* - Machine explores the environment and learns by reward/penalty (what's good or wrong).


**ML Tasks**
*Regression* - Supervised Learning. Target is a number you want to predict.
Example: sales, price, temperature, quantity sold.

*Classification* - Supervised Learning. Target is a category/label.
Example: spam vs not spam, churn vs stay, product type.

*Clustering* - Unsupervised Learning. No labels; group similar items.
Example: grouping customers by behavior when you don't have "types".

**Common Techniques:**

*k-Means Clustering*
- What it does: Groups rows into clusters and adds a new column with cluster labels
- Original: N rows → After k-Means → same N rows + 1 new column "cluster"
- Purpose: Discover natural groups without predefined categories

Real-world use:
- Customer segmentation: Which customers belong to which segment based on their data
- Target marketing: Advertise things each segment might be interested in
- Example: High spenders get VIP treatment, bargain hunters get discount emails

*PCA (Principal Component Analysis)*
- What it does: Reduces number of columns (features), not grouping labels
- Original: 10 features → After PCA → 3 new features (principal components)
- Same rows, fewer columns. The original columns are REPLACED by new, smarter columns
- Purpose: Simplify dataset, speed up models, reduce noise

Real-world use:
- Too many features → slow model, overfitting
- Remove redundant/correlated features
- Example: height, weight, shoe_size all relate to "body size" → combine into 1 component

Key difference:
- PCA: fewer columns (feature reduction)
- k-Means: new column with cluster labels (grouping rows)



Focus: Regression part