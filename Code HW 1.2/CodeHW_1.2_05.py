# Write your code here :-)
from microbit import *

# Assign variable for the data file name
data_table = 'tc_data.csv'

# Declare function to extract data from data log
def read_data(data_table):
    with open(data_table) as data_file:
        data = data_file.read()
    return(str(data))

# Declare function to write collected data to data_table
def write_data(data_table, data):
    with open(data_table, 'w') as data_file:
        data = str(data)
        data_file.write(data)

# Declare function to collect sensor data
def data_logger():

    log_time = 0  # Assign variable for time passed, initial value 0
    temp = temperature()  # Assign variables for sensor readings
    comp = compass.heading()

    # Data collection interface
    while True:

        display.show(Image.ARROW_E)

        if button_a.is_pressed():  # Button A ends data collection loop
            display.show('x')
            sleep(1000)
            display.clear()
            break

        if button_b.is_pressed():  # Button B begins data collection

            log_data = 'Temperature,Heading\r'  # Assign var for data output
            write_data(data_table, log_data)

            while True:

                display.scroll('..... ')

                if(log_time < 120000):  # data collection lasts for 2 min.
                    log_data = read_data(data_table)
                    temp = str(temperature())
                    comp = str(compass.heading())
                    log_data = log_data + temp + ',' + comp + '\r'
                    write_data(data_table, log_data)
                    log_data = read_data(data_table)
                    log_time = log_time + 10000  # frequency of data points
                    sleep(10000)  # interval time per data point
                else:
                    display.scroll('Done!')
                    if button_a.was_pressed():
                        display.show('X')
                        sleep(2000)
                        display.clear()
                        data_logger()

# Call data logger function
data_logger()