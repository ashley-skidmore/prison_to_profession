# Prison to Profession

This project explores the intersection of incarceration, education, and employment opportunities in Kentucky. By analyzing demographic microdata and occupational projections, the project highlights how educational attainment among incarcerated individuals aligns--or fails to align—-with high-demand, high-wage jobs in the state.

## Project Setup Instructions

Follow these steps to set up and run this project on your own computer. No prior coding experience is required.

### 1. Open a Terminal or Command Prompt

- **On Windows:** Press the Windows key, type `cmd`, and press Enter to open the Command Prompt.
- **On Mac:** Open the Terminal app (found in Applications > Utilities).
- **On Linux:** Open your Terminal from the Applications menu.

### 2. Clone the Project Repository

Type the following commands into the terminal window:

git clone https://github.com/ashley-skidmore/prison_to_profession
cd prison_to_profession

This downloads the project files onto your computer.

### 3. Create a Virtual Environment

A virtual environment keeps your project’s packages organized and separate from other programs. In the terminal window, enter:

**On Windows:**
python -m venv venv
venv\Scripts\activate

**On Mac/Linux:**
python3 -m venv venv
source venv/bin/activate

### 4. Install Required Packages

With the virtual environment active, install the required tools by entering:

pip install -r requirements.txt

### 5. Launch the Project in Jupyter Notebook

In the same terminal or command prompt, enter the following command:

jupyter notebook

After a few seconds, your default web browser will open automatically and show a list of project files.

If your browser doesn’t open automatically, copy the link shown in the terminal (it usually starts with `http://localhost:`) and paste it into your browser’s address bar.

## Project Overview

This project examines how the educational attainment of incarcerated individuals in Kentucky compares to the education typically required for high-wage, high-demand jobs in the state.

Using public microdata from the U.S. Census Bureau and labor market projections from the Kentucky Center for Statistics, the analysis identifies broad gaps between current education levels in the incarcerated population and the general qualifications needed to access stable, well-paying careers.

By cleaning, merging, and analyzing multiple datasets, the project helps highlight the need for expanded prison education programs as a way to improve economic mobility and reduce recidivism.

The repository is organized as follows:
- `data/`: Raw and cleaned datasets in CSV and SQLite format  
- `notebooks/`: Jupyter Notebooks for cleaning, analysis, and visualizations  
- `plots/`: Saved charts used in the dashboard and final report  
- `deliverables/`: Final project summary, presentation, and dashboard
- `docs/`: Reference materials, including the Census Bureau data dictionary, census data README, and a job code crosswalk
- `main.ipynb`: Jupyter Notebook where cleaned data is merged and visualized

The results are presented in an interactive Tableau dashboard designed for policymakers, educators, and the general public.

## Tableau Dashboard

Explore the interactive dashboard here:  
**[Prison to Profession – Tableau Public](https://public.tableau.com/app/profile/ashley.skidmore/viz/prison_to_profession_dashboard/PrisontoProfession)**

## Technologies Used

- **Jupyter Notebook**  
  Used to document the entire data cleaning and analysis process in a step-by-step, interactive format.

- **Python**  
  The main programming language used for all data processing and analysis tasks.

- **Pandas**  
  Used extensively to load, clean, transform, and merge datasets.

- **NumPy**  
  Helped with simple math operations and made it easier to work with numeric data.

- **Matplotlib**  
  Provided plotting functionality and was used for custom-styled visualizations throughout the project.

- **Seaborn**  
  Used alongside Matplotlib to create informative and aesthetically pleasing data visualizations.

- **Plotly Express**  
  Used to make an interactive scatterplot.

- **Plotly Graph Objects**  
  Helped customize the scatterplot by adding hover text, adjusting layout, and making the chart easier to read.

- **SQLite**  
  Used to store cleaned data and join datasets efficiently.

- **OS**  
  Used to manage file paths and ensure plots were saved to the correct directories.

- **Sys**  
 Helped the notebooks find and use shared functions saved in a different folder.

- **Typing**  
   Helped label what kind of input each function expects, which makes the code easier to understand.

---

## Dataset 1: ACS Demographic Microdata (acsd_raw.csv)

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
- **Total Columns:** 13  
- **Missing Values:** Several columns have missing data, especially `OCCP`, `COW`, `WKHP`, and `ESR`, reflecting incomplete responses or non-working individuals.
- **Demographics:** Includes a wide age range and diverse racial/ethnic identities.
- **Employment:** `WAGP` and `ESR` allow analysis of wages and employment status, particularly relevant for economic outcomes post-incarceration.
- **Integration:** Will join to the main Occupational Outlook dataset using an `occupation` column where job codes are mapped using a crosswalk.


### Data Source

American Community Survey (ACS) Public Use Microdata 5-year Sample (PUMS) from the U.S. Census Bureau.  
- Accessed via: [https://www.census.gov/programs-surveys/acs/microdata.html](https://www2.census.gov/programs-surveys/acs/data/pums/2023/5-Year/csv_pus.zip)

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

## Dataset 3: ACS Housing Microdata (acsh_raw.csv)

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