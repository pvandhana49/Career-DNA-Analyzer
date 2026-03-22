SKILLS_LIST = [
    # AI & ML
    "Python", "Machine Learning", "Deep Learning", "NLP", "Computer Vision",
    "Reinforcement Learning", "MLOps", "TensorFlow", "PyTorch", "Scikit-learn",
    # Web Development
    "HTML", "CSS", "JavaScript", "TypeScript", "React", "Angular", "Vue",
    "Node.js", "Django", "Flask", "Next.js", "REST API", "GraphQL",
    # Mobile
    "Android", "iOS", "Flutter", "React Native", "Kotlin", "Swift",
    # Cloud & DevOps
    "AWS", "Azure", "GCP", "Docker", "Kubernetes", "Linux", "Git", "CI/CD",
    # Data
    "SQL", "Data Analysis", "Data Engineering", "Power BI", "Tableau",
    "Apache Spark", "Statistics",
    # Cybersecurity
    "Cybersecurity", "Ethical Hacking", "Network Security", "Cryptography",
    # Game Development
    "Unity", "Unreal Engine", "C#", "Game Design",
    # Blockchain
    "Blockchain", "Solidity", "Web3",
    # Systems
    "C", "C++", "Java", "Algorithms", "Data Structures", "Operating Systems",
    "Computer Networks",
]

SKILL_SYNONYMS = {
    "Python": ["python", "py", "python3"],
    "Machine Learning": ["machine learning", "ml", "sklearn", "scikit-learn", "random forest", "xgboost", "classification", "regression", "supervised learning"],
    "Deep Learning": ["deep learning", "dl", "neural network", "neural networks", "cnn", "rnn", "lstm", "transformer", "backpropagation"],
    "NLP": ["nlp", "natural language processing", "text mining", "sentiment analysis", "bert", "gpt", "language model", "text classification"],
    "Computer Vision": ["computer vision", "cv", "image processing", "object detection", "opencv", "yolo", "image recognition"],
    "Reinforcement Learning": ["reinforcement learning", "rl", "q-learning", "reward", "agent", "environment"],
    "MLOps": ["mlops", "model deployment", "model serving", "ml pipeline", "airflow", "mlflow"],
    "TensorFlow": ["tensorflow", "tf", "keras"],
    "PyTorch": ["pytorch", "torch"],
    "Scikit-learn": ["scikit-learn", "sklearn"],
    "HTML": ["html", "html5", "markup"],
    "CSS": ["css", "css3", "styling", "tailwind", "bootstrap"],
    "JavaScript": ["javascript", "js", "es6", "es2015"],
    "TypeScript": ["typescript", "ts"],
    "React": ["react", "reactjs", "react.js"],
    "Angular": ["angular", "angularjs"],
    "Vue": ["vue", "vuejs", "vue.js"],
    "Node.js": ["node", "nodejs", "node.js", "express"],
    "Django": ["django"],
    "Flask": ["flask"],
    "Next.js": ["next", "nextjs", "next.js"],
    "REST API": ["rest", "rest api", "restful", "api"],
    "GraphQL": ["graphql"],
    "Android": ["android", "android development"],
    "iOS": ["ios", "iphone", "ipad"],
    "Flutter": ["flutter", "dart"],
    "React Native": ["react native"],
    "Kotlin": ["kotlin"],
    "Swift": ["swift"],
    "AWS": ["aws", "amazon web services", "ec2", "s3", "lambda"],
    "Azure": ["azure", "microsoft azure"],
    "GCP": ["gcp", "google cloud", "google cloud platform"],
    "Docker": ["docker", "container", "containerization"],
    "Kubernetes": ["kubernetes", "k8s"],
    "Linux": ["linux", "ubuntu", "unix", "bash", "shell"],
    "Git": ["git", "github", "gitlab", "version control"],
    "CI/CD": ["ci/cd", "cicd", "continuous integration", "jenkins", "github actions"],
    "SQL": ["sql", "mysql", "postgresql", "sqlite", "database", "queries"],
    "Data Analysis": ["data analysis", "data analytics", "eda", "pandas", "numpy", "data wrangling"],
    "Data Engineering": ["data engineering", "etl", "data pipeline", "airflow", "kafka"],
    "Power BI": ["power bi", "powerbi"],
    "Tableau": ["tableau"],
    "Apache Spark": ["spark", "apache spark", "pyspark"],
    "Statistics": ["statistics", "statistical", "probability", "hypothesis testing", "bayesian"],
    "Cybersecurity": ["cybersecurity", "cyber security", "information security", "infosec"],
    "Ethical Hacking": ["ethical hacking", "penetration testing", "pen testing", "hacking"],
    "Network Security": ["network security", "firewall", "ids", "ips"],
    "Cryptography": ["cryptography", "encryption", "decryption", "rsa", "aes"],
    "Unity": ["unity", "unity3d"],
    "Unreal Engine": ["unreal", "unreal engine", "ue4", "ue5"],
    "C#": ["c#", "csharp", "c sharp"],
    "Game Design": ["game design", "game development", "game dev"],
    "Blockchain": ["blockchain", "distributed ledger"],
    "Solidity": ["solidity"],
    "Web3": ["web3", "defi", "nft", "smart contract"],
    "C": ["c programming", " c language", "c code"],
    "C++": ["c++", "cpp", "c plus plus"],
    "Java": ["java", "spring", "spring boot", "jvm"],
    "Algorithms": ["algorithms", "algorithm", "sorting", "searching", "complexity"],
    "Data Structures": ["data structures", "linked list", "tree", "graph", "stack", "queue", "heap"],
    "Operating Systems": ["operating systems", "os", "process management", "memory management"],
    "Computer Networks": ["computer networks", "networking", "tcp/ip", "dns", "http", "protocols"],
}

