# Module 1 — Generative AI Basics for Software Development

---

## What to Expect

This module introduces the foundational concepts of **Generative AI in Software Development**.

**You will learn:**

- How Large Language Models (LLMs) and Natural Language Processing (NLP) work
- How to set up AI-enabled development environments
- How to design effective prompts

**Through hands-on labs, you will practice:**

- Generating and refactoring code
- Building simple chatbots
- Creating basic prototypes
- Validating AI-generated outputs for accuracy, safety, and reliability

---

## AI-Powered Development Workflow


| Step | Activity                | AI Role                                                                                                                      |
| ---- | ----------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| 1    | **Morning Standup**     | Reviews commits and suggests potential issues or improvements                                                                |
| 2    | **Feature Development** | Generates initial implementation across multiple files while maintaining consistency                                         |
| 3    | **Code Review**         | Scans for security vulnerabilities, performance bottlenecks, and style violations — acts as a first pass before human review |
| 4    | **Testing**             | Generates comprehensive test cases, including edge cases developers might miss                                               |


---

## Role of AI in the Software Development Life Cycle (SDLC)

### 1. Requirements Gathering

Modern requirements gathering leverages NLP and ML to transform how we capture user needs.

- **AI-Powered Requirement Analysis** — Uses LLMs to process feedback from interviews, tickets, and documentation, extracting insights that human analysts might miss
- **Intelligent Requirement Validation** — Automatically checks requirements against business rules and identifies conflicts early
- **Automated User Story Generation** — Creates detailed stories from business objectives, complete with acceptance criteria
- **Predictive Requirement Modeling** — Analyzes historical data to anticipate future requirements and estimate complexity, enabling accurate project planning

### 2. Design

- Provides architectural recommendations
- Generates system diagrams from descriptions
- Offers data-driven, intelligent pattern recognition for system designs
- Enables performance optimization

### 3. Development

AI coding assistant tools: **GitHub Copilot**, **Cursor**, **Windsurf**

- Provide contextual code generation
- Intelligent refactoring

### 4. Testing

- Provides comprehensive test suites
- Employs adaptive testing strategies
- Predicts potential failures
- Optimizes quality efforts based on business impact

### 5. Deployment

- Orchestrates intelligent CI/CD pipelines
- Automated security scanning

### 6. Maintenance

- Performance monitoring
- Predicts system failures

## Software Development Environment for AI with VSCode, Copilot, and continue.dev

### Visual Studio Code: The Development Environment Foundation

* An environment allowing developers to write code and uses AI coding assistance like:
  * **Continue.dev**: Consider when **data sensitivity** is a concern, use a locally hosted model through tool such as Continue.dev.
  * **Github Copilot**: Verified students, teachers, and maintainers of popular open-source projects qualify for free access to the Pro plan through GitHub Education.


## LLMs (Large Language Models)

* LLMs are advanced AI System trained on massie etxt and code datasets. They Excels at:
  * Code Generation
  * Debugging
  * Architectural Planning
  * Natural Langauge-to-code-translation

* Popular Models:
  * Claude
  * GPT-4o and o1
  * Gemini
  * LLaMA
  * Mistral

* Enhance Productivity by:
  * Generating code
  * Automating bug fixing
  * Acting as intelligent debbelopment partners
  * Provifing Expert Insights

* Key Capabilities of Modern LLMs:
  * Generating Application Architectures
  * Advanced Testing
  * Collaborative Development
  * Autonomous Task Execution

* Limitations:
   * Hallucinations
   * Computational Requirements
   * Data Dependency
   * Need for human oversight

  
## NLP (Natural Language Processing)
* Modern NLP is powered by transformer architectures and large language models, moving beyond traditional statistical methods.

* Essential Tools:
  * Hugging Face Transformers
  * LangChain
  * LlamaIndex

* RAG System combine retrieval with generation to ground LLM outputs in current, proprietary data.
* Semantic search, AI agents, and prompt engineering are fundamental techniques.
* Production applications span code generation, doscument intelligence, conversational AI, and enterprise search.
* Always consider context management, cost optimization, model selection, and implication when deploying NLP systems.


## Essential GenAI Tools for Software Development

> AI coding assistants have evolved into sophisticated agents capable of multifile refactoring, autonomous debugging, and even hours-long coding sessions.

* **GitHub Copilot** is the **industry standard** for AI-assisted coding, now capable of autonomous development through its powerful Agent mode.
* **Claude** is a **reasoning-focused AI model** that excels at complex, multistep coding tasks and large-scale architectural planning.
* **Cursor** is an **AI-native code editor** built for deep integration and intelligent collaboration across your entire codebase.
* **ChatGPT** is a versatile **general-purpose** assistant ideal for quick coding help, brainstorming, and concept explanations.
* **Google Gemini** is a **multimodal AI** system tightly integrated with Google Workspace, offering strong reasoning and seamless development support.
* Some other AI-powered specialized tools include Qodo, Windsurf, Replit, and Tabnine.

> The choice of tool depends on your needs and goals. A hybrid approach, which involves combining multiple tools, yields the best result.

## Tokens in GenAI

* **Tokens** are **fundamental units** that LLMs use to process text, they are the *currency* of AI.
* AI Model breaks down input prompts into tokens using a process **tokenization** before AI Model process the prompts.

> "Hello world!" → 3 tokens: ["Hello", "world", "!"]
> "AI-powered" → 3 tokens: ["AI", "-", "powered"]
> "tokenization" → 2 tokens: ["token", "ization"]

### Why Token Matter for Developers

* Tokens usage **directly affects cost**, every API call incurs a charge based on the number of tokens used, for both input and output.
* The number of tokens also **impact performance**, as higher token counts can increase response latency.
* Each models has a maximum token limit (ex. 200K, 1M, 2M). This is known as **Context Window**.
* Better token management leads to better **quality** of outputs.

> Real-world insight: Output tokens typically **cost two to four times** more than input tokens. So, optimizing your prompts and responses can significantly reduce the expenses.

### Tokenizers

A **tokenizer** is a program that breaks down *prompt text into smaller parts*, called **tokens**.So AI can understand and process it.

> Note: **tiktoken** remains the gold standard for OpenAI models:

[tiktoken.py](tiktoken.py)

> OpenAI Platform Tokenizer: https://platform.openai.com/tokenizer
> Tiktokenizer: https://tiktokenizer.vercel.app (visual breakdown)
