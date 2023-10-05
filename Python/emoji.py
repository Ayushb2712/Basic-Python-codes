# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 21:40:09 2023

@author: ayush
"""

def convert(input_str):
    # Replace :) with 🙂
    input_str = input_str.replace(":)", "🙂")
    
    # Replace :( with 🙁
    input_str = input_str.replace(":(", "🙁")
    
    return input_str

def main():
    user_input = input("Enter a string: ")
    converted_str = convert(user_input)
    print("Converted string:", converted_str)

main()