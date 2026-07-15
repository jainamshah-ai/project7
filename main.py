# main.py
import datetime
import time
import math
import random
import uuid

# Importing our custom package components
import utils
from utils.file_ops import save_log, read_logs
from utils.math import calculate_compound_interest, calculate_area_circle, convert_celsius_to_fahrenheit

LOG_FILE = "toolkit_operations.txt"

def handle_datetime_menu():
    while True:
        print("\n--- Datetime & Time Operations ---")
        print("1. Display Current Date & Time (Custom Format)")
        print("2. Calculate Difference Between Two Dates")
        print("3. Run Simple Stopwatch")
        print("4. Back to Main Menu")
        
        choice = input("Select an option: ").strip()
        
        if choice == '1':
            now = datetime.datetime.now()
            formatted_now = now.strftime("%A, %B %d, %Y - %I:%M:%S %p")
            print(f"\nCurrent Date & Time: {formatted_now}")
            save_log(LOG_FILE, f"[{datetime.datetime.now()}] Displayed time: {formatted_now}")
            
        elif choice == '2':
            print("\nEnter details for Date 1:")
            y1 = int(input("Year (YYYY): "))
            m1 = int(input("Month (1-12): "))
            d1 = int(input("Day (1-31): "))
            
            print("\nEnter details for Date 2 (Future or Past):")
            y2 = int(input("Year (YYYY): "))
            m2 = int(input("Month (1-12): "))
            d2 = int(input("Day (1-31): "))
            
            date1 = datetime.date(y1, m1, d1)
            date2 = datetime.date(y2, m2, d2)
            delta = abs(date2 - date1)
            
            result = f"Difference between {date1} and {date2} is {delta.days} days."
            print(f"\n{result}")
            save_log(LOG_FILE, f"[{datetime.datetime.now()}] calculated date diff: {result}")
            
        elif choice == '3':
            print("\n--- Stopwatch ---")
            input("Press Enter to START the stopwatch...")
            start_time = time.time()
            print("Stopwatch running... Press Ctrl+C or Enter to STOP.")
            try:
                input()
            except KeyboardInterrupt:
                pass
            end_time = time.time()
            elapsed = end_time - start_time
            print(f"Elapsed Time: {elapsed:.2f} seconds.")
            save_log(LOG_FILE, f"[{datetime.datetime.now()}] Stopwatch ran for {elapsed:.2f}s")
            
        elif choice == '4':
            break
        else:
            print("Invalid selection. Try again.")

def handle_math_menu():
    while True:
        print("\n--- Math Operations (Built-in & Custom) ---")
        print("1. Trigonometry, Factorial, and Logarithms (Built-in)")
        print("2. Calculate Compound Interest (Custom)")
        print("3. Calculate Area of a Circle (Custom)")
        print("4. Back to Main Menu")
        
        choice = input("Select an option: ").strip()
        
        if choice == '1':
            num = float(input("Enter a number for Factorial & Log evaluation (e.g., 5): "))
            angle = float(input("Enter an angle in degrees for Sine evaluation: "))
            
            rad = math.radians(angle)
            sine_val = math.sin(rad)
            log_val = math.log(num) if num > 0 else "Undefined (<= 0)"
            fact_val = math.factorial(int(num)) if num >= 0 and num.is_integer() else "Requires positive integer"
            
            res_str = f"Sin({angle}°) = {sine_val:.4f} | Log({num}) = {log_val} | Factorial({int(num)}) = {fact_val}"
            print(f"\nResults:\n{res_str}")
            save_log(LOG_FILE, f"[{datetime.datetime.now()}] Math standard ops: {res_str}")
            
        elif choice == '2':
            p = float(input("Enter principal amount: "))
            r = float(input("Enter annual interest rate (in %): "))
            t = float(input("Enter time in years: "))
            n = int(input("Times interest compounded per year (e.g., 1 for annually, 12 for monthly): "))
            
            total, interest = calculate_compound_interest(p, r, t, n)
            res_str = f"Total Balance: ${total:.2f}, Interest Earned: ${interest:.2f}"
            print(f"\n{res_str}")
            save_log(LOG_FILE, f"[{datetime.datetime.now()}] Interest Calc: {res_str}")
            
        elif choice == '3':
            radius = float(input("Enter circle radius: "))
            area = calculate_area_circle(radius)
            print(f"\nArea of the circle: {area:.4f}")
            save_log(LOG_FILE, f"[{datetime.datetime.now()}] Calculated Circle Area (r={radius}): {area:.4f}")
            
        elif choice == '4':
            break
        else:
            print("Invalid selection. Try again.")

