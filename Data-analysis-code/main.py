import pandas as pd                #library use for data reading , claning and analyze.
import matplotlib.pyplot as plt     # metaplotlib module for making graph and chart.

# Read Employee Data
df = pd.read_csv("employees.csv")   #csv file ko read karne ka pandas function
print("Employee Data:") #csv file name
print(df) #stored employee data in data frame

# Data Cleaning

df["Salary"] = pd.to_numeric(df["Salary"], errors="coerce") #pd.to- value in number,coerce agar koi value num me convert nhi,to iska use

# Remove duplicate employees
before = len(df)             #count total rows
df = df.drop_duplicates(subset="Emp_ID")  #drop duplicate duplicate remove,emp id employee id ke basis pe duplicate check kar
after = len(df)

print("Duplicates removed:", before - after)

# Calculate average salary
average_salary = df["Salary"].mean() #df salary salary column select karta hai

# Fill missing salary
df["Salary"] = df["Salary"].fillna(average_salary)  #.fillna missing values fill karna

# Save cleaned data
df.to_csv("cleaned_employees.csv", index=False) #to csv-data frame ko csv file me save,cleaned-otput file name

print("Data Cleaning Completed!")
print(df)
print("Cleaned data saved successfully!")
# Employee Summary Analysis

print("\n===== EMPLOYEE SUMMARY =====")

# Total number of employees
total_employees = len(df) #tot-variable name
print("Total Employees:", total_employees)

# Average salary
average_salary = df["Salary"].mean()
print("Average Salary:", round(average_salary, 2))

# Highest salary
highest_salary = df["Salary"].max()
print("Highest Salary:", highest_salary)

# Employee with highest salary
highest_paid_employee = df.loc[df["Salary"].idxmax()]

print("Highest Paid Employee:",
      highest_paid_employee["Name"])

# Total payroll
total_payroll = df["Salary"].sum() #df-emplyee data
print("Total Payroll:", total_payroll)
# Department-wise Analysis

print("\n===== DEPARTMENT-WISE ANALYSIS =====")

department_analysis = df.groupby("Department").agg(   #employee ko department ke according grp me divide kar,agg-for calculation
    Total_Employees=("Emp_ID", "count"),
    Average_Salary=("Salary", "mean")
)

print(department_analysis)

# Salary Filtering

print("\n===== SALARY FILTERING =====")

salary_limit = float(input("Enter minimum salary limit: "))

filtered_employees = df[df["Salary"] > salary_limit] #salary limit-user ki entered limit,filtered-matching employee store kar

if len(filtered_employees) > 0:
    print("\nEmployees earning above", salary_limit)
    print(filtered_employees)
else:
    print("No employees found above this salary limit.")

    # Graphical Analysis

print("\n===== GRAPHICAL ANALYSIS =====")

department_salary = df.groupby("Department")["Salary"].mean()

plt.figure(figsize=(8, 5)) #graph fig create

department_salary.plot(kind="bar", color="skyblue") #.plot-graph create,kind-bar - bar graph draw

plt.title("Department-wise Average Salary")
plt.xlabel("Department")
plt.ylabel("Average Salary")

plt.xticks(rotation=0) #x axis ke label control
plt.tight_layout() #graph ke label aur tittle ko properly fit karne me help karta hai

plt.show() # graph show karta hai