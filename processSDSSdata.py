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
			
def command(verbose, input, output, cutfile, start, end, red):
	parser = argparse.ArgumentParser(description =
		'Process SDSS star files for use with MilkyWay@home Separation.')
	parser.add_argument('-v', '--verbose',
		help='Display output to the screen while processing.',
		action="store_true")
	parser.add_argument('-i', '--input', type = str,
		help='Specify the location of the input SDSS csv file.'
		+ 'This defaults to ./sdss.csv .')
	parser.add_argument('-o', '--output', type = str,
		help='Specify the location of the output stars file.')
	parser.add_argument('-c', '--cutfile', type = str,
		help='Specify the location of a csv cuts file.')
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
	if args.cutfile:
		filetype = 'Cutfile: '
		cutfile = args.cutfile
		testfile(filetype, cutfile)
	if args.start:
		start = args.start
	if args.end:
		end = args.end
	if args.red:
		red = True
	return (verbose, input, output, cutfile, start, end, red)

def main():

	# Set default values for control variables

	verbose	= False
	input	= './sdss.csv'
	output	= './sdss'
	cutfile	= None
	start	= 1
	end		= 144
	red		= False	

	# Override control variables if set in command line options

	verbose, input, output, cutfile, start, end, red = command(
		verbose, input, output, cutfile, start, end, red)

	# Load cuts
	
	
	
if __name__ == "__main__":
	main()

