#!/usr/bin/python3
'''A class Student that defines a student'''

class Student:
    '''A class Student that defines a student'''
    
    def __init__(self, first_name, last_name, age):
        '''A function that instantiates the student's first name, last name and age
        '''
        
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''A function that retrieves a dictionary representation of a 
        Student instance (same as 8-class_to_json.py)
        '''
        
        if '__dict__' in dir(self):
            return self.__dict__
