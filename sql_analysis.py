import pandas as pd
import sqlite3


# ============================================================
# STEP 1: LOAD CLEANED DATA
# ============================================================

df = pd.read_csv("HR_applicants_cleaned.csv")


# ============================================================
# STEP 2: CREATE SQLITE DATABASE
# ============================================================

connection = sqlite3.connect("hr_recruitment.db")


# ============================================================
# STEP 3: IMPORT DATA INTO SQL TABLE
# ============================================================

df.to_sql(
    "applicants",
    connection,
    if_exists="replace",
    index=False
)

print("\n======================================")
print("DATA IMPORTED INTO SQL")
print("======================================")


# ============================================================
# QUERY 1: TOTAL NUMBER OF APPLICANTS
# ============================================================

query1 = """
SELECT COUNT(*) AS total_applicants
FROM applicants;
"""

result1 = pd.read_sql_query(query1, connection)

print("\n1. TOTAL APPLICANTS")
print(result1)


# ============================================================
# QUERY 2: APPLICANTS BY DEPARTMENT
# ============================================================

query2 = """
SELECT
    department,
    COUNT(*) AS applicant_count
FROM applicants
GROUP BY department
ORDER BY applicant_count DESC;
"""

result2 = pd.read_sql_query(query2, connection)

print("\n2. APPLICANTS BY DEPARTMENT")
print(result2)


# ============================================================
# QUERY 3: FINAL STATUS DISTRIBUTION
# ============================================================

query3 = """
SELECT
    final_status,
    COUNT(*) AS applicant_count
FROM applicants
GROUP BY final_status
ORDER BY applicant_count DESC;
"""

result3 = pd.read_sql_query(query3, connection)

print("\n3. FINAL STATUS DISTRIBUTION")
print(result3)


# ============================================================
# QUERY 4: AVERAGE TECHNICAL AND HR SCORE
# ============================================================

query4 = """
SELECT
    ROUND(AVG(technical_score), 2) AS avg_technical_score,
    ROUND(AVG(hr_score), 2) AS avg_hr_score
FROM applicants;
"""

result4 = pd.read_sql_query(query4, connection)

print("\n4. AVERAGE SCORES")
print(result4)


# ============================================================
# QUERY 5: AVERAGE SCORES BY DEPARTMENT
# ============================================================

query5 = """
SELECT
    department,
    ROUND(AVG(technical_score), 2) AS avg_technical_score,
    ROUND(AVG(hr_score), 2) AS avg_hr_score
FROM applicants
GROUP BY department
ORDER BY avg_technical_score DESC;
"""

result5 = pd.read_sql_query(query5, connection)

print("\n5. AVERAGE SCORES BY DEPARTMENT")
print(result5)


# ============================================================
# QUERY 6: OFFERS BY DEPARTMENT
# ============================================================

query6 = """
SELECT
    department,
    COUNT(*) AS offers
FROM applicants
WHERE final_status = 'Offer'
GROUP BY department
ORDER BY offers DESC;
"""

result6 = pd.read_sql_query(query6, connection)

print("\n6. OFFERS BY DEPARTMENT")
print(result6)


# ============================================================
# QUERY 7: AVERAGE EXPERIENCE BY FINAL STATUS
# ============================================================

query7 = """
SELECT
    final_status,
    ROUND(AVG(experience_years), 2) AS avg_experience
FROM applicants
GROUP BY final_status;
"""

result7 = pd.read_sql_query(query7, connection)

print("\n7. AVERAGE EXPERIENCE BY FINAL STATUS")
print(result7)


# ============================================================
# QUERY 8: AVERAGE SCORES BY FINAL STATUS
# ============================================================

query8 = """
SELECT
    final_status,
    ROUND(AVG(technical_score), 2) AS avg_technical_score,
    ROUND(AVG(hr_score), 2) AS avg_hr_score
FROM applicants
GROUP BY final_status;
"""

result8 = pd.read_sql_query(query8, connection)

print("\n8. SCORES BY FINAL STATUS")
print(result8)


# ============================================================
# QUERY 9: APPLICANTS WITH HIGH TECHNICAL SCORES
# ============================================================

query9 = """
SELECT
    applicant_id,
    applicant_name,
    department,
    technical_score,
    hr_score,
    final_status
FROM applicants
WHERE technical_score >= 90
ORDER BY technical_score DESC, hr_score DESC
LIMIT 10;
"""

result9 = pd.read_sql_query(query9, connection)

print("\n9. TOP TECHNICAL PERFORMERS")
print(result9)


# ============================================================
# QUERY 10: APPLICANTS WITH HIGH EXPERIENCE
# ============================================================

query10 = """
SELECT
    applicant_id,
    applicant_name,
    experience_years,
    department,
    final_status
FROM applicants
WHERE experience_years >= 10
ORDER BY experience_years DESC
LIMIT 10;
"""

result10 = pd.read_sql_query(query10, connection)

print("\n10. EXPERIENCED APPLICANTS")
print(result10)


# ============================================================
# CLOSE DATABASE
# ============================================================

connection.close()


print("\n======================================")
print("SQL ANALYSIS COMPLETED")
print("======================================")