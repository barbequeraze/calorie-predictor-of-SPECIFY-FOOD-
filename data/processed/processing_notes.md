## Source
- Original file: data/original/calorie_dataset.csv
- Rows: 5000
- Columns: 7

## Processing steps 
1. Dropped the calorie_class column.
   Reason: calorie_class is derived from calories, which is the prediction
   target. Using it as a feature would leak the target and produce
   artificially perfect results.

## Checks performed
- Missing values: 0 found across all columns.
- Duplicate rows: 0 found.
- Impossible values: none found. All macro and calorie values are
  non-negative.
- Outliers: extreme calorie values were inspected and verified as
  legitimate low-calorie and high-calorie food items, not data errors.
  No rows were removed.

## Result
- Processed file: data/processed/calorie_dataset_processed.csv
- Rows: 5000 (unchanged)
- Columns: 6
- Final columns: protein_g, carbs_g, fat_g, fiber_g, sugar_g, calories

