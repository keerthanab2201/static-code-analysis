# Reflection – Static Code Analysis Lab

## 1. Which issues were the easiest to fix, and which were the hardest? Why?

**Easiest:**
- Removing unused imports
- Fixing formatting issues (blank lines, naming)
- Replacing `%` formatting with f-strings  
These were straightforward syntax or style changes and did not require altering program logic.

**Hardest:**
- Replacing `eval()` with safe logic
- Handling mutable default arguments
- Adding input validation and proper exception handling  
These required understanding the logic, identifying safe alternatives, and ensuring behavior remained correct after changes.

---

## 2. Did the static analysis tools report any false positives? If so, describe one example.

Yes.  
- Pylint flagged the use of `global stock_data` as a design issue.  
  While globals are generally discouraged, in this small script context it was intentional and not a harmful bug.  
  However, the tool flagged it since best practice typically avoids global state in production code.

---

## 3. How would you integrate static analysis tools into your actual software development workflow?

- **Local Development:**  
  Run Pylint, Flake8, and Bandit pre-commit to catch issues early.

- **CI Integration:**
  - Add these tools in CI pipelines (GitHub Actions / GitLab CI)
  - Fail builds on severe security issues or critical warnings
  - Generate reports automatically for team review

- **Automation:**
  - Use pre-commit hooks (`pre-commit` framework)
  - Auto-format tools like Black + isort for consistent style

---

## 4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?

- **Improved readability:**  
  Clearer naming, consistent formatting, and docstrings made the code easier to understand.

- **More secure:**  
  Removing `eval()` and replacing bare `except:` prevented dangerous behavior and silent failures.

- **More robust:**  
  Input validation and safer file operations reduced the risk of runtime errors and corrupted data.

- **Maintainable:**  
  Cleaner structure and better error handling improved long-term maintainability and debugging.

Overall, the code became more professional, reliable, and aligned with industry standards.
