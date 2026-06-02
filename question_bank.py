import random

QUESTION_BANK = {

    "Java Developer": [
        "What is OOP?",
        "Explain JVM.",
        "Difference between Array and ArrayList.",
        "What is Exception Handling?",
        "Explain HashMap.",
        "What is Multithreading?",
        "Difference between HashMap and Hashtable.",
        "What is Garbage Collection?",
        "Explain Abstraction.",
        "What is Polymorphism?",
        "What is Encapsulation?",
        "Explain Inheritance.",
        "Difference between Interface and Abstract Class.",
        "What is Method Overloading?",
        "What is Method Overriding?"
    ],

    "Python Developer": [
        "What is Python?",
        "Difference between List and Tuple.",
        "What is a Dictionary?",
        "Explain Decorators.",
        "What are Generators?",
        "What is PEP8?",
        "Difference between List and Set.",
        "Explain Lambda Functions.",
        "What is Inheritance?",
        "Explain Exception Handling.",
        "What is List Comprehension?",
        "What is Duck Typing?",
        "What is a Context Manager?",
        "Explain Iterators.",
        "What are Python Closures?"
    ],

    "AI Engineer": [
        "What is Machine Learning?",
        "What is Deep Learning?",
        "Explain Overfitting.",
        "What is Gradient Descent?",
        "What is CNN?",
        "What is NLP?",
        "Difference between CNN and RNN.",
        "What is Transfer Learning?",
        "Explain Transformers.",
        "What is Reinforcement Learning?",
        "What is Supervised Learning?",
        "What is Unsupervised Learning?",
        "What is Backpropagation?",
        "What is Feature Engineering?",
        "What is Cross Validation?"
    ],

    "Data Analyst": [
        "What is SQL?",
        "Explain JOINs.",
        "What is Normalization?",
        "Difference between WHERE and HAVING.",
        "What is Power BI?",
        "Explain ETL.",
        "What is Data Cleaning?",
        "Difference between Mean and Median.",
        "What is a Primary Key?",
        "What is a Foreign Key?",
        "What is Correlation?",
        "Explain Regression.",
        "What is Data Warehousing?",
        "What is a KPI?",
        "What is Data Visualization?"
    ],

    "Full Stack Developer": [
        "What is REST API?",
        "What is JWT?",
        "Explain React.",
        "What is Node.js?",
        "What is Express.js?",
        "What is MongoDB?",
        "Difference between SQL and NoSQL.",
        "Explain Authentication.",
        "What is Authorization?",
        "What is Middleware?",
        "Explain MVC Architecture.",
        "What is CRUD?",
        "Explain CORS.",
        "What is Responsive Design?",
        "Explain Git Workflow."
    ],

    "Cyber Security Analyst": [
        "What is SQL Injection?",
        "Explain XSS attacks.",
        "What is a Firewall?",
        "What is MFA?",
        "Explain CIA Triad.",
        "What is Encryption?",
        "What is a VPN?",
        "What is Malware?",
        "Explain Phishing.",
        "What is Penetration Testing?",
        "What is IDS?",
        "What is IPS?",
        "Explain Zero Trust Security.",
        "What is a Security Audit?",
        "What is Vulnerability Assessment?"
    ],

    "Cloud Engineer": [
        "What is Cloud Computing?",
        "Difference between IaaS and PaaS.",
        "What is AWS EC2?",
        "Explain Auto Scaling.",
        "What is a VPC?",
        "What is Load Balancing?",
        "Explain Cloud Security.",
        "What is Object Storage?",
        "What is a CDN?",
        "What is Serverless Computing?",
        "What is AWS Lambda?",
        "Explain Availability Zones.",
        "What is Elastic Beanstalk?",
        "What is Disaster Recovery?",
        "What is Infrastructure as Code?"
    ],

    "DevOps Engineer": [
        "What is CI/CD?",
        "Explain Docker.",
        "What is Kubernetes?",
        "What is Jenkins?",
        "What is GitOps?",
        "What is Infrastructure as Code?",
        "Explain Terraform.",
        "What is Containerization?",
        "What is Monitoring?",
        "What is Logging?",
        "What is Ansible?",
        "What is Blue-Green Deployment?",
        "What is Rolling Deployment?",
        "Explain DevSecOps.",
        "What is Prometheus?"
    ],

    "Backend Developer": [
        "What is REST API?",
        "What is Authentication?",
        "What is Authorization?",
        "Explain JWT.",
        "What is Middleware?",
        "What is Caching?",
        "Explain Database Indexing.",
        "What is Microservices Architecture?",
        "What is API Rate Limiting?",
        "What is Session Management?",
        "Explain Load Balancing.",
        "What is Message Queue?",
        "What is Redis?",
        "What is API Gateway?",
        "What is Scalability?"
    ],

    "Frontend Developer": [
        "What is HTML?",
        "What is CSS?",
        "What is JavaScript?",
        "Explain DOM.",
        "What is React?",
        "What are React Hooks?",
        "What is Responsive Design?",
        "What is State Management?",
        "Explain Flexbox.",
        "Explain CSS Grid.",
        "What is Event Bubbling?",
        "What is Virtual DOM?",
        "What is Lazy Loading?",
        "What is Web Accessibility?",
        "What is Cross Browser Compatibility?"
    ],

    "Software Engineer": [
        "What is SDLC?",
        "What is Agile?",
        "What is OOP?",
        "What is Design Pattern?",
        "Explain SOLID Principles.",
        "What is Unit Testing?",
        "What is Integration Testing?",
        "What is Version Control?",
        "Explain Git Workflow.",
        "What is Refactoring?",
        "What is Scalability?",
        "What is System Design?",
        "What is Technical Debt?",
        "What is Code Review?",
        "What is Continuous Integration?"
    ],

    "Data Engineer": [
        "What is ETL?",
        "What is Data Pipeline?",
        "What is Apache Spark?",
        "What is Hadoop?",
        "What is Data Warehouse?",
        "What is Data Lake?",
        "Explain Batch Processing.",
        "Explain Stream Processing.",
        "What is Kafka?",
        "What is Airflow?",
        "What is Data Modeling?",
        "What is Schema Design?",
        "What is Partitioning?",
        "What is Big Data?",
        "What is Data Governance?"
    ],

    "Business Analyst": [
        "What is Requirement Gathering?",
        "What is SWOT Analysis?",
        "What is a BRD?",
        "What is a Use Case?",
        "Explain Gap Analysis.",
        "What is Stakeholder Management?",
        "What is BPMN?",
        "What is User Story?",
        "What is KPI?",
        "What is Feasibility Study?",
        "What is Cost Benefit Analysis?",
        "What is Risk Analysis?",
        "What is Process Mapping?",
        "What is UAT?",
        "What is Functional Requirement?"
    ],

    "QA Engineer": [
        "What is Software Testing?",
        "What is Regression Testing?",
        "What is Smoke Testing?",
        "What is Sanity Testing?",
        "What is Test Case?",
        "What is Bug Life Cycle?",
        "What is Selenium?",
        "What is Automation Testing?",
        "What is Performance Testing?",
        "What is Load Testing?",
        "What is API Testing?",
        "What is Functional Testing?",
        "What is Non Functional Testing?",
        "What is Test Plan?",
        "What is Defect Tracking?"
    ],

    "Mobile App Developer": [
        "What is Android Studio?",
        "What is Flutter?",
        "What is React Native?",
        "What is APK?",
        "What is Activity Lifecycle?",
        "What is State Management?",
        "What is REST API Integration?",
        "What is Firebase?",
        "What is Push Notification?",
        "What is Local Storage?",
        "What is App Deployment?",
        "What is Responsive UI?",
        "What is Navigation?",
        "What is Dependency Injection?",
        "What is Mobile App Security?"
    ]
}


def generate_random_questions(role, count):

    available_questions = QUESTION_BANK.get(role, [])

    if not available_questions:
        return []

    count = min(count, len(available_questions))

    return random.sample(
        available_questions,
        count
    )