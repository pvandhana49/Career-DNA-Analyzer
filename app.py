import streamlit as st
import PyPDF2
import io
import plotly.graph_objects as go
import plotly.express as px
from langdetect import detect
from deep_translator import GoogleTranslator
from skill_extractor import extract_skills
from career_matcher import match_careers
from roadmap_generator import generate_roadmap
import datetime
import random

st.set_page_config(
    page_title="AI Career DNA Analyzer",
    page_icon="🧬",
    layout="wide"
)

st.markdown("""
<style>
    /* Aurora animated background */
    .stApp {
        background: #050510;
        background-image:
            radial-gradient(ellipse at 20% 50%, rgba(120,40,200,0.15) 0%, transparent 50%),
            radial-gradient(ellipse at 80% 20%, rgba(0,255,178,0.1) 0%, transparent 50%),
            radial-gradient(ellipse at 50% 80%, rgba(0,180,216,0.1) 0%, transparent 50%),
            radial-gradient(ellipse at 90% 90%, rgba(255,100,100,0.08) 0%, transparent 40%);
    }
    .stApp::before {
        content: '';
        position: fixed;
        top: -50%; left: -50%;
        width: 200%; height: 200%;
        background:
            radial-gradient(circle at 30% 40%, rgba(0,255,178,0.04) 0%, transparent 30%),
            radial-gradient(circle at 70% 60%, rgba(167,139,250,0.04) 0%, transparent 30%),
            radial-gradient(circle at 50% 20%, rgba(0,180,216,0.04) 0%, transparent 25%);
        animation: aurora 15s ease-in-out infinite alternate;
        pointer-events: none;
        z-index: 0;
    }
    .stApp::after {
        content: '';
        position: fixed;
        inset: 0;
        background-image:
            linear-gradient(rgba(0,255,178,0.02) 1px, transparent 1px),
            linear-gradient(90deg, rgba(0,255,178,0.02) 1px, transparent 1px);
        background-size: 50px 50px;
        pointer-events: none;
        z-index: 0;
    }
    @keyframes aurora {
        0% { transform: translate(0%, 0%) rotate(0deg); }
        33% { transform: translate(3%, 3%) rotate(2deg); }
        66% { transform: translate(-3%, 2%) rotate(-2deg); }
        100% { transform: translate(2%, -3%) rotate(1deg); }
    }
    .main-header {
        text-align: center;
        padding: 30px;
        background: linear-gradient(135deg, rgba(0,255,178,0.1), rgba(167,139,250,0.1));
        border-radius: 20px;
        border: 1px solid rgba(0,255,178,0.3);
        margin-bottom: 20px;
        position: relative;
        z-index: 1;
    }
    .career-card {
        background: linear-gradient(135deg, rgba(26,26,46,0.9), rgba(22,33,62,0.9));
        border: 1px solid #00FFB2;
        border-radius: 15px;
        padding: 20px;
        margin: 10px 0;
    }
    .skill-badge {
        display: inline-block;
        padding: 5px 14px;
        margin: 4px;
        border-radius: 20px;
        background: linear-gradient(135deg, #00FFB2, #00B4D8);
        color: #000;
        font-weight: bold;
        font-size: 13px;
    }
    .stButton > button {
        background: linear-gradient(135deg, #00FFB2, #00B4D8) !important;
        color: #000 !important;
        font-weight: bold !important;
        border-radius: 10px !important;
        border: none !important;
        transition: all 0.3s ease !important;
    }
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 5px 20px rgba(0,255,178,0.4) !important;
    }
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #050510, #0f0c29, #1a0a2e) !important;
        border-right: 1px solid rgba(0,255,178,0.2) !important;
    }
    div[data-testid="stExpander"] {
        background: rgba(5,5,16,0.8) !important;
        border: 1px solid rgba(0,255,178,0.2) !important;
        border-radius: 12px !important;
    }
    div[data-testid="metric-container"] {
        background: linear-gradient(135deg, rgba(5,5,16,0.9), rgba(48,43,99,0.9)) !important;
        border: 1px solid rgba(0,180,216,0.4) !important;
        border-radius: 12px !important;
        padding: 15px !important;
    }
    .stProgress > div > div {
        background: linear-gradient(90deg, #00FFB2, #00B4D8) !important;
    }
    .stTextArea textarea {
        background: rgba(5,5,16,0.8) !important;
        border: 1px solid rgba(0,255,178,0.2) !important;
        color: #E2E8F0 !important;
        border-radius: 8px !important;
    }
    .stSelectSlider {
        color: #00FFB2 !important;
    }
    button[data-baseweb="tab"][aria-selected="true"] {
        color: #00FFB2 !important;
        border-bottom: 2px solid #00FFB2 !important;
    }
</style>
""", unsafe_allow_html=True)

def translate_text(text, target_lang):
    if target_lang == "en":
        return text
    try:
        return GoogleTranslator(source="en", target=target_lang).translate(str(text))
    except:
        return text

def get_grade(score):
    if score >= 80:
        return "A", "🟢 Job Ready!", "#00FFB2"
    elif score >= 60:
        return "B", "🟡 Almost There!", "#FFD700"
    elif score >= 40:
        return "C", "🟠 Good Start!", "#FFA500"
    else:
        return "D", "🔴 Keep Learning!", "#FF6B6B"

def get_badge(completed_count):
    if completed_count >= 10:
        return "🏆 Master Learner"
    elif completed_count >= 5:
        return "🥇 Advanced Learner"
    elif completed_count >= 3:
        return "🥈 Intermediate Learner"
    elif completed_count >= 1:
        return "🥉 Beginner Learner"
    else:
        return "🎯 Ready to Start"

QUOTES = [
    "💡 'The expert in anything was once a beginner.'",
    "🔥 'Code is like humor. When you have to explain it, its bad.' — Cory House",
    "🚀 'First, solve the problem. Then, write the code.'",
    "💪 'The only way to learn a new language is by writing programs.' — Dennis Ritchie",
    "🌟 'Every expert was once a beginner. Start today!'",
    "🎯 'Your limitation — it is only your imagination.'",
    "📚 'Study while others are sleeping.'",
    "🏆 'Push yourself, because no one else is going to do it for you.'",
    "✨ 'Dream big. Start small. Act now.'",
    "🔑 'The secret of getting ahead is getting started.' — Mark Twain",
]

RESOURCE_LINKS = {
    "freeCodeCamp Python (YouTube)": "https://www.youtube.com/watch?v=rfscVS0vtbw",
    "CS50P Harvard (Free)": "https://cs50.harvard.edu/python/",
    "Python.org Tutorial": "https://docs.python.org/3/tutorial/",
    "Andrew Ng ML Coursera (Free Audit)": "https://www.coursera.org/learn/machine-learning",
    "Kaggle ML Course (Free)": "https://www.kaggle.com/learn/intro-to-machine-learning",
    "fast.ai (Free)": "https://www.fast.ai/",
    "deeplearning.ai Specialization": "https://www.deeplearning.ai/",
    "3Blue1Brown (YouTube)": "https://www.youtube.com/c/3blue1brown",
    "HuggingFace Course (Free)": "https://huggingface.co/learn/nlp-course/",
    "Stanford CS224N (YouTube)": "https://www.youtube.com/playlist?list=PLoROMvodv4rOSH4v6133s9LFPRHjEmbmJ",
    "javascript.info (Free)": "https://javascript.info/",
    "freeCodeCamp JS (Free)": "https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/",
    "JavaScript30 (Free)": "https://javascript30.com/",
    "react.dev Official Docs (Free)": "https://react.dev/",
    "freeCodeCamp React (YouTube)": "https://www.youtube.com/watch?v=bMknfKXIFA8",
    "SQLZoo (Free)": "https://sqlzoo.net/",
    "Mode Analytics SQL (Free)": "https://mode.com/sql-tutorial/",
    "LeetCode SQL": "https://leetcode.com/problemset/database/",
    "TechWorld with Nana (YouTube)": "https://www.youtube.com/c/TechWorldwithNana",
    "Docker Official Docs": "https://docs.docker.com/",
    "Play with Docker (Free)": "https://labs.play-with-docker.com/",
    "AWS Free Tier": "https://aws.amazon.com/free/",
    "freeCodeCamp AWS (YouTube)": "https://www.youtube.com/watch?v=3hLmDS179YE",
    "learngitbranching.js.org (Free)": "https://learngitbranching.js.org/",
    "Traversy Media Git (YouTube)": "https://www.youtube.com/watch?v=SWYqp7iY_Tc",
    "TryHackMe (Free)": "https://tryhackme.com/",
    "PortSwigger Academy (Free)": "https://portswigger.net/web-security",
    "flutter.dev Official (Free)": "https://flutter.dev/docs",
    "freeCodeCamp Flutter (YouTube)": "https://www.youtube.com/watch?v=VPvVD8t02U8",
    "Patrick Collins (YouTube - Free)": "https://www.youtube.com/c/PatrickCollins",
    "Kaggle Data Analysis (Free)": "https://www.kaggle.com/learn/pandas",
    "StatQuest (YouTube - Best)": "https://www.youtube.com/c/joshstarmer",
    "Khan Academy Stats (Free)": "https://www.khanacademy.org/math/statistics-probability",
    "Programming with Mosh Java (YouTube)": "https://www.youtube.com/watch?v=eIrMbAQSU34",
    "Krish Naik ML Playlist (YouTube - Free)": "https://www.youtube.com/watch?v=7uwa9aPbBRU",
    "Kaggle NLP (Free)": "https://www.kaggle.com/learn/natural-language-processing",
    "Amigoscode (YouTube)": "https://www.youtube.com/c/amigoscode",
    "TCM Security (YouTube)": "https://www.youtube.com/c/TCMSecurityAcademy",
}

