class MethodNotFoundException(Exception):
    """Exception raised when a requested method is not found."""

    def __init__(self, method):
        self.method = method
        self.message = f"Method '{self.method}' not found."
        super().__init__(self.message)   

    def methodNotFound(self):
        return self.message   