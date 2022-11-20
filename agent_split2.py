import csv
import os

path1='C:/python_work/agent_billing/source/enrollmentReports_report_01102022000000_to_28102022235959.csv'
path2='C:/python_work/agent_billing/agents.txt'
path3='C:/python_work/agent_billing/agents_location.txt'
with open(path2, 'r') as file_object:
    linesq=file_object.read()
    
    contents2=linesq.split('\n')
    print(contents2)
    for agent in contents2[:]:
        print('My agent are fine')
with open(path3, 'r') as file_object1:
    linesq=file_object1.read()
    
    contents3=linesq.split('\n')
    print(contents3)
    for agent_location in contents3[:]:
        # Directory
        directory = agent_location
        print(f'is directory{directory}')

        # Parent Directory path
        parent_dir = f"C:/python_work/agent_billing/AGENT_SPLIT/"
        # Path
        path = os.path.join(parent_dir, directory)

        # Create the directory
        # 'GeeksForGeeks' in
        # '/home / User / Documents'
        #os.mkdir(path)
        print(f"Directory {path} created")
def agents(path1, path,agent):
    try:
        with open(path1, 'r') as file_object:
            lines=file_object.read()
        #print(lines)
    except:
        print(f"The file does not exist in the location")

    else:
        contents1=lines.split('\n')
        #print(contents1)
        textfile = open(f"{path}/{agent}.txt", "a")
        textfile.write('TICKET NUMBER,BVN,AGT MGT INST NAME,AGT MGT INST CODE,AGENT NAME,AGENT CODE,ENROLLER CODE,LATITUDE,LONGITUDE,FINGER PRINT SCANNER,BMS TICKET ID,VALIDATION STATUS,VALIDATION MESSAGE,AMOUNT,CAPTURE DATE,SYNC DATE,VALIDATION DATE\n')
        for line in contents1[:]:
    
            search=agent
            if search in line:
                
                textfile.write(line + "\n")
            #textfile.close()



for agent in contents2[:]:
    agents(path1,path,agent)
    print(f"Main file splited to {agent_location}'s  Directory")


    




