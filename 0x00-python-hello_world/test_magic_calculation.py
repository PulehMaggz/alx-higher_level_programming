import importlib.util
import sys

# Load the module
module_name = "102-magic_calculation"
file_path = f"./{module_name}.py"

spec = importlib.util.spec_from_file_location(module_name, file_path)
module = importlib.util.module_from_spec(spec)
sys.modules[module_name] = module
spec.loader.exec_module(module)

# Test the function
result = module.magic_calculation(2, 3)
print(result)  # Expected output: 106

