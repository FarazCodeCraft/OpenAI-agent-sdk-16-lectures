#dataclass in pythln
from dataclasses import dataclass
from typing import ClassVar
@dataclass
class America:
    name: str
    age: int
    weight: float
    language: ClassVar[str] = "English"
    def eat (self):
        print(f"{self.name} is eating")
    def speak(self):
        print(f"{self.name} is speaking {America.language}")
    @staticmethod
    def country_language():
        return America.language

john = America("John", 30, 70.5)
print(john.name)  # Output: John    
print(john.country_language())  # Output: English
print(john.language)  # Output: English
print(America.country_language())  # Output: English

 
