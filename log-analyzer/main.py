# this script will scan log files and count the number of ERRORS, WARNING, and LOGIN FAILED

# opening the log file in read mode
with open("sample_log.txt", "r") as file:
    lines = file.readlines()  # making sure to read all lines into a list

# initializing counters for the events we want to take note of 
    error_count = 0 
    warning_count = 0 
    failed_login_count = 0 

# for loop that goes through each log file
    for line in lines:
        if "ERROR" in line:
            error_count += 1
        if "WARNING" in line:
                warning_count += 1
        if "LOGIN FAILED" in line:
                    failed_login_count += 1

# print out of summary report                   
    print("Log Anaylsis Report:")
    print("---------------------:")
    print(f"Total lines scanned: {len(lines)}")
    print(f"Errors found: {error_count}")
    print(f"Warning found: {warning_count}")
    print(f"Failed logins: {failed_login_count}")
