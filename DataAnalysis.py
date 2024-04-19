import pandas as pd
df = pd.read_csv("healthcare-dataset-stroke-data.csv")

df = df.dropna(subset=["age", "stroke"])

# Finds correlation between age and liklieness of stroke.
correlation = df["age"].corr(df["stroke"])
print("Correlation between age and likelihood of stroke:", correlation)
print("\n")

# Finds the probaility of individuals getting a stroke if they smoke vs if they didn"t
df = df.dropna(subset=["smoking_status", "stroke"])
smokers_stroke_prob = df[df["smoking_status"].isin(["smokes", "formerly smoked"])]["stroke"].mean()
non_smokers_stroke_prob = df[df["smoking_status"].isin(["never smoked"])]["stroke"].mean()
print("Stroke probability for smokers:", smokers_stroke_prob)
print("Stroke probability for non-smokers:", non_smokers_stroke_prob)
print("Smokers are", smokers_stroke_prob / non_smokers_stroke_prob, "times more likely to experience a stroke than non smokers")
print("\n")

#Finds the correlation between BMI and stroke likeliness
df = df.dropna(subset=["bmi", "stroke"])
correlation = df["bmi"].corr(df["stroke"])
print("Correlation between BMI and likelihood of stroke:", correlation)
print("\n")

# Calculate the correlation between hypertension and stroke
correlation = df["hypertension"].corr(df["stroke"])
print("Correlation between hypertension and stroke:", correlation)
print("\n")

# Calculates the correlation between heart_disease and stroke
correlation = df["heart_disease"].corr(df["stroke"])
print("Correlation between heart disease and stroke:", correlation)
