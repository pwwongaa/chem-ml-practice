"""
Utility functions for chemistry machine learning practice.

These functions are intentionally lightweight and suitable for starter notebooks.
They assume RDKit is installed in the active Python environment.
"""

from __future__ import annotations

from typing import Iterable, Optional

import pandas as pd


def smiles_to_mol(smiles: str):
    """Convert a SMILES string into an RDKit Mol object.

    Returns None if the SMILES string is invalid or RDKit is unavailable.
    """
    try:
        from rdkit import Chem
    except ImportError:
        return None

    if not isinstance(smiles, str) or not smiles.strip():
        return None

    return Chem.MolFromSmiles(smiles)


def calculate_basic_descriptors(smiles: str) -> dict:
    """Calculate a small set of common molecular descriptors from a SMILES string.

    The returned dictionary is suitable for conversion into a pandas DataFrame.
    """
    mol = smiles_to_mol(smiles)

    if mol is None:
        return {
            "valid_molecule": False,
            "mol_weight": None,
            "logp": None,
            "h_donors": None,
            "h_acceptors": None,
            "tpsa": None,
            "rotatable_bonds": None,
        }

    from rdkit.Chem import Descriptors, Crippen, Lipinski, rdMolDescriptors

    return {
        "valid_molecule": True,
        "mol_weight": Descriptors.MolWt(mol),
        "logp": Crippen.MolLogP(mol),
        "h_donors": Lipinski.NumHDonors(mol),
        "h_acceptors": Lipinski.NumHAcceptors(mol),
        "tpsa": rdMolDescriptors.CalcTPSA(mol),
        "rotatable_bonds": Lipinski.NumRotatableBonds(mol),
    }


def build_descriptor_table(
    data: pd.DataFrame,
    smiles_column: str = "smiles",
    keep_original: bool = True,
) -> pd.DataFrame:
    """Create a descriptor table from a DataFrame containing a SMILES column."""
    if smiles_column not in data.columns:
        raise ValueError(f"Column not found: {smiles_column}")

    descriptor_rows = [
        calculate_basic_descriptors(smiles)
        for smiles in data[smiles_column]
    ]

    descriptor_df = pd.DataFrame(descriptor_rows)

    if keep_original:
        return pd.concat([data.reset_index(drop=True), descriptor_df], axis=1)

    return descriptor_df


def get_numeric_feature_columns(
    data: pd.DataFrame,
    exclude: Optional[Iterable[str]] = None,
) -> list[str]:
    """Return numeric feature columns, optionally excluding target or metadata columns."""
    exclude_set = set(exclude or [])
    return [
        col for col in data.select_dtypes(include="number").columns
        if col not in exclude_set
    ]
