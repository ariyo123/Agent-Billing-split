import csv
import os
import shutil
from shutil import copytree, rmtree
from time import time, ctime
import calendar
import time
import datetime 

#get the unique variable to defferentiate date
#date=input("enter date: yyyy-mm-dd: ")    
CurrentDate=datetime.date.today()  
days = datetime.timedelta(0)

new_date = CurrentDate - days
final_date= new_date.strftime('%Y-%m-%d')
#%d is for date  dd
#%m is for month  mm
#Y is for Year  yyyy
date=final_date
print(final_date)


path1='C:/python_work/agent_billing/source/enrollmentReports_report_01102022000000_to_28102022235959.csv'
path2='C:/python_work/agent_billing/agents.txt'
with open(path2, 'r') as file_object:
    linesq=file_object.read()

    contents2=linesq.split('\n')
    print(contents2)
    for agent in contents2[:]:
        # Directory
        directory = agent

        # Parent Directory path
        parent_dir = "C:/python_work/agent_billing/AGENT_SPLIT/"
        # Path
        path = os.path.join(parent_dir, directory)

        # Create the directory
        # 'GeeksForGeeks' in
        # '/home / User / Documents'
        os.mkdir(path)
        print(f"Directory {agent} created")
        continue
def agents(path1, agent_name):
    try:
        with open(path1, 'r') as file_object:
            lines=file_object.read()
        #print(lines)
    except:
        print(f"The file does not exist in the location")

    else:
        contents1=lines.split('\n')
        #print(contents1)
        textfile = open(f"{parent_dir}{agent_name}/{agent_name}_week_ending_{final_date}.txt", "a")
        textfile.write('TICKET NUMBER,BVN,AGT MGT INST NAME,AGT MGT INST CODE,AGENT NAME,AGENT CODE,ENROLLER CODE,LATITUDE,LONGITUDE,FINGER PRINT SCANNER,BMS TICKET ID,VALIDATION STATUS,VALIDATION MESSAGE,AMOUNT,CAPTURE DATE,SYNC DATE,VALIDATION DATE\n')
        for line in contents1[:]:
    
            search=agent_name
            if search in line:
                
                textfile.write(line + "\n")
                continue
            #textfile.close()



for agent in contents2[:]:
    agents(path1, agent)
    print(f"Main file splited to {agent}'s  Directory")
        
path1='C:/python_work/agent_billing/source/enrollmentReports_report_01102022000000_to_28102022235959.csv'
path2='C:/python_work/agent_billing/agents.txt'
with open(path2, 'r') as file_object:
    linesq=file_object.read()
    
    contents2=linesq.split('\n')
    print(contents2)
    for agent in contents2[:]:
             
        dst=f"C:/python_work/bvn_report_movement/Program Files/Ipswitch/WS_FTP Server/nibss-webserver/users/BVN/Agent_billing/{agent}"
        if agent==f'{agent}':
            src=f"C:/python_work/agent_billing/AGENT_SPLIT/{agent}"
            shutil.copytree(src, dst)
            pass
   