CAREER_PATHS = {
    "ML Engineer": {
        "required_skills": ["Python", "Machine Learning", "Deep Learning", "Docker", "MLOps"],
        "description": "Build and deploy machine learning models at scale",
        "avg_salary": "₹12-25 LPA",
        "demand": "Very High"
    },
    "Data Scientist": {
        "required_skills": ["Python", "Statistics", "Data Analysis", "SQL", "Machine Learning"],
        "description": "Extract insights from data to drive business decisions",
        "avg_salary": "₹10-20 LPA",
        "demand": "High"
    },
    "NLP Engineer": {
        "required_skills": ["Python", "NLP", "Deep Learning", "TensorFlow"],
        "description": "Build language understanding systems and chatbots",
        "avg_salary": "₹14-28 LPA",
        "demand": "Very High"
    },
    "Full Stack Developer": {
        "required_skills": ["HTML", "CSS", "JavaScript", "React", "Node.js", "SQL"],
        "description": "Build complete web applications from frontend to backend",
        "avg_salary": "₹8-18 LPA",
        "demand": "Very High"
    },
    "Mobile Developer": {
        "required_skills": ["Flutter", "Dart", "React Native", "Android", "iOS"],
        "description": "Build mobile applications for Android and iOS",
        "avg_salary": "₹8-18 LPA",
        "demand": "High"
    },
    "DevOps Engineer": {
        "required_skills": ["Docker", "Kubernetes", "AWS", "Linux", "CI/CD", "Git"],
        "description": "Automate and optimize software delivery pipelines",
        "avg_salary": "₹10-22 LPA",
        "demand": "Very High"
    },
    "Cybersecurity Engineer": {
        "required_skills": ["Cybersecurity", "Ethical Hacking", "Network Security", "Linux"],
        "description": "Protect systems and networks from cyber threats",
        "avg_salary": "₹8-20 LPA",
        "demand": "High"
    },
    "Data Engineer": {
        "required_skills": ["Python", "SQL", "Apache Spark", "Data Engineering", "AWS"],
        "description": "Build data pipelines and infrastructure",
        "avg_salary": "₹10-22 LPA",
        "demand": "High"
    },
    "Blockchain Developer": {
        "required_skills": ["Blockchain", "Solidity", "Web3", "JavaScript"],
        "description": "Build decentralized applications and smart contracts",
        "avg_salary": "₹12-30 LPA",
        "demand": "Medium"
    },
    "Game Developer": {
        "required_skills": ["Unity", "C#", "Game Design", "C++"],
        "description": "Create video games for multiple platforms",
        "avg_salary": "₹6-15 LPA",
        "demand": "Medium"
    },
    "Computer Vision Engineer": {
        "required_skills": ["Python", "Computer Vision", "Deep Learning", "TensorFlow"],
        "description": "Build systems that can see and understand images and videos",
        "avg_salary": "₹12-25 LPA",
        "demand": "High"
    },
    "Data Analyst": {
        "required_skills": ["SQL", "Data Analysis", "Statistics", "Power BI", "Tableau"],
        "description": "Analyze data and create reports for decision making",
        "avg_salary": "₹5-12 LPA",
        "demand": "High"
    },
}

