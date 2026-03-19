from abc import ABC, abstractmethod
import sqlite3

class PersonManager(ABC):
    def __init__(self, db_name="london_roots.db"):
        self.db_name = db_name

    @abstractmethod
    def insert_person(self, data_tuple):
        """Should execute an INSERT INTO query for the specific table"""
        pass

    @abstractmethod
    def remove_person(self, person_id):
        """Should execute a DELETE FROM query based on ID"""
        pass

    @abstractmethod
    def display_all(self):
        """Should execute a SELECT * query and return/print results"""
        pass