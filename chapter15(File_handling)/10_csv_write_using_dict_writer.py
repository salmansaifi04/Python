## dictwriter

from csv import DictWriter

with open('file4.csv', 'w', newline='') as f:
    # headers
    csv_writer = DictWriter(f, fieldnames=['firstname', 'lastname', 'age'])
    csv_writer.writeheader()

    # write row method
    # csv_writer.writerow(
    #     {
    #         'firstname' : 'Salman',
    #         'lastname' : 'Saifi',
    #         'age' : 21
    #     }
    # )
    
    # csv_writer.writerow(
    #     {
    #         'firstname' : 'Anjali',
    #         'lastname' : 'Choudhary',
    #         'age' : 20
    #     }
    # )
    
    # csv_writer.writerow(
    #     {
    #         'firstname' : 'Nitin',
    #         'lastname' : 'Choudhary',
    #         'age' : 22
    #     }
    # )


    ## write rows
    csv_writer.writerows(
        [
            {
                'firstname' : 'Salman',
                'lastname' : 'Saifi',
                'age' : 21
            },
            {
                'firstname' : 'Anjali',
                'lastname' : 'Choudhary',
                'age' : 19
            },
            {
                'firstname' : 'Nitin',
                'lastname' : 'Choudhary',
                'age' : 22
            }
        ]
    )