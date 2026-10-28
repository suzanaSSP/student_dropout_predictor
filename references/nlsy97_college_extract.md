# NLSY97 college extract

Source: [NLS Investigator](https://nlsinfo.org/investigator/pages/search), NLSY97 public-use release covering 1997–2023 (rounds 1–21), released January 23, 2026. Downloaded as a guest in October 2026. The original generated archive is `C:\Users\tseba\Downloads\default (1).zip`.

- Raw data: [`data/external/nlsy97_college_1997_2023.csv`](../data/external/nlsy97_college_1997_2023.csv) — 8,984 respondents × 45 columns, one row per respondent.
- Readable headers: [`data/interim/nlsy97_college_1997_2023_named.csv`](../data/interim/nlsy97_college_1997_2023_named.csv) — the same records and values, with 45 descriptive column names. Rebuild with `python competitions/rename_nlsy97_columns.py`; the [script](../competitions/rename_nlsy97_columns.py) contains the complete ID-to-name mapping.
- [Codebook](nlsy97_college_1997_2023.cdb) — question wording, response codes, and field-specific missingness.
- [Tagset](nlsy97_college_1997_2023.NLSY97) — selected NLS variable IDs for rebuilding the extract.

The raw CSV headers are NLS reference numbers. Key fields:

| Field | Meaning |
| --- | --- |
| `R0000100` | Respondent ID (`PUBID`) |
| `R0536300`, `R0536401`, `R0536402`, `R1482600` | Sex, birth month/year, race and ethnicity |
| `R1235800` | Cross-sectional versus oversample membership |
| `S2007701` | Enrollment status at the 2003 interview; codes 9 and 10 mean enrolled at a two- or four-year college |
| `S1999000`–`S1999400` | 2003 college type for school roster slots 01–05 |
| `S2004400`–`S2004700`, `S2004900`–`S2005300` | 2003 fraction of associate's/bachelor's credits earned, by school roster slot |
| `B0047900` | First term GPA in the postsecondary transcript study |
| `U6356200` | Enrollment status at the 2023 interview |
| `Z9083900`, `Z9084300`, `Z9084400` | Highest degree and dates of first associate's and bachelor's degrees, cumulative through the respondent's most recent interview |

Enrollment status is included for every survey round from 1997 through 2023. The edited enrollment fields replace the older versions for 1998–2004.

## Modeling implications

The 2003 enrollment field identifies 2,563 respondents observed in a two- or four-year college (801 and 1,762, respectively). Of these, 587 had no postsecondary degree in the cumulative degree field; 403 of those were also observed as not enrolled in 2023. These are **candidate noncompletion groups**, not a verified dropout label. A person can stop out, transfer, earn a later degree, or have an outdated cumulative record after missing an interview. Define the cohort, prediction date, follow-up window, and outcome before training.

NLS missing codes `-1` through `-5` have different meanings; consult the codebook rather than treating them as numeric values. GPA has two implied decimal places (`242` means 2.42) and is available for 3,478 respondents. Credit fractions also have two implied decimal places (`50` means 0.50). Transcript data cover a selected subset, so missing GPA is not evidence of poor performance. Survey weights are not included in this extract; add suitable weights before making population estimates.

The participants were born in 1980–1984. This is a US longitudinal cohort, not a sample of students entering college in 2023. See the [NLS college experience guide](https://nlsinfo.org/content/cohorts/nlsy97/topical-guide/education/college-experience) and [transcript study documentation](https://www.nlsinfo.org/content/cohorts/nlsy97/other-documentation/codebook-supplement/appendix-12-post-secondary-transcript-study).
