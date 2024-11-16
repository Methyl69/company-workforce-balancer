projects = []

print("----------XYZ Company--------")
print("----------Main Menu----------")
print("")
print("1) Add new project to existing projects")
print("2) Remove a completed project from existing projects")
print("3) Add new workers to available workers group")
print("4) update details on ongoing project")
print("5) project statistics")
print("6) Exit")
print("")
a1=int(input("Enter your choice :"))

if a1 ==1:
    print("----------XYZ Company--------")
    print("-------Add new project-------")
    project_code = input("Enter Project Code (Enter '0' to exit): ")
    if project_code == 0:
        Print("Exiting......")
    else:
       client_name = input("Enter Client's Name: ")
       start_date = input("Enter Start Date: ")
       end_date = input("Enter Expected End Date: ")
       num_workers = int(input("Enter Number of Workers working on project: "))
       project_status = input("Enter Project Status (ongoing/ on hold/ completed): ")
       new_project= [client_name, start_date, end_date, num_workers, project_status]


