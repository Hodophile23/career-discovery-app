print("🎯 Welcome to the Career Discovery System!")
print("Please answer the following questions honestly.\n")

score = {
    "govt": 0,
    "tech": 0,
    "creative": 0,
    "business": 0,
    "management": 0
}

# Question 1
print("1. What excites you the most?")
print("a) Solving public issues")
print("b) Building apps or websites")
print("c) Designing, art, or content")
print("d) Leading and organizing teams")
print("e) Running your own business")
ans1 = input("Your choice (a/b/c/d/e): ")

if ans1 == 'a':
    score["govt"] += 1
elif ans1 == 'b':
    score["tech"] += 1
elif ans1 == 'c':
    score["creative"] += 1
elif ans1 == 'd':
    score["management"] += 1
elif ans1 == 'e':
    score["business"] += 1

# Question 2
print("\n2. Your dream workplace?")
print("a) Government office")
print("b) MNC or remote tech job")
print("c) Studio or creative setup")
print("d) Corporate with leadership")
print("e) Own startup or freelancing")
ans2 = input("Your choice (a/b/c/d/e): ")

if ans2 == 'a':
    score["govt"] += 1
elif ans2 == 'b':
    score["tech"] += 1
elif ans2 == 'c':
    score["creative"] += 1
elif ans2 == 'd':
    score["management"] += 1
elif ans2 == 'e':
    score["business"] += 1

# Question 3
print("\n3. What do you enjoy most?")
print("a) Helping society and being disciplined")
print("b) Logical problem-solving or writing code")
print("c) Creating content, music, or visuals")
print("d) Organizing events or handling people")
print("e) Making money independently or freelancing")
ans3 = input("Your choice (a/b/c/d/e): ")

if ans3 == 'a':
    score["govt"] += 1
elif ans3 == 'b':
    score["tech"] += 1
elif ans3 == 'c':
    score["creative"] += 1
elif ans3 == 'd':
    score["management"] += 1
elif ans3 == 'e':
    score["business"] += 1

# Question 4
print("\n4. What are you naturally good at?")
print("a) Following rules and systems")
print("b) Fixing tech issues or exploring gadgets")
print("c) Drawing, acting, writing, or expressing ideas")
print("d) Taking charge or organizing things")
print("e) Finding new ideas or earning money")
ans4 = input("Your choice (a/b/c/d/e): ")

if ans4 == 'a':
    score["govt"] += 1
elif ans4 == 'b':
    score["tech"] += 1
elif ans4 == 'c':
    score["creative"] += 1
elif ans4 == 'd':
    score["management"] += 1
elif ans4 == 'e':
    score["business"] += 1

# Question 5
print("\n5. What’s your long-term goal?")
print("a) Secure job with impact in society")
print("b) Stable tech career with good pay")
print("c) Pursue your passion and get recognized")
print("d) Become a top-level manager/leader")
print("e) Be your own boss and take risks")
ans5 = input("Your choice (a/b/c/d/e): ")

if ans5 == 'a':
    score["govt"] += 1
elif ans5 == 'b':
    score["tech"] += 1
elif ans5 == 'c':
    score["creative"] += 1
elif ans5 == 'd':
    score["management"] += 1
elif ans5 == 'e':
    score["business"] += 1
print("\n🔍 Calculating your best-fit career path...\n")

# Find highest score category
top_field = max(score, key=score.get)

print("✨ Based on your interests, we suggest:")

if top_field == "govt":
    print("→ Career Path: Civil Services, SSC, Policy Analyst, Public Sector Officer")
elif top_field == "tech":
    print("→ Career Path: Software Engineer, QA Tester, Data Analyst, IT Support")
elif top_field == "creative":
    print("→ Career Path: Designer, Content Creator, Filmmaker, Writer")
elif top_field == "management":
    print("→ Career Path: HR, Project Manager, Operations Lead, Coordinator")
elif top_field == "business":
    print("→ Career Path: Entrepreneur, Digital Marketer, Consultant, Freelancer")

print("\n📘 Tip: Research this domain, learn required skills, and take internships.")
