import { useQuery } from '@tanstack/react-query';
import { toast } from 'react-hot-toast';
import { CustomerTable } from '../components/CustomerTable';
import { getCustomers } from '../services/api';
import { CustomerResponse } from '../types';
import React from 'react';

/**
 * CustomersPage component for displaying customer data
 */
export const CustomersPage = () => {
  const { data, isLoading, refetch, error } = useQuery<CustomerResponse>({
    queryKey: ['customers'],
    queryFn: getCustomers,
  });

  // Handle errors with a separate effect
  React.useEffect(() => {
    if (error) {
      const errorMessage = error instanceof Error 
        ? error.message 
        : 'Failed to load customers';
      toast.error(`Error: ${errorMessage}`);
    }
  }, [error]);

  const customers = data?.customers || [];

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <div className="mb-8 flex justify-between items-center">
        <div>
          <h2 className="text-2xl font-bold text-gray-900">Customers</h2>
          <p className="mt-1 text-sm text-gray-500">
            View and manage your customer data
          </p>
        </div>
        <button
          onClick={() => refetch()}
          className="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
          disabled={isLoading}
        >
          {isLoading ? 'Refreshing...' : 'Refresh'}
        </button>
      </div>

      <div className="bg-white shadow overflow-hidden sm:rounded-lg p-6">
        <CustomerTable customers={customers} isLoading={isLoading} />
      </div>
    </div>
  );
}; 