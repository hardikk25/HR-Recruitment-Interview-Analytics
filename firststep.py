import pandas as pd


# ============================================================
# HR RECRUITMENT & INTERVIEW ANALYTICS PROJECT
# ============================================================


# ============================================================
# STEP 1: LOAD THE DATASET
# ============================================================

df = pd.read_csv("HR applicants.csv")

print("\n========== ORIGINAL DATASET ==========")

print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nDataset Information:")
print(df.info())


# ============================================================
# STEP 2: CLEAN COLUMN NAMES
# ============================================================

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace("(", "", regex=False)
    .str.replace(")", "", regex=False)
)

print("\n========== CLEANED COLUMN NAMES ==========")

print(df.columns.tolist())


# ============================================================
# STEP 3: CONVERT INTERVIEW DATE
# ============================================================

df["interview_date"] = pd.to_datetime(df["interview_date"])

print("\n========== DATA TYPES AFTER DATE CONVERSION ==========")

print(df.dtypes)


# ============================================================
# STEP 4: CHECK MISSING VALUES
# ============================================================

print("\n========== MISSING VALUES ==========")

print(df.isnull().sum())


# ============================================================
# STEP 5: CHECK DUPLICATES
# ============================================================

print("\n========== DUPLICATE CHECK ==========")

print("Duplicate rows:", df.duplicated().sum())

print(
    "Duplicate Applicant IDs:",
    df["applicant_id"].duplicated().sum()
)


# ============================================================
# STEP 6: BASIC HR RECRUITMENT KPIs
# ============================================================

print("\n========== RECRUITMENT KPIs ==========")

total_applicants = len(df)

avg_experience = df["experience_years"].mean()

avg_technical = df["technical_score"].mean()

avg_hr = df["hr_score"].mean()


# Candidates who received an offer
offers = (
    df["final_status"]
    .str.lower()
    .eq("offer")
    .sum()
)


# Candidates who were rejected
rejected = (
    df["final_status"]
    .str.lower()
    .eq("rejected")
    .sum()
)


# Candidates still in progress
in_progress = (
    df["final_status"]
    .str.lower()
    .eq("in progress")
    .sum()
)


# Offer rate
offer_rate = (
    offers / total_applicants
) * 100


print("Total Applicants:", total_applicants)

print("Offers:", offers)

print("Rejected:", rejected)

print("In Progress:", in_progress)

print(
    "Offer Rate:",
    round(offer_rate, 2),
    "%"
)

print(
    "Average Experience:",
    round(avg_experience, 2),
    "years"
)

print(
    "Average Technical Score:",
    round(avg_technical, 2)
)

print(
    "Average HR Score:",
    round(avg_hr, 2)
)


# ============================================================
# STEP 7: APPLICANTS BY DEPARTMENT
# ============================================================

print("\n========== APPLICANTS BY DEPARTMENT ==========")

department_applicants = (
    df["department"]
    .value_counts()
)

print(department_applicants)


# ============================================================
# STEP 8: SELECTION RATE BY DEPARTMENT
# ============================================================

print("\n========== SELECTION RATE BY DEPARTMENT ==========")

department_selection = pd.crosstab(
    df["department"],
    df["final_status"],
    normalize="index"
) * 100

print(
    department_selection.round(2)
)


# ============================================================
# STEP 9: AVERAGE SCORES BY DEPARTMENT
# ============================================================

print("\n========== AVERAGE SCORES BY DEPARTMENT ==========")

department_scores = (
    df.groupby("department")[
        [
            "technical_score",
            "hr_score"
        ]
    ]
    .mean()
)

print(
    department_scores.round(2)
)


# ============================================================
# STEP 10: FINAL STATUS ANALYSIS
# ============================================================

print("\n========== FINAL STATUS ==========")

status_count = (
    df["final_status"]
    .value_counts()
)

print(status_count)


# ============================================================
# STEP 11: INTERVIEW ROUND ANALYSIS
# ============================================================

print("\n========== APPLICANTS BY INTERVIEW ROUND ==========")

round_count = (
    df["interview_round"]
    .value_counts()
)

print(round_count)


print("\n========== SCORES BY INTERVIEW ROUND ==========")

round_scores = (
    df.groupby("interview_round")[
        [
            "technical_score",
            "hr_score"
        ]
    ]
    .mean()
)

print(
    round_scores.round(2)
)


# ============================================================
# STEP 12: LOCATION ANALYSIS
# ============================================================

print("\n========== APPLICANTS BY LOCATION ==========")

location_count = (
    df["location"]
    .value_counts()
)

print(location_count)


# ============================================================
# STEP 13: EXPERIENCE ANALYSIS
# ============================================================

print("\n========== EXPERIENCE STATISTICS ==========")

print(
    df["experience_years"].describe()
)


# ============================================================
# STEP 14: TOP PERFORMING APPLICANTS
# ============================================================

print("\n========== TOP 10 APPLICANTS ==========")

top_applicants = (
    df.sort_values(
        by=["technical_score", "hr_score"],
        ascending=False
    )
    .head(10)
)

print(
    top_applicants[
        [
            "applicant_id",
            "applicant_name",
            "technical_score",
            "hr_score",
            "final_status"
        ]
    ]
)


# ============================================================
# STEP 15: SAVE CLEANED DATA
# ============================================================

df.to_csv(
    "HR_applicants_cleaned.csv",
    index=False
)

print("\n========== CLEANED DATASET SAVED ==========")

print(
    "Cleaned dataset saved as: "
    "HR_applicants_cleaned.csv"
)


# ============================================================
# STEP 16: EXPERIENCE VS FINAL STATUS
# ============================================================

print("\n========== EXPERIENCE VS FINAL STATUS ==========")

experience_status = (
    df.groupby("final_status")["experience_years"]
    .mean()
)

print(
    experience_status.round(2)
)


# ============================================================
# STEP 17: SCORES VS FINAL STATUS
# ============================================================

print("\n========== SCORES VS FINAL STATUS ==========")

status_scores = (
    df.groupby("final_status")[
        [
            "technical_score",
            "hr_score"
        ]
    ]
    .mean()
)

print(
    status_scores.round(2)
)


# ============================================================
# STEP 18: EDUCATION VS FINAL STATUS
# ============================================================

print("\n========== EDUCATION VS FINAL STATUS ==========")

education_status = pd.crosstab(
    df["education"],
    df["final_status"]
)

print(education_status)


# ============================================================
# END OF PYTHON EDA STAGE
# ============================================================

print("\n========== STEPS 1-18 COMPLETED ==========")

print("HR Recruitment Analytics basic analysis completed.")