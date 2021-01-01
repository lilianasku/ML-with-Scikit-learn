#List of functions for reuse
import sys
import numpy as np
import pandas as pd

def read_input(inputfile):
    try:
        with open(inputfile, 'r') as input_file:
             column_names = ['date', 'day_in_month', 'temp_month', 'gas_usage_day','terms_month',
             'billing_days_gc', 'kilowatt_total', 'kilowatt_day', 'billing_days_ec',
             'kwh', 'days_heating', 'days_cooling', 'nroom']
             #set date as an index column
             df = pd.read_csv(inputfile, header=None,
                              sep='\s+',
                              names=column_names,
                              index_col='date')
              #Fahrenheith to Celsius
             df['temp_month'] = ((df['temp_month']-32)/1.8).round(decimals=2)
             return df
    except IOError:
            print("File not found or path is incorrect")
            sys.exit()

def main():
   filename = '../data/utility.dat.txt'
   print('Reading file ', filename, '...\n')

   df = read_input(filename)
   try:
      print(df.head(5))
   except(AttributeError, NameError):
      print('Data frame error!')
      sys.exit()


if __name__=="__main__":
    main()
