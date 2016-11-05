#! /bin/bash
#
# $Author: ee364b11 $
# $Date: 2016-03-01 14:43:06 -0500 (Tue, 01 Mar 2016) $
# $Revision: 89168 $
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b11/Lab07/Institute.py $

import sys, math, os

class Simulation:
    def __init__(self, simnNo, simDate, chipName, chipCount, chipCost):
        self.simulationNumber=simnNo
        self.simulationDate=simDate
        self.chipName=chipName
        self.chipCost=chipCost
        self.chipCount=chipCount
        self.simulationCost= round(chipCount * chipCost, 2)

    def __str__(self):
        a=self.chipName+": "
        b="{0:03d}, {1}, ${2:06.2f}".format(self.simulationNumber,self.simulationDate,self.simulationCost)
        return a+b

class Employee:
    def __init__(self, employeeName, employeeID):
        self.simulationsDict={}
        self.employeeName=employeeName
        self.employeeID=employeeID

    def addSimulation(self, sim):
            self.simulationsDict[sim.simulationNumber]=sim

    def getSimulation(self, simNo):
        if simNo in self.simulationsDict:
            return self.simulationsDict[simNo]
        else:
            return None

    def __str__(self):
        a="{:02d}".format(len(self.simulationsDict))
        s=self.employeeID+", "+self.employeeName+": "+ a +" Simulations"
        return s

    def getWorkload(self):
        s=str(self)+"\n"
        l=[]
        for key in self.simulationsDict:
            l.append(str(self.simulationsDict[key]))
        for a in sorted(l):
            s+=a+"\n"
        return s[:-1]

    def addWorkload(self, fileName):
        file = open(fileName,'r')
        all_line=file.readlines()[2:]
        for line in all_line:
            l=line.split()
            sim=Simulation(int(l[0]),l[1],l[2],int(l[3]),float(l[4][1:]))
            self.addSimulation(sim)

class Facility:
    def __init__(self, facilityName):
        self.facilityName=facilityName
        self.employeesDict={}

    def addEmployee(self,employee):
        self.employeesDict[employee.employeeName]=employee

    def getEmployees(self, *args):
        l=[]
        for name in args:
            l.append(self.employeesDict[name])
        return l

    def __str__(self):
        s=self.facilityName+": "+"{:02d}".format(len(self.employeesDict))+" Employees\n"
        l=[]
        for key in self.employeesDict:
            l.append(str(self.employeesDict[key]))
        for a in sorted(l):
            s+=a+"\n"
        return s[:-1]

    def getSimulation(self, simNo):
        for key in self.employeesDict:
            if self.employeesDict[key].getSimulation(simNo):
                    return self.employeesDict[key].getSimulation(simNo)
        return None