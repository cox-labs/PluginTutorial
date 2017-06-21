import sys
from perseuspy import pd
from perseuspy.parameters import *

_, paramfile, infile, outfile = sys.argv
df = pd.read_perseus(infile)
parameters = parse_parameters(paramfile)
number_of_rows = intParam(parameters, 'Number of rows')
result = df.head(number_of_rows)
result.to_perseus(outfile)
