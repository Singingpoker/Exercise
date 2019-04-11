# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 21:21:05 2019

@author: 10502
"""
class Polynomial:
    def __init__(self,dic):
        self.dic=dic
    def __call__(self,x):
        c=0
        for k in self.dic:
            c+=self.dic[k]*x**(k)
        return c
    def __add__(self,another):
        result={}
        for k in self.dic:
            result[k]=self.dic[k]
            for j in another.dic:
                if k==j:
                    result[k]=self.dic[k]+another.dic[j]
                else:
                    result[j]=another.dic[j]
        return Polynomial(result)

x=1    
a=Polynomial({1:1,100:-3})(x)
b=Polynomial({20:1,1:-1,100:4})(x)
print(a+b)
    

