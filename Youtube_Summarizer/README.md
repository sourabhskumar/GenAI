
# LangChain Content Summarization Tool

## Overview

This project is a **Streamlit application** that leverages the power of **LangChain** and the **Gemma-7b-It model** to summarize content from **YouTube videos** and **websites**. The tool allows users to input a URL and receive a concise summary of the content, making it easier to extract meaningful insights from lengthy sources.

## Features

- **YouTube and Website Summarization:** Input a URL from YouTube or a website, and the app will generate a summary of the content.
- **User-Friendly Interface:** A simple and intuitive interface built with Streamlit.
- **Advanced Summarization:** Powered by the Gemma-7b-It model, the app provides accurate and efficient text summaries.
- **Real-Time Processing:** Get summaries within seconds, making it ideal for staying updated on current events, research, or any content-heavy media.

## How It Works

1. **Input URL:** Enter the URL of a YouTube video or website into the text field.
2. **Validation and Content Loading:** The app validates the URL and loads the content.
3. **Summarization:** The content is passed through a summarization chain built using LangChain and the Gemma-7b-It model.
4. **Output:** A concise summary is generated and displayed on the page.

## Example Use Case

With the **transfer window** currently open, the app can be used to quickly stay updated on the latest football transfer rumors. For example, inputting a YouTube video URL discussing the latest **Arsenal transfer rumors** will generate a summary highlighting key points such as potential player transfers, upcoming events, and other relevant news.

## Installation

To run this application locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sourabhskumar/GENAI.git
   cd repository-name
   ```

2. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create a `.env` file and add your Gemma-7b-It model API key:**
   ```
   GROQ_API=your_api_key_here
   ```

4. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

## Usage

Once the application is running, you can use it by entering a YouTube or website URL into the provided text field and clicking the "Summarize the Content from YT or Website" button. The summary will be displayed directly on the page.

## Technologies Used

- **Python**
- **Streamlit**
- **LangChain**
- **Gemma-7b-It model**
- **YouTube and URL Content Loaders**

## Contributing

If you'd like to contribute to this project, please fork the repository and use a feature branch. Pull requests are warmly welcome.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

