import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# --- Page Setup ---
st.set_page_config(page_title="Systems of Linear Equations", page_icon="🧮")

# --- Developer Credit ---
st.markdown("### [www.cognitivecloud.ai](https://www.cognitivecloud.ai)")
st.markdown("**Developed by Xavier Honablue M.Ed**")

st.markdown("---")

# --- Title and Intro ---
st.title("🧮 Systems of Linear Equations: Real-World Solutions")
st.markdown("""
Welcome!  
This lesson helps you **solve, understand, and apply** systems of linear equations to real-world problems.

---

### 📘 Classic Explanation:
A **system of linear equations** is a set of two or more equations that share the same variables.  
The solution is the point where all equations are true at the same time - like finding when two different 
situations reach the same outcome.

---

### 🎯 Objective:
By the end of this lesson, you'll be able to:
- Solve systems using multiple methods (graphing, substitution, elimination)
- Interpret solutions in real-world contexts
- Determine the number of solutions a system has
- Model real situations with systems of equations
""")

# Illinois Learning Standards Alignment
st.info("📚 **Illinois Learning Standards:** This lesson aligns with high school algebra standards for solving systems of equations in real-world contexts.")

# Illinois Standards Dropdown
illinois_standard = st.selectbox("📋 Select specific Illinois Learning Standard:", [
    "HSA.REI.C.6 - Solve systems of linear equations algebraically and graphically",
    "HSA.CED.A.3 - Represent constraints by systems of equations", 
    "HSA.REI.C.5 - Prove that systems have one, zero, or infinitely many solutions",
    "HSA.REI.D.11 - Graph systems of linear inequalities"
])

# --- Student Info ---
name = st.text_input("Enter your name:")
avatar = st.selectbox("Choose your multidimensional shape avatar:", [
    "🔺 Tetrahedron", "🚘 Dodecahedron", "⬛ Cube", "🌀 Torus"
])

if name:
    st.success(f"Welcome, {name} the {avatar}! Let's master systems of equations together.")

# --- Role Selection ---
role_options = [
    "🌟 Skill Mastery Star",
    "🚀 Growth Mode",
    "🎮 Level-Up Leader",
    "🎯 Focus Champ",
    "📊 Data Boss",
    "🧠 Brain Builder",
    "🎓 Scholar",
    "📈 Goal Getter",
    "🛠️ Problem Solver",
    "💡 Idea Generator"
]
role = st.selectbox("Pick your learning mode or style:", role_options)

# --- Matching Challenge Section ---
st.header("🎯 Matching Challenge")
st.markdown("**Match each system to its real-world interpretation before exploring visualizations!**")

# Create the matching data
matching_data = {
    "Scenario": [
        "Business Revenue", "Phone Plans", "Streaming Subscribers", 
        "Travel Distance", "Temperature Change", "Savings Accounts"
    ],
    "System of Equations": [
        "y = 50x + 500, y = 80x + 200",
        "y = 0.10x + 20, y = 0.05x + 35",
        "y = 100x + 2000, y = 50x + 3500",
        "y = 60x + 50, y = 75x",
        "y = 3x + 65, y = -2x + 80",
        "y = 40x + 800, y = 60x + 400"
    ],
    "What We're Finding": [
        "When will companies have equal revenue?",
        "When do plans cost the same?",
        "When equal subscriber count?",
        "When does Car B catch Car A?",
        "When same temperature?",
        "When equal savings?"
    ]
}

df = pd.DataFrame(matching_data)
st.dataframe(df, use_container_width=True, hide_index=True)

# Interactive matching quiz
st.subheader("📝 Quick Matching Quiz")

