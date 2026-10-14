# Data Dictionary

## Original dataset (data/original/calorie_dataset.csv)

| Column | Type | Unit | Description |
|---|---|---|---|
| protein_g | float | grams | Protein content per serving |
| carbs_g | float | grams | Total carbohydrate content per serving |
| fat_g | float | grams | Total fat content per serving |
| fiber_g | float | grams | Dietary fiber content per serving |
| sugar_g | float | grams | Total sugar content per serving |
| calories | float | kcal | Target variable — total energy per serving |
| calorie_class | string | — | Derived label: low / medium / high. Excluded from modeling. |

## Processed dataset (data/processed/calorie_dataset_processed.csv)

| Column | Type | Unit | Description |
|---|---|---|---|
| protein_g | float | grams | Protein content per serving |
| carbs_g | float | grams | Total carbohydrate content per serving |
| fat_g | float | grams | Total fat content per serving |
| fiber_g | float | grams | Dietary fiber content per serving |
| sugar_g | float | grams | Total sugar content per serving |
| calories | float | kcal | Target variable — total energy per serving |

## Notes
- calorie_class exists in the original dataset but is dropped in the
  processed version because it is derived from calories.
- No missing values, no duplicates, and no impossible values were found.
- Rows: 5000 (both versions).
- Columns: 7 (original), 6 (processed).
- Feature ranges (observed):
  - protein_g: 0.0 to 64.3 g
  - carbs_g: 0.0 to 120.6 g
  - fat_g: 0.0 to 47.4 g
  - fiber_g: 0.0 to 25.9 g
  - sugar_g: 0.0 to 51.1 g
  - calories: 56.0 to 975.0 kcal

## Target
- Variable: calories
- Type: continuous (regression)
- Unit: kilocalories (kcal)