# CloudLinker Developer UX Dashboard

A modern web application for querying data using natural language and managing customer records.

## Features

- Natural language query interface
- Customer management
- API key authentication
- Responsive design

## Getting Started

### Prerequisites

- Node.js (v16 or higher)
- npm (v7 or higher)
- Backend server running on http://localhost:8000

### Installation

1. Clone the repository
2. Install dependencies:

```bash
npm install
```

3. Start the development server:

```bash
npm run dev
```

4. Open your browser and navigate to http://localhost:5173

## Testing the Application

### API Key Setup

When you first open the application, you'll be prompted to enter an API key. Use one of the following keys from the backend configuration:

- `clave1`
- `clave2`

### Natural Language Queries

1. Navigate to the Home page
2. Enter a natural language query in the text area, such as:
   - "Show me all customers"
   - "How many customers are there?"
   - "List customers created in the last month"

3. Click "Submit Query" to see the generated SQL and results

### Customer Management

1. Navigate to the Customers page
2. View the list of customers
3. Use the "Refresh" button to reload the customer data

## Troubleshooting

If you encounter any issues:

1. Make sure the backend server is running
2. Check that you've entered a valid API key
3. Check the browser console for any error messages
4. Verify that the backend API endpoints are working correctly

## Development

### Project Structure

- `src/components/`: Reusable UI components
- `src/pages/`: Page components
- `src/services/`: API service layer
- `src/lib/`: Utility functions and configurations
- `src/types/`: TypeScript type definitions
