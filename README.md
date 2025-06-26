# Capstone Project: Prison to Profession

This project uses three datasets to explore occupational opportunities and demographics for formerly incarcerated individuals. Below are detailed documentation sections for both datasets used.

---

## Dataset 1: ACS Microdata (acs_raw.csv)

### Data Dictionary

| Column | Description |
|--------|-------------|
| OCCP   | Occupation code (Census occupation classification) |
| AGEP   | Age of the individual |
| SEX    | Sex (1 = Male, 2 = Female) |
| RAC1P  | Race (Census-defined race codes) |
| HISP   | Hispanic origin (Census-defined codes) |
| SCHL   | Educational attainment (coded by highest level completed) |
| STATE  | State FIPS code |
| PUMA   | Public Use Microdata Area code |
| ESR    | Employment status recode |
| WAGP   | Wage and salary income in past 12 months |
| COW    | Class of worker |
| WKHP   | Usual hours worked per week |

### Data Summary

- **Total Rows:** 224,220  
- **Total Columns:** 12  
- **Missing Values:** Several columns have missing data, especially `OCCP`, `COW`, `WKHP`, and `ESR`, reflecting incomplete responses or non-working individuals.
- **Demographics:** Includes a wide age range and diverse racial/ethnic identities.
- **Employment:** `WAGP` and `ESR` allow analysis of wages and employment status, particularly relevant for economic outcomes post-incarceration.
- **Integration:** Will join to the main Occupational Outlook dataset using an `occupation` column where job codes are mapped using a crosswalk.


### Data Source

American Community Survey (ACS) Public Use Microdata 5-year Sample (PUMS) from the U.S. Census Bureau.  
- Accessed via: https://www.census.gov/programs-surveys/acs/microdata.html](https://www2.census.gov/programs-surveys/acs/data/pums/2023/5-Year/csv_pus.zip

---

## Dataset 2: Kentucky Center for Statistics (KY STATS) Occupational Outlook-2022 to 2032 (oo_raw.xlsx)

### Data Dictionary

| Column | Description |
|--------|-------------|
| Area Name | Name of the geographic area (e.g., Kentucky, Workforce Region) |
| Area Type | Type of geographic area (e.g., Statewide, Workforce Area) |
| SOC Title | Name/title of the occupation |
| Standard Occupational Classification (SOC) | Detailed SOC code |
| SOC Major Group | Two-digit SOC code representing occupational group |
| SOC Classification | Text label describing the SOC classification |
| 2022 Estimated Employment | Estimated number of employed individuals in 2022 |
| 2032 Projected Employment | Projected number of employed individuals in 2032 |
| Change | Numerical change in employment from 2022 to 2032 |
| Percent Change | Percent change in employment over the 10-year span |
| Annualized Percent Growth (Grow Rate) | Yearly average percent growth |
| Exits | Number of workers expected to leave the occupation |
| Transfers | Number of workers transferring to different occupations |
| Openings | Total projected annual job openings |
| Mean Annual | Mean annual wage |
| Entry Annual | Estimated entry-level annual wage |
| 25th Percentile Annual | 25th percentile wage |
| Median Annual | Median (50th percentile) wage |
| 75th Percentile Annual | 75th percentile wage |
| Experienced Annual | Estimated experienced-level wage |
| Typical Education Required for Entry | Typical education level required to enter the occupation |
| Typical Work Experience Required in Related Occupation | Prior experience typically required |
| Typical On-the-Job Training Required to Achieve Competency | Training required to reach full competence |

### Data Summary

- **Total Rows:** 5,245  
- **Total Columns:** 23  
- **Occupational Coverage:** Covers a wide range of occupations across Kentucky with projections through 2032.
- **Wage Data:** Comprehensive wage data including percentiles, entry, and experienced wages.
- **Training & Education:** Includes education level and training requirements for each occupation.
- **Missing Values:** Some fields (e.g., `SOC Classification`, `Work Experience`, and `On-the-Job Training`) have missing values, especially for aggregated or undefined roles.
- **Integration:** Will join to the main ACS dataset using an `occupation` column where job codes are mapped using a crosswalk.

### Data Source

Kentucky Center for Statistics (KYSTATS) - Occupational Outlook Tool  
- Accessed via: https://kystats.ky.gov/Latest/OCC

---

---

## Dataset 3: ACS Housing Type by PUMA (puma_raw.csv)

### Data Dictionary

| Column    | Description |
|-----------|-------------|
| SERIALNO  | Unique housing unit identifier |
| TYPEHUGQ  | Type of housing unit or group quarters (e.g., household, institutional, non-institutional) |

### Data Summary

- **Total Rows:** 22,482  
- **Total Columns:** 2  
- **Purpose:** Used to determine whether each housing unit is part of the institutional or non-institutional group quarters population, which includes incarcerated individuals.
- **Missing Values:** None. All rows have valid entries for both columns.
- **Integration:** Will join to the main ACS dataset using the `SERIALNO` column.

### Data Source

American Community Survey (ACS) Public Use Microdata 5-year Sample (PUMS) — Housing Unit Records  
- Accessed via: [https://www.census.gov/programs-surveys/acs/microdata.html](https://www2.census.gov/programs-surveys/acs/data/pums/2023/5-Year/csv_hus.zip)