SKILL_POPULARITY = {
    "Python": 95, "Machine Learning": 88, "React": 85, "JavaScript": 90,
    "SQL": 82, "Docker": 78, "AWS": 80, "Deep Learning": 75,
    "NLP": 70, "Node.js": 72, "Flutter": 65, "Kubernetes": 68,
    "Java": 75, "TypeScript": 73, "Git": 88, "Data Analysis": 80,
}

EXPLANATIONS = {
    "Python": """**What is Python? Simply Explained!**

Imagine telling a robot to make tea in plain English — that is Python!

**Real Life Analogy:** Python is like a universal remote. Simple buttons, powerful actions!

**Key Points:**
- Uses indentation instead of brackets
- Used in AI, Web, Data Science, Automation
- print("Hello") literally prints Hello on screen
- Libraries like Pandas, NumPy make it super powerful

**Example:** name = "Van" then print("Hello " + name) gives Hello Van!

**Remember:** Python = Simple English + Powerful Results!""",

    "Machine Learning": """**What is Machine Learning? Simply Explained!**

Show a child 1000 dog pictures — now they recognize any dog. ML does the same with data!

**Real Life Analogy:** ML is like training a pet. Show examples, reward correct behavior, it learns!

**Key Points:**
- Supervised Learning = Learning with answers
- Unsupervised Learning = Finding patterns alone
- Model = The brain that learned from data
- Training = Teaching the model with examples

**Remember:** ML = Teaching computers using examples instead of rules!""",

    "Deep Learning": """**What is Deep Learning? Simply Explained!**

Your brain has layers — eyes see, brain processes, you understand. Deep Learning copies this!

**Real Life Analogy:** Like an onion — multiple layers, each learning something deeper!

**Key Points:**
- Neural Network = Many layers of math operations
- Layer 1 learns edges, Layer 2 learns shapes, Layer 3 learns faces
- Needs lots of data and computing power
- Used in image recognition, speech, language

**Remember:** Deep Learning = Multiple layers of learning, like your brain!""",

    "NLP": """**What is NLP? Simply Explained!**

When you talk to Siri and it understands you — that is NLP!

**Real Life Analogy:** NLP is a universal translator between human language and computers!

**Key Points:**
- Tokenization = Breaking sentence into words
- Sentiment Analysis = Understanding if text is positive or negative
- BERT and GPT = Powerful NLP models
- Used in Gmail, Google Translate, Spam filters

**Remember:** NLP = Teaching computers to read and understand human language!""",

    "SQL": """**What is SQL? Simply Explained!**

Imagine a huge Excel sheet with millions of rows. SQL is how you ask questions to that sheet!

**Real Life Analogy:** SQL is like asking a librarian for specific books with exact conditions!

**Key Points:**
- SELECT = Choose what you want to see
- WHERE = Filter the results
- JOIN = Combine two tables
- GROUP BY = Group similar things together

**Example:** SELECT name FROM students WHERE marks > 90 means show names of students who scored above 90!

**Remember:** SQL = A language to ask questions to databases!""",

    "Data Analysis": """**What is Data Analysis? Simply Explained!**

You have 10000 student marks. Data Analysis helps find who topped, what is the average, which subject is hardest!

**Real Life Analogy:** Data Analysis is like being a detective — look at clues, find patterns, tell a story!

**Key Points:**
- EDA = Exploring data to understand it first
- Pandas = Main tool for data manipulation
- Visualization = Converting numbers to charts
- Correlation = Finding which things are related

**Process:** Collect, Clean, Explore, Find Insights, Communicate

**Remember:** Data Analysis = Finding hidden stories inside numbers!""",

    "Statistics": """**What is Statistics? Simply Explained!**

When you say students score 75% on average — you are doing statistics!

**Real Life Analogy:** Statistics is like weather forecasting — look at past patterns to predict future!

**Key Points:**
- Mean = Average value
- Median = Middle value not affected by extremes
- Standard Deviation = How spread out data is
- P-value less than 0.05 = Result is significant

**Examples:** Cricket average = Mean runs. Normal Distribution = Bell curve!

**Remember:** Statistics = Using math to understand patterns and make decisions!""",

    "JavaScript": """**What is JavaScript? Simply Explained!**

HTML builds the house. CSS paints it. JavaScript makes it ALIVE!

**Real Life Analogy:** HTML = Skeleton, CSS = Clothes, JavaScript = Muscles and brain of a website!

**Key Points:**
- Variables: let name = "Van"
- Functions make reusable code blocks
- DOM manipulation changes what you see on page
- Async handles fetching data without freezing page

**Real Examples:** Instagram likes without page refresh, Form validation, Countdown timers — all JavaScript!

**Remember:** JavaScript = The language that makes websites interactive!""",

    "React": """**What is React? Simply Explained!**

Building websites normally is like cement — hard to change. React is like LEGO — build pieces, combine easily!

**Real Life Analogy:** React Components are LEGO blocks. Build Button block, Card block, combine to make any website!

**Key Points:**
- Component = Reusable piece of UI
- Props = Data passed to component
- State = Data that can change and update UI
- useState = Hook to create and update state

**Remember:** React = Build websites with reusable LEGO-like components!""",

    "Docker": """**What is Docker? Simply Explained!**

Have you heard "it works on my computer but not yours"? Docker solves this forever!

**Real Life Analogy:** Docker is like a lunchbox. Pack everything your food needs in one box. Works anywhere!

**Key Points:**
- Image = Blueprint of your application
- Container = Running instance of image
- Dockerfile = Instructions to build your image
- docker run = Starts a container

**Remember:** Docker = Package your app with everything it needs, run anywhere!""",

    "Git": """**What is Git? Simply Explained!**

Saving files as essay_v1, essay_v2, essay_FINAL? Git organizes all this automatically with full history!

**Real Life Analogy:** Git is like a time machine for your code. Go back to any point in history!

**Key Points:**
- git init = Start tracking a project
- git add = Stage your changes
- git commit = Save a snapshot with message
- git push = Upload to GitHub
- git branch = Work on feature without breaking main code

**Workflow:** Make changes, git add, git commit, git push!

**Remember:** Git = A save system for your code with full history!""",

    "AWS": """**What is AWS? Simply Explained!**

Instead of buying expensive servers, rent them from Amazon for a few rupees per hour — that is AWS!

**Real Life Analogy:** AWS is like renting a house. Need more rooms? Rent more. Pay only for what you use!

**Key Points:**
- EC2 = Rented virtual computer in cloud
- S3 = Google Drive for developers
- Lambda = Run code without managing server
- RDS = Managed database service

**Real Examples:** Netflix, Airbnb, LinkedIn all run on AWS!

**Remember:** AWS = Rent computing power instead of buying hardware!""",

    "Java": """**What is Java? Simply Explained!**

Java powers banks, Android apps and enterprise systems worldwide!

**Real Life Analogy:** Java is like English in programming — everywhere, and knowing it opens many doors!

**Key Points:**
- Write Once Run Anywhere — runs on any device with JVM
- OOP = Everything is an Object like real world
- Strongly typed = Must declare variable types
- Spring Boot = Framework for building web APIs

**Real Examples:** Android apps, Banking systems, LinkedIn backend all use Java!

**Remember:** Java = Powerful, reliable, runs everywhere!""",

    "Flutter": """**What is Flutter? Simply Explained!**

Write code once, get apps for Android AND iPhone at the same time!

**Real Life Analogy:** Flutter is like a universal key — one key opens multiple doors!

**Key Points:**
- Widget = Everything in Flutter is a widget
- Dart = The programming language Flutter uses
- StatefulWidget = Widgets that can change and update
- Hot Reload = See changes instantly without restarting

**Real Examples:** Google Pay, Alibaba, BMW all built with Flutter!

**Remember:** Flutter = One code, runs on Android + iOS + Web!""",

    "Cybersecurity": """**What is Cybersecurity? Simply Explained!**

Everything is online — your bank, photos, messages. Cybersecurity is the lock protecting all of this!

**Real Life Analogy:** Cybersecurity is like being a security guard for the digital world!

**Key Points:**
- CIA Triad = Confidentiality, Integrity, Availability
- Encryption = Converting data to unreadable format
- Firewall = Digital security guard checking traffic
- Ethical Hacking = Hacking legally to find vulnerabilities first

**Real Examples:** Bank OTP, HTTPS on websites, Antivirus — all cybersecurity!

**Remember:** Cybersecurity = Protecting digital assets from unauthorized access!""",

    "Blockchain": """**What is Blockchain? Simply Explained!**

A notebook that thousands of people have copies of. When you write something, everyone's copy updates. Nobody can secretly change one copy!

**Real Life Analogy:** Blockchain is like a Google Doc everyone can see but nobody can secretly edit!

**Key Points:**
- Block = A container of transactions
- Chain = Blocks linked using cryptography
- Decentralized = No single person controls it
- Smart Contract = Code that runs automatically when conditions are met

**Real Examples:** Bitcoin, NFTs, Voting systems on blockchain!

**Remember:** Blockchain = A shared tamper-proof record book for the digital world!""",
}

