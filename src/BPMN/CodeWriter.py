from BPMN.ExprFuncDefinitions import expr_code


class CodeWriter():

    def __init__(self, file_name: str):
        self.file_name = file_name

    def init_file(self) -> None:
        with open(f"{self.file_name}.py", "w") as f:
            f.write("import pandas as pd\nimport numpy as np\n#to run this code u need python 3.x with these packages installed pandas, numpy, numexpr\n")
            f.write(expr_code)

    def write_code(self, code: str) -> None:
        with open(f"{self.file_name}.py", "a") as f:
            f.write(code)
            f.write("\n")
