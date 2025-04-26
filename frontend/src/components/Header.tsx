import { Link } from '@tanstack/react-router';

/**
 * Header component with navigation links
 */
export const Header = () => {
  return (
    <header className="bg-white shadow-sm">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-16">
          <div className="flex">
            <div className="flex-shrink-0 flex items-center">
              <h1 className="text-xl font-bold text-gray-900">CloudLinker</h1>
            </div>
            <nav className="ml-6 flex space-x-8">
              <Link
                to="/"
                className="inline-flex items-center px-1 pt-1 text-sm font-medium text-gray-900"
              >
                Home
              </Link>
              <Link
                to="/customers"
                className="inline-flex items-center px-1 pt-1 text-sm font-medium text-gray-900"
              >
                Customers
              </Link>
            </nav>
          </div>
        </div>
      </div>
    </header>
  );
}; 