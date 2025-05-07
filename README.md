# Few-Shot Finance: AI-Powered Earnings Call Analysis

## Overview
Few-Shot Finance is an advanced Natural Language Processing (NLP) tool that leverages Large Language Models (LLMs) to analyze earnings call transcripts. The system automatically processes financial transcripts, breaking them down into question-answer pairs and intelligently classifying responses as either substantive answers or non-answers, providing valuable insights for financial analysis.

## Key Features
- **Intelligent Q&A Extraction**: Automatically splits transcripts into structured question-answer pairs
- **Response Classification**: Tags answers as either "answer" (substantive) or "nonanswer" (evasive/vague)
- **Detailed Analysis**: Provides justification for each classification
- **Few-Shot Learning**: Utilizes few-shot prompting for improved accuracy
- **Easy Integration**: Simple API interface for seamless integration

## Technical Architecture
- **Language**: Python 3.8+
- **Main Dependencies**:
  - LLM API Integration
  - Natural Language Processing Libraries
  - Environment Configuration Management

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/syed-shahbuddin/few-shot-finance-AI.git
   cd few-shot-finance-AI
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API Key**
   - Create a `.env` file in the project root:
     ```
     HYPERBOLIC_API_KEY=your_api_key_here
     ```
   - Or set it as an environment variable:
     ```bash
     export HYPERBOLIC_API_KEY=your_api_key_here
     ```

## Usage

### Basic Usage
```bash
python few-shot-finance.py
```

### Example Output
```json
{
    "question": "Can you discuss the Q4 revenue growth?",
    "answer": "Revenue grew 15% YoY to $2.3B...",
    "classification": "answer",
    "justification": "Provides specific numbers and growth metrics"
}
```

## Security Considerations
- Never commit API keys or sensitive credentials
- Use environment variables for configuration
- Regularly rotate API keys
- Monitor API usage and set appropriate rate limits

## Contributing
We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to your branch
5. Create a Pull Request

### Development Guidelines
- Follow PEP 8 style guide
- Add unit tests for new features
- Update documentation as needed
- Use meaningful commit messages

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer
This tool is provided for research and educational purposes only. Users should exercise their own judgment in making investment decisions. The developers are not responsible for any financial decisions made based on the tool's output.

## Contact
For questions or support, please open an issue in the GitHub repository.

---
Made with ❤️ by Syed Shahbuddin 