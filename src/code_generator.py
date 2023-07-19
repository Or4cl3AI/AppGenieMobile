```python
class CodeGenerator:
    def __init__(self, app_details):
        self.app_name = app_details['app_name']
        self.app_description = app_details['app_description']

    def generate_code(self):
        code = f"""
# {self.app_name}
# {self.app_description}

def main():
    print("Hello, welcome to {self.app_name}!")

if __name__ == "__main__":
    main()
"""
        return code
```