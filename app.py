import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# --- Page Setup ---
st.set_page_config(page_title="Systems of Equations Complete Tutorial", page_icon="📐", layout="wide")

# --- Developer Credit ---
st.markdown("### [www.cognitivecloud.ai](https://www.cognitivecloud.ai)")
st.markdown("**Developed by Xavier Honablue M.Ed**")

st.markdown("---")

# --- Title ---
st.title("📐 Systems of Linear Equations: Complete Tutorial")
st.subheader("Comprehensive Exam Preparation for Meka Wilson")

# --- Progress Tracking ---
if 'completed_sections' not in st.session_state:
    st.session_state.completed_sections = set()

if 'practice_scores' not in st.session_state:
    st.session_state.practice_scores = {}

# --- Sidebar Navigation ---
st.sidebar.header("📚 Tutorial Navigation")
st.sidebar.markdown("**Student:** Meka Wilson")

tutorial_section = st.sidebar.radio("Choose a section:", [
    "📖 Introduction to Systems",
    "📊 Method 1: Graphing",
    "🔄 Method 2: Substitution",
    "➕ Method 3: Elimination",
    "⚠️ Special Cases",
    "📝 Word Problems",
    "🎯 Choosing the Best Method",
    "💪 Practice Problems",
    "📋 Practice Test",
    "📚 Study Resources",
    "🎓 Exam Day Tips"
])

# Progress indicator
total_sections = 11
completed = len(st.session_state.completed_sections)
st.sidebar.progress(completed / total_sections)
st.sidebar.write(f"Progress: {completed}/{total_sections} sections completed")

# Mark section as complete button
if st.sidebar.button(f"✓ Mark '{tutorial_section}' as Complete"):
    st.session_state.completed_sections.add(tutorial_section)
    st.sidebar.success("Section marked complete!")

# ==================== INTRODUCTION TO SYSTEMS ====================
if tutorial_section == "📖 Introduction to Systems":
    st.header("What is a System of Linear Equations?")
    
    st.markdown("""
    ### Definition
    A **system of linear equations** is a collection of two or more linear equations involving the same set of variables.
    
    **Example:**
    ```
    2x + y = 5
    x - y = 1
    ```
    
    Both equations involve the same variables (x and y).
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### What is a Solution?
        A **solution** to a system is an ordered pair (x, y) that makes **ALL** equations true simultaneously.
        
        For the system above:
        - Solution: **(2, 1)**
        - Check equation 1: 2(2) + 1 = 4 + 1 = 5 ✓
        - Check equation 2: 2 - 1 = 1 ✓
        """)
    
    with col2:
        st.markdown("""
        ### Types of Solutions
        A system can have:
        1. **One solution** - Lines intersect at one point (most common)
        2. **No solution** - Lines are parallel (never intersect)
        3. **Infinite solutions** - Lines are the same (overlap completely)
        
        We'll explore these in detail later!
        """)
    
    st.info("💡 **Key Point:** The solution is where ALL equations are true at the same time!")
    
    # Visual representation
    st.subheader("Visual Understanding")
    x = np.linspace(-1, 4, 100)
    y1 = 5 - 2*x  # From 2x + y = 5
    y2 = x - 1     # From x - y = 1
    
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(x, y1, 'b-', linewidth=2, label='2x + y = 5')
    ax.plot(x, y2, 'r-', linewidth=2, label='x - y = 1')
    ax.plot(2, 1, 'go', markersize=12, label='Solution (2, 1)', zorder=5)
    ax.axhline(y=0, color='k', linewidth=0.5)
    ax.axvline(x=0, color='k', linewidth=0.5)
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=10)
    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('y', fontsize=12)
    ax.set_title('System of Linear Equations - One Solution', fontsize=14, fontweight='bold')
    st.pyplot(fig)

# ==================== GRAPHING METHOD ====================
elif tutorial_section == "📊 Method 1: Graphing":
    st.header("Solving Systems by Graphing")
    
    st.markdown("""
    ### When to Use Graphing
    - When you need a **visual representation**
    - When equations are already in **slope-intercept form** (y = mx + b)
    - When you want to **understand** the relationship between equations
    - For **simple integer solutions**
    
    ### Limitations
    - Can be **imprecise** for non-integer solutions
    - Difficult if the solution is not near the origin
    - Requires careful graphing
    """)
    
    st.subheader("Step-by-Step Process")
    
    st.markdown("""
    **Steps:**
    1. Write each equation in slope-intercept form: **y = mx + b**
    2. Graph the first equation (plot y-intercept, use slope to find another point)
    3. Graph the second equation on the same axes
    4. Find the **intersection point** - this is your solution
    5. **Check** your solution in both original equations
    """)
    
    st.markdown("---")
    
    st.subheader("📚 Example 1: Basic Graphing")
    
    st.markdown("""
    **Solve by graphing:**
    ```
    y = 2x - 1
    y = -x + 5
    ```
    
    **Step 1:** Both equations are already in slope-intercept form ✓
    
    **Step 2:** Graph y = 2x - 1
    - y-intercept: (0, -1)
    - slope: 2 (rise 2, run 1)
    - Another point: (1, 1)
    
    **Step 3:** Graph y = -x + 5
    - y-intercept: (0, 5)
    - slope: -1 (rise -1, run 1)
    - Another point: (1, 4)
    
    **Step 4:** Find intersection point
    """)
    
    x = np.linspace(-1, 4, 100)
    y1 = 2*x - 1
    y2 = -x + 5
    
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.plot(x, y1, 'b-', linewidth=3, label='y = 2x - 1')
    ax.plot(x, y2, 'r-', linewidth=3, label='y = -x + 5')
    ax.plot(2, 3, 'go', markersize=15, label='Solution (2, 3)', zorder=5)
    ax.axhline(y=0, color='k', linewidth=0.5)
    ax.axvline(x=0, color='k', linewidth=0.5)
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=12)
    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('y', fontsize=12)
    ax.set_title('Graphing Method Example', fontsize=14, fontweight='bold')
    ax.set_xlim(-1, 4)
    ax.set_ylim(-2, 6)
    st.pyplot(fig)
    
    st.success("""
    **Solution: (2, 3)**
    
    **Step 5: Check:**
    - Equation 1: y = 2(2) - 1 = 4 - 1 = 3 ✓
    - Equation 2: y = -(2) + 5 = 3 ✓
    """)
    
    st.markdown("---")
    
    st.subheader("📚 Example 2: Standard Form to Slope-Intercept")
    
    st.markdown("""
    **Solve by graphing:**
    ```
    2x + y = 6
    x - y = 3
    ```
    
    **Step 1:** Convert to slope-intercept form
    
    **Equation 1:** 2x + y = 6
    ```
    y = -2x + 6
    ```
    
    **Equation 2:** x - y = 3
    ```
    -y = -x + 3
    y = x - 3
    ```
    """)
    
    x = np.linspace(-1, 5, 100)
    y1 = -2*x + 6
    y2 = x - 3
    
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.plot(x, y1, 'b-', linewidth=3, label='y = -2x + 6 (from 2x + y = 6)')
    ax.plot(x, y2, 'r-', linewidth=3, label='y = x - 3 (from x - y = 3)')
    ax.plot(3, 0, 'go', markersize=15, label='Solution (3, 0)', zorder=5)
    ax.axhline(y=0, color='k', linewidth=0.5)
    ax.axvline(x=0, color='k', linewidth=0.5)
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=12)
    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('y', fontsize=12)
    ax.set_title('Converting to Slope-Intercept Form', fontsize=14, fontweight='bold')
    st.pyplot(fig)
    
    st.success("""
    **Solution: (3, 0)**
    
    **Check:**
    - Equation 1: 2(3) + 0 = 6 ✓
    - Equation 2: 3 - 0 = 3 ✓
    """)
    
    st.info("💡 **Pro Tip:** Always convert to y = mx + b form first. It makes graphing much easier!")

