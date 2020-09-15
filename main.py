# average order value = revenue / number of orders
# median is a better metric as it will not let super large orders skew the results

import csv
import statistics


def getStats():
    # make a list where we can drop e
    order_amount_list = list()
    with open('2019 Winter Data Science Intern Challenge Data Set - Sheet1.csv', newline='') as csvfile:
        file = csv.reader(csvfile)
        # ignore first line of data (headers)
        next(file)
        for row in file:
            order_amount_list.append(int(row[3]))
        return statistics.median(order_amount_list)

def main():
    print(getStats())


if __name__ == '__main__':
    main()
