
# 📘 README: Python Programming – Session 05

**Topic:** Understanding Variables & Numbers in Python  
**Course:** Programming for Problem Solving Using Python  
**Institution:** K.R. Mangalam University – School of Engineering & Technology  

## 🧠 Session Overview  

This session introduces Python variables and number types, including how to declare, assign, manipulate, and understand their scope and behavior.

---

## 🔤 Variables in Python

### What is a Variable?

- A container to store reusable data.
- Can be short (`x`, `y`) or descriptive (`age`, `total_volume`).

### Rules for Naming Variables

- Only letters, numbers, and underscores.
- Cannot start with a number.
- Case-sensitive (`myVar` ≠ `MyVar`).

### Naming Conventions

- Use lowercase.
- Separate words with underscores (`user_input`, `num_of_items`).
- Be clear and concise.

### Declaration & Assignment

```python
x = 5
name = "John"
is_student = True
x = 10  # reassignment
```

### Data Type Inference

Python automatically assigns data types based on the value:

```python
x = 2          # int
x = '2'        # str
x = 2.0        # float
y = float(2)   # typecasting
```

---

## 🌍 Variable Scope

### Local vs Global Variables

- **Local:** Defined inside functions; accessible only there.
- **Global:** Defined outside functions; accessible throughout the program.

### Using `global` Keyword

```python
def my_func():
    global my_var
    my_var = 10
```

---

## 🔢 Numbers in Python

### Types & Operations

```python
x = 5           # int
y = 3.14        # float

sum = x + y
difference = x - y
product = x * y
quotient = x / y
```

### Temperature Conversion

```python
celsius = 20
fahrenheit = (celsius * 9/5) + 32

fahrenheit = 68
celsius = (fahrenheit - 32) * 5/9
```

### Simple Interest Calculation

```python
principal = 1000
rate = 5
time = 2
simple_interest = (principal * rate * time) / 100
```

---

## 🧪 Test Your Knowledge

### Fill in the Blanks

- Variables store data.
- Types: int, float, str, bool.
- No need to declare types explicitly.
- Integer division (`//`) gives quotient.
- Modulus (`%`) gives remainder.
- Type conversion: `int()`, `float()`, `str()`.

### MCQs

1. Comment syntax: `# This is a comment`
2. Multiple assignment: `a = b = c = 10`
3. Output of `10 // 3`: `3`
4. Value of `c = a + b`: `25` (if `a = 10`, `b = 15`)

---

## 💬 Interview Questions

1. What are variables and how are they declared?
2. Difference between integers and floats.
3. Type conversion examples.
4. Dynamic typing in Python.
5. Arithmetic operators: `+`, `-`, `*`, `/`, `//`, `%`, `**`
