import pandas as pd
import matplotlib.pyplot as plt

# Read Employee Data
df = pd.read_csv("employees.csv")

print("Employee Data:")
print(df)

# Data Cleaning
df["Salary"] = pd.to_numeric(df["Salary"], errors="coerce")

before = len(df)
df = df.drop_duplicates(subset="Emp_ID")
after = len(df)

print("Duplicates removed:", before - after)

average_salary = df["Salary"].mean()
df["Salary"] = df["Salary"].fillna(average_salary)

df.to_csv("cleaned_employees.csv", index=False)

print("Data Cleaning Completed!")
print(df)
print("Cleaned data saved successfully!")

# Employee Summary Analysis
print("\n===== EMPLOYEE SUMMARY =====")

total_employees = len(df)
print("Total Employees:", total_employees)

average_salary = df["Salary"].mean()
print("Average Salary:", round(average_salary, 2))

highest_salary = df["Salary"].max()
print("Highest Salary:", highest_salary)

highest_paid_employee = df.loc[df["Salary"].idxmax()]
print("Highest Paid Employee:", highest_paid_employee["Name"])

total_payroll = df["Salary"].sum()
print("Total Payroll:", total_payroll)

# Department-wise Analysis
print("\n===== DEPARTMENT-WISE ANALYSIS =====")

department_analysis = df.groupby("Department").agg(
    Total_Employees=("Emp_ID", "count"),
    Average_Salary=("Salary", "mean")
)

print(department_analysis)

# Salary Filtering
print("\n===== SALARY FILTERING =====")

salary_limit = float(input("Enter minimum salary limit: "))

filtered_employees = df[df["Salary"] > salary_limit]

if len(filtered_employees) > 0:
    print("\nEmployees earning above", salary_limit)
    print(filtered_employees)
else:
    print("No employees found above this salary limit.")

# Graphical Analysis
print("\n===== GRAPHICAL ANALYSIS =====")

department_salary = df.groupby("Department")["Salary"].mean()

plt.figure(figsize=(8, 5))
department_salary.plot(kind="bar", color="skyblue")

plt.title("Department-wise Average Salary")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()