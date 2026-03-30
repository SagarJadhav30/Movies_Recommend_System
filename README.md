# Movies_Recommend_System
A machine learning–based movie recommendation system that suggests personalized movies to users


# 🎬 Movie Recommender System

A simple, interactive movie recommendation system built with Streamlit. This app suggests movies similar to your selection using precomputed similarity data.

## Features
- Select a movie from a dropdown and get 5 similar movie recommendations
- Fast, interactive UI powered by Streamlit
- Loads movie data and similarity matrix from local pickle files

## Demo
![Demo Screenshot](demo_screenshot.png) <!-- Add a screenshot if available -->

## Getting Started

### Prerequisites
- Python 3.7+
- Required Python packages: `streamlit`, `pandas`
- `movies.pkl` and `similarity.pkl` files in the project directory

### Installation
1. Clone this repository:
	```bash
	git clone https://github.com/yourusername/Movies_Recommneder_System.git
	cd Movies_Recommneder_System
	```
2. (Optional) Create and activate a virtual environment:
	```bash
	python -m venv .venv
	source .venv/bin/activate  # On Windows: .venv\Scripts\activate
	```
3. Install dependencies:
	```bash
	pip install streamlit pandas
	```

### Usage
1. Ensure `movies.pkl` and `similarity.pkl` are present in the project directory.
2. Run the Streamlit app:
	```bash
	streamlit run main.py
	```
3. Open the provided local URL in your browser and start exploring movie recommendations!

## File Structure
- `main.py` — Streamlit app source code
- `movies.pkl` — Pickle file containing movie data (Pandas DataFrame with at least a 'title' column)
- `similarity.pkl` — Pickle file containing similarity matrix (2D array or DataFrame)

## Notes
- If you don't have the `.pkl` files, you will need to generate them using your own dataset and similarity computation logic.
- The app will show errors if these files are missing or incorrectly formatted.

## License
MIT License

## Credits
- Built with [Streamlit](https://streamlit.io/)
- Developed by Your Name
