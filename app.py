import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# --- Page Setup ---
st.set_page_config(page_title="Systems of Equations Exam Prep", page_icon="📐")

# --- Developer Credit ---
st.markdown("### [www.cognitivecloud.ai](https://www.cognitivecloud.ai)")
st.markdown("**Developed by Xavier Honablue M.Ed**")

st.markdown("---")

# --- Title ---
st.title("📐 Systems of Linear Equations: Exam Prep for Meka Wilson")

st.markdown("""
This program will help you master systems of linear equations for your upcoming exam.

### What is a System of Linear Equations?
A **system of linear equations** consists of two or more linear equations with the same variables. 
The solution is the point(s) where all equations are simultaneously true.

### Three Solution Methods You Need to Know:
1. **Graphing** - Visual method to find intersection
2. **Substitution** - Algebraic method when one variable is isolated
3. **Elimination** - Algebraic method by adding/subtracting equations
""")

# --- Student Name ---
st.sidebar.header("Student Information")
student_name = st.sidebar.text_input("Enter your name:", value="Meka Wilson")
if student_name:
    st.sidebar.success(f"Welcome, {student_name}!")

# --- Method Selection ---
st.header("📚 Choose Your Learning Path")

learning_mode = st.radio("What do you want to practice?", [
    "Learn the Three Methods",
    "Practice Problems",
    "Take a Practice Test",
    "Review Common Mistakes"
])

# ==================== LEARN THE THREE METHODS ====================
if learning_mode == "Learn the Three Methods":
    st.header("The Three Methods for Solving Systems")
    
    method_choice = st.selectbox("Select a method to learn:", [
        "Graphing Method",
        "Substitution Method",
        "Elimination Method"
    ])
    
    if method_choice == "Graphing Method":
        st.subheader("Graphing Method")
        st.markdown("""
        **When to use:** When you need a visual solution or when both equations are in slope-intercept form.
        
        **Steps:**
        1. Write both equations in slope-intercept form (y = mx + b)
        2. Graph both lines on the same coordinate plane
        3. Find the intersection point
        4. Check your answer by substituting into both original equations
        
        **Example:** Solve the system:
        - y = 2x + 1
        - y = -x + 4
        """)
        
        # Graph example
        x = np.linspace(-2, 5, 100)
        y1 = 2*x + 1
        y2 = -x + 4
        
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.plot(x, y1, 'b-', linewidth=2, label='y = 2x + 1')
        ax.plot(x, y2, 'r-', linewidth=2, label='y = -x + 4')
        ax.axhline(y=0, color='k', linewidth=0.5)
        ax.axvline(x=0, color='k', linewidth=0.5)
        ax.grid(True, alpha=0.3)
        ax.legend()
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title('Graphing Method Example')
        
        # Mark intersection point
        ax.plot(1, 3, 'go', markersize=10, label='Solution (1, 3)')
        ax.legend()
        
        st.pyplot(fig)
        
        st.success("**Solution: (1, 3)**")
        st.write("Check: y = 2(1) + 1 = 3 ✓ and y = -(1) + 4 = 3 ✓")
    
    elif method_choice == "Substitution Method":
        st.subheader("Substitution Method")
        st.markdown("""
        **When to use:** When one equation is already solved for a variable, or can be easily solved for one.
        
        **Steps:**
        1. Solve one equation for one variable (x or y)
        2. Substitute that expression into the other equation
        3. Solve for the remaining variable
        4. Substitute back to find the other variable
        5. Check your solution
        
        **Example:** Solve the system:
        - y = 3x - 5
        - 2x + y = 4
        
        **Solution:**
        
        Step 1: First equation is already solved for y
        
        Step 2: Substitute y = 3x - 5 into second equation:
        ```
        2x + (3x - 5) = 4
        ```
        
        Step 3: Solve for x:
        ```
        2x + 3x - 5 = 4
        5x - 5 = 4
        5x = 9
        x = 9/5 = 1.8
        ```
        
        Step 4: Substitute x = 1.8 back into first equation:
        ```
        y = 3(1.8) - 5
        y = 5.4 - 5
        y = 0.4
        ```
        
        Step 5: Check in both equations:
        - y = 3(1.8) - 5 = 0.4 ✓
        - 2(1.8) + 0.4 = 3.6 + 0.4 = 4 ✓
        """)
        
        st.success("**Solution: (1.8, 0.4) or (9/5, 2/5)**")
    
    else:  # Elimination Method
        st.subheader("Elimination Method")
        st.markdown("""
        **When to use:** When coefficients of variables can be made opposites, or when both equations are in standard form.
        
        **Steps:**
        1. Arrange both equations in standard form (Ax + By = C)
        2. Multiply one or both equations to make coefficients of one variable opposites
        3. Add or subtract equations to eliminate that variable
        4. Solve for the remaining variable
        5. Substitute back to find the other variable
        6. Check your solution
        
        **Example:** Solve the system:
        - 3x + 2y = 16
        - 5x - 2y = 8
        
        **Solution:**
        
        Step 1: Both equations are already in standard form
        
        Step 2: Notice that 2y and -2y are already opposites!
        
        Step 3: Add the equations to eliminate y:
        ```
        3x + 2y = 16
        5x - 2y = 8
        ___________
        8x + 0 = 24
        ```
        
        Step 4: Solve for x:
        ```
        8x = 24
        x = 3
        ```
        
        Step 5: Substitute x = 3 into first equation:
        ```
        3(3) + 2y = 16
        9 + 2y = 16
        2y = 7
        y = 3.5
        ```
        
        Step 6: Check in both equations:
        - 3(3) + 2(3.5) = 9 + 7 = 16 ✓
        - 5(3) - 2(3.5) = 15 - 7 = 8 ✓
        """)
        
        st.success("**Solution: (3, 3.5) or (3, 7/2)**")

