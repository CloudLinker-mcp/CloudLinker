"""SQL sanitizer utility.

This module provides functions to check if a SQL query is safe to execute.
"""

import re
from typing import List

# Keywords that are not allowed in queries
BLOCKED_KEYWORDS = [
    "UPDATE", "DELETE", "INSERT", "DROP", "TRUNCATE", "ALTER", "CREATE", "GRANT",
    "REVOKE", "EXECUTE", "EXEC", "MERGE", "REPLACE", "LOAD", "COPY", "LOCK",
    "UNLOCK", "COMMIT", "ROLLBACK", "SAVEPOINT", "SET", "SHOW", "USE", "DESCRIBE",
    "EXPLAIN", "HELP", "SHUTDOWN", "KILL", "FLUSH", "RESET", "PURGE", "OPTIMIZE",
    "REPAIR", "ANALYZE", "CHECK", "CHECKSUM", "BACKUP", "RESTORE", "IMPORT",
    "EXPORT", "DUMP", "LOAD", "BULK", "INSERT", "BULK", "INSERT", "BULK", "INSERT"
]

def is_safe_select(sql: str) -> bool:
    """Check if a SQL query is safe to execute.
    
    Args:
        sql: The SQL query to check
        
    Returns:
        bool: True if the query is safe, False otherwise
    """
    # Normalize the SQL query
    sql = sql.upper().strip()
    
    # Check if the query starts with SELECT
    if not sql.startswith("SELECT"):
        return False
    
    # Check for semicolons (SQL injection attempt)
    if ";" in sql:
        return False
    
    # Check for blocked keywords
    for keyword in BLOCKED_KEYWORDS:
        # Use word boundary to avoid false positives
        pattern = r'\b' + re.escape(keyword) + r'\b'
        if re.search(pattern, sql):
            return False
    
    # Check for UNION (SQL injection attempt)
    if "UNION" in sql:
        return False
    
    # Check for comments (SQL injection attempt)
    if "--" in sql or "/*" in sql or "*/" in sql:
        return False
    
    return True 