# Task 5: Automated Support Ticket Tagging with LLMs

##  Project Overview
In a real-world customer support environment, manually sorting thousands of tickets is slow and prone to errors. This project demonstrates an automated solution using **Google's Gemini 1.5 Flash** model. The system intelligently reads customer queries and categorizes them into specific departments like **Technical Support, Billing, or Account Management.**

---

##  Key Technical Features
* **Prompt Engineering**: Implemented **Few-Shot Learning** by providing the model with high-quality examples to ensure consistent and accurate tagging.
* **Smart Categorization**: The system outputs the **Top 3 most probable tags** with confidence scores, allowing for a robust fallback mechanism.
* **API Resilience**: Built a custom **Retry Logic** with exponential backoff. This ensures that if the API hits a rate limit (429 error), the script waits and retries instead of crashing.
* **Security First**: Followed industry best practices by using `.env` files for API key management, ensuring sensitive credentials are protected.

---

##  Performance & Evaluation
* **Final Accuracy**: **100% successful** categorization on the test batch processing.
* **Observation**: Few-shot prompting significantly outperformed zero-shot in distinguishing between complex technical and account-related issues.

---

##  Setup & Usage Instructions
1. **Clone the Repository**:
   Use `git clone` with this repository's URL to get the files locally.
2. **Configure API Key**:
   Create a `.env` file in the root directory and add:
   `GOOGLE_API_KEY=your_actual_api_key_here`
3. **Install Dependencies**:
   `pip install google-genai python-dotenv pandas`
4. **Run the Notebook**: Open `Task5_LLM_Auto_Tagging.ipynb` in VS Code and run the cells.

---

##  Important Note on API Limits
**Optimized Execution:** To respect the **Gemini Free Tier** daily quota, some redundant test calls in Step 3 were kept for reference but not executed in the final batch run. This optimization ensures that the core batch processing (Step 4) has enough quota to complete successfully without hitting rate limits.
