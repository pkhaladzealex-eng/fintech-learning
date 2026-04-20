# Day 13: Reflections on Days 10-12

### 1. What SQL does for payment testing
For me, SQL is like a **"truth checker."** In payment testing, the website (UI) might say the payment is successful, but I need to be sure. I use SQL to look inside the database and check if the amount, currency, and status are correct. It helps me verify that the data is not lost or changed during the transaction.

### 2. How Python connects to database
Python uses a library (like `sqlite3`) to talk to the database—it acts like a **bridge**. I learned that Python needs a **"cursor"** (it's like a worker or librarian) to run SQL commands. Python can automate the work: it can create tables, insert many rows of data at once, and then calculate totals or find errors much faster than a human.

### 3. One thing I'm confused about
I am still a bit surprised and confused about the **"connection chain."** I understand how Python talks to SQL, but I'm still thinking about how everything works together in real-time. For example, how exactly the database "knows" at the same second when a user clicks a button in a different app or on Stripe. It feels like magic, and I want to understand this connection better.