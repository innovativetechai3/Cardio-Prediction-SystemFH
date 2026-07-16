# *******************Import required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, confusion_matrix,classification_report
from sklearn.preprocessing import  LabelEncoder
from scipy.stats import pearsonr
from scipy.stats import chi2_contingency
import joblib
import warnings
warnings.filterwarnings("ignore")

# *******************1 EDA*******************
df = pd.read_csv("Data/heartdiseaseFH.csv")
pd.set_option("display.max_columns",None)
print(df.head())
print(df.tail())
print(df.shape)
df.info()
print(df.describe())

# *******************2-Visualization of EDA[1-histplot 2-countplot 3-boxplot 4-heatmap]*******************
# *******************2.1 Histplot for Numeric Data
def plotting_histogram (df_hist):
    cols_num = ["Age", "RestingBP", "Cholesterol", "MaxHR", "Oldpeak"]
    fig,axes=plt.subplots(nrows=2,ncols=3,figsize=(20,12))

    # Title of the window
    fig.canvas.manager.set_window_title("Histplot for Numeric Fields_Cardio Prediction System")
    axes = axes.flatten()

    for i, col in enumerate(cols_num):
        sns.histplot(data=df_hist,x=col,kde=True,bins=5,ax=axes[i]) # x=col
        axes[i].set_title(f"Distribution of {col}")
        axes[i].set_xlabel(col,labelpad=12)
        axes[i].set_ylabel("Count", labelpad=5)

    for j in range(len(cols_num),len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()

    plt.subplots_adjust(
        top=0.9,
        bottom=0.1,
        left=0.08,
        right=0.98,
        hspace=0.9,
        wspace=0.3,
        )
    plt.savefig("images/HistplotFH.png",
                dpi=300,
                bbox_inches="tight")
    plt.show()
plotting_histogram(df)

# *******************2.2 Countplot for Categorical Data
cols_cat=['Gender', "ChestPainType", "FastingBS", "RestingECG", "ExerciseAngina", "ST_Slope"]
fig,axes=plt.subplots(nrows=2,ncols=4,figsize=(20,12))

# Title of the window
fig.canvas.manager.set_window_title("Countplot for Categorical Fields_Cardio Prediction System")
axes=axes.flatten()

for i, col in enumerate(cols_cat):
    sns.countplot(data=df,
                  x=col,
                  ax=axes[i],
                  hue="HeartDisease")

    axes[i].set_title(f"Frequency of {col}")
    axes[i].set_xlabel(col,labelpad=12)
    axes[i].set_ylabel("Count")

# Create one legend for the whole figure
handles, labels = axes[0].get_legend_handles_labels()
fig.legend(
    handles,
    labels,
    title="HeartDisease",
    loc="upper center",
    ncol=2
)

# Remove legends from plotted subplots
for ax in axes[:len(cols_cat)]:
    ax.get_legend().remove()

for j in range(len(cols_cat),len(axes)):
    fig.delaxes(axes[j])

plt.tight_layout()

plt.subplots_adjust(
    top=0.90,
    left=0.08,
    right=0.98,
    bottom=0.10,
    hspace=0.90,
    wspace=0.30
            )
plt.show()

# *******************2.3 Boxplot for checking outliers
cols_num = ["Age", "RestingBP", "Cholesterol", "MaxHR", "Oldpeak"]
fig,axes=plt.subplots(nrows=2,ncols=3,figsize=(20,12))

# Title of the window
fig.canvas.manager.set_window_title("Boxplot for Numeric fields_Cardio Prediction System")
axes=axes.flatten()

for i, col in enumerate(cols_num):
    sns.boxplot(data=df,x=col,ax=axes[i]) # x=col
    axes[i].set_title(f"Boxplot of {col}")
    axes[i].set_xlabel(col)
    axes[i].set_ylabel("Count")

for j in range(len(cols_num),len(axes)):
    fig.delaxes(axes[j])

plt.tight_layout()

plt.subplots_adjust(
    top=0.90,
    left=0.08,
    right=0.98,
    bottom=0.10,
    hspace=0.90,
    wspace=0.30
    )
plt.savefig("images/BoxplotFH.png",
            dpi=300,
            bbox_inches="tight")
plt.show()

# *******************2.4 Heatmap for checking co-relation
fig, ax = plt.subplots(figsize=(10, 18))
sns.heatmap(df.corr(numeric_only=True),annot=True)

# Title of the window
fig.canvas.manager.set_window_title("Heatmap for Numeric Fields_Cardio Prediction System")

plt.title("Correlation Heatmap")
plt.xlabel("Features",labelpad=15)
plt.xticks(rotation=90)
plt.ylabel("Features",labelpad=15)
plt.yticks(rotation=0)
plt.tight_layout()

plt.subplots_adjust(
    top=0.90,
    left=0.1,
    right=0.98,
    bottom=.2,
    hspace=0.90,
    wspace=0.30
)
plt.savefig("images/HeatmapFH.png",
            dpi=300,
            bbox_inches="tight")
plt.show()

# *******************3 Data Cleaning & Feature Encoding*******************
# Create a copy of the dataset for data cleaning
df_cleaned=df.copy()
print(df_cleaned.drop_duplicates())

# WRONG VALUE CHECKING
# 1-Can a person have a resting BP 0? --> NO [Visualize through graph]
# As 1 people have 0 RestingBP, so calculate mean for value other than 0 and round it to 2 decimal places
RestBP_mean=round(df.loc[df["RestingBP"]!=0,"RestingBP"].mean(),2)
# Replace 0 values with the rounded mean
df_cleaned["RestingBP"] = df_cleaned["RestingBP"].replace(0, RestBP_mean)

# 1-Can a person have a Cholesterol 0? --> NO [Visualize through graph]
# As 172 people have 0 Cholesterol, so calculate mean for those value other than 0 and round it to 2 decimal places
Chtrol_mean=round(df.loc[df["Cholesterol"]!=0,"Cholesterol"].mean(),2)
# Replace 0 values with the rounded mean
df_cleaned["Cholesterol"] = df_cleaned["Cholesterol"].replace(0, Chtrol_mean)

# # Visualize again data after removing wrong values
plotting_histogram(df_cleaned)

# Encoding
# Label Encoding for Gender & ExerciseAngina
le_gender = LabelEncoder()
le_angina = LabelEncoder()
df_cleaned["Gender"]=le_gender.fit_transform((df_cleaned["Gender"]))
df_cleaned["ExerciseAngina"]=le_angina.fit_transform(df_cleaned["ExerciseAngina"])

# One-Hot Encoding  for all categorical columns
df_cleaned=pd.get_dummies(df_cleaned,drop_first=True,dtype=int)

# *******************4 Feature Selection & Statistical Analysis*******************
selected_features = {'Age', 'Gender', 'RestingBP', 'Cholesterol', 'FastingBS', 'MaxHR',
       'ExerciseAngina', 'Oldpeak', 'ChestPainType_ATA',
       'ChestPainType_NAP', 'ChestPainType_TA', 'RestingECG_Normal',
       'RestingECG_ST', 'ST_Slope_Flat', 'ST_Slope_Up'}

# Store Pearson correlation values in a dictionary
correlations = {
                  feature:pearsonr(df_cleaned[feature],df_cleaned["HeartDisease"])[0]
                for feature in selected_features
}
# Convert dictionary to DataFrame
correlations_df = pd.DataFrame(list(correlations.items()),columns=["Feature","Pearson Correlation"])

# Sort features by correlation value
correlations_df.sort_values(by="Pearson Correlation",ascending=False,inplace=True)

# Categorical features
cat_features = ["Gender", "FastingBS", "ExerciseAngina", "ChestPainType_ATA", "ChestPainType_NAP", "ChestPainType_TA",
                "RestingECG_Normal", "RestingECG_ST", "ST_Slope_Flat", "ST_Slope_Up"]

# Chi-Square Tes to Compare categories
alpha = 0.05

chi2_results = {}

for col in cat_features:
    contingency = pd.crosstab(df_cleaned[col], df_cleaned['HeartDisease'])
    chi2_stat, p_val, _, _ = chi2_contingency(contingency)
    decision = 'Reject Null (Keep Feature)' if p_val < alpha else 'Accept Null (Drop Feature)'
    chi2_results[col] = {
        'chi2_statistic': chi2_stat,
        'p_value': p_val,
        'Decision': decision
    }
# Convert Chi-Square results into a DataFrame
chi2_df = pd.DataFrame(chi2_results).T
chi2_df = chi2_df.sort_values(by='p_value')

# *******************5 Model Training & Evaluation*******************
X = df_cleaned.drop(["HeartDisease"], axis=1)
Y = df_cleaned["HeartDisease"]

# Split the dataset into training and testing sets
X_train, X_test, Y_train, Y_test  = train_test_split(
    X, Y, test_size=0.20, random_state=42, stratify=Y )

param_grid = {
    "criterion": ["gini", "entropy", "log_loss"],
    "max_depth": [None, 5, 10, 15, 20],
    "min_samples_split": [2, 5, 10],
    "min_samples_leaf": [1, 2, 4],
    "max_features": [None, "sqrt", "log2"]
}

# Grid Search
grid = GridSearchCV(
    estimator=DecisionTreeClassifier(random_state=42),
    param_grid=param_grid,
    cv=10,      #cv=5,
    scoring="accuracy",
    n_jobs=-1
)

# Train
grid.fit(X_train, Y_train)

# Best model
dt = grid.best_estimator_

# Display best parameters
print("Best Parameters:")
print(grid.best_params_)

print(f"\nBest Cross Validation Accuracy = {grid.best_score_:.4f}")

print("\nBest Decision Tree Model")
print(dt)

# Prediction
Y_pred_test = dt.predict(X_test)

# Model evaluation
accuracy=accuracy_score(Y_test, Y_pred_test)
print(f"Accuracy = {accuracy}")

conf_matrix=confusion_matrix(Y_test, Y_pred_test)
print(f"confusion_matrix = {conf_matrix}")

clf_report=classification_report(Y_test, Y_pred_test,output_dict=True)
print(f"Clf_report = {clf_report}")

metrics = {
    "accuracy": accuracy,
    "precision": clf_report["weighted avg"]["precision"],
    "recall": clf_report["weighted avg"]["recall"],
    "f1_score": clf_report["weighted avg"]["f1-score"]
}

joblib.dump(metrics, "cardio_metrics.pkl")

feature_importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": dt.feature_importances_
})

