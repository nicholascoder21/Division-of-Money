import streamlit as st

st.title("🍽️ FairSplit - Smart Expense Sharing")

# Enter people
st.header("Step 1: Enter People")

people_input = st.text_input(
    "Enter names separated by commas",
    placeholder="Neke, Kayden, John"
)

if people_input:

    people = [p.strip() for p in people_input.split(",")]

    st.header("Step 2: Add Food Items")

    num_items = st.number_input(
        "Number of food items",
        min_value=1,
        step=1
    )

    payments = {person: 0.0 for person in people}

    for i in range(num_items):

        st.subheader(f"Food Item {i+1}")

        food_name = st.text_input(
            "Food Name",
            key=f"name{i}"
        )

        price = st.number_input(
            "Price ($)",
            min_value=0.0,
            step=0.01,
            key=f"price{i}"
        )

        shared = st.checkbox(
            "Shared Item?",
            key=f"shared{i}"
        )

        if shared:

            quantity = st.number_input(
                "Total Quantity",
                min_value=1,
                step=1,
                key=f"qty{i}"
            )

            consumption = {}
            total_eaten = 0

            st.write("How many portions did each person eat?")

            for person in people:

                amount = st.number_input(
                    person,
                    min_value=0,
                    step=1,
                    key=f"{person}_{i}"
                )

                consumption[person] = amount
                total_eaten += amount

            if total_eaten > 0:

                cost_per_unit = price / quantity

                for person in people:
                    payments[person] += (
                        consumption[person] * cost_per_unit
                    )

        else:

            owner = st.selectbox(
                "Who ordered this item?",
                people,
                key=f"owner{i}"
            )

            payments[owner] += price

    if st.button("Calculate Bill"):

        st.header("💰 Amount Owed")

        grand_total = 0

        for person, amount in payments.items():

            st.write(
                f"**{person}: ${amount:.2f}**"
            )

            grand_total += amount

        st.divider()

        st.write(
            f"**Total Bill: ${grand_total:.2f}**"
        )
