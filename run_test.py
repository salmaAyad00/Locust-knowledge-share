#!/usr/bin/env python3

"""
Simple script to run the Locust test with two simultaneous requests.

Usage:
    python run_test.py

This will start Locust with the create-order.py test file.
The test will send two different requests to the same endpoint simultaneously.
"""

import subprocess
import sys
import os

def run_locust():
    """Run the Locust test."""
    
    # Change to the script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    # Activate virtual environment and run locust
    venv_python = os.path.join(script_dir, 'env', 'bin', 'python')
    
    if os.path.exists(venv_python):
        cmd = [venv_python, '-m', 'locust', '-f', 'create-order.py', '--host=http://127.0.0.1:8000', '--run-time=3s']
    else:
        cmd = [sys.executable, '-m', 'locust', '-f', 'create-order.py', '--host=http://127.0.0.1:8000', '--run-time=3s']
    
    print("Starting Locust...")
    print("Command:", ' '.join(cmd))
    print("\nLocust will run for 30 seconds and then automatically stop")
    print("Go to http://localhost:8089 to access the web UI")
    print("Set number of users to 1 or more to see simultaneous requests")
    
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running Locust: {e}")
        return False
    except FileNotFoundError:
        print("Locust not found. Please install it first:")
        print("pip install locust")
        return False
    
    return True

if __name__ == "__main__":
    run_locust()
