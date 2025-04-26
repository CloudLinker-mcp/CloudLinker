import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { Router, Route, RootRoute, Outlet, RouterProvider } from '@tanstack/react-router';
import { Toaster } from 'react-hot-toast';
import { Header } from './components/Header';
import { HomePage } from './pages/HomePage';
import { CustomersPage } from './pages/CustomersPage';
import { ApiKeySetup } from './components/ApiKeySetup';

// Create a client
const queryClient = new QueryClient();

// Define the root route
const rootRoute = new RootRoute({
  component: () => (
    <div className="min-h-screen bg-gray-100">
      <Header />
      <main>
        <Outlet />
      </main>
      <Toaster position="top-right" />
      <ApiKeySetup />
    </div>
  ),
});

// Define the index route
const indexRoute = new Route({
  getParentRoute: () => rootRoute,
  path: '/',
  component: HomePage,
});

// Define the customers route
const customersRoute = new Route({
  getParentRoute: () => rootRoute,
  path: '/customers',
  component: CustomersPage,
});

// Create the route tree
const routeTree = rootRoute.addChildren([indexRoute, customersRoute]);

// Create the router
const router = new Router({ routeTree });

// Register the router for type safety
declare module '@tanstack/react-router' {
  interface Register {
    router: typeof router;
  }
}

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <RouterProvider router={router} />
    </QueryClientProvider>
  );
}

export default App;
