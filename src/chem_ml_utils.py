"""Small helper functions for the Chem ML Practice notebooks."""

from __future__ import annotations

from typing import Optional

import numpy as np
from rdkit import Chem
from rdkit.Chem import Descriptors, Crippen, Lipinski, rdMolDescriptors


def mol_from_smiles(smiles: str) -> Optional[Chem.Mol]:
    """Parse a SMILES string into an RDKit molecule, returning None if parsing fails."""
    if not isinstance(smiles, str) or not smiles.strip():
        return None
    return Chem.MolFromSmiles(smiles)


def calculate_basic_descriptors(mol: Chem.Mol) -> dict:
    """Calculate a compact set of interpretable RDKit descriptors."""
    return {
        "MolWt": Descriptors.MolWt(mol),
        "LogP": Crippen.MolLogP(mol),
        "TPSA": rdMolDescriptors.CalcTPSA(mol),
        "HBD": Lipinski.NumHDonors(mol),
        "HBA": Lipinski.NumHAcceptors(mol),
        "RotatableBonds": Lipinski.NumRotatableBonds(mol),
        "HeavyAtomCount": mol.GetNumHeavyAtoms(),
        "RingCount": rdMolDescriptors.CalcNumRings(mol),
        "AromaticRingCount": rdMolDescriptors.CalcNumAromaticRings(mol),
    }


def rmse(y_true, y_pred) -> float:
    """Version-safe RMSE calculation for different scikit-learn releases."""
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    return float(np.sqrt(np.mean((y_true - y_pred) ** 2)))
