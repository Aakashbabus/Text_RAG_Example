# Readme

## Project Title

Story Analysis with Langchain and Crew AI

## Description

This project is a Python-based tool that leverages Langchain and Crew AI to analyze text stories. The main functionality is to identify and list all characters within a given story text file using a configured Language Model (LLM) and text processing tools.

## Repository

The project repository can be found [here](https://github.com/Aakashbabus/Text_RAG_Example).

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/Aakashbabus/Text_RAG_Example.git
   cd Text_RAG_Example
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install required dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

## Configuration

1. **Set up the text file:**
   Ensure you have a text file containing the story you want to analyze. Place this file in the `sample_data` directory. Update the `txt` parameter in the `TXTSearchTool` configuration to point to your text file.

2. **LLM Configuration:**
   Configure the `llm` and `embedder` parameters in the `rag_tool` setup to use your desired models and providers. The example is configured to use `Ollama` with the `llama3` model.

## Usage

To run the script and analyze the story:

```sh
python main.py
```

This will initialize the necessary agents and tools, execute the task, and print out the result.

## Code Overview

- **Imports:**
  - The script imports necessary modules and tools from `langchain_community.llms`, `crewai`, and `crewai_tools`.

- **Configuration:**
  - `rag_tool`: Configures the text search tool with the language model, embedder, and chunker parameters.
  - `llm1`: Configures the language model with specific parameters such as temperature and model type.

- **Main Function:**
  - Creates an agent (`data_analyst`) with specific goals and tools.
  - Defines a task (`test_task`) for the agent to perform.
  - Executes the task and prints the result.

## License

MIT License

```
MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

## Contact

For any questions or feedback, please reach out to aakashbabus@gmail.com.
