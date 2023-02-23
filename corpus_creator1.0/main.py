#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 08:00:07 2023

@author: lindsay
"""

import os
import subprocess
main_path=os.getcwd()

def run():
    subprocess.run(["python", "Scripts/Corpus_login.py"])
    
if __name__=='__main__':
    run()