QUIZ_QUESTIONS = {
    "Python": [
        ("What does 'def' keyword do in Python?", ["Defines a function", "Defines a variable", "Imports a module", "Creates a class"], 0),
        ("Which library is used for data manipulation?", ["NumPy", "Pandas", "Matplotlib", "Requests"], 1),
        ("What is a list comprehension?", ["A way to create lists in one line", "A type of loop", "A function", "A class method"], 0),
        ("What does len() do?", ["Returns length", "Returns last element", "Loops through list", "Deletes element"], 0),
        ("What is a lambda function?", ["A named function", "An anonymous one-line function", "A recursive function", "A class"], 1),
        ("What does 'self' refer to in a class?", ["The parent class", "The current instance", "A global variable", "The module"], 1),
        ("Which method adds an item to a list?", ["add()", "insert()", "append()", "push()"], 2),
        ("What is pip used for?", ["Running Python files", "Installing packages", "Debugging code", "Writing tests"], 1),
        ("What does a dictionary store?", ["Only values", "Key-value pairs", "Only keys", "Lists only"], 1),
        ("What keyword is used for exception handling?", ["catch", "try", "error", "handle"], 1),
    ],
    "Machine Learning": [
        ("What is overfitting?", ["Model performs well on training but poorly on test", "Model performs well on both", "Model has too few parameters", "Model trains too slowly"], 0),
        ("Which algorithm is used for classification?", ["Linear Regression", "Logistic Regression", "K-Means", "PCA"], 1),
        ("What is cross-validation?", ["Testing on training data", "Splitting data multiple ways to evaluate model", "A type of neural network", "A feature selection method"], 1),
        ("What does K-Means do?", ["Classification", "Regression", "Clustering", "Dimensionality reduction"], 2),
        ("What is a confusion matrix?", ["A confusing matrix", "A table showing prediction vs actual results", "A type of neural network", "A loss function"], 1),
        ("What is precision?", ["True positives divided by all positives predicted", "True positives divided by all actual positives", "Accuracy metric", "Loss function"], 0),
        ("What is the purpose of train-test split?", ["To make training faster", "To evaluate model on unseen data", "To reduce overfitting only", "To increase accuracy"], 1),
        ("Which is an ensemble method?", ["SVM", "Random Forest", "Linear Regression", "KNN"], 1),
        ("What does feature scaling do?", ["Removes features", "Normalizes feature ranges", "Adds new features", "Selects best features"], 1),
        ("What is gradient descent?", ["A type of neural network", "An optimization algorithm to minimize loss", "A data preprocessing step", "A validation technique"], 1),
    ],
    "Deep Learning": [
        ("What is a neural network inspired by?", ["Computer circuits", "Human brain neurons", "Mathematical equations", "Database tables"], 1),
        ("What does CNN stand for?", ["Computer Neural Network", "Convolutional Neural Network", "Coded Neural Node", "Central Neural Network"], 1),
        ("What is backpropagation?", ["Forward pass through network", "Algorithm to update weights using gradients", "A type of activation function", "A regularization method"], 1),
        ("What does ReLU activation do?", ["Outputs values between 0 and 1", "Outputs max(0, x)", "Outputs -1 or 1", "Outputs probability"], 1),
        ("What is a dropout layer?", ["Removes neurons permanently", "Randomly disables neurons during training to prevent overfitting", "Adds new neurons", "A type of pooling"], 1),
        ("What is transfer learning?", ["Learning from scratch", "Using pretrained model weights for new tasks", "Transferring data between models", "A type of optimizer"], 1),
        ("What does LSTM solve?", ["Vanishing gradient problem in sequences", "Image classification", "Text generation only", "Clustering"], 0),
        ("What is batch normalization?", ["Normalizing input data", "Normalizing layer activations to speed up training", "A type of regularization", "A loss function"], 1),
        ("What is a GAN?", ["A type of CNN", "Generative Adversarial Network two networks competing", "A recurrent network", "An attention mechanism"], 1),
        ("What does the encoder do in transformers?", ["Generates output", "Processes input into embeddings", "Translates text", "Classifies images"], 1),
    ],
    "NLP": [
        ("What does NLP stand for?", ["Natural Language Processing", "Neural Learning Program", "Network Language Protocol", "None"], 0),
        ("Which model revolutionized NLP?", ["CNN", "RNN", "BERT Transformer", "Decision Tree"], 2),
        ("What is tokenization?", ["Splitting text into words or subwords", "Removing stop words", "Converting text to numbers", "Stemming words"], 0),
        ("What is TF-IDF?", ["Term Frequency-Inverse Document Frequency", "Text Format Image Detection", "Token Frequency Index", "None"], 0),
        ("What is word embedding?", ["Encoding words as dense vectors", "Removing words from text", "Counting word frequency", "Splitting sentences"], 0),
        ("What does BERT stand for?", ["Bidirectional Encoder Representations from Transformers", "Basic Encoding Recurrent Transformer", "Binary Encoder Result Transformer", "None"], 0),
        ("What is sentiment analysis?", ["Translating text", "Determining positive negative or neutral opinion in text", "Summarizing text", "Generating text"], 1),
        ("What is named entity recognition?", ["Naming variables", "Identifying names places organizations in text", "Classifying sentences", "Translating text"], 1),
        ("What is attention mechanism?", ["Focusing on specific parts of input while processing", "A type of pooling", "A regularization method", "A data augmentation technique"], 0),
        ("What is a language model?", ["A grammar checker", "A model that predicts next word given context", "A translation model", "A sentiment classifier"], 1),
    ],
    "SQL": [
        ("What does SELECT * do?", ["Selects all columns", "Deletes all rows", "Updates all records", "Creates a table"], 0),
        ("Which JOIN returns all rows from both tables?", ["INNER JOIN", "LEFT JOIN", "FULL OUTER JOIN", "CROSS JOIN"], 2),
        ("What does GROUP BY do?", ["Sorts data", "Groups rows with same values", "Filters rows", "Joins tables"], 1),
        ("What is a PRIMARY KEY?", ["Any column", "A unique identifier for each row", "A foreign reference", "An index"], 1),
        ("What does HAVING do?", ["Filters rows before grouping", "Filters groups after GROUP BY", "Joins tables", "Sorts results"], 1),
        ("What is a subquery?", ["A query inside another query", "A saved query", "A view", "A stored procedure"], 0),
        ("What does COUNT(*) return?", ["Sum of values", "Number of rows", "Average value", "Maximum value"], 1),
        ("What is normalization in databases?", ["Sorting data", "Organizing data to reduce redundancy", "Encrypting data", "Backing up data"], 1),
        ("What does DISTINCT do?", ["Removes duplicates", "Counts rows", "Sorts data", "Filters nulls"], 0),
        ("What is an index in SQL?", ["A type of join", "A data structure to speed up queries", "A constraint", "A view"], 1),
    ],
    "Data Analysis": [
        ("Which Python library is best for data analysis?", ["NumPy", "Pandas", "Matplotlib", "Scikit-learn"], 1),
        ("What does EDA stand for?", ["Exploratory Data Analysis", "Extended Data Algorithm", "External Data Access", "Encoded Data Array"], 0),
        ("Which function shows basic statistics in Pandas?", ["df.info()", "df.describe()", "df.head()", "df.tail()"], 1),
        ("What is a DataFrame?", ["A list of lists", "A 2D labeled data structure like a table", "A dictionary", "A numpy array"], 1),
        ("What does df.dropna() do?", ["Drops columns", "Removes rows with missing values", "Fills missing values", "Renames columns"], 1),
        ("What does correlation measure?", ["Causation between variables", "Strength of linear relationship between variables", "Average of variables", "Distribution of data"], 1),
        ("What is an outlier?", ["A common value", "A data point far from others", "A missing value", "A duplicate row"], 1),
        ("What does groupby() do in Pandas?", ["Sorts data", "Groups data by column values", "Merges DataFrames", "Filters rows"], 1),
        ("What is data wrangling?", ["Visualizing data", "Cleaning and transforming raw data", "Modeling data", "Storing data"], 1),
        ("What does merge() do in Pandas?", ["Splits DataFrame", "Combines two DataFrames based on a key", "Filters rows", "Sorts data"], 1),
    ],
    "Statistics": [
        ("What does the mean represent?", ["Most frequent value", "Middle value", "Average value", "Spread of data"], 2),
        ("What is a p-value less than 0.05?", ["Statistically insignificant", "Statistically significant", "Normal distribution", "Null hypothesis"], 1),
        ("Which measures the spread of data?", ["Mean", "Median", "Standard Deviation", "Mode"], 2),
        ("What is the normal distribution shape?", ["Skewed left", "Skewed right", "Bell curve", "Uniform"], 2),
        ("What is hypothesis testing?", ["Proving a theory", "Testing if results happened by chance", "Calculating mean", "Visualizing data"], 1),
        ("What is variance?", ["Average of data", "Square of standard deviation", "Middle value", "Most frequent value"], 1),
        ("What is a confidence interval?", ["A range of values likely to contain the true parameter", "A single estimate", "A probability value", "A test statistic"], 0),
        ("What does correlation of 1 mean?", ["No correlation", "Perfect negative correlation", "Perfect positive correlation", "Weak correlation"], 2),
        ("What is the median?", ["Average value", "Most frequent value", "Middle value when sorted", "Largest value"], 2),
        ("What is Bayes theorem used for?", ["Calculating mean", "Updating probability based on new evidence", "Finding standard deviation", "Hypothesis testing"], 1),
    ],
    "JavaScript": [
        ("Which keyword declares a constant in JS?", ["var", "let", "const", "def"], 2),
        ("What does DOM stand for?", ["Document Object Model", "Data Object Management", "Direct Output Module", "Dynamic Object Method"], 0),
        ("What is a Promise in JS?", ["A variable", "An object representing future completion of async operation", "A loop", "A class"], 1),
        ("What does async/await do?", ["Makes code run faster", "Handles asynchronous code more cleanly", "Creates a new thread", "Imports modules"], 1),
        ("What is the difference between == and ===?", ["No difference", "=== checks type and value", "== checks type too", "=== is assignment"], 1),
        ("What is closure in JavaScript?", ["A function that remembers its outer scope variables", "A loop that closes", "An error handler", "A class method"], 0),
        ("What does JSON stand for?", ["JavaScript Object Notation", "JavaScript Online Node", "Java Scripted Object Name", "None"], 0),
        ("What is an arrow function?", ["A function with arrow syntax and no own this", "A named function", "A recursive function", "A generator"], 0),
        ("What does map() do to an array?", ["Filters elements", "Transforms each element and returns new array", "Reduces to single value", "Sorts elements"], 1),
        ("What is event bubbling?", ["Creating events", "Event propagating from child to parent elements", "Event propagating from parent to child", "Stopping events"], 1),
    ],
    "React": [
        ("What is JSX?", ["JavaScript XML HTML in JS", "A CSS framework", "A database", "A Python library"], 0),
        ("Which hook manages state in React?", ["useEffect", "useState", "useRef", "useContext"], 1),
        ("What is a component in React?", ["A CSS class", "A reusable UI building block", "A database model", "A routing method"], 1),
        ("What are props?", ["State variables", "Data passed from parent to child component", "Event handlers", "CSS styles"], 1),
        ("What does useEffect do?", ["Manages state", "Handles side effects like API calls", "Creates components", "Manages routing"], 1),
        ("What is the virtual DOM?", ["The real browser DOM", "A lightweight copy of DOM for efficient updates", "A CSS framework", "A database"], 1),
        ("What is React Router used for?", ["State management", "Navigation between pages", "API calls", "Styling"], 1),
        ("What does key prop do in lists?", ["Styles elements", "Helps React identify which items changed", "Passes data", "Creates events"], 1),
        ("What is Context API?", ["A routing library", "A way to share state without prop drilling", "A testing framework", "A CSS solution"], 1),
        ("What is a controlled component?", ["A component with no state", "A component where form data is controlled by React state", "A styled component", "A HOC"], 1),
    ],
    "Docker": [
        ("What is a Docker container?", ["A virtual machine", "A lightweight isolated environment", "A database", "A programming language"], 1),
        ("What file defines a Docker image?", ["docker-compose.yml", "Dockerfile", "requirements.txt", "config.json"], 1),
        ("What does docker pull do?", ["Uploads image", "Downloads image from registry", "Runs container", "Builds image"], 1),
        ("What is Docker Hub?", ["A local registry", "A public registry for Docker images", "A container orchestration tool", "A monitoring tool"], 1),
        ("What does docker-compose do?", ["Builds a single container", "Manages multi-container applications", "Monitors containers", "Pushes images"], 1),
        ("What is a Docker volume?", ["A container", "Persistent storage for containers", "A network", "An image layer"], 1),
        ("What does docker ps show?", ["Images", "Running containers", "Networks", "Volumes"], 1),
        ("What is the difference between image and container?", ["They are same", "Image is blueprint container is running instance", "Container is blueprint image is running", "None"], 1),
        ("What does EXPOSE do in Dockerfile?", ["Opens port on host", "Documents which port the container listens on", "Starts a service", "Installs packages"], 1),
        ("What does docker stop do?", ["Deletes container", "Gracefully stops running container", "Pauses container", "Restarts container"], 1),
    ],
    "Git": [
        ("What does git commit do?", ["Saves changes to remote", "Saves changes locally with message", "Deletes changes", "Creates a branch"], 1),
        ("Which command creates a new branch?", ["git branch name", "git new name", "git create name", "git make name"], 0),
        ("What does git pull do?", ["Pushes local changes", "Fetches and merges remote changes", "Creates a branch", "Deletes a branch"], 1),
        ("What is a merge conflict?", ["When two branches have same changes", "When two branches have conflicting changes in same file", "When branch is deleted", "When commit fails"], 1),
        ("What does git stash do?", ["Deletes changes", "Temporarily saves uncommitted changes", "Commits changes", "Pushes changes"], 1),
        ("What does .gitignore do?", ["Ignores git commands", "Specifies files git should not track", "Deletes files", "Renames files"], 1),
        ("What is a remote repository?", ["Local copy", "Repository hosted on server like GitHub", "A branch", "A tag"], 1),
        ("What does git clone do?", ["Creates a branch", "Copies a remote repository locally", "Merges branches", "Pushes changes"], 1),
        ("What is HEAD in git?", ["First commit", "Current branch pointer", "Last commit", "Remote branch"], 1),
        ("What does git rebase do?", ["Deletes commits", "Moves branch to a new base commit", "Merges branches", "Creates a tag"], 1),
    ],
    "AWS": [
        ("What does S3 stand for?", ["Simple Storage Service", "Secure Server System", "Scalable Software Solution", "Smart Storage Stack"], 0),
        ("What is EC2?", ["A database service", "A virtual server service", "A storage bucket", "A DNS service"], 1),
        ("What is IAM used for?", ["Monitoring", "Managing users and permissions", "Storage", "Networking"], 1),
        ("What is a VPC?", ["Virtual Private Cloud an isolated network", "Virtual PC", "Video Processing Center", "None"], 0),
        ("What is Lambda?", ["A machine learning service", "Serverless compute runs code without managing servers", "A database", "A CDN"], 1),
        ("What is CloudFront?", ["A database service", "A Content Delivery Network", "A compute service", "A monitoring tool"], 1),
        ("What is RDS?", ["Remote Desktop Service", "Relational Database Service", "Resource Distribution System", "None"], 1),
        ("What does Auto Scaling do?", ["Manually scales servers", "Automatically adjusts capacity based on demand", "Monitors applications", "Manages DNS"], 1),
        ("What is an S3 bucket?", ["A virtual server", "A container for storing objects and files in S3", "A database table", "A network"], 1),
        ("What is CloudWatch?", ["A time service", "Monitoring and observability service", "A storage service", "A compute service"], 1),
    ],
    "Java": [
        ("Java is which type of language?", ["Interpreted only", "Compiled only", "Both compiled and interpreted", "Neither"], 2),
        ("What is JVM?", ["Java Virtual Machine", "Java Variable Manager", "Java Version Module", "None"], 0),
        ("What is OOP?", ["Object Oriented Programming", "Only One Program", "Operational Output Processing", "None"], 0),
        ("What is inheritance in Java?", ["A class copying another class", "A class extending another class to reuse code", "A method calling itself", "An interface"], 1),
        ("What is an interface in Java?", ["A concrete class", "A blueprint with abstract methods only", "A data structure", "A loop"], 1),
        ("What does static mean in Java?", ["Belongs to instance", "Belongs to class not instance", "Cannot be changed", "Is abstract"], 1),
        ("What is exception handling?", ["Ignoring errors", "Catching and handling runtime errors gracefully", "Logging errors", "Testing code"], 1),
        ("What is ArrayList vs Array?", ["Same thing", "ArrayList is dynamic size Array is fixed", "Array is dynamic", "ArrayList is faster always"], 1),
        ("What is a constructor?", ["A method that returns value", "A special method called when object is created", "A static method", "An interface method"], 1),
        ("What does final keyword do?", ["Makes variable changeable", "Makes variable method or class unchangeable", "Makes method abstract", "Creates a loop"], 1),
    ],
    "Flutter": [
        ("What language does Flutter use?", ["Java", "Kotlin", "Dart", "Swift"], 2),
        ("What is a Widget in Flutter?", ["A database model", "A UI building block", "A network request", "A file system"], 1),
        ("What is StatefulWidget?", ["A widget with no state", "A widget that can rebuild when state changes", "A layout widget", "An animation widget"], 1),
        ("What is setState() used for?", ["Making API calls", "Updating UI by changing state", "Navigation", "Styling"], 1),
        ("What is pubspec.yaml?", ["A Dart file", "Flutter project configuration and dependencies file", "A layout file", "A test file"], 1),
        ("What does Navigator.push() do?", ["Pops a screen", "Navigates to a new screen", "Updates state", "Makes API call"], 1),
        ("What is a Future in Dart?", ["A past value", "A value that will be available in the future async", "A widget", "A package"], 1),
        ("What is hot reload in Flutter?", ["Restarting the app", "Updating UI instantly without losing state", "Building the app", "Testing the app"], 1),
        ("What is the difference between Row and Column?", ["Same", "Row is horizontal Column is vertical", "Column is horizontal Row is vertical", "Both are vertical"], 1),
        ("What is Provider in Flutter?", ["A network library", "A state management solution", "A database", "A testing framework"], 1),
    ],
    "Cybersecurity": [
        ("What does CIA stand for in security?", ["Central Intelligence Agency", "Confidentiality Integrity Availability", "Computer Internet Access", "None"], 1),
        ("What is phishing?", ["A fishing game", "Tricking users to reveal sensitive info", "A type of malware", "Network scanning"], 1),
        ("What is a firewall?", ["A type of virus", "A network security system that monitors traffic", "An encryption method", "A password manager"], 1),
        ("What is SQL injection?", ["A database backup", "Inserting malicious SQL code into queries", "A type of firewall", "An encryption algorithm"], 1),
        ("What is encryption?", ["Deleting data", "Converting data to unreadable format", "Copying data", "Compressing data"], 1),
        ("What does VPN do?", ["Speeds up internet", "Creates encrypted tunnel for secure communication", "Blocks websites", "Manages passwords"], 1),
        ("What is two-factor authentication?", ["Using two passwords", "Verifying identity with two different methods", "Having two accounts", "Logging in twice"], 1),
        ("What is a zero-day vulnerability?", ["A known bug", "An unknown vulnerability exploited before patch exists", "A patched bug", "A test vulnerability"], 1),
        ("What does HTTPS provide?", ["Faster loading", "Encrypted communication between browser and server", "Better SEO", "Free hosting"], 1),
        ("What is social engineering?", ["Building social media", "Manipulating people to reveal confidential information", "Network engineering", "Software development"], 1),
    ],
    "Blockchain": [
        ("What is a blockchain?", ["A type of database", "A distributed ledger of immutable records", "A programming language", "A cloud service"], 1),
        ("What is a smart contract?", ["A legal document", "Self-executing code on the blockchain", "A type of token", "A wallet"], 1),
        ("What is cryptocurrency?", ["Physical money", "Digital currency secured by cryptography on blockchain", "A bank account", "A stock"], 1),
        ("What makes blockchain immutable?", ["Encryption only", "Each block contains hash of previous block", "Central authority", "Passwords"], 1),
        ("What is a consensus mechanism?", ["A voting system", "Method for all nodes to agree on blockchain state", "A smart contract", "An encryption method"], 1),
        ("What is Ethereum?", ["Only a cryptocurrency", "A blockchain platform for smart contracts and DApps", "A wallet", "A mining tool"], 1),
        ("What is gas in Ethereum?", ["Fuel for cars", "Fee paid for executing transactions on Ethereum", "A cryptocurrency", "A smart contract"], 1),
        ("What is DeFi?", ["Defined Finance", "Decentralized Finance financial services on blockchain", "Default Finance", "Digital Files"], 1),
        ("What is an NFT?", ["Non-Fungible Token unique digital asset on blockchain", "New Financial Token", "Normal File Transfer", "None"], 0),
        ("What is a crypto wallet?", ["A physical wallet", "Software to store and manage private keys", "A bank account", "An exchange"], 1),
    ],
}

