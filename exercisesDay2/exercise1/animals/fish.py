#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 12:18:22 2025

@author: linnekst
"""
class Fish:
    def __init__(self):
        ''' Constructor for this class. '''
 # Create some member animals
        self.members = ['Salmon', 'Shark', 'Cod', 'Sawfish', 'Trout', 'Catfish', 'Lionfish']
    def printMembers(self):
        print('Printing members of the Fish class')
        for member in self.members:
            print('\t%s ' % member)
