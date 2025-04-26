import { apiClient } from '../lib/api';
import { QueryRequest, QueryResponse, CustomerResponse } from '../types';

/**
 * Submit a natural language query to the backend
 * @param question The natural language question to process
 * @returns The SQL and result set
 */
export const submitQuery = async (question: string): Promise<QueryResponse> => {
  const request: QueryRequest = { question };
  const response = await apiClient.post<QueryResponse>('/query', request);
  return response.data;
};

/**
 * Fetch all customers from the backend
 * @returns A list of customers
 */
export const getCustomers = async (): Promise<CustomerResponse> => {
  const response = await apiClient.get<CustomerResponse>('/customers');
  return response.data;
}; 