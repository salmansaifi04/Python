# writer

from csv import writer
with open('file3.csv', 'w', newline='') as f:
    csv_writer = writer(f)

    ## we have two methods to write a csv file
    
    ## 1. write.row
    csv_writer.writerow(['Name', 'Surname'])
    csv_writer.writerow(['Salman', 'Saifi'])

    ## 2. write.rows
    # csv_writer.writerows([['Name', 'Surname'],['Salman', 'Saifi']])