# ==================== SUBSTITUTION METHOD ====================
elif tutorial_section == "🔄 Method 2: Substitution":
    st.header("Solving Systems by Substitution")
    
    st.markdown("""
    ### When to Use Substitution
    - When one equation is **already solved for a variable** (y = ... or x = ...)
    - When one variable has a **coefficient of 1 or -1** (easy to isolate)
    - When you want an **exact algebraic solution**
    
    ### Advantages
    - Gives **exact answers** (no graphing estimation)
    - Works for **any system**, including those with fractions
    - More **precise** than graphing
    """)
    
    st.subheader("Step-by-Step Process")
    
    st.markdown("""
    **Steps:**
    1. Solve one equation for one variable (choose the easiest to isolate)
    2. **Substitute** that expression into the other equation
    3. Solve the resulting equation for one variable
    4. **Substitute back** to find the other variable
    5. **Check** your solution in both original equations
    """)
    
    st.markdown("---")
    
    st.subheader("📚 Example 1: Variable Already Isolated")
    
    st.markdown("""
    **Solve using substitution:**
    ```
    y = 3x + 2
    2x + y = 12
    ```
    
    **Step 1:** First equation is already solved for y ✓
    
    **Step 2:** Substitute y = 3x + 2 into the second equation
    ```
    2x + (3x + 2) = 12
    ```
    
    **Step 3:** Solve for x
    ```
    2x + 3x + 2 = 12
    5x + 2 = 12
    5x = 10
    x = 2
    ```
    
    **Step 4:** Substitute x = 2 back into first equation
    ```
    y = 3(2) + 2
    y = 6 + 2
    y = 8
    ```
    
    **Step 5:** Check the solution (2, 8)
    - Equation 1: y = 3(2) + 2 = 8 ✓
    - Equation 2: 2(2) + 8 = 4 + 8 = 12 ✓
    """)
    
    st.success("**Solution: (2, 8)**")
    
    st.markdown("---")
    
    st.subheader("📚 Example 2: Isolate a Variable First")
    
    st.markdown("""
    **Solve using substitution:**
    ```
    x + 2y = 10
    3x - y = 5
    ```
    
    **Step 1:** Solve the second equation for y (coefficient is -1, easiest to isolate)
    ```
    3x - y = 5
    -y = -3x + 5
    y = 3x - 5
    ```
    
    **Step 2:** Substitute y = 3x - 5 into the first equation
    ```
    x + 2(3x - 5) = 10
    ```
    
    **Step 3:** Solve for x
    ```
    x + 6x - 10 = 10
    7x - 10 = 10
    7x = 20
    x = 20/7 ≈ 2.86
    ```
    
    **Step 4:** Substitute x = 20/7 back
    ```
    y = 3(20/7) - 5
    y = 60/7 - 35/7
    y = 25/7 ≈ 3.57
    ```
    
    **Step 5:** Check (you should always check!)
    - Equation 1: 20/7 + 2(25/7) = 20/7 + 50/7 = 70/7 = 10 ✓
    - Equation 2: 3(20/7) - 25/7 = 60/7 - 25/7 = 35/7 = 5 ✓
    """)
    
    st.success("**Solution: (20/7, 25/7) or approximately (2.86, 3.57)**")
    
    st.markdown("---")
    
    st.subheader("📚 Example 3: More Complex Substitution")
    
    st.markdown("""
    **Solve using substitution:**
    ```
    2x + 3y = 16
    x = y + 2
    ```
    
    **Step 1:** Second equation already solved for x ✓
    
    **Step 2:** Substitute x = y + 2 into first equation
    ```
    2(y + 2) + 3y = 16
    ```
    
    **Step 3:** Solve for y
    ```
    2y + 4 + 3y = 16
    5y + 4 = 16
    5y = 12
    y = 12/5 = 2.4
    ```
    
    **Step 4:** Find x
    ```
    x = y + 2
    x = 2.4 + 2
    x = 4.4
    ```
    
    **Step 5:** Check (4.4, 2.4)
    - Equation 1: 2(4.4) + 3(2.4) = 8.8 + 7.2 = 16 ✓
    - Equation 2: 4.4 = 2.4 + 2 ✓
    """)
    
    st.success("**Solution: (4.4, 2.4) or (22/5, 12/5)**")
    
    st.info("💡 **Key Strategy:** Look for equations where a variable is already isolated or has a coefficient of 1 or -1!")