# ── Session State ──
defaults = {
    "analyzed": False, "completed_topics": {}, "notes": {},
    "study_streak": 0, "last_study_date": None, "skills_found": [],
    "career_results": [], "roadmap_data": {}, "detected_lang": "en",
    "hours_studied_today": 0, "quiz_score": {}, "timer_running": False
}
for key, val in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = val

today = datetime.date.today()
if st.session_state.last_study_date != today:
    if st.session_state.last_study_date == today - datetime.timedelta(days=1):
        st.session_state.study_streak += 1
    elif st.session_state.last_study_date is None:
        st.session_state.study_streak = 1
    st.session_state.last_study_date = today

# ── SIDEBAR ──
with st.sidebar:
    st.markdown("## 🧬 Career DNA")
    st.markdown("---")
    st.markdown("### 💡 Daily Motivation")
    st.info(random.choice(QUOTES))
    st.markdown("---")

    streak = st.session_state.study_streak
    st.markdown("### 🔥 Study Streak")
    st.markdown(f"""
    <div style='text-align:center;padding:15px;background:rgba(0,255,178,0.1);
    border-radius:12px;border:1px solid rgba(0,255,178,0.3);'>
        <h1 style='color:#00FFB2;margin:0;'>{streak} 🔥</h1>
        <p style='color:#94A3B8;margin:0;'>Day Streak!</p>
    </div>""", unsafe_allow_html=True)
    if streak >= 7:
        st.success("🏆 Week Warrior! Amazing!")
    elif streak >= 3:
        st.success("🔥 On fire! Keep going!")
    else:
        st.info("💪 Keep coming back daily!")
    st.markdown("---")

    completed_count = sum(1 for v in st.session_state.completed_topics.values() if v)
    badge = get_badge(completed_count)
    st.markdown("### 🏆 Your Badge")
    st.markdown(f"""
    <div style='text-align:center;padding:12px;background:rgba(167,139,250,0.1);
    border-radius:12px;border:1px solid rgba(167,139,250,0.3);'>
        <h3 style='color:#A78BFA;margin:0;'>{badge}</h3>
        <p style='color:#94A3B8;margin:0;'>{completed_count} topics completed</p>
    </div>""", unsafe_allow_html=True)
    st.markdown("---")

    st.markdown("### ⏱️ Pomodoro Timer")
    st.markdown("25 min study | 5 min break")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("▶️ Start", key="start_timer"):
            st.session_state.timer_running = True
    with c2:
        if st.button("⏹️ Stop", key="stop_timer"):
            st.session_state.timer_running = False
    if st.session_state.timer_running:
        st.success("🔥 Timer running! Stay focused!")
    else:
        st.info("⏱️ Click Start to begin!")
    st.markdown("---")

    st.markdown("### ⏰ Daily Study Goal")
    goal = st.select_slider("Set your goal:", options=["1 hr","2 hrs","3 hrs","4 hrs","5 hrs","6 hrs"], value="2 hrs")
    goal_hours = int(goal.split()[0])
    goal_progress = min(st.session_state.hours_studied_today / goal_hours, 1.0)
    st.progress(goal_progress)
    st.caption(f"Today: {st.session_state.hours_studied_today}h / {goal_hours}h")
    if goal_progress >= 1.0:
        st.success("🎉 Daily goal achieved!")
    else:
        st.caption(f"⏰ {goal_hours - st.session_state.hours_studied_today}h remaining")
    st.markdown("---")

    st.markdown("### 📅 Today")
    st.markdown(f"**{today.strftime('%B %d, %Y')}**")
    st.markdown(f"*{today.strftime('%A')}*")
    st.markdown("---")

    st.markdown("### ✅ Skills Covered")
    for cat in ["🤖 AI & ML","🌐 Web Dev","📱 Mobile","☁️ Cloud","🔐 Security","📊 Data","🔗 Blockchain","🎮 Games"]:
        st.markdown(cat)

