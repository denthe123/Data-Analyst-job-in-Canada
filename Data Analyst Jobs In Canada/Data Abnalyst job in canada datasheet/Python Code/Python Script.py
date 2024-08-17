# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# %%
data = pd.read_csv("Cleaned_Dataset.csv")

# %%
data.head(1)

# %%
data = data[data['Job Title'].str.contains('Data Analyst', case=False, na=False)]
data.head()

# %%
job_title_counts = data['Job Title'].value_counts()
print(job_title_counts)

# %%
avg_salary_by_title = data.groupby('Job Title')['Avg_Salary'].mean()
print(avg_salary_by_title)


# %%
skill_counts = data['Skill'].value_counts()
print(skill_counts)

seniority_counts = data['Seniority'].value_counts()
print(seniority_counts)


# %%
job_titles_by_province = data.groupby('Province')['Job Title'].value_counts()
print(job_titles_by_province)




# %%
job_titles_by_city = data.groupby('City')['Job Title'].value_counts()
print(job_titles_by_city)

# %%
plt.figure(figsize=(10, 6))
sns.barplot(x=avg_salary_by_title.index, y=avg_salary_by_title.values)
plt.xticks(rotation=90)
plt.title('Average Salary by Job Title')
plt.xlabel('Job Title')
plt.ylabel('Average Salary')
plt.show()

# %%
# Calculate average salary by skill
data['Skill'] = data['Skill'].str.split(', ')
data_expanded = data.explode('Skill')

avg_salary_by_skill = data_expanded.groupby('Skill')['Avg_Salary'].mean().sort_values(ascending=False)
print(avg_salary_by_skill)

# %%
top_10_skills = avg_salary_by_skill.head(20)

# Convert Series to DataFrame for plotting
df_top_10_skills = top_10_skills.reset_index()
df_top_10_skills.columns = ['Skill', 'Avg_Salary']

# %%
plt.figure(figsize=(12, 8))
ax = df_top_10_skills.plot(kind='bar', x='Skill', y='Avg_Salary', color='skyblue', legend=False)
plt.title('Top 20 Skills with Highest Average Salaries')
plt.xlabel('Skill')
plt.ylabel('Average Salary')

# %%
df_skills = data[['Job Title', 'Skill']].copy()
df_skills['Skill'] = df_skills['Skill'].str.split(', ')
df_skills = df_skills.explode('Skill')


# %%
df_skills = data_analyst_jobs[['Job Title', 'Skill']].copy()
df_skills['Skill'] = df_skills['Skill'].str.split(', ')

print(df_skills.head())

df_skills = df_skills.explode('Skill')

df_skills['Skill'] = df_skills['Skill'].fillna('No Skill')

df_skills['Skill'] = df_skills['Skill'].astype(str)

print(df_skills.head())

skills_by_job_title = df_skills.groupby('Job Title')['Skill'].apply(lambda x: ', '.join(sorted(set(x)))).reset_index()

print(skills_by_job_title)

output_file_path = 'skills_by_job_title.csv'

skills_by_job_title.to_csv(output_file_path, index=False)

print(f"Data exported to {output_file_path}")

# %%
data.head(1)

# %%
unique_work_types = data['Work Type'].unique()
unique_work_types

# %%
salary_by_work_type = data.groupby('Work Type')['Avg_Salary'].mean()

# %%
plt.figure(figsize=(10, 6))
salary_by_work_type.plot(kind='bar', color='skyblue')
plt.title('Average Salary by Work Type')
plt.xlabel('Work Type')
plt.ylabel('Average Salary')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# %%
unique_position = data['Position'].unique()
unique_position

# %%
salary_by_position = data.groupby('Position')['Avg_Salary'].mean().sort_values()

# %%
plt.figure(figsize=(12, 8))
ax = salary_by_position.plot(kind='bar', color='skyblue')
plt.title('Average Salary by Position')
plt.xlabel('Position')
plt.ylabel('Average Salary')

# %%
unique_industry_type = data['Industry Type'].unique()
unique_industry_type

# %%
salary_by_industry_type = data.groupby('Industry Type')['Avg_Salary'].mean().sort_values()

# %%
plt.figure(figsize=(12, 8))
ax = salary_by_industry_type.plot(kind='bar', color='green')
plt.title('Average Salary by Industry Type')
plt.xlabel('Industry Type')
plt.ylabel('Average Salary')

# %%
unique_employer = data['Employer'].drop_duplicates().tolist()
print(unique_employer)

# %%
unique_employer = data['Employer'].unique()
unique_employer


# %%
top_10_employers = data.nlargest(20, 'Avg_Salary')

# %%
plt.figure(figsize=(16, 12))
ax = top_10_employers.plot(kind='bar', x='Employer', y='Avg_Salary', color='red', legend=False)
plt.title('Top 20 Employers Offering the Highest Salaries')
plt.xlabel('Employer')
plt.ylabel('Average Salary')




# %%
random_10_employers = data.sample(n=10, random_state=1)  

# %%
plt.figure(figsize=(12, 8))
ax = random_10_employers.plot(kind='bar', x='Employer', y='Avg_Salary', color='skyblue', legend=False)
plt.title('Random Sample of 10 Employers with Average Salaries')
plt.xlabel('Employer')
plt.ylabel('Average Salary')



