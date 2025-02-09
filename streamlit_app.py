import streamlit as st
import random

def is_derangement(permutation, original):
    """Check if a permutation is a derangement of the original list."""
    return all(permutation[i] != original[i] for i in range(len(original)))

def has_mutual_assignment(permutation, original):
    """Check if there are any mutual assignments (name1 -> name2 and name2 -> name1)."""
    for i, original_name in enumerate(original):
        assigned_name = permutation[i]
        # Check if the assigned_name assigns back to the original_name
        if assigned_name in original and permutation[permutation.index(assigned_name)] == original_name:
            return True
    return False

def generate_derangement(names):
    """Generate a derangement of the list of names."""
    if len(names) <= 1:
        return []  # Derangement is not possible for lists of size 1 or less

    derangement = names[:]
    while True:
        random.shuffle(derangement)
        if is_derangement(derangement, names) and not has_mutual_assignment(derangement, names):
            return derangement

# Streamlit UI
st.title("Dérangement Generator")

st.write(
    """This app takes a list of names and generates a "dérangement," 
    a permutation where no element appears in its original position and no two names are mutually assigned."""
)

# Input section
names_input = st.text_area("Enter names (one per line):", height=200)
names = [name.strip() for name in names_input.splitlines() if name.strip()]

if names:
    if st.button("Generate Dérangement"):
        deranged_names = generate_derangement(names)

        st.subheader("Original List:")
        st.write(names)

        st.subheader("Déranged Assignments:")
        assignments = [f"{original} is assigned to {deranged}" for original, deranged in zip(names, deranged_names)]
        for assignment in assignments:
            st.write(assignment)
else:
    st.info("Please enter at least two names to generate a dérangement.")