# ==================== PRACTICE PROBLEMS ====================
elif learning_mode == "Practice Problems":
    st.header("Practice Problems")
    
    difficulty = st.selectbox("Choose difficulty level:", [
        "Easy - Graphing",
        "Medium - Substitution",
        "Hard - Elimination"
    ])
    
    if difficulty == "Easy - Graphing":
        st.subheader("Problem 1: Graphing Method")
        st.write("Solve by graphing:")
        st.write("- y = x + 2")
        st.write("- y = -x + 6")
        
        show_solution_1 = st.checkbox("Show solution")
        if show_solution_1:
            x = np.linspace(-2, 8, 100)
            y1 = x + 2
            y2 = -x + 6
            
            fig, ax = plt.subplots(figsize=(8, 6))
            ax.plot(x, y1, 'b-', linewidth=2, label='y = x + 2')
            ax.plot(x, y2, 'r-', linewidth=2, label='y = -x + 6')
            ax.axhline(y=0, color='k', linewidth=0.5)
            ax.axvline(x=0, color='k', linewidth=0.5)
            ax.grid(True, alpha=0.3)
            ax.plot(2, 4, 'go', markersize=10)
            ax.legend()
            ax.set_xlabel('x')
            ax.set_ylabel('y')
            st.pyplot(fig)
            st.success("Solution: (2, 4)")
    
    elif difficulty == "Medium - Substitution":
        st.subheader("Problem 2: Substitution Method")
        st.write("Solve using substitution:")
        st.write("- y = 2x + 3")
        st.write("- 3x + y = 13")
        
        show_solution_2 = st.checkbox("Show solution")
        if show_solution_2:
            st.markdown("""
            **Solution:**
            
            Substitute y = 2x + 3 into second equation:
            ```
            3x + (2x + 3) = 13
            5x + 3 = 13
            5x = 10
            x = 2
            ```
            
            Find y:
            ```
            y = 2(2) + 3 = 7
            ```
            
            Check:
            - y = 2(2) + 3 = 7 ✓
            - 3(2) + 7 = 13 ✓
            """)
            st.success("Solution: (2, 7)")
    
    else:  # Hard - Elimination
        st.subheader("Problem 3: Elimination Method")
        st.write("Solve using elimination:")
        st.write("- 2x + 3y = 12")
        st.write("- 4x - y = 5")
        
        show_solution_3 = st.checkbox("Show solution")
        if show_solution_3:
            st.markdown("""
            **Solution:**
            
            Multiply first equation by 2 to make x coefficients 4 and 4:
            ```
            4x + 6y = 24
            4x - y = 5
            ```
            
            Subtract second from first:
            ```
            (4x + 6y) - (4x - y) = 24 - 5
            7y = 19
            y = 19/7 ≈ 2.71
            ```
            
            Substitute back into 4x - y = 5:
            ```
            4x - 19/7 = 5
            4x = 5 + 19/7 = 35/7 + 19/7 = 54/7
            x = 54/28 = 27/14 ≈ 1.93
            ```
            """)
            st.success("Solution: (27/14, 19/7) or approximately (1.93, 2.71)")

