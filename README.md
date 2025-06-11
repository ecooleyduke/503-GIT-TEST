# **AIPI 503 GitHub Collaboration Challenge**

Welcome to the Week 1 Day 4 challenge for AIPI 503! In this assignment, you’ll practice collaborating on GitHub by forking a repository, creating a branch, editing a Python file, and submitting a pull request.

---

## 🚀 Challenge Overview

Your mission is to contribute a word to a class **Madlibs** Python program. This fun script randomly generates an AI-themed sentence using variables like tools, places, and Duke references. Each student will personalize the script by adding a word to one of the lists—or create a new one!

---

## 📝 What You’ll Do

1. **Fork this repository** to your GitHub account.
2. **Clone** your fork to your local machine:

   ```bash
   git clone https://github.com/YOUR-USERNAME/503-GIT-TEST.git
   ```
3. **Create a new branch** for your edits:

   ```bash
   git checkout -b add-my-word
   ```
4. **Open `madlibs.py`** and:

   * Add one word to any existing list (e.g., `tools`, `verbs`, `nouns`, etc.)
   * OR create a new category and integrate it into the final sentence
5. **Run the script** to test your changes:

   ```bash
   python madlibs.py
   ```
6. **Commit and push** your changes:

   ```bash
   git add madlibs.py
   git commit -m "Add my word to madlibs"
   git push origin add-my-word
   ```
7. **Create a pull request** back to the original repository from your GitHub page.

---

## ✅ Example Submission

Before:

```python
tools = ["Python", "TensorFlow"]
```

After:

```python
tools = ["Python", "TensorFlow", "Hugging Face"]
```

Then update your branch and submit a PR!

---

## 💡 Tips

* Keep your additions school-appropriate and relevant to AI or Duke.
* Only edit `madlibs.py`.
* Be sure to **test your sentence** by running the script before submitting your PR.

Happy collaborating, and have fun making AI-powered Duke-themed madlibs!
