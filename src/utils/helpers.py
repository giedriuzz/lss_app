def validate_input(data):
    """Validate input data for correctness."""
    if not data:
        raise ValueError("Input data cannot be empty.")
    # Add more validation rules as needed

def format_date(date):
    """Format a date object to a string."""
    return date.strftime("%Y-%m-%d")

def log_message(message):
    """Log a message to the console."""
    print(f"[LOG] {message}")