def handle_random_menu():
    while True:
        print("\n--- Randomization & Simulation ---")
        print("1. Generate Secure Random Password")
        print("2. Generate Random OTP (One-Time Password)")
        print("3. Simulate Random Sampling from Dataset")
        print("4. Quick Higher-or-Lower Game Simulation")
        print("5. Back to Main Menu")
        
        choice = input("Select an option: ").strip()
        
        if choice == '1':
            length = int(input("Enter desired password length (min 6): "))
            length = max(6, length)
            chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
            password = "".join(random.choice(chars) for _ in range(length))
            print(f"\nGenerated Password: {password}")
            save_log(LOG_FILE, f"[{datetime.datetime.now()}] Generated secure password.")
            
        elif choice == '2':
            otp = random.randint(100000, 999999)
            print(f"\nYour 6-Digit OTP: {otp}")
            save_log(LOG_FILE, f"[{datetime.datetime.now()}] Generated OTP.")
            
        elif choice == '3':
            dataset = ["Product A", "Product B", "Product C", "Product D", "Product E", "Product F"]
            k = int(input(f"Enter sample size (1 to {len(dataset)}): "))
            k = max(1, min(k, len(dataset)))
            sample = random.sample(dataset, k)
            print(f"\nRandom Sample Selected: {sample}")
            save_log(LOG_FILE, f"[{datetime.datetime.now()}] Dataset random sample: {sample}")
            
        elif choice == '4':
            target = random.randint(1, 10)
            print("\n[Game Simulation] Guess a number between 1 and 10.")
            guess = int(input("Your guess: "))
            if guess == target:
                print("Correct! You won.")
            else:
                print(f"Wrong! The number was {target}.")
            save_log(LOG_FILE, f"[{datetime.datetime.now()}] Played a micro-game simulation.")
            
        elif choice == '5':
            break
        else:
            print("Invalid selection. Try again.")

def handle_uuid_menu():
    print("\n--- UUID Module Unique Identifiers ---")
    generated_uuid = uuid.uuid4()
    print(f"Generated Secure Unique ID (UUID4): {generated_uuid}")
    
    invoice_mock = f"INV-{str(generated_uuid)[:8].upper()}"
    print(f"Example Business Invoice Mapping: {invoice_mock}")
    
    save_log(LOG_FILE, f"[{datetime.datetime.now()}] Generated UUID: {generated_uuid} mapped to {invoice_mock}")

def handle_dynamic_exploration():
    print("\n--- Dynamic Module Exploration using dir() ---")
    print("Choose a module to explore:")
    print("1. math (Built-in)")
    print("2. random (Built-in)")
    print("3. utils.math_utils (Our Custom Module)")
    
    choice = input("Select choice: ").strip()
    if choice == '1':
        print(f"\nAttributes inside 'math' module:\n{dir(math)}")
    elif choice == '2':
        print(f"\nAttributes inside 'random' module:\n{dir(random)}")
    elif choice == '3':
        print(f"\nAttributes inside 'utils.math_utils' module:\n{dir(utils.math)}")
    else:
        print("Invalid Choice.")

def run_business_use_case():
    print("\n==================================================")
    print("      EXECUTING WORKPLACE USE CASE SCENARIO       ")
    print("==================================================")
    print("Scenario: Small business owner managing daily operations.")
    
    # 1. Calculate working hours
    print("\n[Step 1] Tracking Shift Duration...")
    print("Simulating employee checking in...")
    start_shift = time.time()
    time.sleep(1.5)  # Mock delay simulating operational time
    print("Simulating employee checking out...")
    end_shift = time.time()
    hours_worked = (end_shift - start_shift) * 4  # scaled up mock presentation
    print(f"Calculated Working Hours: {hours_worked:.2f} hours.")
    
    # 2. Password Generation
    print("\n[Step 2] Generating random system passwords for team...")
    chars = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"
    emp_pass = "".join(random.choice(chars) for _ in range(8))
    print(f"Temporary Team Password Issued: {emp_pass}")
    
    # 3. UUID Assignment to Invoice
    print("\n[Step 3] Issuing unique invoice identifier...")
    inv_id = uuid.uuid4()
    print(f"New Invoice Registered with UUID Key: {inv_id}")
    
    # 4. Save using Custom Module
    print("\n[Step 4] Committing transaction records via custom module 'file_ops'...")
    log_entry = f"--- BUSINESS LOG | Date: {datetime.date.today()} | Hours Logged: {hours_worked:.2f} | Tracked Invoice: {inv_id} ---"
    if save_log(LOG_FILE, log_entry):
        print("Status: Success! Transaction logs fully committed to disk.")
    
    # 5. Dynamic exploration
    print("\n[Step 5] Dynamically inspecting capabilities of Toolkit array structure...")
    print(f"Available features inside custom package: {dir(utils)}")
    print("==================================================\n")

def main():
    while True:
        print("\n=========================================")
        print("     MULTI-FUNCTIONAL PYTHON TOOLKIT     ")
        print("=========================================")
        print("1. Datetime & Time Operations")
        print("2. Math Module Utilities (Built-in/Custom)")
        print("3. Randomization & Simulation Utilities")
        print("4. UUID Identifier Generation")
        print("5. Dynamic Module Exploration via dir()")
        print("6. Run Automated Business Example Use Case")
        print("7. View Application Saved Logs File")
        print("8. Exit Application")
        print("=========================================")
        
        choice = input("Enter your terminal option (1-8): ").strip()
        
        if choice == '1':
            handle_datetime_menu()
        elif choice == '2':
            handle_math_menu()
        elif choice == '3':
            handle_random_menu()
        elif choice == '4':
            handle_uuid_menu()
        elif choice == '5':
            handle_dynamic_exploration()
        elif choice == '6':
            run_business_use_case()
        elif choice == '7':
            print("\n--- Displaying App Text Log Records ---")
            print(read_logs(LOG_FILE))
        elif choice == '8':
            print("\nThank you for using the Business Operator Toolkit. Goodbye!")
            break
        else:
            print("Invalid global command selection. Please try selecting 1-8.")

# Using the requested __name__ and __main__ paradigm execution guard
if __name__ == "__main__":
    main()