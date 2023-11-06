# Python type hints
num1 : int = 12
num2 : int = 13
myString : str = 'String'
myList : list[int] = [1,2,3,4,5,6]
myDic : dict[str,str] = {'String' : 'String'}

# Type hints in functions
def suM(a : int, b : int) -> int:
    print(suM(1,4))

# Create my own type hints
new_dic = dict[str, list[str]]

my_new_dic : new_dic = {'Network1': ['10.0.2.4', '12:32:43:32:41', '80'],
                        'Network2' : ['10.0.2.5', '42:22:34:65:12', '80']}

# If the function returns something, need to change the None fot the type that i'm returning
def run(map : new_dic) -> None:
    for key, value in map.items():
        print(f'Network name: {key}, IP/MAC/PORT: {value[0]}/{value[1]}/{value[2]}')

run(my_new_dic)
# 9:55
# More advanced type hints

from typing import Any, Sequence, Callable, Union, Optional

# Any : returns anything 
def my_any(value : Any) -> Any:
    return value ** 2

# Sequence : Whatever it's a sequence
def my_sequence(value : Sequence):
    for n in value:
        print(n)

# Callable : Creates a function that receives as parameter another function
def my_fct(fct : Callable):
    fct()
# 2nd function
def sec_fct():
    print('Hello world')

my_fct(sec_fct)

# Union : Allows to have multiple try:
def my_union(value : Union[str,int]) -> None:
    print(value)

# Optional : Optional parameter
# Needs to have the optional parameter, if it isn't, doesn't work
def my_optional(value : Optional[int] = 5) -> None:
    print(value)

# Generics
from typing import TypeVar, Generic

# Generic Class
# Only creates a object that says that the return value ins any type of var

# I can create many as i want to show more datatypes that i'm going to use
T = TypeVar('T')

# Creates a class that is generic and can work with many datatypes
class generic_class(Generic[T]):
    # content is any datatype
    def __init__(self, content : T):
        self.content = content

    def get_content(self) -> T:
        return self.content

string_type = generic_class('String type')
int_type = generic_class(12)

# Generic methods or functions
def first(seq : Sequence[T]) -> T:
    return seq[0]
# Si le paso una lista de enteros, me devolvera un valor de tipo entero
# El return esta determinado por el tipo de dato del primer elemento de la lista
