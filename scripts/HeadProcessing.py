import sys
from perseuspy import pd
from perseuspy.parameters import *

_, paramfile, infile, outfile = sys.argv
df = pd.read_perseus(infile)
number_of_rows = 15
result = df.head(number_of_rows)
result.to_perseus(outfile)
