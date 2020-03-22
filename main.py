#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 15:48:09 2020

@author: bernardintheo
"""

from openpyxl import load_workbook


class ecritureXLSX:

    def ecrireXLSX(self,filename,sheet,data):        
        workbook_name = filename
        wb = load_workbook(workbook_name)
        page = wb.get_sheet_by_name(sheet)
        
              
        for info in data:
            page.append(info)
        
        wb.save(filename=workbook_name)
        
    
