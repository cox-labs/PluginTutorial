# parse command-line arguments
args = commandArgs(trailingOnly=TRUE)
if (length(args) != 3) {
		stop("Should provide three arguments: parameters inFile outFile", call.=FALSE)
}
paramFile <- args[1]
inFile <- args[2]
outFile <- args[3]
# import PerseusR
library(PerseusR)
numberOfRows <- 15
# read data
mdata <- read.perseus(inFile)
# extract top rows
top.main <- head(main(mdata), numberOfRows)
top.annotCols <- head(annotCols(mdata), numberOfRows)
# create new matrixData
top <- matrixData(main=top.main, annotCols=top.annotCols,
		  annotRows=annotRows(mdata), description=description(mdata))
# write results to file
write.perseus(top, outFile)