# ==================== PRACTICE TEST ====================
elif learning_mode == "Take a Practice Test":
    st.header("Practice Test")
    st.write("Answer these questions to test your understanding:")
    
    # Question 1
    st.subheader("Question 1: Multiple Choice")
    q1 = st.radio(
        "What is the graphical representation of the solution to a system of linear equations?",
        ["The y-intercept", "The point of intersection", "The slope", "The origin"]
    )
    if st.button("Check Answer 1"):
        if q1 == "The point of intersection":
            st.success("Correct! The solution is where the lines intersect.")
        else:
            st.error("Incorrect. The solution is the point of intersection.")
    
    # Question 2
    st.subheader("Question 2: Which method?")
    q2 = st.radio(
        "Which method is best when one equation is already solved for y?",
        ["Graphing", "Substitution", "Elimination", "Any method"]
    )
    if st.button("Check Answer 2"):
        if q2 == "Substitution":
            st.success("Correct! Substitution is most efficient when a variable is already isolated.")
        else:
            st.error("Incorrect. Substitution is best when a variable is already isolated.")
    
    # Question 3
    st.subheader("Question 3: Solve this system")
    st.write("Solve: y = x + 1 and y = 2x - 1")
    q3 = st.text_input("Enter your answer as (x, y):")
    if st.button("Check Answer 3"):
        if "2" in q3 and "3" in q3:
            st.success("Correct! The solution is (2, 3)")
        else:
            st.error("Incorrect. Try substituting the first equation into the second.")
            with st.expander("Show solution"):
                st.write("x + 1 = 2x - 1")
                st.write("1 = x - 1")
                st.write("x = 2")
                st.write("y = 2 + 1 = 3")
                st.write("Solution: (2, 3)")

# ==================== COMMON MISTAKES ====================
else:  # Review Common Mistakes
    st.header("Common Mistakes to Avoid")
    
    st.subheader("1. Sign Errors in Elimination")
    st.write("Be careful when adding or subtracting equations!")
    st.code("""
    WRONG:
    2x + 3y = 7
    2x - y = 3
    Subtract: 3y - (-y) = 4y ✗  (Common mistake!)
    
    RIGHT:
    2x + 3y = 7
    2x - y = 3
    Subtract: (3y) - (-y) = 3y + y = 4y ✓
    """)
    
    st.subheader("2. Forgetting to Substitute Back")
    st.write("After finding one variable, always substitute back to find the other!")
    
    st.subheader("3. Not Checking Your Answer")
    st.write("Always verify your solution in BOTH original equations.")
    
    st.subheader("4. Arithmetic Errors")
    st.write("Take your time with calculations. Show all your work.")
    
    st.subheader("5. Graphing Mistakes")
    st.write("Make sure to:")
    st.write("- Plot at least 2 points per line")
    st.write("- Use a ruler for straight lines")
    st.write("- Label your axes")
    st.write("- Check that your graphical solution satisfies both equations")

# --- Study Tips Sidebar ---
st.sidebar.header("Exam Prep Tips")
st.sidebar.markdown("""
**Before the Exam:**
- Practice all three methods
- Work through at least 10 problems
- Review common mistakes
- Get a good night's sleep

**During the Exam:**
- Read each problem carefully
- Choose the most efficient method
- Show all your work
- Check your answers
- Manage your time wisely

**Key Formulas:**
- Standard form: Ax + By = C
- Slope-intercept: y = mx + b
- Point-slope: y - y₁ = m(x - x₁)
""")

# --- Progress Tracker ---
st.sidebar.header("Your Progress")
methods_learned = st.sidebar.multiselect(
    "Methods I've mastered:",
    ["Graphing", "Substitution", "Elimination"]
)
if len(methods_learned) == 3:
    st.sidebar.success("Great! You've learned all three methods!")
elif len(methods_learned) > 0:
    st.sidebar.info(f"Keep going! {3 - len(methods_learned)} method(s) to go.")

problems_completed = st.sidebar.number_input(
    "Problems completed today:",
    min_value=0,
    max_value=50,
    value=0
)
if problems_completed >= 10:
    st.sidebar.success("Excellent practice! You're ready for the exam!")
elif problems_completed >= 5:
    st.sidebar.info("Good work! Try to complete at least 10 problems.")

# --- Footer ---
st.markdown("---")
st.markdown("**Good luck on your exam, Meka! You've got this!**")
