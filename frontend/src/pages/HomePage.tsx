import { useState } from 'react';
import { useMutation } from '@tanstack/react-query';
import { toast } from 'react-hot-toast';
import { QueryInput } from '../components/QueryInput';
import { submitQuery } from '../services/api';
import { QueryResponse } from '../types';

/**
 * HomePage component for querying data
 */
export const HomePage = () => {
  const [queryResult, setQueryResult] = useState<QueryResponse | null>(null);

  const { mutate, isPending } = useMutation({
    mutationFn: submitQuery,
    onSuccess: (data) => {
      setQueryResult(data);
      if (data.error) {
        toast.error(`Error: ${data.error}`);
      }
    },
    onError: (error) => {
      const errorMessage = error instanceof Error 
        ? error.message 
        : 'An unknown error occurred';
      toast.error(`Error: ${errorMessage}`);
    },
  });

  const handleSubmitQuery = (question: string) => {
    mutate(question);
  };

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <div className="mb-8">
        <h2 className="text-2xl font-bold text-gray-900">Natural Language Query</h2>
        <p className="mt-1 text-sm text-gray-500">
          Ask questions about your data in plain English
        </p>
      </div>

      <div className="bg-white shadow overflow-hidden sm:rounded-lg p-6 mb-8">
        <QueryInput onSubmit={handleSubmitQuery} isLoading={isPending} />
      </div>

      {queryResult && (
        <div className="space-y-6">
          <div className="bg-white shadow overflow-hidden sm:rounded-lg p-6">
            <h3 className="text-lg font-medium text-gray-900 mb-4">Generated SQL</h3>
            <pre className="bg-gray-50 p-4 rounded-md overflow-x-auto">
              <code>{queryResult.sql}</code>
            </pre>
          </div>

          <div className="bg-white shadow overflow-hidden sm:rounded-lg p-6">
            <h3 className="text-lg font-medium text-gray-900 mb-4">Results</h3>
            {queryResult.result.length > 0 ? (
              <div className="overflow-x-auto">
                <table className="min-w-full divide-y divide-gray-200">
                  <thead className="bg-gray-50">
                    <tr>
                      {Object.keys(queryResult.result[0]).map((key) => (
                        <th
                          key={key}
                          scope="col"
                          className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
                        >
                          {key}
                        </th>
                      ))}
                    </tr>
                  </thead>
                  <tbody className="bg-white divide-y divide-gray-200">
                    {queryResult.result.map((row, rowIndex) => (
                      <tr key={rowIndex}>
                        {Object.values(row).map((value, colIndex) => (
                          <td
                            key={colIndex}
                            className="px-6 py-4 whitespace-nowrap text-sm text-gray-500"
                          >
                            {String(value)}
                          </td>
                        ))}
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            ) : (
              <p className="text-gray-500">No results found.</p>
            )}
          </div>
        </div>
      )}
    </div>
  );
}; 