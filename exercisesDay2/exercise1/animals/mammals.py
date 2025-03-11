#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 11:15:07 2025

@author: linnekst
"""
class Mammals:
    def __init__(self): 
        ''' Constructor for this class. '''
 # Create some member animals
        self.members = ['Tiger', 'Elephant', 'Wild Cat']
    def printMembers(self):
        print('Printing members of the Mammals class')
        for member in self.members:
            print('\t%s ' % member)