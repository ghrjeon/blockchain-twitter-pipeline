import subprocess

# Run all scripts in order for ingestion
python_scripts = [
    "blockchain/transactions.py", 
    "blockchain/users.py",
    "twitter/scrape.py",
    "twitter/clean.py",
    "twitter/infer.py",
    # "blockchain/flipside_test.py",
]

# Run all scripts 
for script in python_scripts:
    subprocess.call(['python', script])
    print("finished", script)  