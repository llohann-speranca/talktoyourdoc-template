

class DatabaseConnector:
    """Class that receives a hash_code and retrieves a row from the database."""
    def __call__(self, hash_code):
        """returns the row"""
        raise NotImplementedError
