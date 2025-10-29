# Wizualizacje Ulg Pro-innowacyjnych

React application for visualizing Polish innovation tax relief data (2017-2024).

## Overview

This application generates 21 interactive charts analyzing Polish innovation tax reliefs:
- **B+R (R&D Relief)**: Main tax relief for research and development
- **IP Box**: Intellectual property tax relief
- **2022 Reliefs**: Robotyzacja, Ekspansja, CSR, Prototyp

## Data Source

Data from Ministry of Finance (KAS), current as of October 14, 2025.

## Installation

```bash
# Install dependencies
npm install
```

## Running the Application

```bash
# Start development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

The application will be available at `http://localhost:3000`

## Exporting Charts

Each chart has an "Eksportuj jako PNG" button that exports the chart as a high-resolution PNG image (300 DPI equivalent).

## Chart List

### Core Charts (1-12)

1. **Chart 1**: B+R Participant Growth (2017-2024)
2. **Chart 2**: B+R Deduction Amounts (2017-2024)
3. **Chart 3**: CIT vs PIT Breakdown (2024)
4. **Chart 4**: All 6 Reliefs Comparison (2024)
5. **Chart 5**: Ecosystem Time Series
6. **Chart 6**: B+R Growth Rates
7. **Chart 7**: IP Box Time Series
8. **Chart 8**: 2022 Reliefs Comparison
9. **Chart 9**: Average Deduction per Participant
10. **Chart 10**: CIT Dominance Over Time
11. **Chart 11**: IP Box CIT vs PIT Distribution
12. **Chart 12**: Market Share by Relief (2024)

### Additional Charts (13-21)

13. **Chart 13**: B+R CIT Amount Growth
14. **Chart 14**: B+R PIT Amount Growth
15. **Chart 15**: IP Box Amount Distribution
16. **Chart 16**: 2022 Reliefs Amount Comparison
17. **Chart 17**: CSR Growth Trend (Fastest Growing)
18. **Chart 18**: Robotyzacja Trend (Largest 2022 Relief)
19. **Chart 19**: Prototyp Decline (Declining Relief)
20. **Chart 20**: Cumulative Participants All Reliefs
21. **Chart 21**: Cumulative Amounts All Reliefs

## Technology Stack

- **React 18**: UI framework
- **Vite**: Build tool
- **Recharts**: Chart library
- **html-to-image**: PNG export functionality

## File Structure

```
charts/
├── src/
│   ├── components/
│   │   ├── AllCharts.jsx      # All chart components
│   │   └── ChartWrapper.jsx   # Reusable chart wrapper
│   ├── data.js                 # Data loading and transformation
│   ├── App.jsx                 # Main application component
│   ├── App.css                 # Styling
│   └── main.jsx                # Entry point
├── index.html                  # HTML template
├── package.json                # Dependencies
└── vite.config.js              # Vite configuration
```

## Data Updates

To update the data:
1. Run the Python export script: `python ../scripts/export_chart_data.py`
2. Restart the development server

The chart data is automatically imported from `../data/chart-data.json`.