quiz_questions = [
    {
        "question": "What does the solution of a system of equations represent graphically?",
        "options": ["The y-intercept", "The point where the lines intersect", "The slope of the lines", "The domain of the functions"],
        "correct": 1,
        "explanation": "The solution is where both equations are true simultaneously - the intersection point!"
    },
    {
        "question": "Which method would be fastest if one equation is already solved for y?",
        "options": ["Graphing", "Substitution", "Elimination", "Guess and check"],
        "correct": 1,
        "explanation": "Substitution is ideal when one variable is already isolated!"
    },
    {
        "question": "What does it mean if two lines in a system are parallel?",
        "options": ["One solution", "No solution", "Infinite solutions", "Two solutions"],
        "correct": 1,
        "explanation": "Parallel lines never intersect, meaning no solution exists!"
    }
]

for i, q in enumerate(quiz_questions):
    st.write(f"**Question {i+1}:** {q['question']}")
    answer = st.radio(f"Select your answer for Q{i+1}:", q['options'], key=f"q{i}")
    
    if st.button(f"Check Answer {i+1}", key=f"check{i}"):
        if q['options'].index(answer) == q['correct']:
            st.success(f"✅ Correct! {q['explanation']}")
        else:
            st.error(f"❌ Try again! {q['explanation']}")

st.markdown("---")

# --- Real-Life System Examples ---
st.header("📊 Interactive System Visualizations")

scenarios = {
    "Business Revenue": {
        "desc": "💼 Two businesses competing: Company A starts with $500 and earns $50/day. Company B starts with $200 and earns $80/day.",
        "eq1": "y = 50x + 500",
        "eq2": "y = 80x + 200",
        "system": "y = 50x + 500 and y = 80x + 200",
        "solution": "x = 10 days, y = $1000",
        "domain": "Days (0-20)",
        "range": "Revenue ($200-$2100)",
        "context": "When will both companies have equal revenue?",
        "func1": lambda x: 50 * x + 500,
        "func2": lambda x: 80 * x + 200,
        "x_max": 20
    },
    "Phone Plans": {
        "desc": "📱 Plan A: $20/month + $0.10/minute. Plan B: $35/month + $0.05/minute.",
        "eq1": "y = 0.10x + 20",
        "eq2": "y = 0.05x + 35",
        "system": "y = 0.10x + 20 and y = 0.05x + 35",
        "solution": "x = 300 minutes, y = $50",
        "domain": "Minutes (0-500)",
        "range": "Cost ($20-$70)",
        "context": "At what usage are both plans equal cost?",
        "func1": lambda x: 0.10 * x + 20,
        "func2": lambda x: 0.05 * x + 35,
        "x_max": 500
    },
    "Streaming Subscribers": {
        "desc": "🎬 Platform A: 2000 subscribers, gaining 100/week. Platform B: 3500 subscribers, gaining 50/week.",
        "eq1": "y = 100x + 2000",
        "eq2": "y = 50x + 3500",
        "system": "y = 100x + 2000 and y = 50x + 3500",
        "solution": "x = 30 weeks, y = 5000 subscribers",
        "domain": "Weeks (0-40)",
        "range": "Subscribers (2000-6500)",
        "context": "When will both platforms have equal subscribers?",
        "func1": lambda x: 100 * x + 2000,
        "func2": lambda x: 50 * x + 3500,
        "x_max": 40
    },
    "Travel Distance": {
        "desc": "🚗 Car A travels at 60 mph starting 50 miles ahead. Car B travels at 75 mph from origin.",
        "eq1": "y = 60x + 50",
        "eq2": "y = 75x",
        "system": "y = 60x + 50 and y = 75x",
        "solution": "x ≈ 3.33 hours, y = 250 miles",
        "domain": "Hours (0-10)",
        "range": "Distance (0-750 miles)",
        "context": "When does Car B catch up to Car A?",
        "func1": lambda x: 60 * x + 50,
        "func2": lambda x: 75 * x,
        "x_max": 10
    },
    "Temperature Change": {
        "desc": "🌡️ Room A: starts at 65°F, warms 3°F/hour. Room B: starts at 80°F, cools 2°F/hour.",
        "eq1": "y = 3x + 65",
        "eq2": "y = -2x + 80",
        "system": "y = 3x + 65 and y = -2x + 80",
        "solution": "x = 3 hours, y = 74°F",
        "domain": "Hours (0-10)",
        "range": "Temperature (60-85°F)",
        "context": "When will both rooms be the same temperature?",
        "func1": lambda x: 3 * x + 65,
        "func2": lambda x: -2 * x + 80,
        "x_max": 10
    },
    "Savings Accounts": {
        "desc": "💰 Account A: $800 initial, add $40/month. Account B: $400 initial, add $60/month.",
        "eq1": "y = 40x + 800",
        "eq2": "y = 60x + 400",
        "system": "y = 40x + 800 and y = 60x + 400",
        "solution": "x = 20 months, y = $1600",
        "domain": "Months (0-30)",
        "range": "Balance ($400-$2600)",
        "context": "When will both accounts have equal balance?",
        "func1": lambda x: 40 * x + 800,
        "func2": lambda x: 60 * x + 400,
        "x_max": 30
    }
}

