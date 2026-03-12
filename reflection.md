# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- Putting a low number (<50) would infinitely tell me to go Lower - fixed
- Entering a high number >50~ would keep telling me to go higher, even if i put 99999999999999999999999999999999999999999999 - fixed
- "New Game" functionality doesn't work - fixed
- Always 1 attempt used in the beginning - fixed

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
-> used Claude Code, specifically github/coder/claudecode.nvim plugin which is very nice
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
-> Everything was correct given the low complexity of the app
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
-> Not anything incorrect given app's scope.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
-> Business logic is reflected on the UI/UX, tests pass
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
-> Verify that when check_guess() is called, and input < solution, then it would say go higher, and go lower for vice versa
- Did AI help you design or understand any tests? How?
-> Just gives me exactly what I described

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
-> I don't remember this happening to be honest, maybe I fixed it and forgot about it.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
-> Once you update your code, it hot-fixes or hot-updates right after you write and save any code.
-> One does not need to cancel the streamlit service, then streamlit run app.py again
- What change did you make that finally gave the game a stable secret number?
-> N/A

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
-> Being extra descriptive to hit a bullseye on the solution with an assistant
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
