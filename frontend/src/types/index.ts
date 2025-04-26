// Query types
export interface QueryRequest {
  question: string;
  db?: string;
}

export interface QueryResponse {
  sql: string;
  result: any[];
  error?: string;
}

// Customer types
export interface Customer {
  id: number;
  name: string;
  email: string;
  created_at: string;
}

export interface CustomerResponse {
  customers: Customer[];
}