# ==================== ELIMINATION METHOD ====================
elif tutorial_section == "➕ Method 3: Elimination":
    st.header("Solving Systems by Elimination (Addition)")
    
    st.markdown("""
    ### When to Use Elimination
    - When both equations are in **standard form** (Ax + By = C)
    - When coefficients can be easily made **opposites**
    - When neither variable is easily isolated
    - Often the **fastest method** for many systems
    
    ### The Big Idea
    Add or subtract equations to **eliminate** one variable, making it possible to solve for the other.
    """)
    
    st.subheader("Step-by-Step Process")
    
    st.markdown("""
    **Steps:**
    1. Write both equations in **standard form** (Ax + By = C)
    2. **Multiply** one or both equations to make coefficients of one variable opposites
    3. **Add** the equations to eliminate that variable
    4. Solve for the remaining variable
    5. **Substitute back** into either original equation to find the other variable
    6. **Check** your solution
    """)
    
    st.markdown("---")
    
    st.subheader("📚 Example 1: Ready to Eliminate")
    
    st.markdown("""
    **Solve using elimination:**
    ```
    3x + 2y = 16
    5x - 2y = 8
    ```
    
    **Step 1:** Both equations in standard form ✓
    
    **Step 2:** Notice that +2y and -2y are already opposites! No multiplication needed.
    
    **Step 3:** Add the equations
    ```
     3x + 2y = 16
    +5x - 2y =  8
    _______________
     8x + 0  = 24
    ```
    
    **Step 4:** Solve for x
    ```
    8x = 24
    x = 3
    ```
    
    **Step 5:** Substitute x = 3 into either original equation (use the first)
    ```
    3(3) + 2y = 16
    9 + 2y = 16
    2y = 7
    y = 3.5
    ```
    
    **Step 6:** Check (3, 3.5)
    - Equation 1: 3(3) + 2(3.5) = 9 + 7 = 16 ✓
    - Equation 2: 5(3) - 2(3.5) = 15 - 7 = 8 ✓
    """)
    
    st.success("**Solution: (3, 3.5) or (3, 7/2)**")
    
    st.markdown("---")
    
    st.subheader("📚 Example 2: Multiply to Create Opposites")
    
    st.markdown("""
    **Solve using elimination:**
    ```
    2x + 3y = 7
    3x + 2y = 8
    ```
    
    **Step 1:** Both in standard form ✓
    
    **Step 2:** Make coefficients of x opposites
    - Multiply first equation by 3: **6x + 9y = 21**
    - Multiply second equation by -2: **-6x - 4y = -16**
    
    **Step 3:** Add the equations
    ```
     6x + 9y = 21
    -6x - 4y = -16
    _______________
     0  + 5y = 5
    ```
    
    **Step 4:** Solve for y
    ```
    5y = 5
    y = 1
    ```
    
    **Step 5:** Substitute y = 1 into first original equation
    ```
    2x + 3(1) = 7
    2x + 3 = 7
    2x = 4
    x = 2
    ```
    
    **Step 6:** Check (2, 1)
    - Equation 1: 2(2) + 3(1) = 4 + 3 = 7 ✓
    - Equation 2: 3(2) + 2(1) = 6 + 2 = 8 ✓
    """)
    
    st.success("**Solution: (2, 1)**")
    
    st.markdown("---")
    
    st.subheader("📚 Example 3: Eliminate y Instead")
    
    st.markdown("""
    **Solve using elimination:**
    ```
    4x + 3y = 10
    2x - y = 0
    ```
    
    **Strategy:** Eliminate y (coefficient -1 is easy to work with)
    
    **Step 2:** Multiply second equation by 3
    ```
    4x + 3y = 10  (keep as is)
    6x - 3y = 0   (multiplied by 3)
    ```
    
    **Step 3:** Add the equations
    ```
     4x + 3y = 10
     6x - 3y =  0
    _____________
    10x + 0  = 10
    ```
    
    **Step 4:** Solve for x
    ```
    10x = 10
    x = 1
    ```
    
    **Step 5:** Substitute x = 1 into second original equation
    ```
    2(1) - y = 0
    2 - y = 0
    y = 2
    ```
    
    **Step 6:** Check (1, 2)
    - Equation 1: 4(1) + 3(2) = 4 + 6 = 10 ✓
    - Equation 2: 2(1) - 2 = 0 ✓
    """)
    
    st.success("**Solution: (1, 2)**")
    
    st.info("💡 **Pro Tip:** Look for the variable with the smallest coefficients to eliminate - it means less multiplication!")

# ==================== SPECIAL CASES ====================
elif tutorial_section == "⚠️ Special Cases":
    st.header("Special Cases: No Solution and Infinite Solutions")
    
    st.markdown("""
    Not all systems have exactly one solution! Sometimes you'll encounter special cases.
    """)
    
    st.subheader("Case 1: No Solution (Inconsistent System)")
    
    st.markdown("""
    ### What Does It Mean?
    The two lines are **parallel** - they never intersect!
    
    ### How to Recognize It:
    - **Graphically:** Lines are parallel (same slope, different y-intercepts)
    - **Algebraically:** You get a **false statement** like 0 = 5 or 3 = 7
    """)
    
    st.markdown("---")
    
    st.markdown("""
    ### Example: No Solution
    
    **Solve:**
    ```
    y = 2x + 3
    y = 2x - 1
    ```
    
    **Using Substitution:**
    ```
    2x + 3 = 2x - 1
    3 = -1  ← FALSE!
    ```
    
    When you get a false statement, there is **NO SOLUTION**.
    """)
    
    # Graph parallel lines
    x = np.linspace(-2, 4, 100)
    y1 = 2*x + 3
    y2 = 2*x - 1
    
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.plot(x, y1, 'b-', linewidth=3, label='y = 2x + 3')
    ax.plot(x, y2, 'r-', linewidth=3, label='y = 2x - 1')
    ax.axhline(y=0, color='k', linewidth=0.5)
    ax.axvline(x=0, color='k', linewidth=0.5)
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=12)
    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('y', fontsize=12)
    ax.set_title('No Solution - Parallel Lines', fontsize=14, fontweight='bold')
    ax.text(1, 8, 'Lines never intersect!', fontsize=12, bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))
    st.pyplot(fig)
    
    st.warning("**Answer:** No solution (parallel lines)")
    
    st.markdown("---")
    
    st.markdown("""
    ### Another Example: Using Elimination
    
    **Solve:**
    ```
    2x + 3y = 6
    4x + 6y = 18
    ```
    
    **Multiply first equation by -2:**
    ```
    -4x - 6y = -12
     4x + 6y =  18
    ________________
     0  + 0  =  6  ← FALSE! (0 ≠ 6)
    ```
    
    When both variables eliminate and you get a false statement: **NO SOLUTION**
    """)
    
    st.warning("**Answer:** No solution")
    
    st.markdown("---")
    st.markdown("---")
    
    st.subheader("Case 2: Infinite Solutions (Dependent System)")
    
    st.markdown("""
    ### What Does It Mean?
    The two equations represent the **same line** - they overlap completely!
    
    ### How to Recognize It:
    - **Graphically:** Lines are identical (they overlap perfectly)
    - **Algebraically:** You get a **true statement** like 0 = 0 or 5 = 5
    """)
    
    st.markdown("---")
    
    st.markdown("""
    ### Example: Infinite Solutions
    
    **Solve:**
    ```
    y = 3x + 2
    6x - 2y = -4
    ```
    
    **Convert second equation to slope-intercept form:**
    ```
    6x - 2y = -4
    -2y = -6x - 4
    y = 3x + 2  ← Same as first equation!
    ```
    
    **Using Substitution:**
    ```
    6x - 2(3x + 2) = -4
    6x - 6x - 4 = -4
    -4 = -4  ← TRUE!
    ```
    
    When you get a true statement, there are **INFINITE SOLUTIONS**.
    """)
    
    # Graph same line
    x = np.linspace(-2, 3, 100)
    y1 = 3*x + 2
    
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.plot(x, y1, 'purple', linewidth=5, label='Both equations: y = 3x + 2')
    ax.axhline(y=0, color='k', linewidth=0.5)
    ax.axvline(x=0, color='k', linewidth=0.5)
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=12)
    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('y', fontsize=12)
    ax.set_title('Infinite Solutions - Same Line', fontsize=14, fontweight='bold')
    ax.text(0, 10, 'Lines overlap completely!', fontsize=12, bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))
    st.pyplot(fig)
    
    st.success("**Answer:** Infinite solutions (same line)")
    
    st.markdown("---")
    
    st.markdown("""
    ### Another Example: Using Elimination
    
    **Solve:**
    ```
    3x + 2y = 12
    6x + 4y = 24
    ```
    
    **Multiply first equation by -2:**
    ```
    -6x - 4y = -24
     6x + 4y =  24
    ________________
     0  + 0  =  0  ← TRUE! (0 = 0)
    ```
    
    When both variables eliminate and you get a true statement: **INFINITE SOLUTIONS**
    """)
    
    st.success("**Answer:** Infinite solutions (same line)")
    
    st.markdown("---")
    
    st.subheader("📊 Summary of Solution Types")
    
    summary_df = pd.DataFrame({
        'Type': ['One Solution', 'No Solution', 'Infinite Solutions'],
        'Lines': ['Intersect at one point', 'Parallel (never intersect)', 'Same line (overlap)'],
        'Slopes': ['Different slopes', 'Same slope, different y-intercept', 'Same slope, same y-intercept'],
        'Algebraic Result': ['One (x, y) pair', 'False statement (0 = 5)', 'True statement (0 = 0)'],
        'Example': ['x + y = 5, x - y = 1', 'y = 2x + 1, y = 2x + 5', 'y = x + 2, 2y = 2x + 4']
    })
    
    st.dataframe(summary_df, use_container_width=True, hide_index=True)
    
    st.info("💡 **Exam Tip:** Always check what happens at the end! False statement = no solution. True statement = infinite solutions.")

