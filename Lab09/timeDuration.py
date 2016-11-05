#! /bin/bash
#
# $Author: ee364b11 $
# $Date: 2016-03-22 15:18:14 -0400 (Tue, 22 Mar 2016) $
# $Revision: 89781 $
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b11/Lab09/timeDuration.py $

import sys, math, os

class TimeSpan:
    def __init__(self,weeks,days,hours):
        if type(weeks) != int or type(days) != int or type(hours) != int:
            raise TypeError("int only")
        if weeks<0 or days<0 or hours<0:
            raise ValueError("greater than zero")
        if hours >= 24:
            day,hours = divmod(hours,24)
            days+=day
        if days >= 7:
            week,days= divmod(days,7)
            weeks+=week
        self.hours = hours
        self.days = days
        self.weeks = weeks

    def __str__(self):
        s = "{:02d}W {:01d}D {:02d}H".format(self.weeks,self.days,self.hours)
        return s

    def getTotalHours(self):
        total=self.weeks*7*24+self.days*24+self.hours
        return total

    def __add__(self,other):
        if type(self) != TimeSpan or type(other) != TimeSpan:
            raise TypeError("expect timespan")
        newTS = TimeSpan(self.weeks+other.weeks,self.days+other.days,self.hours+other.hours)
        return newTS

    def __mul__(self, other):
        if type(other) is not int:
            raise TypeError("expect timespan multiply int")
        if other <= 0:
            raise ValueError("int need to be greater than zero")
        if type(self) == TimeSpan and type(other) == int:
            newTS= TimeSpan(self.weeks*other,self.days*other,self.hours*other)
            return newTS


    def __rmul__(self, other):
        if type(self) == TimeSpan and type(other) == int:
            newTS= TimeSpan(self.weeks*other,self.days*other,self.hours*other)
            return newTS