DETAILED_ROADMAP = {
    "Python": {
        "total_weeks": 4,
        "total_hours": 60,
        "weeks": [
            {
                "week": 1,
                "title": "Python Basics",
                "days": [
                    "Day 1-2: Variables, Data Types, Input/Output",
                    "Day 3-4: Loops (for, while), Conditionals (if/else)",
                    "Day 5-6: Functions, Parameters, Return Values",
                    "Day 7: Mini Project — Simple Calculator"
                ],
                "resources": [
                    "📺 CS50P - Harvard Python Course (YouTube - Free)",
                    "📚 python.org/docs - Official Documentation",
                    "🎯 Practice: HackerRank Python track"
                ]
            },
            {
                "week": 2,
                "title": "Object Oriented Programming",
                "days": [
                    "Day 1-2: Classes, Objects, Constructors",
                    "Day 3-4: Inheritance, Polymorphism",
                    "Day 5-6: File Handling, Exception Handling",
                    "Day 7: Mini Project — Student Management System"
                ],
                "resources": [
                    "📺 Corey Schafer OOP Python (YouTube - Free)",
                    "📚 realpython.com tutorials",
                    "🎯 Practice: LeetCode Easy problems"
                ]
            },
            {
                "week": 3,
                "title": "Python Libraries",
                "days": [
                    "Day 1-2: NumPy - Arrays and Mathematical operations",
                    "Day 3-4: Pandas - DataFrames and Data Manipulation",
                    "Day 5-6: Matplotlib & Seaborn - Data Visualization",
                    "Day 7: Mini Project — Data Analysis on CSV file"
                ],
                "resources": [
                    "📺 Keith Galli Pandas Tutorial (YouTube)",
                    "📚 pandas.pydata.org documentation",
                    "🎯 Practice: Kaggle Python course (Free)"
                ]
            },
            {
                "week": 4,
                "title": "Advanced Python",
                "days": [
                    "Day 1-2: List Comprehensions, Generators, Decorators",
                    "Day 3-4: APIs with requests library",
                    "Day 5-6: Virtual environments, pip, project structure",
                    "Day 7: Final Project — Build a Web Scraper or API client"
                ],
                "resources": [
                    "📺 Tech With Tim Advanced Python (YouTube)",
                    "📚 docs.python-requests.org",
                    "🎯 Build: A weather app using API"
                ]
            }
        ]
    },
    "Machine Learning": {
        "total_weeks": 6,
        "total_hours": 100,
        "weeks": [
            {
                "week": 1,
                "title": "ML Foundations",
                "days": [
                    "Day 1-2: What is ML? Types — Supervised, Unsupervised, Reinforcement",
                    "Day 3-4: Linear Regression — theory and implementation",
                    "Day 5-6: Logistic Regression — classification problems",
                    "Day 7: Mini Project — House Price Predictor"
                ],
                "resources": [
                    "📺 Andrew Ng ML Course (Coursera - Free Audit)",
                    "📺 StatQuest with Josh Starmer (YouTube)",
                    "📚 scikit-learn.org documentation"
                ]
            },
            {
                "week": 2,
                "title": "Core ML Algorithms",
                "days": [
                    "Day 1-2: Decision Trees — how they split data",
                    "Day 3-4: Random Forest — ensemble methods",
                    "Day 5-6: SVM — Support Vector Machines",
                    "Day 7: Mini Project — Titanic Survival Predictor"
                ],
                "resources": [
                    "📺 Krish Naik ML Playlist (YouTube - Free)",
                    "📚 Kaggle ML Course (Free)",
                    "🎯 Practice: Kaggle Titanic competition"
                ]
            },
            {
                "week": 3,
                "title": "Model Evaluation",
                "days": [
                    "Day 1-2: Train/Test split, Cross Validation",
                    "Day 3-4: Accuracy, Precision, Recall, F1 Score",
                    "Day 5-6: Overfitting, Underfitting, Regularization",
                    "Day 7: Mini Project — Spam Email Classifier"
                ],
                "resources": [
                    "📺 sentdex ML tutorials (YouTube)",
                    "📚 mlcourse.ai (Free)",
                    "🎯 Practice: Kaggle intermediate ML"
                ]
            },
            {
                "week": 4,
                "title": "Feature Engineering",
                "days": [
                    "Day 1-2: Handling missing values, outliers",
                    "Day 3-4: Feature scaling — normalization, standardization",
                    "Day 5-6: Feature selection techniques",
                    "Day 7: Mini Project — Customer Churn Predictor"
                ],
                "resources": [
                    "📺 Feature Engineering for ML (Coursera)",
                    "📚 Kaggle Feature Engineering course",
                    "🎯 Practice: Kaggle competitions"
                ]
            },
            {
                "week": 5,
                "title": "Advanced Algorithms",
                "days": [
                    "Day 1-2: K-Means Clustering — unsupervised learning",
                    "Day 3-4: Principal Component Analysis (PCA)",
                    "Day 5-6: XGBoost and Gradient Boosting",
                    "Day 7: Mini Project — Customer Segmentation"
                ],
                "resources": [
                    "📺 codebasics ML playlist (YouTube)",
                    "📚 xgboost.readthedocs.io",
                    "🎯 Practice: Kaggle tabular competitions"
                ]
            },
            {
                "week": 6,
                "title": "ML Projects & Deployment",
                "days": [
                    "Day 1-2: Build end-to-end ML pipeline",
                    "Day 3-4: Save models with pickle/joblib",
                    "Day 5-6: Deploy ML model with Flask/Streamlit",
                    "Day 7: Final Project — End-to-end ML web app"
                ],
                "resources": [
                    "📺 Deploy ML model tutorial (YouTube)",
                    "📚 mlflow.org documentation",
                    "🎯 Build: Deploy your own ML model online"
                ]
            }
        ]
    },
    "Deep Learning": {
        "total_weeks": 6,
        "total_hours": 120,
        "weeks": [
            {
                "week": 1,
                "title": "Neural Network Basics",
                "days": [
                    "Day 1-2: What is a Neural Network? Neurons, Layers",
                    "Day 3-4: Activation Functions — ReLU, Sigmoid, Softmax",
                    "Day 5-6: Forward Propagation & Backpropagation",
                    "Day 7: Mini Project — Build NN from scratch with NumPy"
                ],
                "resources": [
                    "📺 3Blue1Brown Neural Networks (YouTube - Must Watch)",
                    "📺 deeplearning.ai specialization (Coursera)",
                    "📚 neuralnetworksanddeeplearning.com (Free book)"
                ]
            },
            {
                "week": 2,
                "title": "TensorFlow & Keras",
                "days": [
                    "Day 1-2: TensorFlow basics — tensors, operations",
                    "Day 3-4: Building models with Keras Sequential API",
                    "Day 5-6: Training, validation, callbacks",
                    "Day 7: Mini Project — Handwritten digit classifier (MNIST)"
                ],
                "resources": [
                    "📺 TensorFlow official tutorials (tensorflow.org)",
                    "📺 Sentdex TensorFlow (YouTube)",
                    "📚 keras.io documentation"
                ]
            },
            {
                "week": 3,
                "title": "Convolutional Neural Networks",
                "days": [
                    "Day 1-2: Convolution, Pooling, Padding",
                    "Day 3-4: CNN architectures — VGG, ResNet, Inception",
                    "Day 5-6: Transfer Learning — use pretrained models",
                    "Day 7: Mini Project — Cat vs Dog Image Classifier"
                ],
                "resources": [
                    "📺 CS231n Stanford CNN course (YouTube)",
                    "📚 cs231n.github.io notes",
                    "🎯 Practice: Kaggle image classification"
                ]
            },
            {
                "week": 4,
                "title": "Recurrent Neural Networks",
                "days": [
                    "Day 1-2: RNN — sequence data, vanishing gradient",
                    "Day 3-4: LSTM and GRU — long term memory",
                    "Day 5-6: Time series prediction with LSTM",
                    "Day 7: Mini Project — Stock Price Predictor"
                ],
                "resources": [
                    "📺 Andrej Karpathy RNN blog (must read)",
                    "📺 Sequence models deeplearning.ai",
                    "🎯 Practice: Text generation with LSTM"
                ]
            },
            {
                "week": 5,
                "title": "Transformers & Attention",
                "days": [
                    "Day 1-2: Attention mechanism — why it works",
                    "Day 3-4: Transformer architecture — encoder, decoder",
                    "Day 5-6: BERT, GPT — pretrained transformers",
                    "Day 7: Mini Project — Sentiment Analysis with BERT"
                ],
                "resources": [
                    "📺 Attention is All You Need explained (YouTube)",
                    "📚 huggingface.co/course (Free)",
                    "🎯 Practice: HuggingFace tasks"
                ]
            },
            {
                "week": 6,
                "title": "Advanced DL & Projects",
                "days": [
                    "Day 1-2: GANs — Generative Adversarial Networks",
                    "Day 3-4: Autoencoders — dimensionality reduction",
                    "Day 5-6: Model optimization — pruning, quantization",
                    "Day 7: Final Project — Build your own image generator"
                ],
                "resources": [
                    "📺 Ian Goodfellow GAN lecture (YouTube)",
                    "📚 fastai.com course (Free)",
                    "🎯 Build: Deploy DL model on HuggingFace Spaces"
                ]
            }
        ]
    },
    "NLP": {
        "total_weeks": 5,
        "total_hours": 90,
        "weeks": [
            {
                "week": 1,
                "title": "Text Preprocessing",
                "days": [
                    "Day 1-2: Tokenization, Stemming, Lemmatization",
                    "Day 3-4: Stop words, Punctuation removal, Cleaning",
                    "Day 5-6: Regular Expressions for text",
                    "Day 7: Mini Project — Text cleaner pipeline"
                ],
                "resources": [
                    "📺 NLP with Python (YouTube - freeCodeCamp)",
                    "📚 nltk.org documentation",
                    "🎯 Practice: Text preprocessing on real dataset"
                ]
            },
            {
                "week": 2,
                "title": "Text Representation",
                "days": [
                    "Day 1-2: Bag of Words, TF-IDF",
                    "Day 3-4: Word2Vec, GloVe embeddings",
                    "Day 5-6: Sentence embeddings with SBERT",
                    "Day 7: Mini Project — Semantic similarity finder"
                ],
                "resources": [
                    "📺 Word2Vec explained (YouTube)",
                    "📚 gensim.readthedocs.io",
                    "🎯 Practice: Build a document similarity tool"
                ]
            },
            {
                "week": 3,
                "title": "NLP Tasks",
                "days": [
                    "Day 1-2: Sentiment Analysis — classify opinions",
                    "Day 3-4: Named Entity Recognition (NER)",
                    "Day 5-6: Text Classification — spam detection",
                    "Day 7: Mini Project — Movie Review Sentiment Analyzer"
                ],
                "resources": [
                    "📺 Krish Naik NLP playlist (YouTube)",
                    "📚 spacy.io course (Free)",
                    "🎯 Practice: Kaggle NLP competitions"
                ]
            },
            {
                "week": 4,
                "title": "Transformers for NLP",
                "days": [
                    "Day 1-2: BERT — Bidirectional Encoder Representations",
                    "Day 3-4: Fine-tuning BERT for classification",
                    "Day 5-6: GPT models — text generation",
                    "Day 7: Mini Project — Question Answering system"
                ],
                "resources": [
                    "📚 huggingface.co/course (Free — Best NLP resource)",
                    "📺 HuggingFace tutorials (YouTube)",
                    "🎯 Practice: HuggingFace model hub"
                ]
            },
            {
                "week": 5,
                "title": "Advanced NLP & Deployment",
                "days": [
                    "Day 1-2: RAG — Retrieval Augmented Generation",
                    "Day 3-4: Chatbot development with transformers",
                    "Day 5-6: Deploy NLP model with FastAPI",
                    "Day 7: Final Project — Build your own AI chatbot"
                ],
                "resources": [
                    "📺 LangChain tutorials (YouTube)",
                    "📚 langchain.com documentation",
                    "🎯 Build: Deploy chatbot on HuggingFace Spaces"
                ]
            }
        ]
    },
    "SQL": {
        "total_weeks": 3,
        "total_hours": 40,
        "weeks": [
            {
                "week": 1,
                "title": "SQL Basics",
                "days": [
                    "Day 1-2: SELECT, FROM, WHERE, ORDER BY",
                    "Day 3-4: INSERT, UPDATE, DELETE operations",
                    "Day 5-6: Aggregate functions — COUNT, SUM, AVG, MAX, MIN",
                    "Day 7: Mini Project — Query a real sales database"
                ],
                "resources": [
                    "📺 MySQL Tutorial for Beginners (Programming with Mosh)",
                    "📚 sqlzoo.net (Free interactive practice)",
                    "🎯 Practice: Mode Analytics SQL tutorial"
                ]
            },
            {
                "week": 2,
                "title": "Intermediate SQL",
                "days": [
                    "Day 1-2: JOINS — INNER, LEFT, RIGHT, FULL",
                    "Day 3-4: Subqueries and CTEs",
                    "Day 5-6: Window Functions — ROW_NUMBER, RANK, LAG",
                    "Day 7: Mini Project — E-commerce database analysis"
                ],
                "resources": [
                    "📺 SQL Window Functions (YouTube)",
                    "📚 pgexercises.com (PostgreSQL practice)",
                    "🎯 Practice: LeetCode SQL problems"
                ]
            },
            {
                "week": 3,
                "title": "Advanced SQL & Database Design",
                "days": [
                    "Day 1-2: Database normalization — 1NF, 2NF, 3NF",
                    "Day 3-4: Indexes, Query optimization",
                    "Day 5-6: Stored procedures, Triggers, Views",
                    "Day 7: Final Project — Design a hospital database"
                ],
                "resources": [
                    "📺 Database Design course (freeCodeCamp YouTube)",
                    "📚 use-the-index-luke.com",
                    "🎯 Build: Full database with relationships"
                ]
            }
        ]
    },
    "JavaScript": {
        "total_weeks": 5,
        "total_hours": 80,
        "weeks": [
            {
                "week": 1,
                "title": "JavaScript Basics",
                "days": [
                    "Day 1-2: Variables (var, let, const), Data Types",
                    "Day 3-4: Functions, Arrow Functions, Scope",
                    "Day 5-6: Arrays, Objects, Loops",
                    "Day 7: Mini Project — To-Do List app"
                ],
                "resources": [
                    "📺 JavaScript Full Course (freeCodeCamp YouTube)",
                    "📚 javascript.info (Best free resource)",
                    "🎯 Practice: freeCodeCamp JS certification"
                ]
            },
            {
                "week": 2,
                "title": "DOM & Events",
                "days": [
                    "Day 1-2: DOM manipulation — getElementById, querySelector",
                    "Day 3-4: Event listeners, Event bubbling",
                    "Day 5-6: Form validation, Local Storage",
                    "Day 7: Mini Project — Quiz app with score tracking"
                ],
                "resources": [
                    "📺 DOM Manipulation (Traversy Media YouTube)",
                    "📚 MDN Web Docs (developer.mozilla.org)",
                    "🎯 Practice: Build 10 small JS projects"
                ]
            },
            {
                "week": 3,
                "title": "Async JavaScript",
                "days": [
                    "Day 1-2: Callbacks, Promises",
                    "Day 3-4: Async/Await — modern async pattern",
                    "Day 5-6: Fetch API — calling REST APIs",
                    "Day 7: Mini Project — Weather app using API"
                ],
                "resources": [
                    "📺 Async JS (Fireship YouTube)",
                    "📚 javascript.info/async",
                    "🎯 Practice: Build apps with public APIs"
                ]
            },
            {
                "week": 4,
                "title": "Modern JavaScript",
                "days": [
                    "Day 1-2: ES6+ features — destructuring, spread, rest",
                    "Day 3-4: Modules — import/export",
                    "Day 5-6: Error handling, Debugging",
                    "Day 7: Mini Project — Shopping cart app"
                ],
                "resources": [
                    "📺 ES6 Tutorial (Mosh Hamedani YouTube)",
                    "📚 exploringjs.com (Free book)",
                    "🎯 Practice: JavaScript30 challenge (30 projects)"
                ]
            },
            {
                "week": 5,
                "title": "Node.js & Backend",
                "days": [
                    "Day 1-2: Node.js basics — runtime, npm",
                    "Day 3-4: Express.js — building REST APIs",
                    "Day 5-6: Connecting to database with Mongoose",
                    "Day 7: Final Project — Full REST API with CRUD"
                ],
                "resources": [
                    "📺 Node.js Course (Traversy Media YouTube)",
                    "📚 nodejs.org documentation",
                    "🎯 Build: Deploy your API on Render (Free)"
                ]
            }
        ]
    },
    "React": {
        "total_weeks": 4,
        "total_hours": 70,
        "weeks": [
            {
                "week": 1,
                "title": "React Fundamentals",
                "days": [
                    "Day 1-2: What is React? JSX syntax, Components",
                    "Day 3-4: Props — passing data between components",
                    "Day 5-6: State with useState hook",
                    "Day 7: Mini Project — Counter and Color picker app"
                ],
                "resources": [
                    "📚 react.dev (Official React docs — best resource)",
                    "📺 React Course (freeCodeCamp YouTube)",
                    "🎯 Practice: Build small components"
                ]
            },
            {
                "week": 2,
                "title": "React Hooks",
                "days": [
                    "Day 1-2: useEffect — side effects and lifecycle",
                    "Day 3-4: useContext — global state management",
                    "Day 5-6: useRef, useMemo, useCallback",
                    "Day 7: Mini Project — Movie search app with API"
                ],
                "resources": [
                    "📺 React Hooks (Corey Schafer YouTube)",
                    "📚 usehooks.com — custom hooks library",
                    "🎯 Practice: Rebuild Todo app with hooks"
                ]
            },
            {
                "week": 3,
                "title": "React Router & State",
                "days": [
                    "Day 1-2: React Router — navigation between pages",
                    "Day 3-4: Redux — global state management",
                    "Day 5-6: React Query — server state management",
                    "Day 7: Mini Project — Multi-page portfolio website"
                ],
                "resources": [
                    "📺 React Router Tutorial (YouTube)",
                    "📚 redux.js.org documentation",
                    "🎯 Practice: Build e-commerce frontend"
                ]
            },
            {
                "week": 4,
                "title": "Advanced React & Deployment",
                "days": [
                    "Day 1-2: Performance optimization — memo, lazy loading",
                    "Day 3-4: Testing React components with Jest",
                    "Day 5-6: Build and deploy React app",
                    "Day 7: Final Project — Full React web application"
                ],
                "resources": [
                    "📺 React Testing (YouTube)",
                    "📚 vitejs.dev — modern build tool",
                    "🎯 Build: Deploy on Vercel (Free)"
                ]
            }
        ]
    },
    "Docker": {
        "total_weeks": 3,
        "total_hours": 45,
        "weeks": [
            {
                "week": 1,
                "title": "Docker Basics",
                "days": [
                    "Day 1-2: What is Docker? Containers vs VMs",
                    "Day 3-4: Docker images, containers, registries",
                    "Day 5-6: Basic commands — pull, run, stop, remove",
                    "Day 7: Mini Project — Containerize a Python app"
                ],
                "resources": [
                    "📺 Docker Tutorial (TechWorld with Nana YouTube)",
                    "📚 docs.docker.com",
                    "🎯 Practice: Docker labs (play-with-docker.com)"
                ]
            },
            {
                "week": 2,
                "title": "Dockerfiles & Compose",
                "days": [
                    "Day 1-2: Writing Dockerfiles — FROM, RUN, COPY, CMD",
                    "Day 3-4: Multi-stage builds — optimize image size",
                    "Day 5-6: Docker Compose — multi-container apps",
                    "Day 7: Mini Project — Full stack app with Compose"
                ],
                "resources": [
                    "📺 Docker Compose Tutorial (YouTube)",
                    "📚 docs.docker.com/compose",
                    "🎯 Practice: Compose Flask + PostgreSQL app"
                ]
            },
            {
                "week": 3,
                "title": "Docker in Production",
                "days": [
                    "Day 1-2: Docker networking — bridge, host, overlay",
                    "Day 3-4: Docker volumes — persistent data",
                    "Day 5-6: Push images to Docker Hub",
                    "Day 7: Final Project — Deploy containerized app to cloud"
                ],
                "resources": [
                    "📺 Docker in Production (YouTube)",
                    "📚 hub.docker.com",
                    "🎯 Build: Deploy your app with Docker on AWS"
                ]
            }
        ]
    },
    "Data Analysis": {
        "total_weeks": 4,
        "total_hours": 60,
        "weeks": [
            {
                "week": 1,
                "title": "Pandas Basics",
                "days": [
                    "Day 1-2: DataFrames, Series — creating and reading data",
                    "Day 3-4: Selecting, filtering, sorting data",
                    "Day 5-6: Handling missing values, duplicates",
                    "Day 7: Mini Project — Analyze a real CSV dataset"
                ],
                "resources": [
                    "📺 Pandas Tutorial (Keith Galli YouTube)",
                    "📚 pandas.pydata.org documentation",
                    "🎯 Practice: Kaggle Pandas course (Free)"
                ]
            },
            {
                "week": 2,
                "title": "Data Manipulation",
                "days": [
                    "Day 1-2: GroupBy — aggregate and transform",
                    "Day 3-4: Merge, Join, Concat DataFrames",
                    "Day 5-6: Apply functions, Lambda expressions",
                    "Day 7: Mini Project — Sales data analysis report"
                ],
                "resources": [
                    "📺 Data Analysis with Python (freeCodeCamp)",
                    "📚 realpython.com pandas tutorials",
                    "🎯 Practice: Kaggle competitions"
                ]
            },
            {
                "week": 3,
                "title": "Data Visualization",
                "days": [
                    "Day 1-2: Matplotlib — line, bar, scatter, pie charts",
                    "Day 3-4: Seaborn — statistical visualizations",
                    "Day 5-6: Plotly — interactive charts",
                    "Day 7: Mini Project — COVID data visualization dashboard"
                ],
                "resources": [
                    "📺 Matplotlib Tutorial (Corey Schafer YouTube)",
                    "📚 seaborn.pydata.org",
                    "🎯 Practice: Build 5 different chart types"
                ]
            },
            {
                "week": 4,
                "title": "Exploratory Data Analysis",
                "days": [
                    "Day 1-2: EDA process — understand, clean, explore",
                    "Day 3-4: Statistical analysis — correlations, distributions",
                    "Day 5-6: Feature engineering basics",
                    "Day 7: Final Project — Complete EDA report on real dataset"
                ],
                "resources": [
                    "📺 EDA Tutorial (Ken Jee YouTube)",
                    "📚 kaggle.com/learn",
                    "🎯 Build: Publish EDA notebook on Kaggle"
                ]
            }
        ]
    },
    "Statistics": {
        "total_weeks": 4,
        "total_hours": 60,
        "weeks": [
            {
                "week": 1,
                "title": "Descriptive Statistics",
                "days": [
                    "Day 1-2: Mean, Median, Mode, Variance, Standard Deviation",
                    "Day 3-4: Probability basics — events, outcomes",
                    "Day 5-6: Distributions — Normal, Binomial, Poisson",
                    "Day 7: Mini Project — Statistical analysis on real data"
                ],
                "resources": [
                    "📺 Statistics (StatQuest YouTube — Best resource)",
                    "📚 Khan Academy Statistics (Free)",
                    "🎯 Practice: statsmodels.org"
                ]
            },
            {
                "week": 2,
                "title": "Inferential Statistics",
                "days": [
                    "Day 1-2: Hypothesis Testing — null vs alternative",
                    "Day 3-4: T-test, Chi-square test, ANOVA",
                    "Day 5-6: P-value, Confidence Intervals",
                    "Day 7: Mini Project — A/B test analysis"
                ],
                "resources": [
                    "📺 Hypothesis Testing (StatQuest YouTube)",
                    "📚 scipy.stats documentation",
                    "🎯 Practice: Real A/B testing datasets"
                ]
            },
            {
                "week": 3,
                "title": "Regression & Correlation",
                "days": [
                    "Day 1-2: Pearson correlation, Spearman correlation",
                    "Day 3-4: Simple Linear Regression",
                    "Day 5-6: Multiple Regression",
                    "Day 7: Mini Project — Predict exam scores from study hours"
                ],
                "resources": [
                    "📺 Regression (StatQuest YouTube)",
                    "📚 statsmodels.org documentation",
                    "🎯 Practice: Regression on Kaggle datasets"
                ]
            },
            {
                "week": 4,
                "title": "Bayesian Statistics",
                "days": [
                    "Day 1-2: Bayes theorem — prior, likelihood, posterior",
                    "Day 3-4: Bayesian vs Frequentist approach",
                    "Day 5-6: Bayesian inference with Python",
                    "Day 7: Final Project — Bayesian analysis on real problem"
                ],
                "resources": [
                    "📺 Bayesian Statistics (YouTube)",
                    "📚 Think Bayes (Free online book)",
                    "🎯 Build: Bayesian spam filter"
                ]
            }
        ]
    },
    "AWS": {
        "total_weeks": 4,
        "total_hours": 70,
        "weeks": [
            {
                "week": 1,
                "title": "AWS Fundamentals",
                "days": [
                    "Day 1-2: What is Cloud? AWS Global Infrastructure",
                    "Day 3-4: IAM — Users, Roles, Policies, Security",
                    "Day 5-6: EC2 — Virtual servers, instance types",
                    "Day 7: Mini Project — Launch and configure EC2 server"
                ],
                "resources": [
                    "📺 AWS Tutorial (TechWorld with Nana YouTube)",
                    "📚 aws.amazon.com/training (Free tier)",
                    "🎯 Practice: AWS Free Tier account"
                ]
            },
            {
                "week": 2,
                "title": "Core AWS Services",
                "days": [
                    "Day 1-2: S3 — Object storage, buckets, policies",
                    "Day 3-4: RDS — Managed databases on AWS",
                    "Day 5-6: Lambda — Serverless functions",
                    "Day 7: Mini Project — Build serverless image processor"
                ],
                "resources": [
                    "📺 AWS Services explained (YouTube)",
                    "📚 docs.aws.amazon.com",
                    "🎯 Practice: AWS hands-on labs"
                ]
            },
            {
                "week": 3,
                "title": "AWS Networking & Security",
                "days": [
                    "Day 1-2: VPC — Virtual Private Cloud",
                    "Day 3-4: Security Groups, NACLs",
                    "Day 5-6: CloudFront — CDN, Route53 — DNS",
                    "Day 7: Mini Project — Deploy secure web app on AWS"
                ],
                "resources": [
                    "📺 AWS VPC Tutorial (YouTube)",
                    "📚 AWS Well-Architected Framework",
                    "🎯 Practice: Build 3-tier architecture"
                ]
            },
            {
                "week": 4,
                "title": "AWS DevOps & Certification",
                "days": [
                    "Day 1-2: CodePipeline, CodeBuild — CI/CD on AWS",
                    "Day 3-4: ECS, EKS — containers on AWS",
                    "Day 5-6: CloudWatch — monitoring and logging",
                    "Day 7: Final Project — Deploy full stack app on AWS"
                ],
                "resources": [
                    "📺 AWS DevOps Tutorial (YouTube)",
                    "📚 AWS Cloud Practitioner exam guide",
                    "🎯 Certify: AWS Cloud Practitioner (Entry level)"
                ]
            }
        ]
    },
    "Git": {
        "total_weeks": 2,
        "total_hours": 20,
        "weeks": [
            {
                "week": 1,
                "title": "Git Basics",
                "days": [
                    "Day 1-2: What is Git? init, add, commit, status",
                    "Day 3-4: Branches — create, switch, merge",
                    "Day 5-6: Remote repos — push, pull, clone",
                    "Day 7: Mini Project — Collaborate on a GitHub project"
                ],
                "resources": [
                    "📺 Git Tutorial (Traversy Media YouTube)",
                    "📚 learngitbranching.js.org (Interactive)",
                    "🎯 Practice: Create your GitHub profile"
                ]
            },
            {
                "week": 2,
                "title": "Advanced Git",
                "days": [
                    "Day 1-2: Resolving merge conflicts",
                    "Day 3-4: Rebase, Cherry-pick, Stash",
                    "Day 5-6: Git workflows — Gitflow, trunk-based",
                    "Day 7: Final Project — Open source contribution"
                ],
                "resources": [
                    "📺 Advanced Git (YouTube)",
                    "📚 atlassian.com/git/tutorials",
                    "🎯 Build: Contribute to a real open source project"
                ]
            }
        ]
    },
    "Java": {
        "total_weeks": 6,
        "total_hours": 100,
        "weeks": [
            {
                "week": 1,
                "title": "Java Basics",
                "days": [
                    "Day 1-2: JDK setup, Hello World, Variables, Data Types",
                    "Day 3-4: Operators, Conditionals, Loops",
                    "Day 5-6: Arrays, Strings, Methods",
                    "Day 7: Mini Project — Calculator app"
                ],
                "resources": [
                    "📺 Java Tutorial (Programming with Mosh YouTube)",
                    "📚 docs.oracle.com/java",
                    "🎯 Practice: HackerRank Java track"
                ]
            },
            {
                "week": 2,
                "title": "OOP in Java",
                "days": [
                    "Day 1-2: Classes, Objects, Constructors",
                    "Day 3-4: Inheritance, Polymorphism, Interfaces",
                    "Day 5-6: Abstract classes, Encapsulation",
                    "Day 7: Mini Project — Bank account management system"
                ],
                "resources": [
                    "📺 Java OOP (Telusko YouTube)",
                    "📚 baeldung.com Java tutorials",
                    "🎯 Practice: LeetCode Easy in Java"
                ]
            },
            {
                "week": 3,
                "title": "Java Collections & Generics",
                "days": [
                    "Day 1-2: ArrayList, LinkedList, HashMap, HashSet",
                    "Day 3-4: Generics — type safe collections",
                    "Day 5-6: Iterators, Comparable, Comparator",
                    "Day 7: Mini Project — Student grade management"
                ],
                "resources": [
                    "📺 Java Collections (YouTube)",
                    "📚 docs.oracle.com/collections",
                    "🎯 Practice: Collections problems on HackerRank"
                ]
            },
            {
                "week": 4,
                "title": "Java Advanced",
                "days": [
                    "Day 1-2: Exception handling — try, catch, finally",
                    "Day 3-4: File I/O, Serialization",
                    "Day 5-6: Multithreading, Concurrency",
                    "Day 7: Mini Project — Multithreaded download manager"
                ],
                "resources": [
                    "📺 Java Advanced (YouTube)",
                    "📚 jenkov.com Java tutorials",
                    "🎯 Practice: Concurrency problems"
                ]
            },
            {
                "week": 5,
                "title": "Spring Framework",
                "days": [
                    "Day 1-2: Spring Boot — setup, dependencies",
                    "Day 3-4: REST API with Spring Boot",
                    "Day 5-6: Spring Data JPA — database integration",
                    "Day 7: Mini Project — REST API with Spring Boot"
                ],
                "resources": [
                    "📺 Spring Boot Tutorial (Amigoscode YouTube)",
                    "📚 spring.io documentation",
                    "🎯 Practice: Build CRUD REST API"
                ]
            },
            {
                "week": 6,
                "title": "Java Projects & Testing",
                "days": [
                    "Day 1-2: Unit testing with JUnit",
                    "Day 3-4: Maven/Gradle — build tools",
                    "Day 5-6: Deploy Spring Boot app",
                    "Day 7: Final Project — Full stack Java web application"
                ],
                "resources": [
                    "📺 Java Testing (YouTube)",
                    "📚 junit.org documentation",
                    "🎯 Build: Deploy Java app on Render"
                ]
            }
        ]
    },
    "Cybersecurity": {
        "total_weeks": 5,
        "total_hours": 90,
        "weeks": [
            {
                "week": 1,
                "title": "Cybersecurity Fundamentals",
                "days": [
                    "Day 1-2: CIA Triad — Confidentiality, Integrity, Availability",
                    "Day 3-4: Types of attacks — phishing, malware, ransomware",
                    "Day 5-6: Networking basics for security — TCP/IP, DNS, HTTP",
                    "Day 7: Mini Project — Security audit checklist"
                ],
                "resources": [
                    "📺 Cybersecurity for Beginners (YouTube - freeCodeCamp)",
                    "📚 cybrary.it (Free cybersecurity courses)",
                    "🎯 Practice: TryHackMe (Free rooms)"
                ]
            },
            {
                "week": 2,
                "title": "Network Security",
                "days": [
                    "Day 1-2: Firewalls, IDS, IPS",
                    "Day 3-4: VPN, Proxy, Tor",
                    "Day 5-6: Wireshark — network traffic analysis",
                    "Day 7: Mini Project — Capture and analyze network packets"
                ],
                "resources": [
                    "📺 Wireshark Tutorial (YouTube)",
                    "📚 nmap.org documentation",
                    "🎯 Practice: TryHackMe Network rooms"
                ]
            },
            {
                "week": 3,
                "title": "Ethical Hacking",
                "days": [
                    "Day 1-2: Penetration testing methodology",
                    "Day 3-4: Kali Linux — essential security tools",
                    "Day 5-6: Nmap — network scanning, Metasploit basics",
                    "Day 7: Mini Project — Pen test a vulnerable VM"
                ],
                "resources": [
                    "📺 Ethical Hacking (TCM Security YouTube)",
                    "📚 hackthebox.com (Practice hacking legally)",
                    "🎯 Practice: TryHackMe, HackTheBox"
                ]
            },
            {
                "week": 4,
                "title": "Web Application Security",
                "days": [
                    "Day 1-2: OWASP Top 10 vulnerabilities",
                    "Day 3-4: SQL Injection, XSS, CSRF",
                    "Day 5-6: Burp Suite — web app testing tool",
                    "Day 7: Mini Project — Find vulnerabilities in DVWA"
                ],
                "resources": [
                    "📺 Web App Hacking (YouTube)",
                    "📚 owasp.org",
                    "🎯 Practice: PortSwigger Web Security Academy (Free)"
                ]
            },
            {
                "week": 5,
                "title": "Certifications & Career",
                "days": [
                    "Day 1-2: CompTIA Security+ exam preparation",
                    "Day 3-4: CEH — Certified Ethical Hacker overview",
                    "Day 5-6: Bug bounty programs — HackerOne, Bugcrowd",
                    "Day 7: Final Project — Write a penetration testing report"
                ],
                "resources": [
                    "📺 Security+ Study Guide (YouTube)",
                    "📚 professormesser.com (Free Security+ prep)",
                    "🎯 Certify: CompTIA Security+"
                ]
            }
        ]
    },
    "Flutter": {
        "total_weeks": 5,
        "total_hours": 80,
        "weeks": [
            {
                "week": 1,
                "title": "Flutter & Dart Basics",
                "days": [
                    "Day 1-2: Dart language — variables, functions, OOP",
                    "Day 3-4: Flutter setup, first app, Hot reload",
                    "Day 5-6: Widgets — Text, Container, Row, Column",
                    "Day 7: Mini Project — Simple profile card UI"
                ],
                "resources": [
                    "📺 Flutter Course (freeCodeCamp YouTube)",
                    "📚 flutter.dev documentation",
                    "🎯 Practice: Flutter widget catalog"
                ]
            },
            {
                "week": 2,
                "title": "Flutter UI Development",
                "days": [
                    "Day 1-2: Stateful vs Stateless widgets",
                    "Day 3-4: ListView, GridView, Stack",
                    "Day 5-6: Navigation — push, pop, named routes",
                    "Day 7: Mini Project — Multi-screen todo app"
                ],
                "resources": [
                    "📺 Flutter UI (YouTube - Reso Coder)",
                    "📚 pub.dev — Flutter packages",
                    "🎯 Practice: Clone popular app UI"
                ]
            },
            {
                "week": 3,
                "title": "State Management",
                "days": [
                    "Day 1-2: setState — local state management",
                    "Day 3-4: Provider — app-wide state",
                    "Day 5-6: Riverpod — modern state management",
                    "Day 7: Mini Project — Shopping cart with state management"
                ],
                "resources": [
                    "📺 Flutter State Management (YouTube)",
                    "📚 riverpod.dev documentation",
                    "🎯 Practice: Implement multiple state solutions"
                ]
            },
            {
                "week": 4,
                "title": "Firebase & Backend",
                "days": [
                    "Day 1-2: Firebase setup — Authentication",
                    "Day 3-4: Firestore — NoSQL database",
                    "Day 5-6: REST API integration with Flutter",
                    "Day 7: Mini Project — Chat app with Firebase"
                ],
                "resources": [
                    "📺 Flutter Firebase (YouTube)",
                    "📚 firebase.google.com/docs",
                    "🎯 Build: Real-time chat application"
                ]
            },
            {
                "week": 5,
                "title": "Publishing & Advanced",
                "days": [
                    "Day 1-2: Animations in Flutter",
                    "Day 3-4: Platform channels — native features",
                    "Day 5-6: Build and publish to Play Store / App Store",
                    "Day 7: Final Project — Publish your Flutter app"
                ],
                "resources": [
                    "📺 Flutter Animations (YouTube)",
                    "📚 flutter.dev/deployment",
                    "🎯 Build: Publish real app to Play Store"
                ]
            }
        ]
    },
    "Blockchain": {
        "total_weeks": 5,
        "total_hours": 85,
        "weeks": [
            {
                "week": 1,
                "title": "Blockchain Fundamentals",
                "days": [
                    "Day 1-2: What is Blockchain? Distributed ledger, Consensus",
                    "Day 3-4: Cryptography basics — hashing, public/private keys",
                    "Day 5-6: Bitcoin — how transactions work",
                    "Day 7: Mini Project — Build a simple blockchain in Python"
                ],
                "resources": [
                    "📺 Blockchain Explained (YouTube - 3Blue1Brown)",
                    "📚 bitcoin.org/bitcoin.pdf (Original whitepaper)",
                    "🎯 Practice: Build blockchain from scratch"
                ]
            },
            {
                "week": 2,
                "title": "Ethereum & Smart Contracts",
                "days": [
                    "Day 1-2: Ethereum — EVM, Gas, Accounts",
                    "Day 3-4: Solidity basics — variables, functions",
                    "Day 5-6: Deploy smart contract with Remix IDE",
                    "Day 7: Mini Project — Simple token smart contract"
                ],
                "resources": [
                    "📺 Solidity Tutorial (YouTube - Patrick Collins)",
                    "📚 docs.soliditylang.org",
                    "🎯 Practice: Remix IDE online"
                ]
            },
            {
                "week": 3,
                "title": "DApp Development",
                "days": [
                    "Day 1-2: Web3.js / Ethers.js — interact with blockchain",
                    "Day 3-4: MetaMask — wallet integration",
                    "Day 5-6: Hardhat — development framework",
                    "Day 7: Mini Project — Simple DApp with React frontend"
                ],
                "resources": [
                    "📺 Full Stack DApp (YouTube)",
                    "📚 hardhat.org documentation",
                    "🎯 Practice: Build DApp on testnet"
                ]
            },
            {
                "week": 4,
                "title": "DeFi & NFTs",
                "days": [
                    "Day 1-2: DeFi concepts — AMM, liquidity pools",
                    "Day 3-4: ERC-20 tokens — fungible tokens",
                    "Day 5-6: ERC-721 — NFT standard",
                    "Day 7: Mini Project — Create and deploy your own NFT"
                ],
                "resources": [
                    "📺 DeFi explained (Finematics YouTube)",
                    "📚 openzeppelin.com contracts",
                    "🎯 Build: Mint NFT on testnet"
                ]
            },
            {
                "week": 5,
                "title": "Security & Advanced",
                "days": [
                    "Day 1-2: Smart contract vulnerabilities — reentrancy, overflow",
                    "Day 3-4: Auditing smart contracts",
                    "Day 5-6: Layer 2 solutions — Polygon, Arbitrum",
                    "Day 7: Final Project — Deploy secure DApp on mainnet"
                ],
                "resources": [
                    "📺 Smart Contract Security (YouTube)",
                    "📚 consensys.github.io/smart-contract-best-practices",
                    "🎯 Certify: Blockchain Council certifications"
                ]
            }
        ]
    },
}

