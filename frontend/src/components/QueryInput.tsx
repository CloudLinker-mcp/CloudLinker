import { useState } from 'react';

interface QueryInputProps {
  onSubmit: (question: string) => void;
  isLoading: boolean;
}

/**
 * QueryInput component for submitting natural language queries
 * @param onSubmit Function to call when the query is submitted
 * @param isLoading Whether the query is currently loading
 */
export const QueryInput = ({ onSubmit, isLoading }: QueryInputProps) => {
  const [question, setQuestion] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (question.trim()) {
      onSubmit(question);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <div>
        <label htmlFor="question" className="block text-sm font-medium text-gray-700">
          Ask a question about your data
        </label>
        <div className="mt-1">
          <textarea
            id="question"
            name="question"
            rows={3}
            className="shadow-sm focus:ring-indigo-500 focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md"
            placeholder="e.g., Show me all customers who signed up in the last month"
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            disabled={isLoading}
          />
        </div>
      </div>
      <div>
        <button
          type="submit"
          className="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
          disabled={isLoading || !question.trim()}
        >
          {isLoading ? 'Processing...' : 'Submit Query'}
        </button>
      </div>
    </form>
  );
}; 