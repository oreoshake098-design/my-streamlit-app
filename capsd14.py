import pandas as pd 
data = { 
"Name": ["Aman", "Diya", "Rahul", "Sneha", "Aman"], 
"Marks": [78, None, 85, 67, 78] 
} 
df = pd.DataFrame(data) 
print("Original Dataset:") 
print(df) 
# Identify missing values 
print("\nMissing Values:") 
print(df.isnull().sum()) 
# Replace missing Marks with mean 
df["Marks"] = df["Marks"].fillna(df["Marks"].mean()) 
# Remove duplicate rows 
df = df.drop_duplicates() 
# Convert names to uppercase 
df["Name"] = df["Name"].str.upper() 
# Rename Marks to Score 
df.rename(columns={"Marks": "Score"}, inplace=True) 
print("\nCleaned Dataset:") 
print(df)