LEARNING_HOURS = {
    "Python": 60, "Machine Learning": 100, "Deep Learning": 120,
    "NLP": 90, "Computer Vision": 100, "Reinforcement Learning": 120,
    "MLOps": 80, "TensorFlow": 60, "PyTorch": 60, "Scikit-learn": 40,
    "HTML": 20, "CSS": 30, "JavaScript": 80, "TypeScript": 50,
    "React": 70, "Angular": 70, "Vue": 60, "Node.js": 60,
    "Django": 60, "Flask": 40, "Next.js": 50, "REST API": 30,
    "GraphQL": 40, "Android": 80, "iOS": 90, "Flutter": 80,
    "React Native": 70, "Kotlin": 70, "Swift": 80,
    "AWS": 70, "Azure": 70, "GCP": 70, "Docker": 45,
    "Kubernetes": 60, "Linux": 50, "Git": 20, "CI/CD": 40,
    "SQL": 40, "Data Analysis": 60, "Data Engineering": 90,
    "Power BI": 40, "Tableau": 40, "Apache Spark": 70, "Statistics": 60,
    "Cybersecurity": 90, "Ethical Hacking": 100, "Network Security": 70,
    "Cryptography": 60, "Unity": 90, "Unreal Engine": 100,
    "C#": 70, "Game Design": 60, "Blockchain": 85, "Solidity": 70,
    "Web3": 60, "C": 70, "C++": 90, "Java": 100,
    "Algorithms": 80, "Data Structures": 80, "Operating Systems": 70,
    "Computer Networks": 60,
}

