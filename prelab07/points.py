#! /bin/bash
#
# $Author$
# $Date$
# $Revision$
# $HeadURL$

import sys, math, os

class PointND:
    def __init__(self, *args):
        t = []
        n = 0
        for a in args:
            if type(a) is not float:
                raise ValueError("Cannot instantiate an object with non-float values.")
            else:
                t.append(round(a,2))
                n += 1
        self.t = tuple(t)
        self.n = n

    def __str__(self):
        s = '('
        for num in self:
            s += ("{0:.2f}".format(num)) + ', '
        s = s.strip()[:-1]
        s += ')'
        return s
    def __hash__(self):
        return hash(self.t)

    def clone(self):
        new_t = self.t
        return PointND(*new_t)

    def __add__(self,other):
        if type(other) is float and type(self) is not float:
            s = []
            for i in range(self.n):
                s.append(float(list(self.t)[i])+other)
            s = tuple(s)
            return PointND(*s)
        elif self.n == other.n:
            s = []
            for i in range(self.n):
                s.append(list(self.t)[i]+list(other.t)[i])
            s = tuple(s)
            return PointND(*s)
        else:
            raise ValueError("Cannot operate on points with different cardinalities.")
    def __radd__(self, other):
        if type(other) is float and type(self) is not float:
            s = []
            for i in range(self.n):
                s.append(float(list(self.t)[i])+other)
            s = tuple(s)
            return PointND(*s)

    def __sub__(self,other):
        if type(other) is float and type(self) is not float:
            s = []
            for i in range(self.n):
                s.append(float(list(self.t)[i])-other)
            s = tuple(s)
            return PointND(*s)
        elif self.n == other.n:
            s = []
            for i in range(self.n):
                s.append(list(self.t)[i]-list(other.t)[i])
            s = tuple(s)
            return PointND(*s)
        else:
            raise ValueError("Cannot operate on points with different cardinalities.")
    def __rsub__(self, other):
        if type(other) is float and type(self) is not float:
            s = []
            for i in range(self.n):
                s.append(float(list(self.t)[i])-other)
            s = tuple(s)
            return PointND(*s)

    def __mul__(self,other):
        if type(other) is float and type(self) is not float:
            s = []
            for i in range(self.n):
                s.append(float(list(self.t)[i])*other)
            s = tuple(s)
            return PointND(*s)
        elif self.n == other.n:
            s = []
            for i in range(self.n):
                s.append(list(self.t)[i]*list(other.t)[i])
            s = tuple(s)
            return PointND(*s)
        else:
            raise ValueError("Cannot operate on points with different cardinalities.")
    def __rmul__(self, other):
        if type(other) is float and type(self) is not float:
            s = []
            for i in range(self.n):
                s.append(float(list(self.t)[i])*other)
            s = tuple(s)
            return PointND(*s)

    def __truediv__(self,other):
        if type(other) is float and type(self) is not float:
            s = []
            for i in range(self.n):
                s.append(float(list(self.t)[i])/other)
            s = tuple(s)
            return PointND(*s)
        elif self.n == other.n:
            s = []
            for i in range(self.n):
                s.append(list(self.t)[i]/list(other.t)[i])
            s = tuple(s)
            return PointND(*s)
        else:
            raise ValueError("Cannot operate on points with different cardinalities.")
    def __rtruediv__(self, other):
        if type(other) is float and type(self) is not float:
            s = []
            for i in range(self.n):
                s.append(float(list(self.t)[i])/other)
            s = tuple(s)
            return PointND(*s)

    def __neg__(self):
        new_t = []
        for n in self.t:
            new_t.append((-1)*n)
        new_t = tuple(new_t)
        return PointND(*new_t)

    def __getitem__(self, item):
        return list(self.t)[item]

    def __eq__(self, other):
        if self.n == other.n:
            for i in range(self.n):
                if list(self.t)[i] != list(other.t)[i]:
                    return False
            return True
        else:
            raise ValueError("Cannot compare points with different cardinalities.")
    def __ne__(self, other):
        if self.n == other.n:
            for i in range(self.n):
                if list(self.t)[i] != list(other.t)[i]:
                    return True
            return False
        else:
            raise ValueError("Cannot compare points with different cardinalities.")
    def __gt__(self, other):
        if self.n == other.n:
            if self.distanceFrom(self-self) > other.distanceFrom(other - other):
                return True
            return False
        else:
            raise ValueError("Cannot compare points with different cardinalities.")
    def __ge__(self, other):
        if self.n == other.n:
            if self.distanceFrom(self-self) >= other.distanceFrom(other - other):
                return True
            return False
        else:
            raise ValueError("Cannot compare points with different cardinalities.")
    def __lt__(self, other):
        if self.n == other.n:
            if self.distanceFrom(self-self) < other.distanceFrom(other - other):
                return True
            return False
        else:
            raise ValueError("Cannot compare points with different cardinalities.")
    def __le__(self, other):
        if self.n == other.n:
            if self.distanceFrom(self-self) <= other.distanceFrom(other - other):
                return True
            return False
        else:
            raise ValueError("Cannot compare points with different cardinalities.")
    def distanceFrom(self,other):
       if self.n == other.n:
           sq = (self - other) * (self - other)
           ssq = 0
           for num in sq:
               ssq += num
           print(math.sqrt(ssq))
           return float(math.sqrt(ssq))
       else:
           raise ValueError("Cannot calculate distance between points of different cardinality.")

    def nearestPoint(self,points):
        if points != []:
            smallest = points[0]
            for p in points:
                if self.distanceFrom(p) < self.distanceFrom(smallest):
                    smallest = p
            return smallest
        else:
            raise ValueError("Input cannot be empty.")

    def printPoint(self):
        print(str(self))

