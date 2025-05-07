# Few-Shot Finance Earnings Call Analyzer

This project uses a Large Language Model (LLM) API to analyze earnings call transcripts, splitting them into question-answer pairs and tagging each answer as either an "answer" (substantive) or "nonanswer" (vague/evasive). It is designed for financial analysts and researchers who want to automate the extraction of actionable insights from conference call transcripts.

## Features
- Splits transcripts into question-answer pairs
- Tags answers as "answer" or "nonanswer" with justifications
- Uses a few-shot prompt template for high accuracy

## Setup
1. **Clone the repository**
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Set your API key:**
   - Create a `.env` file in the project root:
     ```
     HYPERBOLIC_API_KEY=your_api_key_here
     ```
   - Or set the environment variable directly in your shell.

## Usage
Run the script with:
```bash
python few-shot-finance (3).py
```

The script will send a sample transcript to the LLM API and print the extracted question-answer pairs with tags.

## Security Best Practices
- **Never** hardcode your API key in the code.
- Use environment variables or a `.env` file (which is gitignored).
- Rotate your API key if you suspect it has been exposed.
- Do not share logs or error messages that may contain sensitive data.

## License
See [LICENSE](LICENSE) for license information.

## Disclaimer
This project is for educational and research purposes. Use at your own risk. 