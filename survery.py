import sys
import gzip
import os

class Record(object):


class Respondent(Record):


class Pregnancy(Record):


class Table(object):


    def __init__(self):
        self.records = []

    def __len__(self):
        return len(self.records)

    def ReadFile(self, data_dir, filename, fields, constructor, n=None):
