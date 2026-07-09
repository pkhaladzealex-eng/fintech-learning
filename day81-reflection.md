# Day 81 Reflection: WebDriverWait vs time.sleep

### 1. What Confused Me Most
Days 62-79 introduced Selenium, and at first, I kept using `time.sleep(5)` whenever the automation broke because an element wasn't found yet. It felt simple, but it made my tests extremely slow and unstable. Understanding `WebDriverWait` (Explicit Waits) was the hardest part for me.

### 2. Looking Back at My Code
In my earlier tasks, I used hardcoded sleep times. Later, I refactored it using `WebDriverWait` inside `selenium_utils.py`:
```python
wait = WebDriverWait(driver, 10)
username_field = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
cat << 'EOF' >> README.md



---



### Day 81: Personal reflection on explicit waits versus hardcoded sleep times.

- [Day 81 Reflection Document](./day81-reflection.md) 

