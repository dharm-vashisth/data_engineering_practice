from pydantic import BaseModel, field_validator, EmailStr, ValidationError
from typing import Optional


# Data Contract
class StudentRecords(BaseModel):
    reg_no: int
    student_name: str
    marks: float
    email: Optional[EmailStr] = None

    # field validation
    @field_validator('reg_no')
    @classmethod
    def validate_reg_no(cls, value):
        if value < 1:
            raise ValueError(f"Invalid registration number. It should be a positive number. Got: {value} \n")
        return value


if __name__ == "__main__":
    data = [
        {'reg_no': 1, 'student_name': 'Dharm Vashisth', 'marks': 91.76},  # good data
        {'reg_no': -123, 'student_name': 'Rakesh Vashisth', 'marks': 88.0},  # bad data
        # good data since auto type casting
        {'reg_no': "23", 'student_name': 'Rakesh D', 'marks': 85.0, 'email': 'abc@ab.com'},
        {'reg_no': 13, 'student_name': 'Rakesh K', 'marks': 86.0, 'email': 'abc'}  # bad data
    ]

    for record in data:
        try:
            student = StudentRecords(**record)
            print(f"✅Data validation is successful for {record['student_name']} \n")
        except ValidationError as e:
            print(f"❌Data validation failed for {record['student_name']}. \n {e.json()}\n")
