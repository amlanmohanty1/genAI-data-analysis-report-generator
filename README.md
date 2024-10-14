## Data Analysis and EDA Report Generator using Generative AI
### Introduction
This Data Analysis and EDA Report Generator uses Generative AI to help data analysts and business professionals quickly generate insightful EDA and data analysis reports from csv files, streamlining the process of extracting valuable insights from raw data.

### Generative AI

#### LangChain
LangChain is used to create a seamless integration with language models. In this project, LangChain helps manage the interactions with the Groq API, ensuring efficient prompt generation and response handling.

#### Groq API
Groq provides the computational backbone for running the language models. This project uses the Groq API to leverage the power of LLaMA LLM for generating insightful data analysis reports.

#### LLaMA LLM
The LLaMA Large Language Model (LLM) is utilized to process and understand the data provided in the CSV files. It generates comprehensive and coherent analysis reports, mimicking the output of a skilled data analyst.


### Set-up
1. Clone the repository:
    ```
    git clone https://github.com/amlanmohanty1/genAI-data-analysis-report-generator.git
    ```
2. Get an API_KEY from here: https://console.groq.com/keys. Update the value of `GROQ_API_KEY` with the API_KEY you created inside the `.env` file. 

3. Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```
   
4. Run the `app.py` file.


### License
This project is licensed under the MIT License. Check out the [LICENSE](LICENSE) file for more details. 
