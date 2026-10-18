# Test Cases – Simulated Device Monitoring and Alert System

Tested by: Christian Ross Barrios       Date: 17 October 2026

| Test Case | Input or Action | Expected Result | Actual Result | Pass/Fail |
|---|---|---|---|---|
| TC01 | Choose 1 | Five readings: 28, 31, 35, 37, 29 | Showed Reading 1 to 5: 28, 31, 35, 37, 29 °C | Pass |
| TC02 | Choose 2, enter 33 | "Reading added successfully." | Showed "Reading added successfully."; viewing again listed 33 °C as Reading 6 | Pass |
| TC03 | Choose 2, enter abc | Rejected; list unchanged | Showed "Invalid input. Enter a whole number only."; list still had the original 5 readings | Pass |
| TC04 | Choose 2, enter -5 | Rejected; list unchanged | Showed "Invalid reading. Enter a value from 0 to 100."; list still had the original 5 readings | Pass |
| TC05 | Choose 2, enter 120 | Rejected; list unchanged | Showed "Invalid reading. Enter a value from 0 to 100."; list still had the original 5 readings | Pass |
| TC06 | Add 30, then choose 3 | 30 °C -> WARNING | Reading added; classification showed "30 °C -> WARNING" | Pass |
| TC07 | Choose 3 | 35 °C -> WARNING | Showed "35 °C -> WARNING" | Pass |
| TC08 | Choose 4 (initial data) | Total 160, Avg 32.00, Min 28, Max 37, status ATTENTION REQUIRED | Total 160, Average 32.00 °C, Min 28 °C, Max 37 °C, NORMAL 2 (40.00%), WARNING 2 (40.00%), CRITICAL 1 (20.00%), Overall Status: ATTENTION REQUIRED | Pass |
| TC09 | Enter 9 | Error message; menu shown again | Showed "Invalid choice. Please enter a number from 1 to 5." and the menu appeared again | Pass |
| TC10 | Choose 5 | Exit message; program ends | Showed "Thank you for using the Device Monitoring System." and the program ended normally | Pass |

## Extra Tests

| Test Case | Input or Action | Expected Result | Actual Result | Pass/Fail |
|---|---|---|---|---|
| TC11 | Choose 2, press Enter only | Rejected; list unchanged | Showed "Invalid input. The reading cannot be empty." | Pass |
| TC12 | Choose 2, enter 3.5 | Rejected; list unchanged | Showed "Invalid input. Enter a whole number only." | Pass |
| TC13 | Add 33, then choose 4 | 6 readings, total 193, average 32.17 | Showed 6 readings, total 193, average 32.17 °C, WARNING 3 (50.00%) | Pass |

## Bugs Found and Fixed

- No bugs were found during final testing. The hardest tests to pass were the boundary tests TC06 and TC07, because 30 and 35 must both be WARNING. This depends on classify_reading using < for the NORMAL check and <= for the WARNING check. If the second condition were < instead, 35 would wrongly become CRITICAL.