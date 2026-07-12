import streamlit as st

st.title("🍽️ Smart Bill Splitter")

# Number of people
num_people = st.number_input(
    "Number of people",
    min_value=1,
    step=1
)

people = []

st.subheader("Enter Names")

for i in range(num_people):
    name = st.text_input(
        f"Person {i+1}",
        key=f"name_{i}"
    )

    if name:
        people.append(name)

st.divider()

food_name = st.text_input("Food Name")

food_price = st.number_input(
    "Total Price ($)",
    min_value=0.0,
    step=0.01
)

food_quantity = st.number_input(
    "Total Quantity",
    min_value=1,
    step=1
)

consumption = {}

st.subheader("Who Ate How Many?")

total_consumed = 0

for person in people:
    amount = st.number_input(
        f"{person}",
        min_value=0,
        step=1,
        key=f"eat_{person}"
    )

    consumption[person] = amount
    total_consumed += amount

if st.button("Calculate"):

    if total_consumed != food_quantity:
        st.error(
            f"Total consumed ({total_consumed}) must equal quantity ({food_quantity})"
        )

    else:

        cost_per_unit = food_price / food_quantity

        st.subheader("Results")

        for person in people:

            payment = consumption[person] * cost_per_unit

            st.write(
                f"{person}: ${payment:.2f}"
            )