# ==================== WORD PROBLEMS ====================
elif tutorial_section == "📝 Word Problems":
    st.header("Solving Word Problems with Systems")
    
    st.markdown("""
    Word problems are where systems of equations become really useful! The key is translating words into equations.
    """)
    
    st.subheader("Step-by-Step Strategy")
    
    st.markdown("""
    **Steps for Word Problems:**
    1. **Read carefully** - understand what's being asked
    2. **Define variables** - decide what x and y represent
    3. **Write two equations** - translate words to math
    4. **Solve the system** - use any method
    5. **Answer the question** - state your answer in context
    6. **Check** - does your answer make sense?
    """)
    
    st.markdown("---")
    
    st.subheader("📚 Example 1: Number Problems")
    
    st.markdown("""
    **Problem:**
    The sum of two numbers is 25. Their difference is 7. Find the two numbers.
    
    **Step 1: Define variables**
    - Let x = first number
    - Let y = second number
    
    **Step 2: Write equations**
    - "The sum of two numbers is 25" → **x + y = 25**
    - "Their difference is 7" → **x - y = 7**
    
    **Step 3: Solve using elimination (add the equations)**
    ```
    x + y = 25
    x - y = 7
    _________
    2x = 32
    x = 16
    ```
    
    **Step 4: Find y**
    ```
    16 + y = 25
    y = 9
    ```
    
    **Step 5: Answer in context**
    The two numbers are **16 and 9**.
    
    **Step 6: Check**
    - Sum: 16 + 9 = 25 ✓
    - Difference: 16 - 9 = 7 ✓
    """)
    
    st.success("**Answer: The numbers are 16 and 9**")
    
    st.markdown("---")
    
    st.subheader("📚 Example 2: Age Problems")
    
    st.markdown("""
    **Problem:**
    Maria is 3 years older than her brother Juan. The sum of their ages is 27. How old are they?
    
    **Step 1: Define variables**
    - Let m = Maria's age
    - Let j = Juan's age
    
    **Step 2: Write equations**
    - "Maria is 3 years older than Juan" → **m = j + 3**
    - "Sum of their ages is 27" → **m + j = 27**
    
    **Step 3: Solve using substitution**
    ```
    Substitute m = j + 3 into second equation:
    (j + 3) + j = 27
    2j + 3 = 27
    2j = 24
    j = 12
    ```
    
    **Step 4: Find m**
    ```
    m = j + 3
    m = 12 + 3
    m = 15
    ```
    
    **Step 5: Answer in context**
    Maria is **15 years old** and Juan is **12 years old**.
    
    **Step 6: Check**
    - Maria is 3 years older: 15 = 12 + 3 ✓
    - Sum is 27: 15 + 12 = 27 ✓
    """)
    
    st.success("**Answer: Maria is 15, Juan is 12**")
    
    st.markdown("---")
    
    st.subheader("📚 Example 3: Money/Coin Problems")
    
    st.markdown("""
    **Problem:**
    A store sells adult tickets for $8 and child tickets for $5. One day they sold 45 tickets and made $315. How many of each ticket did they sell?
    
    **Step 1: Define variables**
    - Let a = number of adult tickets
    - Let c = number of child tickets
    
    **Step 2: Write equations**
    - "Sold 45 tickets total" → **a + c = 45**
    - "Made $315" → **8a + 5c = 315**
    
    **Step 3: Solve using substitution**
    ```
    From first equation: c = 45 - a
    
    Substitute into second equation:
    8a + 5(45 - a) = 315
    8a + 225 - 5a = 315
    3a + 225 = 315
    3a = 90
    a = 30
    ```
    
    **Step 4: Find c**
    ```
    c = 45 - a
    c = 45 - 30
    c = 15
    ```
    
    **Step 5: Answer in context**
    They sold **30 adult tickets** and **15 child tickets**.
    
    **Step 6: Check**
    - Total tickets: 30 + 15 = 45 ✓
    - Total money: 8(30) + 5(15) = 240 + 75 = 315 ✓
    """)
    
    st.success("**Answer: 30 adult tickets, 15 child tickets**")
    
    st.markdown("---")
    
    st.subheader("📚 Example 4: Mixture Problems")
    
    st.markdown("""
    **Problem:**
    A chemist needs to mix a 20% acid solution with a 50% acid solution to create 30 liters of a 35% acid solution. How many liters of each should be used?
    
    **Step 1: Define variables**
    - Let x = liters of 20% solution
    - Let y = liters of 50% solution
    
    **Step 2: Write equations**
    - "Total volume is 30 liters" → **x + y = 30**
    - "Final mixture is 35% acid" → **0.20x + 0.50y = 0.35(30)**
    
    Simplify second equation:
    ```
    0.20x + 0.50y = 10.5
    or multiply by 100:
    20x + 50y = 1050
    ```
    
    **Step 3: Solve using elimination**
    ```
    Multiply first equation by -20:
    -20x - 20y = -600
     20x + 50y = 1050
    _________________
          30y = 450
            y = 15
    ```
    
    **Step 4: Find x**
    ```
    x + 15 = 30
    x = 15
    ```
    
    **Step 5: Answer in context**
    Use **15 liters of 20% solution** and **15 liters of 50% solution**.
    
    **Step 6: Check**
    - Total: 15 + 15 = 30 liters ✓
    - Acid amount: 0.20(15) + 0.50(15) = 3 + 7.5 = 10.5 = 0.35(30) ✓
    """)
    
    st.success("**Answer: 15 liters of each solution**")
    
    st.info("💡 **Word Problem Tips:** Always define your variables clearly and write down what each equation represents!")

