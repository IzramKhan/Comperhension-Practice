import datetime as dt
import json
import random

STUDENTS = {}

def add_student():
    '''Add a student with name and year'''
    name = input('\nEnter student name: ')
    year = dt.datetime.now().year
    STUDENTS[name] = {'grades': [random.randint(50, 100), random.randint(50, 100), random.randint(50, 100)], 'year': year}

def percentage_to_points(grade):
    '''Helper for calculate_gpa to give a gpa for each grade'''
    if grade in range(90, 101):
        return 4
    elif grade in range(80, 90):
        return 3
    elif grade in range(70, 80):
        return 2
    elif grade in range(60, 70):
        return 1
    else:
        return 0

def calculate_gpa(name):
    '''Calculate gpa by converting percentage to points using helper'''
    student = STUDENTS[name]
    gpa = [percentage_to_points(grade) for grade in student['grades']]
    return round((sum(gpa) / len(gpa)), 1)

def filter_by_range(min_gpa, max_gpa):
    '''Filter the students by min & max gpa'''
    range_ = [(name, calculate_gpa(name)) for name in STUDENTS if min_gpa <= calculate_gpa(name) <= max_gpa]
    return range_

def sort_by_gpa(reverse=False):
    '''Sort students in reverse or non-reverse by gpa'''
    all_gpa = [(name, calculate_gpa(name)) for name in STUDENTS.keys()]
    all_gpa.sort(key=lambda x: x[1], reverse=reverse)
    return all_gpa
    
def get_top_n(n):
    '''Give top n students by gpa'''
    return sort_by_gpa(reverse=True)[:n]

def export_to_json():
    '''Exporting STUDENTS dict to students.json'''
    try:
        with open('students.json', 'r') as f:
            existing = json.load(f)
    except FileNotFoundError:
        existing = {}
        
    existing.update(STUDENTS)
    
    with open('students.json', 'w') as f:
        json.dump(existing, f, indent=3)
        
# Practiced by: Izram Khan
# Date practiced: 17-May-2026