import os
import sys
import csv

import argparse

from database.sqlite import get_session
from models.organizations import OrganizationModel

PROG = os.path.basename(sys.argv[0])

if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(
            description="Load data fixtures into database",
            prog=PROG
        )
        parser.add_argument("-f", "--file",
                            type=str, default="database/fixtures/organizations.csv",
                            help="Path to CSV file")
        parser.add_argument("-a", "--append", action="store_true",
                            help="Append to existing data")

        args = parser.parse_args()
        print(PROG, "loading data from", args.file)
        column_map = {
            "name": ["Name", str],
            "country": ["Country", str],
            "industry": ["Industry", str],
            "website": ["Website", str],
            "description": ["Description", str],
            "founded_year": ["Founded", int],
            "employees_count": ["Number of employees", int]
        }

        session = next(get_session())
        db_data = []
        with open(args.file, "r") as f:
            records = csv.DictReader(f)
            for record in records:
                db_row = {}
                for db_key, v in column_map.items():
                    csv_key, type_ = v
                    new_val = record[csv_key]
                    if new_val is not None:
                        new_val = type_(new_val)
                    db_row[db_key] = new_val
                db_data.append(OrganizationModel(**db_row))
        print(PROG, "found", len(db_data), "records")
        if not args.append:
            print(PROG, "deleting existing data")
            session.query(OrganizationModel).delete()
        print(PROG, "inserting data")
        session.bulk_save_objects(db_data)
        session.commit()
        print(PROG, "done")

    except Exception as x:
        sys.stderr.write(f"{x}\n")
        sys.exit(1)
    else:
        sys.exit(0)