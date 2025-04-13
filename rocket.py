import streamlit as st  # This brings in the Streamlit module

# Title on the page
st.title("Rocket Launch Calculator")

# User inputs
mass = st.number_input("Enter rocket mass (kg)", value=500)
thrust = st.number_input("Enter thrust (N)", value=10000)
burn_time = st.number_input("Enter burn time (seconds)", value=5)

# Earth's gravity (constant)
gravity = 9.81

# Calculate when user clicks button
if st.button("Calculate"):
    # Physics calculations
    acceleration = (thrust - mass * gravity) / mass
    final_velocity = acceleration * burn_time
    height = 0.5 * acceleration * (burn_time ** 2)

    # Show results
    st.write(f"Acceleration: {acceleration:.2f} m/s²")
    st.write(f"Final Velocity: {final_velocity:.2f} m/s")
    st.write(f"Estimated Height Reached: {height:.2f} m")
