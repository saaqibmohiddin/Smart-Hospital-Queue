import streamlit as st

st.set_page_config(
    page_title="Smart Hospital Queue System",
    page_icon="🏥",
    layout="centered"
)

st.title("🏥 Smart Hospital Queue System")
st.write("Manage patient queues easily.")

# Initialize queue
if "queue" not in st.session_state:
    st.session_state.queue = []

if "next_token" not in st.session_state:
    st.session_state.next_token = 1

# Add patient
st.subheader("Add Patient")

patient_name = st.text_input("Enter patient name")

if st.button("Add Patient"):
    if patient_name.strip():
        token = st.session_state.next_token

        st.session_state.queue.append({
            "name": patient_name.strip(),
            "token": token
        })

        st.session_state.next_token += 1

        st.success(
            f"Patient added! Token: {token}"
        )
    else:
        st.warning("Please enter patient name.")

# Display queue
st.subheader("Current Patient Queue")

if st.session_state.queue:
    for position, patient in enumerate(
        st.session_state.queue, start=1
    ):
        st.write(
            f"Token {patient['token']} — "
            f"{patient['name']} — "
            f"Waiting time: {(position - 1) * 10} minutes"
        )
else:
    st.info("No patients waiting.")

# Call next patient
st.subheader("Patient Service")

if st.button("Call Next Patient"):
    if st.session_state.queue:
        patient = st.session_state.queue.pop(0)

        st.success(
            f"Now serving: {patient['name']} "
            f"(Token {patient['token']})"
        )
    else:
        st.warning("No patients waiting.")