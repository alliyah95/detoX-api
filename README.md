<div align="center">
  <img src="" alt="Logo" width="200">

# detoX API

</div>

This API serves as the backend for the [detoX browser extension](https://github.com/alliyah95/detoX) designed to address hate speech detection with a particular focus on election-related and politics-related content in the Philippines. It employs a fine-tuned [RoBERTA Tagalog Base model](https://huggingface.co/jcblaise/roberta-tagalog-base), a variant of the BERT (Bidirectional Encoder Representations from Transformers) model known for its exceptional performance in NLP tasks.

The model was trained using two datasets. The first dataset was a [pre-labeled Filipino hate speech dataset](https://huggingface.co/datasets/hate_speech_filipino). The second dataset consisted of tweets from the 2022 Philippine elections.

## Local Setup and Installation

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

## Usage

1.  Run the app by executing the following command:

    ```
    uvicorn main:app --reload
    ```

2.  To test the API endpoints with a GUI, navigate to the following URL in your browser:
    ```
    http://127.0.0.1:8000/docs#/
    ```

## Authors

-   Danica L. Castro
-   Lenina Jemima V. Dizon
-   Alliyah Joyce M. Sarip
-   Mark Aaron P. Soriano
