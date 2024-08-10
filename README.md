
# StashDB

An extremly lightweight json storage for small Python projects.


## Features


- Easy to learn
- Fast
- Does not require any previous knowledge of databases to get started




## Installation

Install StashDB with `pip`

```bash
  pip install stashdb
```
    


## Usage/Examples

Creating a Database
```python
from stashdb import DB

db = DB("app") # replace app with whatever you want to name the database
```


Adding values to the Database
```python
from stashdb import DB

db = DB("app") 

db.append("age", 18)
```

One thing to note is that even if the script is rerun, as long as it has been created once, the database will not override itself, so there is no need to remove the `DB` class.


Overriding the entire database
```python
from stashdb import DB

db = DB("app") 

data = {
    "age": 18,
    "active": False
}
db.write_all(data) # rewrites the entire database
```


Reading the entire database
```python
from stashdb import DB

db = DB("app") 

data = db.read_all() # returns a dictionary
print(data)
```


Reading the value of a specified key
```python
from stashdb import DB

db = DB("app")

value = db.get_value("age")
print(value)
```



Getting all the keys in the database
```python
from stashdb import DB

db = DB("app")

keys = db.get_keys() # returns a list
print(keys)
```



Updating a value
```python
from stashdb import DB

db = DB("app")

db.update("age", 17) 
```



Deleting a value
```python
from stashdb import DB

db = DB("app")

is_deleted = db.delete("age") # this returns a bool
```


Deleting the entire database
```python
from stashdb import DB

db = DB("app")

db.delete_all()
```







## Badges


[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

## 🔗 Links

[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://x.com/lordryns)


## Contributing

Contributions are always welcome!

See `contributing.md` for ways to get started.

Please adhere to this project's `code of conduct`.


## Authors

- [@lordryns](https://www.github.com/lordryns)

