import csv
import datetime

def current_weekday():
    return datetime.datetime.today().weekday()

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# リストから重複を取り除いて返す（順序を保つ）
def remove_duplicates(items):
    seen = set()
    return [x for x in items if not (x in seen or seen.add(x))]

# Specify the path to your CSV file
csv_file_path = 'path/to/your/file.csv'

# Open the CSV file
with open(csv_file_path, mode='r', newline='') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)
    
    # Iterate over each row in the CSV file
    for row in csv_reader:
        print(row)