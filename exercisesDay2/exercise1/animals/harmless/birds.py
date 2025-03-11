#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 12:11:56 2025

@author: linnekst
"""
class Birds:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        super().__init__()
        self.members = ['Sparrow', 'Robin', 'Duck']
    def printMembers(self):
        print('Printing harmless members of the Bird class')
        for member in self.members:
            print('\t%s ' % member)
