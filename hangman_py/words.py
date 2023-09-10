words=["camel","advard","baboon","beach","mountain","forest","space","castle","superhero","fruit","animal","sports","music","food","vehicle","occupation","mythology","technology","countries","movies","books","colors","emotions"]
gussedrwords=[]

def get_days_in_months(year):
    """
    Returns a list of the number of days in each month of the given year.

    Args:
        year (int): The year for which to determine the number of days in each month.

    Returns:
        list: A list containing the number of days in each month of the given year.
              The list follows the order of months from January to December.

    Example:
        >>> get_days_in_months(2023)
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    """
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year):
        # February has 29 days in a leap year
        days_in_month[1] = 29
    return days_in_month