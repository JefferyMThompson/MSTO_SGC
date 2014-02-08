#!/usr/bin/env python

# This file is to process data files from the SDSS Data Release 9
# Originally generated 2/6/2014
# Written by Jeffery M. Thompson

# import modules

import csv             # For reading the csv SDSS star files
import sys             # For basic system commands
import argparse        # For processing of command line options
import os              # For file tests

def testfile(filetype, filename):	 
	try:
		fh = open(filename)
	except IOError as error:
		print("{0} {1}".format(filetype, error))
	return

def loadbounds(file, start, end):
	count = range(start, end)
	bounds = [([0]*2) for i in count]
	for stripe in count:
		with open(file, 'rb') as boundfile:
			boundfile.seek(0)
			dictionary = csv.DictReader(boundfile)
			for row in dictionary:
				stripe_column = int(row['Stripe'])
            	start_column = float(row['Start'])
            	end_column = float(row['End'])
            if(stripe_column == stripe):
                bounds[stripe-start] = [start_column, end_column]
	return (bounds)
	
def command(verbose, input, output, boundfile, start, end, red):
	parser = argparse.ArgumentParser(description =
		'Process SDSS star files for use with MilkyWay@home Separation.')
	parser.add_argument('-v', '--verbose',
		help='Display output to the screen while processing.',
		action="store_true")
	parser.add_argument('-i', '--input', type = str,
		help='Specify the location of the input SDSS csv file.'
		+ 'This defaults to ./sdss.csv .')
	parser.add_argument('-o', '--output', type = str,
		help='Specify the location of the output stars file.'
		+ 'This defaults to ./sdss . The Stripe number and the'
		+ 'extension .stars is appended to each file created.')
	parser.add_argument('-b', '--boundfile', type = str,
		help='Specify the location of a csv bound file.')
	parser.add_argument('-s', '--start', type = int,
		help='Limit the starting wedge number to process.')
	parser.add_argument('-e', '--end', type = int,
		help='Limit the ending wedge number to process.')
	parser.add_argument('-r', '--red', 
		help='Using a correction to the reddening values from Schlafly,'
		+ 'Finkbeiner 2011.')
	args = parser.parse_args()
	if args.verbose:
		verbose = True
	if args.input:
		input = args.input
	filetype = 'Input file: '
	testfile(filetype, input)
	if args.output:
		filetype = 'Output file: '
		output = args.output
		testfile(filetype, output)
	if args.boundfile:
		filetype = 'Boundfile: '
		boundfile = args.boundfile
		testfile(filetype, boundfile)
	if args.start:
		start = args.start
	if args.end:
		end = args.end
	if args.red:
		red = True
	return (verbose, input, output, boundfile, start, end, red)

def main():

	# Set default values for control variables

	verbose		= False
	input		= './sdss.csv'
	output		= './sdss'
	boundfile	= None
	start		= 1
	end			= 144
	red			= False	

	# Override control variables if set in command line options

	verbose, input, output, boundfile, start, end, red = command(
		verbose, input, output, boundfile, start, end, red)

	# Load bounds
	if boundfile:
		bounds = loadbounds(boundfile, start, end)
	
if __name__ == "__main__":
	main()

