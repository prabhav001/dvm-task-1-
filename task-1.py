import csv
import openpyxl

class Course:

    def __init__(self, name, code, test_date, credits):
        self.name = name
        self.code = code
        self.credits = credits
        self.test_date = test_date
        self.sections = []

    def get_all_sections(self):
        return self.sections

    def __str__(self):
        pass

    def populate_section(self, section):
        self.sections.append(section)


class Section:

    def __init__(self, course, id, room, type):
        self.course = course
        self.section_id = id
        self.room = room
        self.day = []
        self.hours = []
        self.type = type


class Timetable:

    def __init__(self):
        self.courses = []
        self.enrolled_sections = []

    def enroll_subject(self, course):
        self.courses.append(course)

    def check_clashes(self, section):
        
        for course in self.courses:
            if section in course.get_all_sections():
                for enrolled_sections in self.enrolled_sections:
                    if enrolled_sections.course != section.course:
                            if set(enrolled_sections.day) & set(section.day):
                                if set(enrolled_sections.hours) & set(section.hours):
                                    return True
                                else:
                                    return False
                            else:
                                return False
                    else:
                        if enrolled_sections.type != section.type:
                            if set(enrolled_sections.day) & set(section.day):
                                if set(enrolled_sections.hours) & set(section.hours):
                                    return True
                                else:
                                    return False
                            else:
                                return False
        return True