feature_importance = feature_importance.sort_values(
    by="Importance",
    ascending=False
)

print("\nFeature Importance")
print(feature_importance)

# *******************6 Model Performance Visualization*******************
# *******************6.1 Confusion Matrix Heatmap
fig, ax = plt.subplots(figsize=(7, 5))
# Title of the window
fig.canvas.manager.set_window_title("Confusion Matrix_Cardio Prediction System")
sns.heatmap(
    conf_matrix,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=["No Disease", "Heart Disease"],
    yticklabels=["No Disease", "Heart Disease"]
)

plt.title("Decision Tree Confusion Matrix")
plt.xlabel("Predicted Label")
plt.ylabel("True Label")

plt.tight_layout()
plt.savefig("images/conf_mtxFH.png",
            dpi=300,
            bbox_inches="tight")
plt.show()

# *******************6.2 Feature Importance Plot
fig=plt.figure(figsize=(10,6))
# Title of the window
fig.canvas.manager.set_window_title("Feature Importance Plot_Cardio Prediction System")

plt.barh(
    feature_importance["Feature"],
    feature_importance["Importance"]
)

plt.title("Decision Tree Feature Importance")
plt.xlabel("Importance")
plt.ylabel("Features")

plt.tight_layout()
plt.savefig("images/featuresFH.png",
            dpi=300,
            bbox_inches="tight")
plt.show()

# *******************6.3 Decision Tree Visualization
# fig=plt.figure(figsize=(35,20))
fig=plt.figure(figsize=(50,25))
# Title of the window
fig.canvas.manager.set_window_title("Decision Tree Visualization_Cardio Prediction System")

plot_tree(
    dt,
    feature_names=X.columns,
    class_names=["No Disease", "Heart Disease"],
    filled=True,
    rounded=True,
    fontsize=5
)

plt.title("Decision Tree Classifier")
plt.savefig("images/dt_clfFH.png",
            dpi=300,
            bbox_inches="tight")
plt.show()

#  Save Model
joblib.dump(dt, "cardio_predict.pkl")
print("Model saved successfully.")

# Save Feature Columns
joblib.dump(X.columns.tolist(), "cardio_columns.pkl")
print("Feature columns saved successfully.")

# Save Label Encoders
label_encoders = {
    "Gender": le_gender,
    "ExerciseAngina": le_angina
}

joblib.dump(label_encoders, "label_encoders.pkl")
print("Label encoders saved successfully.")