# ── MAIN HEADER ──
st.markdown("""
<div class='main-header'>
    <h1 style='color:#00FFB2;font-size:2.8em;margin:0;
    text-shadow:0 0 30px rgba(0,255,178,0.5);'>🧬 AI Career DNA Analyzer</h1>
    <p style='color:#A78BFA;font-size:1.1em;margin-top:8px;'>
    Discover your perfect career path — powered by AI</p>
    <p style='color:#64748B;font-size:0.9em;'>
    🌍 100+ Languages | 50+ Skills | Day-by-Day Roadmaps | AI Quiz | Notes</p>
</div>
""", unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(["🔍 Analyze","📊 Dashboard","📝 My Notes","📈 Insights"])

# ════════════════════════════════════════
# TAB 1: ANALYZE
# ════════════════════════════════════════
with tab1:
    st.markdown("### 🔍 Analyze Your Skills")
    input_method = st.radio("Choose input method:", ["📝 Type your skills","📄 Upload PDF resume"], horizontal=True)
    resume_text = ""

    if input_method == "📝 Type your skills":
        resume_text = st.text_area(
            "Describe your skills (any language!)", height=150,
            placeholder="English: I know Python, Machine Learning, React, SQL, Docker...\nதமிழ்: எனக்கு Python, Machine Learning தெரியும்\nHindi: मुझे Python, React आती है\n\nYou can mention: Python, Java, React, SQL, Docker, AWS, Flutter, Machine Learning, NLP, Cybersecurity, Blockchain, Git, JavaScript, Statistics, Data Analysis..."
        )
    else:
        uploaded_file = st.file_uploader("Upload your resume (PDF)", type="pdf")
        if uploaded_file is not None:
            pdf_reader = PyPDF2.PdfReader(io.BytesIO(uploaded_file.read()))
            for page in pdf_reader.pages:
                resume_text += page.extract_text()
            st.success("✅ PDF uploaded!")
            with st.expander("View extracted text"):
                st.text(resume_text[:500] + "..." if len(resume_text) > 500 else resume_text)

    if st.button("🔍 Analyze My Career DNA", type="primary", use_container_width=True):
        if not resume_text.strip():
            st.warning("Please enter your skills first!")
        else:
            try:
                detected_lang = detect(resume_text)
                if detected_lang != "en":
                    st.info(f"🌍 Detected: **{detected_lang.upper()}** — Translating...")
                    resume_text_en = GoogleTranslator(source="auto", target="en").translate(resume_text)
                else:
                    detected_lang = "en"
                    resume_text_en = resume_text
            except:
                detected_lang = "en"
                resume_text_en = resume_text

            st.session_state.detected_lang = detected_lang
            with st.spinner("🔬 Extracting skills..."):
                skills_found = extract_skills(resume_text_en)

            if not skills_found:
                st.error("No skills found! Try: Python, React, SQL, Java, Docker, Machine Learning, Flutter...")
            else:
                st.session_state.skills_found = skills_found
                with st.spinner("🎯 Matching careers..."):
                    career_results = match_careers(skills_found)
                st.session_state.career_results = career_results
                top_career = career_results[0]
                roadmap_data = generate_roadmap(skills_found, top_career["required_skills"])
                st.session_state.roadmap_data = roadmap_data
                st.session_state.analyzed = True
                st.success(f"✅ Found **{len(skills_found)} skills**!")
                badges_html = "".join([f'<span class="skill-badge">{s}</span>' for s in skills_found])
                st.markdown(badges_html, unsafe_allow_html=True)
                st.markdown("---")
                st.info("👉 Go to **📊 Dashboard** tab to see your full results!")

# ════════════════════════════════════════
# TAB 2: DASHBOARD
# ════════════════════════════════════════
with tab2:
    if not st.session_state.analyzed:
        st.markdown("""
        <div style='text-align:center;padding:80px;
        background:rgba(0,255,178,0.03);
        border-radius:20px;border:1px dashed rgba(0,255,178,0.2);'>
            <h2 style='color:#64748B;'>🔍 Analyze your skills first!</h2>
            <p style='color:#475569;'>Go to the Analyze tab and enter your skills.</p>
        </div>""", unsafe_allow_html=True)
    else:
        skills_found = st.session_state.skills_found
        career_results = st.session_state.career_results
        roadmap_data = st.session_state.roadmap_data
        detected_lang = st.session_state.detected_lang
        top_career = career_results[0]
        readiness_score = min(int(top_career["match"]), 100)
        grade, grade_text, grade_color = get_grade(readiness_score)

        st.markdown("### 🏆 Your Career DNA Results")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("🏆 Readiness Score", f"{readiness_score}%", grade_text)
        with col2:
            st.metric("🎯 Best Match", top_career["career"])
        with col3:
            st.metric("💰 Expected Salary", top_career["avg_salary"])
        with col4:
            st.metric("📊 Skills Found", len(skills_found))

        all_topics = []
        for item in roadmap_data.get("roadmap", []):
            all_topics.append(item["skill"])
            if item.get("detailed"):
                for week in item["detailed"]["weeks"]:
                    for day_idx in range(len(week["days"])):
                        all_topics.append(f"{item['skill']}_w{week['week']}_d{day_idx}")
            else:
                for idx in range(3):
                    all_topics.append(f"{item['skill']}_gen_{idx}")

        completed = sum(1 for t in all_topics if st.session_state.completed_topics.get(t, False))
        total = max(len(all_topics), 1)
        progress = min(completed / total, 1.0)
        st.markdown(f"### 📈 Overall Learning Progress: {int(progress*100)}%")
        st.progress(progress)
        if progress >= 1.0:
            st.balloons()
            st.success("🎉 You completed everything! Amazing work!")

        st.markdown("---")
        st.markdown("### 🎯 Career Match Analysis")
        careers = [r["career"] for r in career_results]
        scores = [r["match"] for r in career_results]
        colors = ["#00FFB2","#4ECDC4","#45B7D1","#96CEB4","#FFEAA7","#FF6B6B","#A78BFA","#F97316","#06B6D4","#84CC16","#EC4899","#8B5CF6"]

        fig = go.Figure(go.Bar(x=scores, y=careers, orientation="h",
            marker_color=colors[:len(careers)],
            text=[f"{s}%" for s in scores], textposition="outside"))
        fig.update_layout(title="Career Match Scores", xaxis_title="Match %",
            height=420, paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)", font=dict(color="white"))
        st.plotly_chart(fig, use_container_width=True)

        cols = st.columns(3)
        for i, result in enumerate(career_results[:3]):
            border = ["#00FFB2","#A78BFA","#00B4D8"][i]
            with cols[i]:
                st.markdown(f"""
                <div style='background:linear-gradient(135deg,rgba(5,5,16,0.95),rgba(48,43,99,0.95));
                border:2px solid {border};border-radius:16px;padding:20px;margin:5px 0;
                box-shadow:0 0 20px {border}22;'>
                    <h3 style='color:{border};margin:0;'>{result["career"]}</h3>
                    <h1 style='color:white;margin:8px 0;'>{result["match"]}%</h1>
                    <p style='color:#94A3B8;font-size:13px;'>{result["description"]}</p>
                    <p style='color:#00FFB2;'>💰 {result["avg_salary"]}</p>
                    <p style='color:#A78BFA;'>📈 {result["demand"]} Demand</p>
                </div>""", unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("### 🎯 Skill Gap Radar")
        required = top_career["required_skills"]
        radar_skills = required[:6]
        have_values = [1 if s in skills_found else 0 for s in radar_skills]
        fig_radar = go.Figure()
        fig_radar.add_trace(go.Scatterpolar(r=have_values, theta=radar_skills,
            fill='toself', name='Your Skills',
            fillcolor='rgba(0,255,178,0.3)', line=dict(color='#00FFB2', width=2)))
        fig_radar.add_trace(go.Scatterpolar(r=[1]*len(radar_skills), theta=radar_skills,
            fill='toself', name='Required Skills',
            fillcolor='rgba(255,107,107,0.15)', line=dict(color='#FF6B6B', width=2)))
        fig_radar.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0,1]), bgcolor="rgba(0,0,0,0)"),
            showlegend=True, paper_bgcolor="rgba(0,0,0,0)",
            font=dict(color="white"), height=420)
        st.plotly_chart(fig_radar, use_container_width=True)

        st.markdown("---")
        st.markdown(f"### 🗺️ Your Personalized Roadmap → {top_career['career']}")

        if roadmap_data.get("already_have"):
            st.success(f"✅ Skills you already have: **{', '.join(roadmap_data['already_have'])}**")

        if roadmap_data.get("roadmap"):
            col1, col2 = st.columns(2)
            with col1:
                st.info(f"⏱️ Total Learning Time: ~{roadmap_data['total_hours']} hours")
            with col2:
                st.info(f"📚 Skills to Learn: {len(roadmap_data['missing_skills'])}")

            skill_names = [item["skill"] for item in roadmap_data["roadmap"]]
            skill_hours = [item["hours"] for item in roadmap_data["roadmap"]]
            fig_hours = px.bar(x=skill_names, y=skill_hours,
                title="⏱️ Learning Time Per Skill (Hours)",
                color=skill_hours, color_continuous_scale="teal")
            fig_hours.update_layout(paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)", font=dict(color="white"))
            st.plotly_chart(fig_hours, use_container_width=True)

            st.markdown("### 📅 Week-by-Week Learning Plan")
            st.caption("Click each skill to expand — check off topics as you complete them!")

            for item in roadmap_data["roadmap"]:
                skill_key = item["skill"]
                skill_done = st.session_state.completed_topics.get(skill_key, False)
                done_icon = "✅" if skill_done else "📚"

                with st.expander(f"{done_icon} **{item['skill']}** — ⏱️ {item['hours']} hours"):

                    col1, col2 = st.columns([1, 2])
                    with col1:
                        btn_label = "↩️ Mark Incomplete" if skill_done else "✅ Mark Skill Done"
                        if st.button(btn_label, key=f"skill_done_{skill_key}",
                            type="secondary" if skill_done else "primary"):
                            st.session_state.completed_topics[skill_key] = not skill_done
                            if not skill_done:
                                st.balloons()
                            st.rerun()
                    with col2:
                        if skill_done:
                            st.success("🏆 Skill Completed! Amazing work!")
                        else:
                            st.warning("⬅️ Click when you finish this entire skill!")

                    st.markdown("---")
                    st.markdown("**🔗 Free Learning Resources:**")
                    for course in item["courses"]:
                        link = RESOURCE_LINKS.get(course, "")
                        if link:
                            st.markdown(f"- 🔗 [{course}]({link})")
                        else:
                            st.markdown(f"- 📚 {course}")

                    if item.get("detailed"):
                        st.markdown("---")
                        st.markdown("**📅 Check off each topic as you complete it:**")
                        for week in item["detailed"]["weeks"]:
                            week_num = week["week"]
                            week_title = week["title"]
                            week_key = f"{skill_key}_week_{week_num}"
                            week_done = st.session_state.completed_topics.get(week_key, False)
                            week_icon = "✅" if week_done else "📖"
                            st.markdown(f"#### {week_icon} Week {week_num} — {week_title}")

                            for day_idx, day in enumerate(week["days"]):
                                topic_key = f"{skill_key}_w{week_num}_d{day_idx}"
                                topic_done = st.session_state.completed_topics.get(topic_key, False)
                                checked = st.checkbox(day, value=topic_done, key=f"cb_{topic_key}")
                                if checked != topic_done:
                                    st.session_state.completed_topics[topic_key] = checked
                                    st.rerun()

                            st.markdown("**📚 Resources:**")
                            for resource in week["resources"]:
                                clean = resource.replace("📺 ","").replace("📚 ","").replace("🎯 ","")
                                link = RESOURCE_LINKS.get(clean, "")
                                if link:
                                    st.markdown(f"  - 🔗 [{clean}]({link})")
                                else:
                                    st.markdown(f"  - {resource}")

                            w_btn = "↩️ Undo Week" if week_done else f"✅ Week {week_num} Done"
                            if st.button(w_btn, key=f"wbtn_{week_key}",
                                type="secondary" if week_done else "primary"):
                                st.session_state.completed_topics[week_key] = not week_done
                                for d_idx in range(len(week["days"])):
                                    t_key = f"{skill_key}_w{week_num}_d{d_idx}"
                                    st.session_state.completed_topics[t_key] = not week_done
                                if not week_done:
                                    st.success(f"🎉 Week {week_num} completed!")
                                st.rerun()
                            st.markdown("---")
                    else:
                        st.markdown("---")
                        st.markdown("**📅 General Learning Path — Check off as you complete:**")
                        general = [
                            "Week 1-2: Learn fundamentals and basics",
                            "Week 3-4: Build projects and practice",
                            "Week 5-6: Advanced topics and deployment"
                        ]
                        for idx, topic in enumerate(general):
                            t_key = f"{skill_key}_gen_{idx}"
                            t_done = st.session_state.completed_topics.get(t_key, False)
                            checked = st.checkbox(topic, value=t_done, key=f"gen_{t_key}")
                            if checked != t_done:
                                st.session_state.completed_topics[t_key] = checked
                                st.rerun()

                    # ── Explain Simply ──
                    st.markdown("---")
                    explain_key = f"explain_state_{skill_key}"
                    if explain_key not in st.session_state:
                        st.session_state[explain_key] = False

                    col1, col2 = st.columns([1, 2])
                    with col1:
                        e_label = "✅ Hide Explanation" if st.session_state[explain_key] else "💬 Explain Simply"
                        if st.button(e_label, key=f"explain_{skill_key}",
                            type="secondary" if st.session_state[explain_key] else "primary"):
                            st.session_state[explain_key] = not st.session_state[explain_key]
                            st.rerun()
                    with col2:
                        if st.session_state[explain_key]:
                            st.success("✅ Explanation is showing below!")
                        else:
                            st.info("👆 Click to see a simple friendly explanation!")

                    if st.session_state[explain_key]:
                        explanation = EXPLANATIONS.get(skill_key,
                            f"**{skill_key}** is an important tech skill. Start with basics, build projects, and practice daily!")
                        st.markdown(f"""
                        <div style='background:linear-gradient(135deg,rgba(0,255,178,0.08),rgba(167,139,250,0.08));
                        border:1px solid #00FFB2;border-radius:12px;padding:20px;margin:10px 0;
                        color:#E2E8F0;line-height:1.8;white-space:pre-wrap;'>
                        {explanation}
                        </div>""", unsafe_allow_html=True)

                    # ── Quiz ──
                    st.markdown("---")
                    st.markdown("**🤖 Quick Quiz — Test yourself!**")

                    if skill_key in QUIZ_QUESTIONS:
                        for q_idx, (question, options, correct) in enumerate(QUIZ_QUESTIONS[skill_key]):
                            st.markdown(f"**Q{q_idx+1}: {question}**")
                            answer = st.radio("", options,
                                key=f"quiz_{skill_key}_q{q_idx}",
                                index=None,
                                label_visibility="collapsed")
                            if answer is not None:
                                if options.index(answer) == correct:
                                    st.success("✅ Correct! Well done!")
                                else:
                                    st.error(f"❌ Wrong! Correct answer: **{options[correct]}**")
                            st.markdown("")
                    else:
                        st.info("💡 Quiz coming soon for this skill!")

                    # ── Notes ──
                    st.markdown("---")
                    st.markdown("**📝 My Notes:**")
                    note_key = f"note_{skill_key}"
                    current_note = st.session_state.notes.get(note_key, "")
                    new_note = st.text_area(
                        f"Write your notes for {skill_key}:",
                        value=current_note, key=f"ta_{skill_key}",
                        placeholder=f"Write what you learned about {skill_key}... key concepts, doubts, code snippets...",
                        height=100)

                    col1, col2, col3 = st.columns(3)
                    with col1:
                        if st.button(f"💾 Save Note", key=f"save_{skill_key}", type="primary"):
                            st.session_state.notes[note_key] = new_note
                            st.success("✅ Note saved!")
                    with col2:
                        if new_note:
                            st.download_button("📥 Download", data=new_note,
                                file_name=f"{skill_key}_notes.txt",
                                mime="text/plain", key=f"dl_{skill_key}")
                    with col3:
                        if st.button("🗑️ Clear", key=f"clear_{skill_key}"):
                            st.session_state.notes[note_key] = ""
                            st.rerun()
        else:
            st.balloons()
            st.success("🎉 You already have all required skills for this career!")

