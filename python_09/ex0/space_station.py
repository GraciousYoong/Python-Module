from pydantic import BaseModel, EmailStr, Field, ValidationError

# 1. Define the schema by inheriting from BaseModel
class User(BaseModel):
    # Minimum value constraint: id must be 1 or higher
    id: int = Field(gt=0)                              
    
    # String length constraint: name must be between 2 and 50 characters
    name: str = Field(min_length=2, max_length=50)                            
    
    # Strict email validation replaces the plain 'str' type hint
    email: EmailStr                           
    
    # Numeric constraint: if age is provided, it must be between 0 and 120
    age: int | None = Field(default=None, ge=0, le=120)               
    
    is_active: bool = True               

# 2. Parse and validate valid data 
valid_user = User(id="123", name="Alice", email="alice@example.com")
print(valid_user.id)  # Output: 123 (integer)

# 3. Export to JSON
json_data = valid_user.model_dump_json()
print(json_data)

# 4. Invalid data now accurately catches bad emails and bad field constraints
try:
    invalid_user = User(id=0, name="B", email="not-an-email", age=-5)
except ValidationError as e:
    print(e)