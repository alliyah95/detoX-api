<div align="center">
  <img src="https://github.com/alliyah95/detoX-api/assets/74038500/2e4cf664-3f92-4acb-a514-6bb26f30a8b3" alt="detoX Logo" width="200">

# detoX API

</div>

This API serves as the backend for the [detoX browser extension](https://github.com/alliyah95/detoX) designed to address hate speech detection with a particular focus on election-related and politics-related content in the Philippines. It employs a fine-tuned [RoBERTA Tagalog Base model](https://huggingface.co/jcblaise/roberta-tagalog-base), a variant of the BERT (Bidirectional Encoder Representations from Transformers) model known for its exceptional performance in NLP tasks.

The model was trained using a [combined dataset](https://huggingface.co/datasets/mapsoriano/2016_2022_hate_speech_filipino) from two sources. The first dataset was a [pre-labeled Filipino hate speech dataset](https://huggingface.co/datasets/hate_speech_filipino). The second dataset consisted of newly crawled 2022 Philippine Presidential Elections-related Tweets.

## 📄 Contents

-   [🌐 Relevant Links](#🌐-relevant-links)
    1. [🗂️ Datasets](#🗂️-datasets)
    2. [🤖 Models](#🤖-models)
    3. [🧰 Browser Extension](#🧰-browser-extension)
-   [💻 Local Setup and Installation](#⚙-local-setup-and-installation)
-   [🔍 Endpoints](#🔍-endpoints)
-   [🛠️ Built With](#🛠️-built-with)
-   [💙 Acknowledgements](#💙-acknowledgements)
-   [🧠 Authors](#🧠-authors)

## 🌐 Relevant Links

### 🗂️ Datasets

-   **Hate Speech Filipino:** [hate_speech_filipino](https://huggingface.co/datasets/hate_speech_filipino)
-   **Combined Dataset:** [mapsoriano/2016_2022_hate_speech_filipino](https://huggingface.co/datasets/mapsoriano/2016_2022_hate_speech_filipino)

### 🤖 Models

-   **RoBERTA Tagalog Base Model:** [jcblaise/roberta-tagalog-base](https://huggingface.co/jcblaise/roberta-tagalog-base)
-   **Fine-tuned Model:** [mapsoriano/roberta-tagalog-base-philippine-elections-2016-2022-hate-speech](https://huggingface.co/mapsoriano/roberta-tagalog-base-philippine-elections-2016-2022-hate-speech)

### 🧰 Browser Extension

-   **Development repo:** [alliyah95/detoX](https://github.com/alliyah95/detoX)
-   **Live:** [detoX](https://chrome.google.com/webstore/detail/detox/efibkphbodijlgbhflloachnigfmgfdi)

## 💻 Local Setup and Installation

1. Download or clone the repository to your local machine using the following command:

    ```
    git clone https://github.com/alliyah95/detoX-api.git
    ```

2. Navigate to the project directory:

    ```
    cd detoX-api
    ```

3. Install the project dependencies:

    ```
    pip install -r requirements.txt
    ```

4. Run the app by executing the following command:

    ```
    uvicorn main:app --reload
    ```

5. To test the API endpoints with a GUI, navigate to the following URL in your browser. The default port is `8000`.
    ```
    http://127.0.0.1:<PORT>/docs#/
    ```

## 🔍 Endpoints

### `/` (Root endpoint)

-   Used for checking whether the server is running.

    #### Response:

    ```json
    {
        "1": "Server is up and running"
    }
    ```

### `/api/v1/detect`

-   Returns the result of the hate speech detection.

    #### Parameter:

    `?content` - the text content used for hate speech classification.

    #### Example:

    ```
    /api/v1/detect?content=hahaha%20basta%20pulangaw%20bobo
    ```

    #### Response:

    ```json
    {
        "result": 1
    }
    ```

## 🛠️ Built With

<img src="https://skillicons.dev/icons?i=python,pytorch,fastapi" alt="Tools used for building the detoX API">

## 💙 Acknowledgements

| Name                           | Contribution                                                                     |
| ------------------------------ | -------------------------------------------------------------------------------- |
| 🌟 Dr. Mary Jane Rabena        | Our thesis adviser                                                               |
| 🌟 Dr. Arlan Dela Cruz         | For sharing his expertise in research                                            |
| 🌟 Ms. Abijah Louise Dela Cruz | For validating our 2022 dataset                                                  |
| 🌟 Dr. Ocirne Jun-Jun Liwanag  | For evaluating our browser extension                                             |
| 🌟 Mr. Arvin del Rosario       | For evaluating our browser extension                                             |
| 🌟 Mr. John Montes             | For evaluating our browser extension                                             |
| 🌟 Mr. Nelson Dizon            | For evaluating our browser extension                                             |
| 🌟 Mr. Alberto Castro Jr.      | For evaluating our browser extension                                             |
| 🌟 Mr. Blaise Cruz             | Publisher of the RoBERTa Tagalog Base model and the Hate Speech Filipino Dataset |

## 🧠 Authors

-   👧 Danica L. Castro
-   👧 Lenina Jemima V. Dizon
-   👧 Alliyah Joyce M. Sarip
-   👦 Mark Aaron P. Soriano
