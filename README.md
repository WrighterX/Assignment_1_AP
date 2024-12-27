# Assignment_1_AP

# Chat with LLM Models

This project is a web application built using Streamlit that allows users to interact with various language models (LLMs) through a chat interface. The application leverages ChromaDB for context retrieval, enabling more informed and context-aware responses from the models.

## Installation

To run this project, you need to install the required libraries. You can do this by creating a virtual environment and using pip to install the dependencies. Here are the steps:

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. **Create a virtual environment (optional but recommended)**:
   ```bash
   python -m venv venv
   source venv/bin/activate # On Windows use venv\Scripts\activate
   ```
3. **Install the required libraries**:
   ```bash
   pip install chromadb chromadb-client langchain streamlit
   ```
4. **Install any additional dependencies for Llama Index** (check specific instructions in their documentation).

## Usage

To run the application, execute the following command in your terminal:
   ```bash
   streamlit run model.py
   ```
This will start a local web server and open the application in your default web browser.

Once the application is running, you can select a language model from the sidebar and start chatting by entering your questions in the input box.

## Examples

Here are some examples of how to interact with the application:

1. **Basic Interaction**:
   - User: "hi"
   - Assistant: "How can I help you?"
![interface](https://github.com/user-attachments/assets/e04a0a90-c1f8-4ff0-b16a-9804977b69d3)

2. **Basic Questions**:
   - User: "How long does it take to train an LLM?"
   - Assistant: "Training a Large Language Model (LLM) is a complex process that requires significant computational resources and time. The training time for an LLM can vary greatly depending on several factors, such as..."
![test_3](https://github.com/user-attachments/assets/f7c6ee53-300c-4ca3-8a2b-fdde1c838f36)

The application retrieves relevant context from previous interactions stored in ChromaDB to provide more accurate and context-aware responses.

## Contributing

Contributions are welcome! If you have suggestions for improvements or features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
