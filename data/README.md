# Data directory

This directory is reserved for small public/example datasets only.

The notebooks can also load public datasets directly from URLs or DeepChem loaders. Do not commit private, proprietary, patient, API-key-linked or commercially restricted datasets.

Expected simple CSV schema for custom classification practice:

```csv
name,smiles,label
benzyl acetate,CC(=O)OCC1=CC=CC=C1,1
glucose,C(C1C(C(C(C(O1)O)O)O)O)O,0
```

For regression, use `target` instead of `label`.
