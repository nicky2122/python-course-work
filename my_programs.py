# 1. Median of a List
def median_of_list():
    print("🧠 Program: Find the Median of a List\n")
    print("📄 Code:\n\"\"\"\nnums = [12, 5, 8, 21, 14]\nnums.sort()\nif len(nums) % 2 == 0:\n    median = (nums[len(nums)//2 - 1] + nums[len(nums)//2]) / 2\nelse:\n    median = nums[len(nums)//2]\nprint(median)\n\"\"\"")
    print("\n🧪 Test Case:")
    print("Input: [12, 5, 8, 21, 14] ➝ Output: 12")
    print("\n📝 Explanation:")
    print("Sort the list. If odd length, median is the middle element; if even, average of two middle values.\n")

# 2. Even-indexed Characters
def even_indexed_chars():
    print("🧠 Program: Print Even-Indexed Characters from String\n")
    print("📄 Code:\n\"\"\"\ntext = 'PythonProgramming'\nresult = text[::2]\nprint(result)\n\"\"\"")
    print("\n🧪 Test Case:")
    print("Input: 'PythonProgramming' ➝ Output: 'Pto rgamn'")
    print("\n📝 Explanation:")
    print("Using slicing with step 2 returns characters at indices 0, 2, 4, ...\n")

# 3. Random Number
def random_number():
    print("🧠 Program: Generate a Random Number Between 1 to 100\n")
    print("📄 Code:\n\"\"\"\nimport random\nnum = random.randint(1, 100)\nprint(num)\n\"\"\"")
    print("\n🧪 Test Case:")
    print("Output Example: 73 (varies each run)")
    print("\n📝 Explanation:")
    print("random.randint(1, 100) generates a number between 1 and 100 inclusive.\n")

# 4. Calendar Display
def display_calendar():
    print("🧠 Program: Display Calendar for a Given Month and Year\n")
    print("📄 Code:\n\"\"\"\nimport calendar\nyear = 2025\nmonth = 8\nprint(calendar.month(year, month))\n\"\"\"")
    print("\n🧪 Test Case:")
    print("Input: Year=2025, Month=8 ➝ Output: August 2025 calendar")
    print("\n📝 Explanation:")
    print("calendar.month(year, month) prints that month's calendar in a formatted way.\n")

# 5. Triangle Type
def triangle_type():
    print("🧠 Program: Check if a Triangle is Equilateral, Isosceles, or Scalene\n")
    print("📄 Code:\n\"\"\"\na, b, c = 5, 5, 5\nif a == b == c:\n    print('Equilateral')\nelif a == b or b == c or a == c:\n    print('Isosceles')\nelse:\n    print('Scalene')\n\"\"\"")
    print("\n🧪 Test Case:")
    print("Input: 5, 5, 5 ➝ Output: Equilateral")
    print("\n📝 Explanation:")
    print("All sides equal = Equilateral, two equal = Isosceles, all different = Scalene.\n")

# 6. BMI Calculation
def bmi_calc():
    print("🧠 Program: Calculate BMI (Body Mass Index)\n")
    print("📄 Code:\n\"\"\"\nweight = 60\nheight = 1.65\nbmi = weight / (height ** 2)\nprint(round(bmi, 2))\n\"\"\"")
    print("\n🧪 Test Case:")
    print("Input: Weight=60kg, Height=1.65m ➝ Output: 22.04")
    print("\n📝 Explanation:")
    print("BMI formula: weight / height², rounded to 2 decimal places.\n")

# 7. Factors of a Number
def factors():
    print("🧠 Program: Find All Factors of a Number\n")
    print("📄 Code:\n\"\"\"\nnum = 28\nfactors = []\nfor i in range(1, num + 1):\n    if num % i == 0:\n        factors.append(i)\nprint(factors)\n\"\"\"")
    print("\n🧪 Test Case:")
    print("Input: 28 ➝ Output: [1, 2, 4, 7, 14, 28]")
    print("\n📝 Explanation:")
    print("Loop from 1 to n, append i if it divides n evenly.\n")

# 8. Title Case Without .title()
def title_case():
    print("🧠 Program: Convert a String to Title Case Without Using title()\n")
    print("📄 Code:\n\"\"\"\ntext = 'hello world from python'\nwords = text.split()\ntitle_case = ' '.join(w[0].upper() + w[1:] for w in words)\nprint(title_case)\n\"\"\"")
    print("\n🧪 Test Case:")
    print("Input: 'hello world from python' ➝ Output: 'Hello World From Python'")
    print("\n📝 Explanation:")
    print("Split string into words, capitalize first letter of each, then join.\n")

# 9. Count Spaces
def count_spaces():
    print("🧠 Program: Count Total Number of Spaces in a String\n")
    print("📄 Code:\n\"\"\"\ntext = 'Python is fun to learn'\nspaces = text.count(' ')\nprint(spaces)\n\"\"\"")
    print("\n🧪 Test Case:")
    print("Input: 'Python is fun to learn' ➝ Output: 4")
    print("\n📝 Explanation:")
    print("count(' ') returns the number of spaces in the string.\n")

# 10. Hours & Minutes to Seconds
def time_to_seconds():
    print("🧠 Program: Convert Hours and Minutes into Seconds\n")
    print("📄 Code:\n\"\"\"\nhours = 2\nminutes = 30\nseconds = hours * 3600 + minutes * 60\nprint(seconds)\n\"\"\"")
    print("\n🧪 Test Case:")
    print("Input: 2h 30m ➝ Output: 9000")
    print("\n📝 Explanation:")
    print("1 hour = 3600s, 1 minute = 60s, multiply and add.\n")



