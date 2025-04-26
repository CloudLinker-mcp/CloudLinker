import { useState, useEffect } from 'react';

/**
 * ApiKeySetup component for setting up the API key
 */
export const ApiKeySetup = () => {
  const [apiKey, setApiKey] = useState('');
  const [isSetup, setIsSetup] = useState(false);

  useEffect(() => {
    const storedApiKey = localStorage.getItem('api_key');
    if (storedApiKey) {
      setApiKey(storedApiKey);
      setIsSetup(true);
    }
  }, []);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (apiKey.trim()) {
      localStorage.setItem('api_key', apiKey.trim());
      setIsSetup(true);
    }
  };

  if (isSetup) {
    return null;
  }

  return (
    <div className="fixed inset-0 bg-gray-500 bg-opacity-75 flex items-center justify-center p-4">
      <div className="bg-white rounded-lg shadow-xl p-6 max-w-md w-full">
        <h2 className="text-xl font-bold text-gray-900 mb-4">API Key Setup</h2>
        <p className="text-gray-600 mb-4">
          Please enter your API key to continue. This is required to access the API.
        </p>
        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label htmlFor="apiKey" className="block text-sm font-medium text-gray-700">
              API Key
            </label>
            <input
              type="text"
              id="apiKey"
              value={apiKey}
              onChange={(e) => setApiKey(e.target.value)}
              className="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
              placeholder="Enter your API key"
              required
            />
          </div>
          <div>
            <button
              type="submit"
              className="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
            >
              Save API Key
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}; 