from typing import TypedDict

class Person(TypedDict):

    name: str
    age: int

new_person: Person = {'name':'Gourab Kumar', 'age':'25'}

print(new_person)