# Scenario Selection
selected = st.selectbox("Choose a real-world scenario to explore:", list(scenarios.keys()))
scenario = scenarios[selected]

# Display scenario details
col1, col2, col3 = st.columns(3)

with col1:
    st.info(f"**Description**\n\n{scenario['desc']}")

with col2:
    st.success(f"**System**\n\n{scenario['system']}\n\n{scenario['context']}")

with col3:
    st.warning(f"**Solution**\n\n{scenario['solution']}\n\nDomain: {scenario['domain']}\n\nRange: {scenario['range']}")

# Generate graph data
x_vals = np.linspace(0, scenario['x_max'], 200)
y1_vals = [scenario['func1'](x) for x in x_vals]
y2_vals = [scenario['func2'](x) for x in x_vals]

# Create the plot
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x_vals, y1_vals, linewidth=3, color='#1f77b4', label=f"Equation 1: {scenario['eq1']}")
ax.plot(x_vals, y2_vals, linewidth=3, color='#82ca9d', label=f"Equation 2: {scenario['eq2']}")
ax.set_title(f"{selected} System", fontsize=14, fontweight='bold')
ax.set_xlabel("Input (x)", fontsize=12)
ax.set_ylabel("Output (y)", fontsize=12)
ax.grid(True, alpha=0.3)
ax.legend()
ax.set_facecolor('#f8f9fa')

st.pyplot(fig)

# --- Solution Methods Section ---
st.header("🔧 Solution Methods")

methods = {
    "Graphing": {
        "description": "Plot both equations and find where they intersect",
        "steps": [
            "1. Graph the first equation",
            "2. Graph the second equation",
            "3. Find intersection point",
            "4. Check solution in both equations"
        ],
        "pros": "Visual and intuitive",
        "cons": "Can be imprecise for non-integer solutions"
    },
    "Substitution": {
        "description": "Solve one equation for a variable, substitute into the other",
        "steps": [
            "1. Solve one equation for x or y",
            "2. Substitute into other equation",
            "3. Solve for remaining variable",
            "4. Back-substitute to find other variable"
        ],
        "pros": "Exact solutions, good when one variable is isolated",
        "cons": "Can involve fractions and complex algebra"
    },
    "Elimination": {
        "description": "Add or subtract equations to eliminate one variable",
        "steps": [
            "1. Align equations vertically",
            "2. Multiply to make coefficients opposites",
            "3. Add/subtract to eliminate variable",
            "4. Solve and back-substitute"
        ],
        "pros": "Efficient for many systems, exact solutions",
        "cons": "Requires careful coefficient manipulation"
    }
}

selected_method = st.selectbox("Explore solution method:", list(methods.keys()))
method = methods[selected_method]

st.subheader(f"{selected_method} Method")
st.write(method['description'])

st.write("**Steps:**")
for step in method['steps']:
    st.write(step)

