import csv
def search_book():
    #openingCSV file for reading
    csvfile = open('newbook.csv','r',newline='')
    #reading the CSV contenet in object
    csvobj = csv.reader(csvfile)  
    n=input("Enter the book number to be searched :")
    #flag variable
    found = False
    #extracting line by line content
    for l in csvobj:
        if l[0] == n:
            print('Record found')
            print(l)
            found = True
            break
    if not found:
        print("Record not found")
    #closing a CSV file
    csvfile.close()

#function calling statement
search_book()