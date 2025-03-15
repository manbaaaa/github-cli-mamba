import csv
import json
import sys
from typing import List

from options import OutputOption
from rich import print, print_json
from rich.console import Console
from rich.table import Table


def print_beautify(data: List[dict], output_option: OutputOption):
    if output_option == OutputOption.json:
        # json key is double quotes, python dict key is single quotes
        # print(json.dumps(data, indent=4, ensure_ascii=False))
        print_json(json.dumps(data))
    elif output_option == OutputOption.csv:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    elif output_option == OutputOption.table:
        table = Table()
        table.add_column("")
        for field in data[0].keys():
            table.add_column(str(field))
        for row in data:
            table.add_row(*[str(data.index(row) + 1)] + [str(v) for v in row.values()])
        console = Console()
        console.print(table)