COURSE_RECOMMENDATIONS = {
    "Python": ["freeCodeCamp Python (YouTube)", "CS50P Harvard (Free)", "Python.org Tutorial"],
    "Machine Learning": ["Andrew Ng ML Coursera (Free Audit)", "Kaggle ML Course (Free)", "fast.ai (Free)"],
    "Deep Learning": ["deeplearning.ai Specialization", "fast.ai Practical DL (Free)", "3Blue1Brown (YouTube)"],
    "NLP": ["HuggingFace Course (Free)", "Stanford CS224N (YouTube)", "Kaggle NLP (Free)"],
    "JavaScript": ["javascript.info (Free)", "freeCodeCamp JS (Free)", "JavaScript30 (Free)"],
    "React": ["react.dev Official Docs (Free)", "freeCodeCamp React (YouTube)", "Scrimba React Course"],
    "SQL": ["SQLZoo (Free)", "Mode Analytics SQL (Free)", "LeetCode SQL"],
    "Docker": ["TechWorld with Nana (YouTube)", "Docker Official Docs", "Play with Docker (Free)"],
    "AWS": ["AWS Free Tier", "freeCodeCamp AWS (YouTube)", "AWS Skill Builder (Free)"],
    "Git": ["learngitbranching.js.org (Free)", "Traversy Media Git (YouTube)", "GitHub Skills (Free)"],
    "Java": ["Programming with Mosh Java (YouTube)", "Telusko Java (YouTube)", "Oracle Java Tutorials"],
    "Cybersecurity": ["TryHackMe (Free)", "PortSwigger Academy (Free)", "TCM Security (YouTube)"],
    "Flutter": ["flutter.dev Official (Free)", "freeCodeCamp Flutter (YouTube)", "Reso Coder (YouTube)"],
    "Blockchain": ["Patrick Collins (YouTube - Free)", "CryptoZombies (Free)", "Buildspace (Free)"],
    "Data Analysis": ["Kaggle Data Analysis (Free)", "Keith Galli Pandas (YouTube)", "freeCodeCamp DA (YouTube)"],
    "Statistics": ["StatQuest (YouTube - Best)", "Khan Academy Stats (Free)", "Think Stats (Free Book)"],
}