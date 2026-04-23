## My Project Proposal
# Team: Alejandro Macia, Kamila Stasiowska

**What we're building:**  
A Flask web application that allows users to search real estate listings by location and analyze potential house flipping deals using key financial metrics such as total cost, profit, and ROI.

**Why we chose this:**  
We are interested in real estate and house flipping, and we wanted to build something we could realistically use in the future to quickly evaluate deals before spending more time researching them.

**Core features:**
- Search for real estate listings by city or ZIP code using an external API
- Display property details including price, beds/baths, and square footage
- Property analysis page where users input deal assumptions (purchase price, rehab cost, resale value, additional costs)
- Calculates total cost, profit, and ROI
- Displays results on a separate page with clear visual indicators
- Basic input validation so the app doesn’t crash

**MVP vs Stretch Goals:**

**MVP:**
- Working Flask app with multiple pages
- Integration with a real estate API to fetch live property data
- Correct deal calculations (profit, total cost, ROI)
- Clean and readable results page with visual indicators

**Stretch Goals:**
- Add more inputs like holding costs or contingency
- Compare multiple deals side by side
- Add a map or location-based feature using a free API
- Improve the UI with better layout and design

**What we don't know yet:**
- How to best structure the AI API call and format the response
- How to design the web app so it looks clean and professional
- How to handle unexpected user input
- How to add additional APIs without making the project too complex