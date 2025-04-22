import streamlit as st

# Custom CSS for a "bluesky" look
st.markdown("""
    <style>
        .main {
            background-color: #e6f0ff;
            color: #003366;
        }
        .stButton>button {
            background-color: #66a3ff;
            color: white;
            border-radius: 10px;
            height: 3em;
            width: 10em;
            font-weight: bold;
        }
        .stSelectbox, .stNumberInput {
            background-color: #ffffff;
            border: 2px solid #99c2ff;
            border-radius: 5px;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🌤️ Bluesky Calculator")

# Input numbers
num1 = st.number_input("Enter the first number", format="%.2f")
num2 = st.number_input("Enter the second number", format="%.2f")

# Select operation
operation = st.selectbox(
    "Select an operation",
    [
        "Addition (+)",
        "Subtraction (-)",
        "Multiplication (×)",
        "Division (÷)",
        "Modulus (%)",
        "Exponentiation (^)",
        "Floor Division (//)"
    ]
)

# Calculate result
def calculate(n1, n2, op):
    if op == "Addition (+)":
        return n1 + n2
    elif op == "Subtraction (-)":
        return n1 - n2
    elif op == "Multiplication (×)":
        return n1 * n2
    elif op == "Division (÷)":
        if n2 == 0:
            return "Error: Division by zero"
        return n1 / n2
    elif op == "Modulus (%)":
        if n2 == 0:
            return "Error: Division by zero"
        return n1 % n2
    elif op == "Exponentiation (^)":
        return n1 ** n2
    elif op == "Floor Division (//)":
        if n2 == 0:
            return "Error: Division by zero"
        return n1 // n2

if st.button("Calculate"):
    result = calculate(num1, num2, operation)
    st.success(f"☁️ Result: {result}")
