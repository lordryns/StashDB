import json, os 


class DB:
    """The Base Database class"""
    def __init__(self, path: str) -> None:
        new_path = path.split('.')[0] + ".json"
        if os.path.exists(new_path):
            self.path = new_path
        else:
            try:
                with open(new_path, 'w') as fp:
                    fp.write("{}")

                self.path = new_path

            except Exception as e:
                print(e)



    def read_all(self) -> dict:
        """Reads all data in the Database and returns a dictionary."""
        with open(self.path, 'r') as fp:
            return json.load(fp=fp)
        

    
    def write_all(self, data: dict) -> None:
        """ignores every other data in the Database and rewrites it with new data, Be careful when working with this method."""
        if type(data) is dict:
            with open(self.path, 'w') as fp:
                json.dump(data, fp, skipkeys=True, indent=4)

        else:
            raise ValueError("All data must be contained within a dictionary!")
        

    def append(self, key: str | int, value: any) -> None:
        """Appends a key/value pair to the Database, replaces any other key/value pair in the Database."""
        json_data = self.read_all()
        json_data[key] = value 

        self.write_all(json_data)


    def update(self, key: str | int, value: any) -> None:
        """Updates a key/value pair with new specified data, wrapper for append."""
        self.append(key, value)

    
    def get_value(self, key: str | int) -> any:
        """Specify a valid key and get the value it stores."""
        json_data = self.read_all()
        if key in json_data:
            return json_data[key]
        
        else:
            raise KeyError(f"Key '{key}' does not exist in the database!")
        

    def get_keys(self) -> list:
        """This returns every key in the Database."""
        json_data = self.read_all()
        return list(json_data.keys())
    

    def delete(self, key: str | int) -> bool:
        """This deletes a certain key/value pair based on the key specified."""
        json_data = self.read_all()

        if key in json_data:
            del json_data[key]
            self.write_all(json_data)

            return True
        
        else:
            raise KeyError(f"'{key}' is not a valid key in this db, it might have already been deleted or renamed.")
        

    def delete_all(self) -> bool:
        """This empties the database, be careful when using this."""
        self.write_all({})
        return True