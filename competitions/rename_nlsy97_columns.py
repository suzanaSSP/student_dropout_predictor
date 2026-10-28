"""Give the NLSY97 college extract readable column names without changing its values."""

import csv
from pathlib import Path


COLUMN_NAMES = {
    "B0047900": "transcript_term_01_gpa_raw",
    "R0000100": "respondent_id",
    "R0536300": "sex_1997",
    "R0536401": "birth_month",
    "R0536402": "birth_year",
    "R1201400": "enrollment_status_1997",
    "R1235800": "sample_type_1997",
    "R1482600": "race_ethnicity_1997",
    "R2560001": "enrollment_status_1998",
    "R3881501": "enrollment_status_1999",
    "R5460601": "enrollment_status_2000",
    "R7224201": "enrollment_status_2001",
    "S1538001": "enrollment_status_2002",
    "S1999000": "college_type_2003_school_01",
    "S1999100": "college_type_2003_school_02",
    "S1999200": "college_type_2003_school_03",
    "S1999300": "college_type_2003_school_04",
    "S1999400": "college_type_2003_school_05",
    "S2004400": "associates_credit_fraction_2003_school_01_raw",
    "S2004500": "associates_credit_fraction_2003_school_02_raw",
    "S2004600": "associates_credit_fraction_2003_school_03_raw",
    "S2004700": "associates_credit_fraction_2003_school_04_raw",
    "S2004900": "bachelors_credit_fraction_2003_school_01_raw",
    "S2005000": "bachelors_credit_fraction_2003_school_02_raw",
    "S2005100": "bachelors_credit_fraction_2003_school_03_raw",
    "S2005200": "bachelors_credit_fraction_2003_school_04_raw",
    "S2005300": "bachelors_credit_fraction_2003_school_05_raw",
    "S2007701": "enrollment_status_2003",
    "S3808501": "enrollment_status_2004",
    "S5408900": "enrollment_status_2005",
    "S7509700": "enrollment_status_2006",
    "T0013000": "enrollment_status_2007",
    "T2015900": "enrollment_status_2008",
    "T3606200": "enrollment_status_2009",
    "T5206600": "enrollment_status_2010",
    "T6656400": "enrollment_status_2011",
    "T8128800": "enrollment_status_2013",
    "U0008700": "enrollment_status_2015",
    "U1845300": "enrollment_status_2017",
    "U3443800": "enrollment_status_2019",
    "U4949500": "enrollment_status_2021",
    "U6356200": "enrollment_status_2023",
    "Z9083900": "highest_degree_ever",
    "Z9084300": "first_associates_degree_date_month_index",
    "Z9084400": "first_bachelors_degree_date_month_index",
}


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    source = root / "data/external/nlsy97_college_1997_2023.csv"
    output = root / "data/interim/nlsy97_college_1997_2023_named.csv"
    output.parent.mkdir(parents=True, exist_ok=True)

    with source.open(newline="", encoding="utf-8-sig") as source_file:
        reader = csv.reader(source_file)
        if next(reader) != list(COLUMN_NAMES):
            raise ValueError("Source columns differ from the reviewed NLSY97 extract")
        if len(set(COLUMN_NAMES.values())) != len(COLUMN_NAMES):
            raise ValueError("Renamed columns must be unique")

        with output.open("w", newline="", encoding="utf-8") as output_file:
            writer = csv.writer(output_file)
            writer.writerow(COLUMN_NAMES.values())
            for row in reader:
                if len(row) != len(COLUMN_NAMES):
                    raise ValueError("Source row has an unexpected number of fields")
                writer.writerow(row)


if __name__ == "__main__":
    main()
