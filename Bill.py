from datetime import date
from decimal import Decimal
from dateutil.relativedelta import relativedelta


class Bill:
    def __init__(self, description: str, amount: Decimal, current_date: date, next_date: date=None):
        self.description = description
        self.amount = amount
        self.current_date = current_date
        self.next_date = current_date + relativedelta(months=1) if next_date is None else next_date

    def shift(self, next_date: date=None):
        self.current_date = self.next_date
        self.next_date = self.current_date + relativedelta(months=1) if next_date is None else next_date

    def __str__(self):
        return (
            f"| {self.description:<25} "
            f"| ${self.amount:>10.2f} "
            f"| {str(self.current_date):<12} "
            f"| {str(self.next_date):<12} |"
        )