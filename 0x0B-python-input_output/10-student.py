#!/usr/bin/python3
'''A class Student that defines a student by: (based on 9-student.py)'''

class Student:
    '''A class Student'''
    
    def __init__(self, first_name, last_name, age):
        '''A function that instantiates the student's first name, last name and age
        '''
        
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''A function that retrieves a dictionary representation of a 
        Student instance (same as 8-class_to_json.py)
        PARAMETER
            self:
            attrs:
        '''
        
        if '__dict__' in dir(self):
            res = dict()
            can_filter = False
            if (type(attrs) is list) and all(type(s) is str for s in attrs):
                can_filter = True
            for key in self.__dict__.keys():
                if (not can_filter) or (can_filter and key in attrs):
                    res[key] = self.__dict__[key]
            return res
