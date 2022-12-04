from aocd import get_data

for i in range(1,26):
    dat= get_data(day=i,year=2018)
    with open('input/'+str(i), 'w') as file:
        # Write the string to the file
        file.write(dat)
