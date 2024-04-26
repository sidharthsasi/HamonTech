import argparse
import csv


def parse_args():
    parser = argparse.ArgumentParser
    parser.add_argument("/Users/sidharthsasi/Desktop/Hamon Techology/unemployment-rate.csv")
    parser.add_argument("BEL")
    parser.add_argument("-o", choices=["avg", "min", "max"], default="avg")
    parser.add_argument("--from", dest="from_year", type=int)
    parser.add_argument("--to", dest="to_year", type=int)
    return parser.parse_args()


def main():
    args = parse_args()

   
    with open(args.input_file, "r") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  
        data = [(country, int(year), float(unemployment_rate)) for country, _, year, unemployment_rate in reader]

  
    data = [(country, year, rate) for country, year, rate in data if country.lower() == args.country.lower() and
            (args.from_year is None or year >= args.from_year) and
            (args.to_year is None or year <= args.to_year)]

  
    if data:
        if args.o == "avg":
            statistic = sum(rate for _, _, rate in data) / len(data)
        elif args.o == "min":
            statistic = min(rate for _, _, rate in data)
        else:
            statistic = max(rate for _, _, rate in data)
        print(f"{args.o.capitalize()} unemployment rate for {args.country}: {statistic:.2f}")
    else:
        print(f"No data found for {args.country} in the specified range.")


if __name__ == "__main__":
    main()
