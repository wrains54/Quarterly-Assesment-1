import sqlite3

# Connect to the SQLite database (it will be created if it doesn't exist)
connection = sqlite3.connect('questions_answers.db')
cursor = connection.cursor()

# Create tables for each category
cursor.execute('''CREATE TABLE IF NOT EXISTS adv_finance_questions (
  id INTEGER PRIMARY KEY,
  question TEXT NOT NULL,
  answer TEXT NOT NULL
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS database_questions (
  id INTEGER PRIMARY KEY,
  question TEXT NOT NULL,
  answer TEXT NOT NULL
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS python_questions (
  id INTEGER PRIMARY KEY,
  question TEXT NOT NULL,
  answer TEXT NOT NULL
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS computer_forensics_questions (
  id INTEGER PRIMARY KEY,
  question TEXT NOT NULL,
  answer TEXT NOT NULL
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS financial_modeling_questions (
  id INTEGER PRIMARY KEY,
  question TEXT NOT NULL,
  answer TEXT NOT NULL
)''')

# Sample data for each category
adv_finance_data = [
    ("What is the Capital Asset Pricing Model?", "A model that describes the relationship between systematic risk and expected return for assets."),
    ("What is arbitrage?", "The simultaneous purchase and sale of an asset to profit from a difference in the price."),
    ("What is diversification in finance?", "A risk management strategy that mixes a wide variety of investments within a portfolio."),
    ("What is the efficient market hypothesis?", "The theory that all available information is already reflected in stock prices."),
    ("What is a derivative in finance?", "A financial security with a value that is reliant upon or derived from an underlying asset or group of assets."),
    ("What is a hedge fund?", "An investment fund that pools capital from accredited individuals or institutional investors and invests in a variety of assets."),
    ("What is the difference between a bond and a stock?", "Bonds are debt investments while stocks are equity."),
    ("What is a mutual fund?", "An investment program funded by shareholders that trades in diversified holdings and is professionally managed."),
    ("What is market capitalization?", "The total market value of a company's outstanding shares."),
    ("What is ROI?", "Return on Investment, a measure used to evaluate the efficiency of an investment."),
]

database_data = [
    ("What is a primary key in a database?", "A unique identifier for each record in a table."),
    ("What is SQL?", "Structured Query Language, used for managing data in a relational database."),
    ("What is a foreign key?", "A key used to link two tables together."),
    ("What is normalization in databases?", "The process of organizing data to reduce redundancy and improve data integrity."),
    ("What is a database index?", "A data structure that improves the speed of data retrieval operations on a database table."),
    ("What is a query in database context?", "A request for data or information from a database table or combination of tables."),
    ("What are transactions in a database?", "A sequence of database operations that are treated as a single logical unit."),
    ("What is a relational database?", "A type of database that stores and provides access to data points that are related to one another."),
    ("What is data redundancy?", "The existence of duplicate data in a database."),
    ("What is a NoSQL database?", "A database that provides a mechanism for storage and retrieval of data that is modeled in means other than the tabular relations used in relational databases."),
]

python_data = [
    ("What is a list comprehension in Python?", "A concise way to create lists."),
    ("What does the 'self' keyword in Python do?", "Refers to the instance of the class itself."),
    ("What is a lambda function?", "An anonymous function expressed as a single statement."),
    ("What is inheritance in Python?", "A mechanism in which one class inherits the attributes and methods of another."),
    ("What is polymorphism in Python?", "The ability of different types to be accessed through the same interface."),
    ("What is encapsulation in Python?", "The bundling of data with the methods that operate on that data."),
    ("What is a module in Python?", "A file containing Python definitions and statements."),
    ("What is the difference between a shallow copy and a deep copy?", "Shallow copy is a bit-wise copy of an object. Deep copy is a copy of object as well as the objects to which it refers."),
    ("What is a decorator in Python?", "A design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure."),
    ("What are generators in Python?", "A simple way of creating iterators."),
]

computer_forensics_data = [
    ("What is the main goal of computer forensics analysis?", "To examine digital media in a forensically sound manner with the aim of identifying, preserving, recovering, analyzing and presenting facts and opinions about the digital information."),
    ("What is a write blocker?", "A device that allows acquisition of information on a drive without creating the possibility of accidentally damaging the drive contents."),
    ("What is digital evidence?", "Information stored or transmitted in binary form that may be relied on in court."),
    ("What is a disk image in computer forensics?", "A digital copy of the contents of a storage device."),
    ("What is live forensics?", "The analysis of a computer system without shutting it down."),
    ("What is chain of custody?", "A process that tracks the movement of evidence through its collection, safeguarding, and analysis lifecycle."),
    ("What is steganography?", "The practice of hiding messages or information within other non-secret text or data."),
    ("What are the steps involved in a computer forensic investigation?", "Identification, preservation, analysis, and reporting."),
    ("What is a hash value in digital forensics?", "A value used to ensure data integrity, often used to compare two sets of data."),
    ("What is e-discovery?", "The process by which electronic data is sought, located, secured, and searched with the intent of using it as evidence in a legal case."),
]

financial_modeling_data = [
    ("What is a financial model?", "A tool (typically built with Excel) to forecast a business's financial performance into the future."),
    ("What is NPV?", "Net Present Value, a measure of the profitability of an investment."),
    ("What is a DCF model?", "Discounted Cash Flow, a valuation method used to estimate the value of an investment."),
    ("What is an LBO model?", "Leveraged Buyout, a financial model used to evaluate the acquisition of a company."),
    ("What is the difference between WACC and IRR?", "WACC is the average rate of return a company expects to pay its investors; IRR is the rate of return that makes the net present value (NPV) of all cash flows equal to zero."),
    ("What is a Monte Carlo simulation in financial modeling?", "A technique used to understand the impact of risk and uncertainty in financial, project management, cost, and other forecasting models."),
    ("What is sensitivity analysis in financial modeling?", "A technique used to determine how different values of an independent variable affect a particular dependent variable."),
    ("What are financial ratios?", "Metrics used to evaluate the financial condition or performance of a business entity."),
    ("What is a balance sheet in financial modeling?", "A statement of the assets, liabilities, and capital of a business at a particular point in time."),
    ("What is EBITDA?", "Earnings Before Interest, Taxes, Depreciation, and Amortization, a measure of a company's operational performance."),
]

# Insert data into each table
for question, answer in adv_finance_data:
    cursor.execute("INSERT INTO adv_finance_questions (question, answer) VALUES (?, ?)", (question, answer))

for question, answer in database_data:
    cursor.execute("INSERT INTO database_questions (question, answer) VALUES (?, ?)", (question, answer))

for question, answer in python_data:
    cursor.execute("INSERT INTO python_questions (question, answer) VALUES (?, ?)", (question, answer))

for question, answer in computer_forensics_data:
    cursor.execute("INSERT INTO computer_forensics_questions (question, answer) VALUES (?, ?)", (question, answer))

for question, answer in financial_modeling_data:
    cursor.execute("INSERT INTO financial_modeling_questions (question, answer) VALUES (?, ?)", (question, answer))

# Commit changes and close the connection
connection.commit()
connection.close()