# Specification & Requirements

## Requirements

### REQ-001: Subtotal Calculation
The service must sum a list of numerical item prices. If the list is empty, the subtotal is 0.0. Negative prices must raise a `ValueError`.

### REQ-002: Tax Application
The service must apply a tax percentage rate (e.g. 0.16 for 16%) to an amount. Negative amounts or tax rates must raise a `ValueError`.

### REQ-003: Percentage Discount (Pending / Issue #1)
The service must support applying a discount percentage (between 0% and 100%) to a subtotal before tax calculation.
