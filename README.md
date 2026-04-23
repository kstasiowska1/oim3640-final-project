# FlipFinder  
A Flask web application that allows users to search real estate listings and analyze potential house flipping deals.

## What This Project Does
FlipFinder helps users quickly evaluate real estate investment opportunities.

Users can:
- Search for properties by city or ZIP code
- View listing details (price, beds/baths, square footage)
- Select a property to analyze
- Input deal assumptions (purchase price, rehab cost, resale value, etc.)
- See calculated results including:
  - Total cost
  - Estimated profit
  - Return on investment (ROI)
- View a color-coded deal rating:
  - Green = Strong
  - Yellow = Moderate
  - Red = Risky

## How to Install and Run
### 1. Clone the repository
"```bash
git clone https://github.com/kstasiowska1 oim3640-final-project.git
cd oim3640-final-project"

### 2. Install dependencies
"pip install -r requirements.txt"

### 3. Create an .env file and add two API keys
- Mapbox API Key
- RapidAI API Key

### 4. Run the app
"python app.py"

## OR Follow this link: 
https://oim3640-final-project.onrender.com