import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("employees.csv")

# 1. BAR CHART
avg_salary = df.groupby("department")["salary"].mean()

plt.figure(figsize=(8, 5))

bars = plt.bar(avg_salary.index, avg_salary.values,
               color="skyblue", edgecolor="black")

plt.title("Average Salary per Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")

for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2,
             height, f"{height:.0f}",
             ha="center", va="bottom")

plt.tight_layout()
plt.savefig("average_salary.png")
plt.show()


# 2. HISTOGRAM
plt.figure(figsize=(8, 5))

plt.hist(df["salary"], bins=5,
         color="orange", edgecolor="black")

plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")

plt.tight_layout()
plt.savefig("salary_histogram.png")
plt.show()


# 3. SCATTER PLOT
plt.figure(figsize=(8, 5))

for department in df["department"].unique():
    data = df[df["department"] == department]

    plt.scatter(data["id"], data["salary"],
                label=department)

plt.title("Employee ID vs Salary")
plt.xlabel("Employee ID")
plt.ylabel("Salary")
plt.legend(title="Department")

plt.tight_layout()
plt.savefig("id_vs_salary.png")
plt.show()


# 4. LINE CHART
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [12, 15, 14, 18, 22, 25]

plt.figure(figsize=(8, 5))

plt.plot(months, sales, marker="o",
         color="green", label="Monthly Sales")

plt.title("Monthly Sales (Jan to Jun)")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig("monthly_sales.png")
plt.show()

print("All 4 charts created successfully!")