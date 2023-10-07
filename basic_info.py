import numpy as np
import re

index = 0 # user passes in for planet index
data = {} # dictionary for all the data

with open('podaci.txt') as f:
    lines = f.readlines() # opening the .txt file

for line in lines: # for every line
    if ":" not in line: # check if semicolon present
        continue  # Skip lines without a colon
    key, values_str = line.split(":") # split by semicolon
    values_str = re.sub('[^0-9. ,]', '', values_str) # remove all values which aren't necessary
    values_list = values_str.split(', ') # split by row
    values_list = [float(x) for x in values_list] # convert all values into float and not string
    data[key.strip()] = values_list # save everything

specific_planet = [] # make a list for a specific planet based on index
for dic in data:
    specific_planet.append(data[dic][index]) # for every parameter pick the value based on index

print(specific_planet)