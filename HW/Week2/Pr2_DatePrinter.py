def main():
    # Create a dictionary about all months
    month = ['January', 'February', 'March', 'April', 'May', 'June',
             'July', 'August', 'September', 'October', 'November',
             'December']
    # Ask the user the date with format
    date = input('Enter a date(mm/dd/yyy): ').split('/')
    date[0] = month[int(date[0])-1]

    print(date[0] + ", " + date[1] + ", " + date[2])


main()