# ════════════════════════════════════════
# TAB 3: MY NOTES
# ════════════════════════════════════════
with tab3:
    st.markdown("### 📝 My Study Notes")
    has_notes = any(v and v.strip() for v in st.session_state.notes.values())

    if not has_notes:
        st.markdown("""
        <div style='text-align:center;padding:60px;
        background:rgba(0,255,178,0.03);border-radius:20px;
        border:1px dashed rgba(0,255,178,0.2);'>
            <h2 style='color:#64748B;'>📝 No notes yet!</h2>
            <p style='color:#475569;'>Start learning and add notes in the Dashboard tab.</p>
        </div>""", unsafe_allow_html=True)
    else:
        all_notes = ""
        for key, note in st.session_state.notes.items():
            if note and note.strip():
                skill_name = key.replace("note_","")
                all_notes += f"\n{'='*40}\n{skill_name.upper()}\n{'='*40}\n{note}\n"

        st.download_button("📥 Download All Notes as TXT", data=all_notes,
            file_name=f"career_dna_notes_{today}.txt",
            mime="text/plain", use_container_width=True)
        st.markdown("---")

        for key, note in st.session_state.notes.items():
            if note and note.strip():
                skill_name = key.replace("note_","")
                with st.expander(f"📝 {skill_name}"):
                    st.text_area("", value=note, key=f"view_{key}", height=120)
                    st.download_button("📥 Download", data=note,
                        file_name=f"{skill_name}_notes.txt", key=f"ndl_{key}")

    st.markdown("---")
    st.markdown("### 🏆 Completed Skills")
    done_skills = [k for k, v in st.session_state.completed_topics.items()
                   if v and "_week_" not in k and "_w" not in k and "_gen_" not in k]
    if done_skills:
        for s in done_skills:
            st.success(f"✅ {s}")
    else:
        st.info("No skills fully completed yet. Start learning!")

