#understanding data science workflow
"""_Summary_
1. Problem definition
2.Data acquisition data.gov, kaggle, databases, APIs, External datasets
Ensure data quality, data validation, cleaning and processing
#EDA Data exploratory Analysis
#Data preparation and processing
"""

#multithreading and multiprocessing 
#context manager - an object that defines a temporary context for a block of code
#Example: Demonstrate a context manager to open a file and returns a context manager instance
"""class OpenFileContextManager:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, "r")
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()

# Usage example
with OpenFileContextManager("my_file.txt") as f:
    contents = f.read()
    print(contents)
"""
"""
Multithreading is a technique where multiple threads of execution run concurrently within a single process.
Each thread represents an independent flow of control, allowing for concurrent execution of multiple tasks.
In Python, the threading module provides a way to create and manage threads.
""",
import threading

def worker():
    print("Worker thread executing")

# Create two worker threads
thread1 = threading.Thread(target=worker)
thread2 = threading.Thread(target=worker)

# Start the threads
thread1.start()
thread2.start()

# Wait for threads to complete
thread1.join()
thread2.join()

print("All threads completed")
print("----------------------------------------------------------------")

"""
Multiprocessing, on the other hand, involves running multiple processes in parallel, each with its own instance of the Python interpreter.
This allows for true parallel execution of CPU-bound tasks.
The multiprocessing module in Python provides a way to create and manage processes.
"""
import multiprocessing

def worker():
    print("Worker process executing")

# Create two worker processes
process1 = multiprocessing.Process(target=worker)
process2 = multiprocessing.Process(target=worker)

# Start the processes
process1.start()
process2.start()

# Wait for processes to complete
process1.join()
process2.join()

print("All processes completed")
print("----------------------------------------------------------------")

"""Assignment A7"""
#Number 1
class OpenFile:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, "w")  # Open file in write mode
        return self.file

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.file.close()

with OpenFile("my_file.txt") as f:
    f.write("Multithreading, Multiprocessing, and Context Manager\n")
    f.write("\n")

    f.write("Table:\n")
    f.write("-----------\n")
    f.write("| Title       | Description                 |\n")
    f.write("-----------|------------------------|\n")
    f.write("| Multithreading  | Allows concurrent execution of multiple threads within a process. |\n")
    f.write("| Multiprocessing | Enables parallel execution by running multiple processes.           |\n")
    f.write("| Context Manager | Provides a convenient way to manage resources using the 'with' statement.|\n")
    f.write("-----------|------------------------|\n")

print("File created and written successfully.")
print("----------------------------------------------------------------")

#Number 2
import sqlite3

# Create the database file and table
def create_database():
    conn = sqlite3.connect("my_database.db")

    create_table_query = """
    CREATE TABLE IF NOT EXISTS my_table (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
    """
    conn.execute(create_table_query)

    insert_data_query = """
    INSERT INTO my_table (name, age) VALUES
        ('Geoffrey', 35),
        ('Dorothy', 21),
        ('Jonathan', 28)
    """
    conn.execute(insert_data_query)

    conn.commit()
    conn.close()

# Define the DatabaseConnectionContextManager
class DatabaseConnectionContextManager:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_name)
        return self.connection

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.connection.close()

# Create the database file and table
create_database()

# Usage example of the DatabaseConnectionContextManager
with DatabaseConnectionContextManager("my_database.db") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM my_table")
    results = cursor.fetchall()
    for row in results:
        print(row)
print("----------------------------------------------------------------")

import time
import threading
import multiprocessing

# Perform a task for a given duration
def perform_task(duration):
    print(f"Executing task. This task will run for {duration} seconds.")
    time.sleep(duration)
    print("Task completed.")

# Example using multithreading
def run_multithreading_example():
    tasks = [
        {"duration": 3},
        {"duration": 5},
        {"duration": 2}
    ]

    threads = []

    for task in tasks:
        duration = task["duration"]
        thread = threading.Thread(target=perform_task, args=(duration,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    print("All tasks executed successfully.")

# Example using multiprocessing
def run_multiprocessing_example():
    tasks = [
        {"duration": 3},
        {"duration": 5},
        {"duration": 2}
    ]

    processes = []

    for task in tasks:
        duration = task["duration"]
        process = multiprocessing.Process(target=perform_task, args=(duration,))
        processes.append(process)
        process.start()

    # Wait for all processes to complete
    for process in processes:
        process.join()

    print("All tasks executed successfully.")

# Run the multithreading example
print("Executing multithreading example:")
run_multithreading_example()
print()

# Run the multiprocessing example
print("Executing multiprocessing example:")
run_multiprocessing_example()




