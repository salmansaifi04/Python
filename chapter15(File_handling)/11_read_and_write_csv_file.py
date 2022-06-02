from csv import DictReader, DictWriter

with open('file4.csv', 'r') as rf:
    with open('file5.csv', 'w', newline='') as wf:
        csv_reader = DictReader(rf)
        csv_writer = DictWriter(wf, fieldnames=['first_name', 'last_name', 'age'])
        csv_writer.writeheader()
        for i in csv_reader:
            fname, lname, age = i['firstname'], i['lastname'], i['age']
            csv_writer.writerow(
                {
                    'first_name' : 'fname',
                    'last_name' : 'lname',
                    'age' : 'age'
                }
            ) 