# ════════════════════════════════════════
# TAB 4: INSIGHTS
# ════════════════════════════════════════
with tab4:
    st.markdown("### 📈 Tech Skills Insights")
    st.markdown("#### 🔥 Most In-Demand Skills in Job Market")
    st.caption("🟢 Green bars = Skills YOU already have!")

    pop_skills = list(SKILL_POPULARITY.keys())
    pop_scores = list(SKILL_POPULARITY.values())

    fig_pop = go.Figure(go.Bar(
        x=pop_scores, y=pop_skills, orientation="h",
        marker_color=["#00FFB2" if s in st.session_state.skills_found else "#1e293b" for s in pop_skills],
        text=[f"{s}%" for s in pop_scores], textposition="outside"))
    fig_pop.update_layout(
        title="Skill Demand in Job Market",
        xaxis_title="Demand Score", height=500,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="white"))
    st.plotly_chart(fig_pop, use_container_width=True)

    st.markdown("---")
    st.markdown("### 📤 Share Your Career DNA")
    if st.session_state.analyzed:
        top = st.session_state.career_results[0]
        share_text = f"""🧬 My AI Career DNA Analysis Results:
🎯 Best Career Match: {top['career']}
📊 Match Score: {top['match']}%
💰 Expected Salary: {top['avg_salary']}
✅ Skills I have: {', '.join(st.session_state.skills_found)}
🚀 Analyzed with AI Career DNA Analyzer!"""
        st.text_area("Copy and share this:", share_text, height=150)
        st.download_button("📥 Download My Career DNA Report",
            data=share_text,
            file_name=f"career_dna_report_{today}.txt",
            mime="text/plain", use_container_width=True)
    else:
        st.info("Analyze your skills first to see your results here!")