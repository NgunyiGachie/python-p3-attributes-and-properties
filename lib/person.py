#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name="Jane", job="ITC"):
        self._name = None
        self._job = None
        self.name = name  
        self.job = job    
    
    def set_name(self, new_name):
        if isinstance(new_name, str) and 1 <= len(new_name) <= 25:
            self._name = new_name.title()
        else:
            print("Name must be string between 1 and 25 characters.")
    
    def get_name(self):
        return self._name
    
    def set_job(self, person_job):
        if person_job in APPROVED_JOBS:
            self._job = person_job
        else:
            print("Job must be in list of approved jobs.")
    
    def get_job(self):
        return self._job
    
    name = property(get_name, set_name)
    job = property(get_job, set_job)

    


