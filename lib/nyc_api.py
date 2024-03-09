import requests
import json

class GetPrograms:

    def get_programs(self):
        URL = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"
        try:
            response = requests.get(URL)
            response.raise_for_status() 
            return response.json() 
        except requests.exceptions.RequestException as e:
            print("Error fetching data:", e)
            return None
    
    def program_school(self):
        programs_list = []
        programs = self.get_programs() 
        if programs is not None:
            for program in programs:
                programs_list.append(program.get("agency", "Unknown"))  
        return programs_list

programs = GetPrograms()
programs_schools = programs.program_school()

for school in set(programs_schools):
    print(school)
