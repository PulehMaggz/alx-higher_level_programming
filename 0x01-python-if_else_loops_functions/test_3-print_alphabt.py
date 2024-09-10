import subprocess

def test_script():
    result = subprocess.run(['./3-print_alphabt.py'], capture_output=True, text=True)
    output = result.stdout.strip()
    expected_output = 'abcdfghijklmnoprstuvwxyz'
    
    assert output == expected_output, f"Expected '{expected_output}', but got '{output}'"

if __name__ == "__main__":
    test_script()
