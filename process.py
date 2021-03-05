# Opens a file and saves the output to log_file var
log_file = open("um-server-01.txt")

def sales_reports(log):
    for line in log:
        line = line.rstrip()
        day = line[0:3]
        if day == "Tue":
            print(line)


sales_reports(log_file)