col1, col2 = st.columns(2)
with col1:
    st.success(f"**Pros:** {method['pros']}")
with col2:
    st.warning(f"**Cons:** {method['cons']}")

# --- Test Your System ---
st.header("🧮 Test the System")
st.write(f"Try different input values for the **{selected}** system:")

test_input = st.slider("Input value (x):", 0, int(scenario['x_max']), int(scenario['x_max']//2))

col1, col2 = st.columns(2)
with col1:
    result1 = scenario['func1'](test_input)
    st.info(f"**Equation 1:** {scenario['eq1']}\n\n**y = {result1:.2f}**")
with col2:
    result2 = scenario['func2'](test_input)
    st.success(f"**Equation 2:** {scenario['eq2']}\n\n**y = {result2:.2f}**")

# --- IXL Practice Section ---
st.header("📚 IXL Practice & Related Lessons")

strand = st.selectbox("Choose Your Learning Focus:", [
    "HSA-REI.C.6 – Solve systems of linear equations",
    "HSA-CED.A.3 – Represent constraints by systems",
    "HSA-REI.C.5 – Analyze number of solutions",
    "HSA-REI.D.11 – Graph systems of inequalities"
])

st.info(f"**Focus:** {strand.split('–')[1]}")

grade_level = st.selectbox("Select your grade level for IXL recommendations:", ["Algebra 1", "Algebra 2"])

ixl_lessons = {
    "Algebra 1": {
        "System Basics": [
            "S.1 - Is (x, y) a solution to the system?",
            "S.2 - Solve a system by graphing",
            "S.3 - Solve a system by substitution",
            "S.4 - Solve a system by elimination",
            "S.5 - Solve systems: word problems"
        ],
        "Applications": [
            "S.6 - Write systems from word problems",
            "S.7 - Systems with three variables",
            "S.8 - Number of solutions to systems",
            "S.9 - Classify systems of equations"
        ]
    },
    "Algebra 2": {
        "Advanced Systems": [
            "A.1 - Solve linear-quadratic systems",
            "A.2 - Solve systems with matrices",
            "A.3 - Systems of inequalities",
            "A.4 - Linear programming"
        ]
    }
}

for topic, lessons in ixl_lessons[grade_level].items():
    with st.expander(f"📖 {topic} - IXL Lessons"):
        for lesson in lessons:
            st.write(f"• {lesson}")
        st.markdown(f"**🎯 Practice Tip:** Complete these lessons on IXL to master {topic.lower()} concepts!")

# --- Additional Resources ---
st.header("🌐 Additional Learning Resources")

with st.expander("📺 Video Tutorials"):
    st.write("• **Khan Academy - Systems of Equations:** Comprehensive video series on all solution methods")
    st.write("• **Professor Leonard - Systems:** Detailed explanations with worked examples")
    st.write("• **The Organic Chemistry Tutor:** Clear, step-by-step problem solving")

with st.expander("💻 Interactive Tools"):
    st.write("• **Desmos Graphing Calculator:** Free online tool to visualize systems")
    st.write("• **GeoGebra Systems:** Interactive system solver with step-by-step solutions")
    st.write("• **Wolfram Alpha:** Computational engine for solving any system")

with st.expander("📚 Study Guides & Practice"):
    st.write("• **Paul's Online Math Notes:** Comprehensive notes with examples")
    st.write("• **Purplemath:** Step-by-step tutorials and problem-solving strategies")
    st.write("• **Mathway:** Online problem solver with solutions")

# --- Personalized Study Plan ---
st.header("📅 Personalized Study Plan")

current_level = st.selectbox("What's your current comfort level with systems?", [
    "Beginner - Just starting to learn about systems",
    "Intermediate - Understand basics, need more practice",
    "Advanced - Ready for complex applications",
    "Expert - Looking for challenge problems"
])

study_time = st.selectbox("How much time can you dedicate per week?", [
    "1-2 hours",
    "3-4 hours",
    "5-6 hours",
    "7+ hours"
])

if st.button("Generate My Study Plan"):
    st.success("🎯 Your Personalized Systems Mastery Plan:")
    
    if "Beginner" in current_level:
        st.markdown("""
        **Week 1-2: Foundation Building**
        - Watch Khan Academy's "Systems of Equations" introduction videos
        - Complete IXL lessons S.1-S.2 (Identifying solutions and graphing)
        - Practice with Desmos graphing calculator daily (15 min)
        - Work through 5 real-world scenarios in this app
        
        **Week 3-4: Solution Methods**
        - Focus on IXL lessons S.3-S.4 (Substitution and Elimination)
        - Practice each method with 10 problems per technique
        - Use GeoGebra to check your algebraic work
        - Complete reflection exercises in this app
        """)
    
    elif "Intermediate" in current_level:
        st.markdown("""
        **Week 1: Review and Strengthen**
        - Complete remaining IXL system basics lessons
        - Practice with all three methods until fluent
        - Work through Paul's Online Math Notes systematically
        - Focus on choosing the best method for each problem
        
        **Week 2-3: Word Problems and Applications**
        - Complete IXL S.5-S.6 (Word problems and writing systems)
        - Create 5 original real-world system problems
        - Use Wolfram Alpha to verify complex solutions
        - Practice translating scenarios into mathematical systems
        """)
    
    elif "Advanced" in current_level:
        st.markdown("""
        **Week 1: Master Advanced Concepts**
        - Complete Algebra 2 IXL lessons on systems
        - Study systems with three variables
        - Explore linear-quadratic systems
        - Learn matrix methods for solving systems
        
        **Week 2: Real-World Modeling**
        - Research systems in your field of interest
        - Create presentations on system modeling
        - Tackle systems of inequalities and linear programming
        - Work on competition-level problems
        """)
    
    else:
        st.markdown("""
        **Ongoing Challenge Plan:**
        - Explore systems in higher dimensions
        - Study numerical methods for large systems
        - Research applications in engineering and economics
        - Mentor other students learning systems
        - Participate in math competitions (AMC, AIME)
        - Explore systems of differential equations
        """)
    
    if study_time == "1-2 hours":
        st.info("💡 **Tip:** Focus on one concept per week with daily 15-minute practice sessions. Quality over quantity!")
    elif study_time == "3-4 hours":
        st.info("💡 **Tip:** Balance video learning (40%) with hands-on practice (60%). Review previous material weekly.")
    elif study_time == "5-6 hours":
        st.info("💡 **Tip:** Add teaching others to solidify understanding. Create study guides and example problems.")
    else:
        st.info("💡 **Tip:** Consider pursuing advanced topics and helping tutor peers. Explore competition mathematics.")

# --- Reflection ---
st.header("🧾 Reflection")
reflection = st.text_area("Describe a real-world situation you could model with a system of equations. What are the two equations, and what does the solution represent?")

if st.button("Submit Reflection"):
    if reflection.strip():
        st.success("✅ Excellent mathematical thinking! You understand how systems model real situations!")
        st.balloons()
    else:
        st.warning("Please share your thoughts to complete the reflection.")

# --- Final Summary ---
st.header("🎓 What You've Learned")
st.markdown("""
**Congratulations!** You've explored:
- ✅ **6 real-world system scenarios** from business to technology
- ✅ **3 solution methods** - graphing, substitution, and elimination
- ✅ **Interactive testing** to see how systems behave
- ✅ **Visual representations** showing where equations intersect

**Remember:** Systems of equations help us find when two different situations reach the same outcome - 
from business break-even points to when two phone plans cost the same. Math models the decisions we make every day!
""")

st.markdown("---")
st.markdown("**📍 Illinois Learning Standards:** This lesson supports high school algebra standards for solving and graphing systems of equations.")
