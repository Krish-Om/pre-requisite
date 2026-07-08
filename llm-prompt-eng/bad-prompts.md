### Bad Pompts

**Prompt 1:**
Hey, Build me analytics dashboard

> **Failure Mode — Ambiguity:** No tech stack, no features, no target users, no scale defined. The model has to guess everything; every output will differ wildly.

---

**Prompt 2:**
Hey, act as mentor and teach me how to build an analytics dashboard

> **Failure Mode — Ambiguity:** Role ("mentor") is loosely defined. No skill level, no tech context, no preferred teaching style or output format specified.

---

**Prompt 3:**
Act as a best teacher and guide me on learning System Design.

> **Failure Mode — Drift:** "System Design" is a vast domain with no scope boundary. The response will wander across networking, databases, scalability, etc. with no anchor to stop it.

---

**Prompt 4:**
Act as a best teacher and guide me on learning Python from scratch, I am a beginner and I dont know a shit about it.
Write the guide in a latex document or in text format. Generate the diagrams in mermaid format.

> **Failure Mode — Ambiguity:** The `or` in the format instruction forces the model to pick arbitrarily between LaTeX and plain text. Conflicting constraints produce inconsistent output.

---

**Prompt 5:**
Try to fix this issue, as if you are best programmer

> **Failure Mode — Ambiguity:** No issue, no code, and no error message provided — the model has nothing to act on. "Try to" also weakens the directive, making the expected output unclear.

---

**Prompt 6:**
Imagine you are a Leonardo Da Vinci, create a beautiful painting of David.

> **Failure Mode — Hallucination:** LLMs cannot produce visual art. The model will either fabricate a description pretending to be a painting, or confabulate Da Vinci's "intent" — both are hallucinations caused by a capability mismatch.

---

**Prompt 7:**
Try to optimize this code, as if you are best programmer

> **Failure Mode — Ambiguity:** No code is provided. "Best programmer" is a meaningless superlative with no measurable standard, and "try to" weakens the instruction further.

---

**Prompt 8:**
I have to write a essay on "Dead Poet Society". Write the essay for me in txt format.

> **Failure Mode — Missing Format:** `txt` is a file extension, not a format. No word count, structure (analytical? personal? academic?), thesis direction, or tone is specified.

---

**Prompt 9:**

I am unable to write a good essay on "Dead Poet Society".Guide me to write a good essay.

> **Failure Mode — Missing Format:** No output structure defined for the guide — bullet points? outline? step-by-step? Also missing context on what "good" means or at what academic level the essay should be.

---

**Prompt 10:**
What are the key themes in "Dead Poet Society"?. Generate a list of them.

> **Failure Mode —
