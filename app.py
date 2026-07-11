import streamlit as st

st.title("🍽️ Bill Splitter")

# Number of people
num_people = st.number_input(
    "Number of People",
    min_value=1,
    step=1
)

people = []

if num_people:

    st.subheader("Enter Names")

    for i in range(int(num_people)):
        name = st.text_input(f"Person {i+1}")
        people.append(name)

    st.subheader("Food Items")

    num_items = st.number_input(
        "Number of Food Items",
        min_value=1,
        step=1
    )

    total_bill = 0

    for i in range(int(num_items)):

        food_name = st.text_input(
            f"Food Name {i+1}",
            key=f"food{i}"
        )

        price = st.number_input(
            f"Price of {food_name or f'Item {i+1}'}",
            min_value=0.0,
            key=f"price{i}"
        )

        quantity = st.number_input(
            f"Quantity",
            min_value=1,
            step=1,
            key=f"qty{i}"
        )

        total_bill += price * quantity

    if st.button("Calculate Split"):

        share = total_bill / len(people)

        st.success(f"Total Bill: ${total_bill:.2f}")

        st.subheader("Payment Breakdown")

        for person in people:
            st.write(f"💵 {person}: ${share:.2f}")
