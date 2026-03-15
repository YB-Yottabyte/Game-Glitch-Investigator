# 🔍 Debugging Reflection & AI Collaboration Log

As you work through this project, use this file to document your debugging process, how you used Copilot, and what you learned about working with AI-generated code.

---

## Phase 1: Glitch Hunt

### 1. What was broken when you started?

Document the three bugs you found. For each bug, describe:
- **What you expected to happen**
- **What actually happened**
- **Where in the code you think the bug is**

#### Bug #1: [Name/Description]
- **Expected:** 
- **Actual:** 
- **Location (file and function):** 

#### Bug #2: [Name/Description]
- **Expected:** 
- **Actual:** 
- **Location (file and function):** 

#### Bug #3: [Name/Description]
- **Expected:** 
- **Actual:** 
- **Location (file and function):** 

---

## Phase 2: Investigate and Repair

### 2. How did you use AI as a teammate?

Describe two examples:

#### ✅ Example of CORRECT AI Suggestion
- **What you asked Copilot:** 
- **What it suggested:** 
- **Was it correct?** Yes
- **How you verified it:** 
- **Why did it work?** 

#### ❌ Example of INCORRECT/MISLEADING AI Suggestion
- **What you asked Copilot:** 
- **What it suggested:** 
- **Was it correct?** No
- **What was wrong?** 
- **How did you catch the error?** 
- **What you did instead:** 

### 3. Debugging and testing your fixes

For each bug you fixed, document:

#### Fix #1: [Bug Name]
- **The problem:** 
- **Copilot's explanation:** 
- **The fix I made:** 
- **Test case I wrote:** 
- **Test passed?** ✓ / ✗

#### Fix #2: [Bug Name]
- **The problem:** 
- **Copilot's explanation:** 
- **The fix I made:** 
- **Test case I wrote:** 
- **Test passed?** ✓ / ✗

#### Fix #3: [Bug Name]
- **The problem:** 
- **Copilot's explanation:** 
- **The fix I made:** 
- **Test case I wrote:** 
- **Test passed?** ✓ / ✗

---

## Phase 3: Final Reflection

### 4. What did you learn?

#### How did this project change your view on AI-assisted debugging?
> Your answer here

#### What surprised you most about the bugs?
> Your answer here

#### If you had to debug this code WITHOUT Copilot, what would be harder?
> Your answer here

#### If you had to trust ONLY what Copilot suggested (without testing), what could go wrong?
> Your answer here

#### How confident are you in your final code? Why?
> Your answer here (explain what tests/verification you did)

---

## 💡 Tips for Filling This Out

- **Be specific:** Instead of "Copilot was helpful," say "Copilot explained that the if/else logic was reversed, which I verified by adding print statements."
- **Be honest:** If Copilot gave bad advice, own it. It shows you were thinking critically.
- **Reference code:** Point to specific lines or functions when explaining bugs (e.g., "In `logic_utils.py` line 42, the comparison is backwards").
- **Show your work:** Describe how you tested each fix (e.g., "I ran pytest and saw the test pass" or "I played the game and confirmed the hint was correct").

---

## Commit Messages Reference

As you fix bugs and make changes, remember to commit your work:

```bash
# After fixing a bug
git add .
git commit -m "fix: correct [bug name] in logic_utils.py"

# After adding tests
git add test/
git commit -m "test: add pytest cases for [bug name]"

# After updating documentation
git add README.md reflection.md
git commit -m "docs: update reflection with debugging notes"

# Final push
git push origin main
```

Good luck, and happy debugging! 🚀
