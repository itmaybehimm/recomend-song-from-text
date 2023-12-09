## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/itmaybehimm/recomend-song-from-text

2. Navigate to the cloned directory:
   
   ```bash
    cd recomend-song-from-text
   
3. Run the virtual environment:
   
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```
   
4. Install dependencies:
   
    ```bash
    pip install -r requirements.txt
    ```

5. Install frontend dependencies:
   
    ```bash
    cd frontend
    yarn add
    ```

6. Follow the instructions within each notebook for execution and experimentation.



## AI

Dataset link: [https://www.kaggle.com/datasets/parulpandey/emotion-dataset?select=training.csv]

Rename downloaded dataset to: tweet_emotions.csv

Pretrained models at: [https://drive.google.com/drive/folders/1b4Xe-sRH4INpyxTD04oJio7ao8DYYDhQ?usp=share_link]

Folder structure for dataset:

- 📁 AI
  - 📁 text
    - 📂 data
      - tweet_emotions.csv

### Training model

1. Run the data_processing.ipynb notebook
2. Run the train_model.ipynb notebook to train your own model by tweaking architecture
3. Move model.h5 and countvectorizer.pkl files to recomend-song-from-text/backend/userInput directory

## Frontend

After navigating to frontend folder
  ```bash
    yarn run
  ```

follow instructions afterwards

## Backend

After navigating to backend folder
  ```bash
    python3 manage.py runserver
  ```

## Integration with spotify

