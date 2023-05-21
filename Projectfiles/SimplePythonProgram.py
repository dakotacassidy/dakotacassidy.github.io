# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 16:25:27 2020

@author: cococ
"""

import pandas as pd
import numpy as np
import tkinter.filedialog

record = None
numaud = None
def audnames():
    global names
    names = []

def namelist():
    global names
    print('\nAuditor names:')
    for i in names:
        print(i)
  
def recordlist():
    global names
    for j in names:
        print('\nRecords assigned to',j,':')
        aud2= df['Auditor'].tolist()
        aud3 = df['Employee_Name'].tolist()
        audited = dict(zip(aud3,aud2))
        for k in audited:
            if audited[k] is j:
                print(k)

def exportCSV ():
    global df
    export_file_path = tkinter.filedialog.asksaveasfilename(defaultextension='.csv')
    df.to_csv (export_file_path, index = False, header=True)

print('''Audit Group Program
  
1) Select employee record file
2) Enter auditor names
3) Assign records to auditors
4) View auditor names
5) View records assigned to auditors
6) Export list assignment to file
7) Quit menu, i.e., Quit
  
''')

while True:
    try:
        command = int(input('Enter command here: '))
        if command == 1:
            record = pd.read_csv(tkinter.filedialog.askopenfile(mode='r'))
            print('File successfully opened')
  
        if command == 2:
            while True:
                try:
                    audnames()
                    numaud = int(input('How many auditors will be conducting the audit? '))
                except:
                    print('That is not a valid entry, please enter an integer for this value')
                else:
                    for x in range(numaud):
                        print('Enter the name of Auditor', x+1,':')
                        nameentry = input()
                        names.append(nameentry)
                    print('\nAuditor names successfully recorded.')
                    namelist()
                    break
        if command == 3:
            if record is None:
                print('Please select an employee record file before running this command')
            else:
                if numaud is None:
                    print('Please enter auditor names before running this command')
                else:
                    while True:
                        try:
                            numrecords = int(input('How many records will be assigned to each auditor? '))
                        except:
                            print('That is not a valid entry, please enter an integer for this value')
                        else:
                            auditor = names*numrecords
                            newcols = record[['Employee_Name','Sex','DOB','State','Zip']] 
                            randomize = pd.DataFrame(np.random.permutation(newcols),columns=['Employee_Name','Sex','DOB','State','Zip']) 
                            df = randomize.loc[:(len(auditor)-1),['Employee_Name','Sex','DOB','State','Zip']] 
                            df['Auditor']=auditor 
                            df = df.sort_values(by='Auditor')
                            recordlist()
                            break
  
        if command == 4:
            namelist()
        if command == 5:
            recordlist()
        if command == 6:
            exportCSV()
            print('File Saved')
        if command == 7:
            print('Quitting now')
            break
        if command not in range(1,8):
            print('''Please enter a number from 1 to 7.
  
Try again.''')
  
    except:
        print('Error, please enter a number from 1 to 7 and try again.')