class Point3D(PointND):
    def __init__(self,x=0.0,y=0.0,z=0.0):
        PointND.__init__(self,x,y,z)
        self.x = x
        self.y = y
        self.z = z

class PointSet():
    def __init__(self, **kwargs):
        points = []
        n = 0
        if kwargs is not None:
            if "pointList" in kwargs:
                if kwargs["pointList"] != []:
                    for value in kwargs["pointList"]:
                        if value not in points:
                            points.append(value)
                        n = points[0].n
                        self.n = n
                    for p in points:
                        if p.n != self.n:
                            raise ValueError("Expecting a point with cardinality {0}.".format(self.n))
                else:
                    raise ValueError("'pointList' input parameter cannot be empty.")
            else:
                raise KeyError("'pointList' input parameter not found.")
        self.points = points
        self.n = n

    def addPoint(self,p):
        if p.n == self.n:
            self.points.append(p)
        else:
            raise ValueError("Expecting a point with cardinality {0}.".format(self.n))

    def count(self):
        ct = 0
        list = []
        for num in self.points:
            if num not in list:
                list.append(num)
                ct += 1
        return ct

    def computeBoundingHyperCube(self):
        minPoint = []
        maxPoint = []
        for ind in range(self.n):
            mini = self.points[0][ind]
            maxi = self.points[0][ind]
            for p in self.points:
                if p[ind] < mini:
                    mini = p[ind]
                if p[ind] > maxi:
                    maxi = p[ind]
            minPoint.append(mini)
            maxPoint.append(maxi)
        minPoint = PointND(*minPoint)
        maxPoint = PointND(*maxPoint)
        return (minPoint,maxPoint)

    def computeNearestNeighbors(self, otherPointSet):
        list = []
        for p in self.points:
            dis = p.distanceFrom(otherPointSet.points[0])
            minDis = (p,otherPointSet.points[0])
            for op in otherPointSet.points:
                if dis > p.distanceFrom(op):
                    dis = p.distanceFrom(op)
                    minDis = (p,op)
            list.append(minDis)
        return sorted(list)

    def __add__(self,other):
        if other.n == self.n:
            self.points.append(other)
            return self
        else:
            raise ValueError("Expecting a point with cardinality {0}.".format(self.n))

    def __sub__(self,other):
        if other in self.points:
            self.points.remove(other)
        return self

    def __contains__(self,item):
        for p in self.points:
            if item == p:
                return True
        return False


if __name__ == "__main__":
        a = PointND(10.10,10.20,10.03)
        b = PointND(0.00,0.00,0.00)
        print(str(a))
