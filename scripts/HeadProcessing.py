import argparse

parser = argparse.ArgumentParser(description='Head processing in Python')
parser.add_argument('number_of_rows', type=int,
        help='Number of rows. Has to be specified as additional argument in the Perseus Gui')
parser.add_argument('input_file', help='Input file containing the matrix')
parser.add_argument('output_file', help='Output file that should contain the result')
args = parser.parse_args()

from perseuspy import pd
df = pd.read_perseus(args.input_file)
result = df.head(args.number_of_rows)
result.to_perseus(args.output_file)
