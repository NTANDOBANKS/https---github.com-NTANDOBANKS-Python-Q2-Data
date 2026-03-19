from abc import ABC, abstractmethod

class PersonManager(ABC):
    def __init__(self, db_name="london_roots.db"):
        self.db_name = db_name

    @abstractmethod
    def insert_person(self, data_tuple):
        """Must be implemented by subclasses to insert into specific tables"""
        pass

    @abstractmethod
    def remove_person(self, person_id):
        """Must be implemented by subclasses to delete from specific tables"""
        pass

    @abstractmethod
    def display_all(self):
        """Must be implemented by subclasses to show all records"""
        pass