# ==================== CHOOSING THE BEST METHOD ====================
elif tutorial_section == "🎯 Choosing the Best Method":
    st.header("Choosing the Most Efficient Method")
    
    st.markdown("""
    You know three methods now. But which one should you use? Here's how to decide!
    """)
    
    st.subheader("Decision Guide")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### Use GRAPHING when:
        - Need visual representation
        - Equations in y = mx + b form
        - Solution looks like integers
        - Asked to graph
        - Want to see relationship
        
        **Example:**
        ```
        y = 2x + 1
        y = -x + 4
        ```
        ✓ Ready to graph!
        """)
    
    with col2:
        st.markdown("""
        ### Use SUBSTITUTION when:
        - Variable already isolated
        - Coefficient is 1 or -1
        - One equation solved for y
        
        **Example:**
        ```
        y = 3x + 5
        2x + y = 9
        ```
        ✓ y already isolated!
        """)
    
    with col3:
        st.markdown("""
        ### Use ELIMINATION when:
        - Both in standard form
        - Coefficients are opposites
        - No variable isolated
        - Easiest to make opposites
        
        **Example:**
        ```
        3x + 2y = 8
        3x - 2y = 4
        ```
        ✓ 2y and -2y opposites!
        """)
    
    st.markdown("---")
    
    st.subheader("Practice: Choose the Method")
    
    st.markdown("""
    For each system, which method would YOU choose and why?
    """)
    
    system1 = st.radio(
        "**System 1:** `y = 4x - 3` and `2x + y = 9`",
        ["Graphing", "Substitution", "Elimination"],
        key="method1"
    )
    if st.button("Check Choice 1"):
        if system1 == "Substitution":
            st.success("✓ Best choice! y is already isolated in first equation - perfect for substitution!")
        else:
            st.info("Substitution would be most efficient here since y is already isolated.")
    
    system2 = st.radio(
        "**System 2:** `3x + 4y = 12` and `3x - 2y = 6`",
        ["Graphing", "Substitution", "Elimination"],
        key="method2"
    )
    if st.button("Check Choice 2"):
        if system2 == "Elimination":
            st.success("✓ Best choice! The x-coefficients are already the same - just subtract!")
        else:
            st.info("Elimination would be most efficient here since coefficients of x are the same.")
    
    system3 = st.radio(
        "**System 3:** `y = 2x + 1` and `y = -x + 7`",
        ["Graphing", "Substitution", "Elimination"],
        key="method3"
    )
    if st.button("Check Choice 3"):
        if system3 in ["Graphing", "Substitution"]:
            st.success("✓ Good choice! Both methods work well here. Graphing shows the visual, substitution gives exact answer.")
        else:
            st.info("Graphing or substitution would be easier here since both are in y = form.")
    
    st.markdown("---")
    
    st.subheader("Quick Reference Table")
    
    method_df = pd.DataFrame({
        'Method': ['Graphing', 'Substitution', 'Elimination'],
        'Best For': [
            'Visual problems, y = mx + b form',
            'Variable isolated, coefficient of 1',
            'Standard form, opposite coefficients'
        ],
        'Advantage': [
            'See the relationship visually',
            'Direct substitution, fewer steps',
            'Eliminates variable quickly'
        ],
        'Limitation': [
            'Can be imprecise',
            'Can get messy with fractions',
            'Need to manipulate equations'
        ]
    })
    
    st.dataframe(method_df, use_container_width=True, hide_index=True)

# ==================== PRACTICE PROBLEMS ====================
elif tutorial_section == "💪 Practice Problems":
    st.header("Practice Problems by Difficulty")
    
    difficulty_level = st.selectbox("Choose difficulty:", [
        "Level 1: Basic",
        "Level 2: Intermediate",
        "Level 3: Advanced",
        "Level 4: Challenge"
    ])
    
    if difficulty_level == "Level 1: Basic":
        st.subheader("Level 1: Basic Problems")
        
        with st.expander("Problem 1: Simple Graphing"):
            st.markdown("""
            **Solve by graphing:**
            ```
            y = x + 1
            y = -x + 5
            ```
            """)
            if st.checkbox("Show solution", key="p1"):
                x = np.linspace(-2, 7, 100)
                y1 = x + 1
                y2 = -x + 5
                fig, ax = plt.subplots(figsize=(8, 6))
                ax.plot(x, y1, 'b-', linewidth=2, label='y = x + 1')
                ax.plot(x, y2, 'r-', linewidth=2, label='y = -x + 5')
                ax.plot(2, 3, 'go', markersize=12)
                ax.grid(True, alpha=0.3)
                ax.axhline(y=0, color='k', linewidth=0.5)
                ax.axvline(x=0, color='k', linewidth=0.5)
                ax.legend()
                st.pyplot(fig)
                st.success("**Answer: (2, 3)**")
        
        with st.expander("Problem 2: Simple Substitution"):
            st.markdown("""
            **Solve using substitution:**
            ```
            y = 2x
            x + y = 6
            ```
            """)
            if st.checkbox("Show solution", key="p2"):
                st.markdown("""
                **Solution:**
                ```
                Substitute y = 2x into second equation:
                x + 2x = 6
                3x = 6
                x = 2
                
                y = 2(2) = 4
                ```
                """)
                st.success("**Answer: (2, 4)**")
        
        with st.expander("Problem 3: Simple Elimination"):
            st.markdown("""
            **Solve using elimination:**
            ```
            x + y = 8
            x - y = 2
            ```
            """)
            if st.checkbox("Show solution", key="p3"):
                st.markdown("""
                **Solution:**
                ```
                Add equations:
                x + y = 8
                x - y = 2
                _________
                2x = 10
                x = 5
                
                5 + y = 8
                y = 3
                ```
                """)
                st.success("**Answer: (5, 3)**")
    
    elif difficulty_level == "Level 2: Intermediate":
        st.subheader("Level 2: Intermediate Problems")
        
        with st.expander("Problem 4: Requires Conversion"):
            st.markdown("""
            **Solve using any method:**
            ```
            2x + y = 7
            x - y = 2
            ```
            """)
            if st.checkbox("Show solution", key="p4"):
                st.markdown("""
                **Solution (Elimination):**
                ```
                Add equations (y and -y are opposites):
                2x + y = 7
                 x - y = 2
                __________
                3x = 9
                x = 3
                
                3 - y = 2
                y = 1
                ```
                """)
                st.success("**Answer: (3, 1)**")
        
        with st.expander("Problem 5: Multiplication Needed"):
            st.markdown("""
            **Solve:**
            ```
            2x + 3y = 12
            x + y = 5
            ```
            """)
            if st.checkbox("Show solution", key="p5"):
                st.markdown("""
                **Solution (Elimination):**
                ```
                Multiply second equation by -2:
                2x + 3y = 12
                -2x - 2y = -10
                _______________
                y = 2
                
                x + 2 = 5
                x = 3
                ```
                """)
                st.success("**Answer: (3, 2)**")
        
        with st.expander("Problem 6: Word Problem"):
            st.markdown("""
            **Problem:**
            Two numbers sum to 50. One number is 6 more than the other. Find both numbers.
            """)
            if st.checkbox("Show solution", key="p6"):
                st.markdown("""
                **Solution:**
                ```
                Let x = first number, y = second number
                
                x + y = 50
                x = y + 6
                
                Substitute:
                (y + 6) + y = 50
                2y + 6 = 50
                2y = 44
                y = 22
                
                x = 22 + 6 = 28
                ```
                """)
                st.success("**Answer: The numbers are 28 and 22**")
    
    elif difficulty_level == "Level 3: Advanced":
        st.subheader("Level 3: Advanced Problems")
        
        with st.expander("Problem 7: Fractions"):
            st.markdown("""
            **Solve:**
            ```
            (1/2)x + y = 5
            x - (1/3)y = 2
            ```
            """)
            if st.checkbox("Show solution", key="p7"):
                st.markdown("""
                **Solution:**
                ```
                Clear fractions by multiplying:
                Equation 1 × 2: x + 2y = 10
                Equation 2 × 3: 3x - y = 6
                
                Multiply second by 2:
                x + 2y = 10
                6x - 2y = 12
                ___________
                7x = 22
                x = 22/7
                
                22/7 + 2y = 10
                2y = 70/7 - 22/7 = 48/7
                y = 24/7
                ```
                """)
                st.success("**Answer: (22/7, 24/7) or approximately (3.14, 3.43)**")
        
        with st.expander("Problem 8: Special Case - No Solution"):
            st.markdown("""
            **Solve:**
            ```
            2x + y = 5
            4x + 2y = 15
            ```
            """)
            if st.checkbox("Show solution", key="p8"):
                st.markdown("""
                **Solution:**
                ```
                Multiply first equation by -2:
                -4x - 2y = -10
                 4x + 2y =  15
                ______________
                 0 = 5  ← FALSE!
                ```
                """)
                st.warning("**Answer: No solution (parallel lines)**")
        
        with st.expander("Problem 9: Special Case - Infinite Solutions"):
            st.markdown("""
            **Solve:**
            ```
            3x - y = 6
            -6x + 2y = -12
            ```
            """)
            if st.checkbox("Show solution", key="p9"):
                st.markdown("""
                **Solution:**
                ```
                Multiply first equation by 2:
                6x - 2y = 12
                -6x + 2y = -12
                _____________
                0 = 0  ← TRUE!
                ```
                """)
                st.success("**Answer: Infinite solutions (same line)**")
    
    else:  # Challenge
        st.subheader("Level 4: Challenge Problems")
        
        with st.expander("Problem 10: Complex Word Problem"):
            st.markdown("""
            **Problem:**
            A farmer has chickens and cows. There are 30 animals total and 76 legs total. How many chickens and how many cows are there?
            
            (Remember: chickens have 2 legs, cows have 4 legs)
            """)
            if st.checkbox("Show solution", key="p10"):
                st.markdown("""
                **Solution:**
                ```
                Let c = chickens, w = cows
                
                c + w = 30  (total animals)
                2c + 4w = 76  (total legs)
                
                From first: c = 30 - w
                Substitute:
                2(30 - w) + 4w = 76
                60 - 2w + 4w = 76
                60 + 2w = 76
                2w = 16
                w = 8
                
                c = 30 - 8 = 22
                ```
                """)
                st.success("**Answer: 22 chickens and 8 cows**")
        
        with st.expander("Problem 11: Three Variables (Bonus)"):
            st.markdown("""
            **Problem:**
            Can you solve this system with three equations?
            ```
            x + y + z = 6
            2x - y + z = 3
            x + 2y - z = 4
            ```
            """)
            if st.checkbox("Show solution", key="p11"):
                st.markdown("""
                **Solution (using elimination twice):**
                ```
                Add equations 1 and 3:
                x + y + z = 6
                x + 2y - z = 4
                ___________
                2x + 3y = 10  ... (A)
                
                Add equations 2 and 3:
                2x - y + z = 3
                x + 2y - z = 4
                ___________
                3x + y = 7  ... (B)
                
                Now solve (A) and (B):
                Multiply (B) by -3:
                2x + 3y = 10
                -9x - 3y = -21
                ____________
                -7x = -11
                x = 11/7
                
                Then solve for y and z...
                ```
                """)
                st.success("**Answer: (11/7, 4/7, 17/7)** - This is advanced!")

# ==================== PRACTICE TEST ====================
elif tutorial_section == "📋 Practice Test":
    st.header("Practice Test: Systems of Equations")
    st.markdown("Test your knowledge! Answer all questions to see your score.")
    
    if 'test_submitted' not in st.session_state:
        st.session_state.test_submitted = False
    
    score = 0
    total_questions = 10
    
    st.subheader("Multiple Choice Section")
    
    # Question 1
    q1 = st.radio(
        "**1. What is the graphical representation of the solution to a system?**",
        ["The y-intercept", "The point where lines intersect", "The slope", "The x-intercept"],
        key="test_q1"
    )
    if q1 == "The point where lines intersect":
        score += 1
    
    # Question 2
    q2 = st.radio(
        "**2. Which method is best when one variable is already isolated?**",
        ["Graphing", "Substitution", "Elimination", "Any method"],
        key="test_q2"
    )
    if q2 == "Substitution":
        score += 1
    
    # Question 3
    q3 = st.radio(
        "**3. What does it mean if you get 0 = 5 when solving a system?**",
        ["One solution", "No solution", "Infinite solutions", "Invalid equation"],
        key="test_q3"
    )
    if q3 == "No solution":
        score += 1
    
    # Question 4
    q4 = st.radio(
        "**4. What does it mean if you get 0 = 0 when solving a system?**",
        ["One solution", "No solution", "Infinite solutions", "Invalid equation"],
        key="test_q4"
    )
    if q4 == "Infinite solutions":
        score += 1
    
    # Question 5
    q5 = st.radio(
        "**5. Parallel lines have:**",
        ["Same slope, same y-intercept", "Same slope, different y-intercept", "Different slopes", "No slope"],
        key="test_q5"
    )
    if q5 == "Same slope, different y-intercept":
        score += 1
    
    st.markdown("---")
    st.subheader("Problem Solving Section")
    
    # Question 6
    st.markdown("**6. Solve: y = x + 2 and y = 2x**")
    q6 = st.text_input("Enter solution as (x, y):", key="test_q6")
    if "2" in q6 and "4" in q6:
        score += 1
    
    # Question 7
    st.markdown("**7. Solve: x + y = 10 and x - y = 4**")
    q7 = st.text_input("Enter solution as (x, y):", key="test_q7")
    if "7" in q7 and "3" in q7:
        score += 1
    
    # Question 8
    st.markdown("**8. The sum of two numbers is 15. Their difference is 3. What is the larger number?**")
    q8 = st.number_input("Enter the larger number:", min_value=0, max_value=20, key="test_q8")
    if q8 == 9:
        score += 1
    
    # Question 9
    st.markdown("**9. Does the system y = 2x + 1 and y = 2x + 5 have one solution, no solution, or infinite solutions?**")
    q9 = st.radio("Select answer:", ["One solution", "No solution", "Infinite solutions"], key="test_q9")
    if q9 == "No solution":
        score += 1
    
    # Question 10
    st.markdown("**10. Which method would be most efficient for: 3x + y = 7 and 3x - y = 5?**")
    q10 = st.radio("Select method:", ["Graphing", "Substitution", "Elimination"], key="test_q10")
    if q10 == "Elimination":
        score += 1
    
    if st.button("Submit Test", type="primary"):
        st.session_state.test_submitted = True
        st.session_state.test_score = score
    
    if st.session_state.test_submitted:
        percentage = (st.session_state.test_score / total_questions) * 100
        st.markdown("---")
        st.subheader("Test Results")
        st.metric("Your Score", f"{st.session_state.test_score}/{total_questions}")
        st.metric("Percentage", f"{percentage:.1f}%")
        
        if percentage >= 90:
            st.success("🌟 Excellent! You're ready for the exam!")
            st.balloons()
        elif percentage >= 70:
            st.info("👍 Good work! Review the sections where you missed questions.")
        else:
            st.warning("📚 Keep studying! Go back through the tutorial sections.")
        
        if st.button("Retake Test"):
            st.session_state.test_submitted = False

# ==================== STUDY RESOURCES ====================
elif tutorial_section == "📚 Study Resources":
    st.header("Study Resources for Systems of Equations")
    
    st.markdown("""
    Use these resources to supplement your learning and get extra practice!
    """)
    
    # Video Resources
    st.subheader("🎥 Video Tutorials")
    st.markdown("Watch these high-quality video lessons to reinforce concepts:")
    
    with st.expander("📺 Introduction to Systems"):
        st.markdown("""
        **Khan Academy - Introduction to Systems of Linear Equations**
        - [What is a System of Equations?](https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:systems-of-equations)
        - Clear explanations with visual examples
        - Perfect for understanding the basics
        
        **The Organic Chemistry Tutor - Systems Overview**
        - [Systems of Equations - Complete Review](https://www.youtube.com/watch?v=FRaJv2Faass)
        - Comprehensive 30-minute tutorial covering all methods
        - Great for exam review
        """)
    
    with st.expander("📺 Graphing Method"):
        st.markdown("""
        **Khan Academy - Solving by Graphing**
        - [Solving Systems by Graphing](https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:systems-of-equations/x2f8bb11595b61c86:solving-systems-of-equations-by-graphing/v/solving-systems-by-graphing)
        - Step-by-step graphing demonstrations
        
        **MathAntics - Graphing Systems**
        - [Systems of Equations - Graphing](https://www.youtube.com/watch?v=gF6Wtq-OJjA)
        - Simple, clear explanations with visual aids
        - Good for beginners
        """)
    
    with st.expander("📺 Substitution Method"):
        st.markdown("""
        **Khan Academy - Substitution Method**
        - [Solving Systems by Substitution](https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:systems-of-equations/x2f8bb11595b61c86:solving-systems-of-equations-with-substitution/v/solving-systems-of-equations-by-substitution)
        - Multiple practice examples
        
        **The Organic Chemistry Tutor - Substitution**
        - [Solving Systems Using Substitution](https://www.youtube.com/watch?v=FdAW18GGsMQ)
        - Clear algebraic steps
        - Works through complex examples
        
        **Professor Dave Explains - Substitution**
        - [Solving Systems of Equations by Substitution](https://www.youtube.com/watch?v=Jm6VkI4lIjw)
        - Concise and focused
        """)
    
    with st.expander("📺 Elimination Method"):
        st.markdown("""
        **Khan Academy - Elimination Method**
        - [Solving Systems by Elimination](https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:systems-of-equations/x2f8bb11595b61c86:solving-systems-of-equations-with-elimination/v/solving-systems-of-equations-by-elimination)
        - Practice exercises included
        
        **The Organic Chemistry Tutor - Elimination**
        - [Solving Systems Using Elimination](https://www.youtube.com/watch?v=s7S3oJsv6YA)
        - Handles multiplication cases
        - Multiple worked examples
        
        **Math with Mr. J - Elimination**
        - [Elimination Method Step by Step](https://www.youtube.com/watch?v=YJ9cMLBs8Io)
        - Very clear teaching style
        """)
    
    with st.expander("📺 Special Cases"):
        st.markdown("""
        **Khan Academy - Number of Solutions**
        - [Number of Solutions to Systems](https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:systems-of-equations/x2f8bb11595b61c86:number-of-solutions-to-systems-of-equations/v/inconsistent-systems-of-equations)
        - Covers no solution and infinite solutions
        
        **The Organic Chemistry Tutor - Special Cases**
        - [Systems with No Solution or Infinite Solutions](https://www.youtube.com/watch?v=6kzSK9-9kBg)
        - Visual explanations of parallel and identical lines
        """)
    
    with st.expander("📺 Word Problems"):
        st.markdown("""
        **Khan Academy - Systems Word Problems**
        - [Word Problems with Systems](https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:systems-of-equations/x2f8bb11595b61c86:systems-of-equations-word-problems/v/systems-of-equations-word-problems)
        - Real-world application practice
        
        **The Organic Chemistry Tutor - Applications**
        - [Systems of Equations Word Problems](https://www.youtube.com/watch?v=AZ5F-AYEsME)
        - Multiple problem types
        - Age, money, mixture problems
        
        **MathAntics - Word Problems**
        - [Setting Up Systems from Word Problems](https://www.youtube.com/watch?v=KjF3drnRhM8)
        - Translation strategies
        """)
    
    st.markdown("---")
    
    # IXL Lessons
    st.subheader("📖 IXL Practice Lessons")
    st.markdown("Complete these IXL lessons for structured practice and immediate feedback:")
    
    grade_select = st.selectbox("Select your math level:", ["Algebra 1", "Algebra 2", "Pre-Calculus"])
    
    if grade_select == "Algebra 1":
        with st.expander("🟢 Algebra 1 - Systems Basics"):
            st.markdown("""
            **Understanding Systems**
            - S.1 - Is (x, y) a solution to the system of equations?
            - S.2 - Find the number of solutions to a system of equations
            - S.3 - Classify a system of equations
            
            **Solving by Graphing**
            - S.4 - Solve a system of equations by graphing
            - S.5 - Solve a system of equations by graphing: word problems
            
            **Solving by Substitution**
            - S.6 - Solve a system of equations using substitution
            - S.7 - Solve a system of equations using substitution: word problems
            
            **Solving by Elimination**
            - S.8 - Solve a system of equations using elimination
            - S.9 - Solve a system of equations using elimination: word problems
            - S.10 - Solve a system of equations using any method
            - S.11 - Solve a system of equations using any method: word problems
            """)
        
        with st.expander("🟡 Algebra 1 - Applications"):
            st.markdown("""
            **Word Problem Practice**
            - S.12 - Write a system of equations given a graph
            - S.13 - Write and solve a system of equations
            - S.14 - Solve a system of equations by graphing: word problems
            - S.15 - Systems of equations word problems
            
            **Real-World Applications**
            - S.16 - Rate problems
            - S.17 - Mixture problems
            - S.18 - Distance-rate-time problems
            """)
    
    elif grade_select == "Algebra 2":
        with st.expander("🟢 Algebra 2 - Advanced Systems"):
            st.markdown("""
            **Linear Systems**
            - A.1 - Solve systems of linear equations
            - A.2 - Determine the number of solutions to a system
            - A.3 - Classify systems of equations
            
            **Systems with Three Variables**
            - A.4 - Solve a system of equations in three variables
            - A.5 - Solve a system of equations in three variables using elimination
            
            **Matrix Methods**
            - A.6 - Solve systems using matrices
            - A.7 - Solve systems using augmented matrices
            - A.8 - Identify invertible matrices and their inverses
            
            **Linear-Quadratic Systems**
            - A.9 - Solve a linear-quadratic system by graphing
            - A.10 - Solve a linear-quadratic system using substitution
            """)
    
    else:  # Pre-Calculus
        with st.expander("🟢 Pre-Calculus - Systems"):
            st.markdown("""
            **Advanced Systems**
            - P.1 - Solve systems of linear and quadratic equations
            - P.2 - Solve systems of nonlinear equations
            - P.3 - Systems of linear inequalities
            - P.4 - Linear programming
            - P.5 - Solve systems using matrices and determinants
            """)
    
    st.info("💡 **IXL Tip:** Try to achieve 80%+ mastery on each lesson before moving to the next!")
    
    st.markdown("---")
    
    # Interactive Tools
    st.subheader("🛠️ Interactive Tools")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Desmos Graphing Calculator**
        - [www.desmos.com/calculator](https://www.desmos.com/calculator)
        - Free online graphing tool
        - Perfect for visualizing systems
        - Can check your graphing solutions
        
        **GeoGebra Systems Solver**
        - [www.geogebra.org](https://www.geogebra.org/)
        - Interactive system solver
        - Shows step-by-step solutions
        - Great for checking work
        """)
    
    with col2:
        st.markdown("""
        **Symbolab Systems Solver**
        - [www.symbolab.com](https://www.symbolab.com/solver/system-of-equations-calculator)
        - Shows detailed solution steps
        - Handles all three methods
        - Good for verification
        
        **Wolfram Alpha**
        - [www.wolframalpha.com](https://www.wolframalpha.com)
        - Powerful computational engine
        - Type: "solve x + y = 5, x - y = 1"
        - Shows graphs and solutions
        """)
    
    st.markdown("---")
    
    # Study Guides and Notes
    st.subheader("📝 Study Guides & Notes")
    
    with st.expander("Written Resources"):
        st.markdown("""
        **Paul's Online Math Notes**
        - [Systems of Equations](https://tutorial.math.lamar.edu/Classes/Alg/SystemsTwoVrble.aspx)
        - Comprehensive written explanations
        - Practice problems with solutions
        
        **Purplemath - Systems**
        - [Systems of Linear Equations](https://www.purplemath.com/modules/systlin1.htm)
        - Step-by-step tutorials
        - Clear examples
        
        **Math is Fun - Systems**
        - [Solving Systems of Equations](https://www.mathsisfun.com/algebra/systems-linear-equations.html)
        - Simple explanations
        - Interactive examples
        """)
    
    st.markdown("---")
    
    # Practice Worksheets
    st.subheader("📄 Practice Worksheets")
    
    st.markdown("""
    **Kuta Software** - Free worksheets with answer keys
    - Search "Kuta Software Systems of Equations" for printable practice
    - Multiple difficulty levels available
    
    **Math-Drills.com** - Worksheet generator
    - [Systems of Equations Worksheets](https://www.math-drills.com/)
    - Can generate custom practice sets
    """)
    
    st.markdown("---")
    
    # Study Tips
    st.subheader("💡 How to Use These Resources")
    
    study_tips_df = pd.DataFrame({
        'Resource Type': ['Videos', 'IXL Lessons', 'Interactive Tools', 'Study Guides', 'Practice Worksheets'],
        'Best Used For': [
            'Learning new concepts, visual explanations',
            'Structured practice with immediate feedback',
            'Checking your work, visualizing problems',
            'Review, looking up specific topics',
            'Timed practice, simulating test conditions'
        ],
        'Recommended Time': [
            '15-20 min per topic',
            '20-30 min per lesson',
            'As needed for verification',
            '10-15 min for reference',
            '20-30 min per worksheet'
        ]
    })
    
    st.dataframe(study_tips_df, use_container_width=True, hide_index=True)
    
    st.success("🎯 **Study Plan Suggestion:** Watch a video → Practice on IXL → Do a worksheet → Check with tools!")

# ==================== EXAM DAY TIPS ====================
elif tutorial_section == "🎓 Exam Day Tips":
    st.header("Exam Day Success Tips")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Before the Exam")
        st.markdown("""
        ✅ **Get a good night's sleep** - Your brain needs rest!
        
        ✅ **Eat a healthy breakfast** - Fuel your brain
        
        ✅ **Review key formulas** - Not for memorizing, just refreshing
        
        ✅ **Bring necessary materials**:
        - Pencils with erasers
        - Calculator (if allowed)
        - Ruler for graphing
        - Scratch paper
        
        ✅ **Arrive early** - Avoid stress, get settled
        
        ✅ **Stay positive** - You've prepared well!
        """)
    
    with col2:
        st.subheader("During the Exam")
        st.markdown("""
        📝 **Read each problem carefully** - Don't rush
        
        📝 **Show ALL your work** - Partial credit matters!
        
        📝 **Check your arithmetic** - Simple errors are common
        
        📝 **Choose the best method** - Think before solving
        
        📝 **Label your answers** - Make it clear
        
        📝 **Verify your solutions** - Substitute back if time allows
        
        📝 **Skip and return** - Don't get stuck on one problem
        
        📝 **Manage your time** - Budget time per question
        """)
    
    st.markdown("---")
    
    st.subheader("Common Mistakes to Avoid")
    
    mistakes_df = pd.DataFrame({
        'Mistake': [
            'Sign errors when subtracting',
            'Forgetting to distribute',
            'Not checking answer',
            'Arithmetic mistakes',
            'Mixing up x and y',
            'Not showing work',
            'Rushing through problems',
            'Forgetting to answer the question'
        ],
        'How to Avoid': [
            'Take your time, use parentheses',
            'Write out distribution step by step',
            'Substitute answer into both equations',
            'Double-check calculations',
            'Label clearly which is which',
            'Write every step',
            'Work at steady pace',
            'Read what the question asks for'
        ]
    })
    
    st.dataframe(mistakes_df, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    st.subheader("Quick Formula Reference")
    
    st.markdown("""
    **Forms of Linear Equations:**
    - **Slope-intercept form:** y = mx + b
    - **Standard form:** Ax + By = C
    - **Point-slope form:** y - y₁ = m(x - x₁)
    
    **Key Concepts:**
    - **Solution:** Point that satisfies all equations
    - **One solution:** Lines intersect (different slopes)
    - **No solution:** Parallel lines (same slope, different intercepts)
    - **Infinite solutions:** Same line (equivalent equations)
    
    **Method Selection:**
    - **Graphing:** Visual, slope-intercept form ready
    - **Substitution:** Variable isolated or coefficient of 1
    - **Elimination:** Standard form, opposites possible
    """)
    
    st.success("**You've got this, Meka! Trust your preparation and do your best!**")

# --- Footer Stats ---
st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Sections Completed", f"{len(st.session_state.completed_sections)}/11")

with col2:
    if hasattr(st.session_state, 'test_score'):
        st.metric("Practice Test Score", f"{st.session_state.test_score}/10")
    else:
        st.metric("Practice Test", "Not taken")

with col3:
    ready_score = len(st.session_state.completed_sections) * 10
    st.metric("Readiness", f"{ready_score}%")

st.markdown("---")
st.markdown("**Good luck on your exam, Meka Wilson! 🎓**")
