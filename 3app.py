import streamlit as st
import math

st.title("🧪 Scientific Calculator")

# Number input
x = st.number_input("Enter a number", value=0.0)

# Operation selector
operation = st.selectbox(
    "Select Operation",
    [
        "Addition (+)",
        "Subtraction (-)",
        "Multiplication (×)",
        "Division (÷)",
        "Power (x^y)",
        "Square Root (√x)",
        "Logarithm (log10)",
        "Natural Log (ln)",
        "Sine (sin)",
        "Cosine (cos)",
        "Tangent (tan)"
    ]
)

# Extra input for operations requiring two numbers
y_needed = ["Addition (+)", "Subtraction (-)", "Multiplication (×)", "Division (÷)", "Power (x^y)"]

if operation in y_needed:
    y = st.number_input("Enter second number", value=0.0)

# Calculate
if st.button("Calculate"):
    try:
        if operation == "Addition (+)":
            result = x + y
        elif operation == "Subtraction (-)":
            result = x - y
        elif operation == "Multiplication (×)":
            result = x * y
        elif operation == "Division (÷)":
            if y == 0:
                result = "Error: Cannot divide by zero"
            else:
                result = x / y
        elif operation == "Power (x^y)":
            result = math.pow(x, y)
        elif operation == "Square Root (√x)":
            result = math.sqrt(x) if x >= 0 else "Error: Negative number"
        elif operation == "Logarithm (log10)":
            result = math.log10(x) if x > 0 else "Error: Must be positive"
        elif operation == "Natural Log (ln)":
            result = math.log(x) if x > 0 else "Error: Must be positive"
        elif operation == "Sine (sin)":
            result = math.sin(math.radians(x))
        elif operation == "Cosine (cos)":
            result = math.cos(math.radians(x))
        elif operation == "Tangent (tan)":
            result = math.tan(math.radians(x))
        else:
            result = "Invalid operation"

        st.success(f"Result: {result}")

    except Exception as e:
        st.error(f"Error: {e}")
