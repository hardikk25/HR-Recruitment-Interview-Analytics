import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# LOAD CLEANED DATA
# ============================================================

df = pd.read_csv("HR_applicants_cleaned.csv")

df["interview_date"] = pd.to_datetime(df["interview_date"])


# ============================================================
# CHART 1: APPLICANTS BY DEPARTMENT
# ============================================================

department_count = df["department"].value_counts()

plt.figure(figsize=(8, 5))

department_count.plot(kind="bar")

plt.title("Applicants by Department")
plt.xlabel("Department")
plt.ylabel("Number of Applicants")

plt.xticks(rotation=0)

plt.tight_layout()

plt.show()


# ============================================================
# CHART 2: FINAL STATUS DISTRIBUTION
# ============================================================

status_count = df["final_status"].value_counts()

plt.figure(figsize=(8, 5))

status_count.plot(kind="bar")

plt.title("Applicant Final Status")
plt.xlabel("Final Status")
plt.ylabel("Number of Applicants")

plt.xticks(rotation=0)

plt.tight_layout()

plt.show()


# ============================================================
# CHART 3: AVERAGE SCORES BY FINAL STATUS
# ============================================================

status_scores = df.groupby("final_status")[
    ["technical_score", "hr_score"]
].mean()

status_scores.plot(
    kind="bar",
    figsize=(9, 5)
)

plt.title("Average Technical and HR Scores by Final Status")
plt.xlabel("Final Status")
plt.ylabel("Average Score")

plt.xticks(rotation=0)

plt.legend(
    ["Technical Score", "HR Score"]
)

plt.tight_layout()

plt.show()


# ============================================================
# CHART 4: APPLICANTS BY LOCATION
# ============================================================

location_count = df["location"].value_counts()

plt.figure(figsize=(9, 5))
location_count.plot(kind="bar")

plt.title("Applicants by Location")
plt.xlabel("Location")
plt.ylabel("Number of Applicants")
plt.xticks(rotation=45)

plt.tight_layout()

plt.show()


# ============================================================
# CHART 5: EXPERIENCE DISTRIBUTION
# ============================================================

plt.figure(figsize=(8, 5))

plt.hist(
    df["experience_years"],
    bins=15
)

plt.title("Experience Distribution of Applicants")
plt.xlabel("Experience (Years)")
plt.ylabel("Number of Applicants")

plt.tight_layout()

plt.show()