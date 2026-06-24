"""Reusable cheminformatics utilities for the practice notebooks.

The functions are intentionally small and explicit so they remain useful for
learning, debugging and adapting into larger cheminformatics projects.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

import numpy as np
import pandas as pd
from rdkit import Chem
from rdkit.Chem import Crippen, Descriptors, Lipinski, rdMolDescriptors
from rdkit.Chem.rdFingerprintGenerator import GetMorganGenerator


@dataclass(frozen=True)
class MoleculeRecord:
    """Simple molecule record used in examples and tests."""

    name: str
    smiles: str


def smiles_to_mol(smiles: str):
    """Convert a SMILES string into an RDKit Mol object, returning None if invalid."""
    if smiles is None or pd.isna(smiles):
        return None
    try:
        return Chem.MolFromSmiles(str(smiles))
    except Exception:
        return None


def canonical_smiles(smiles: str) -> str | None:
    """Return canonical SMILES, or None for invalid input."""
    mol = smiles_to_mol(smiles)
    if mol is None:
        return None
    return Chem.MolToSmiles(mol, canonical=True)


def calculate_basic_descriptors(mol) -> dict[str, float]:
    """Calculate a compact descriptor set used across the notebooks."""
    return {
        "MolWt": Descriptors.MolWt(mol),
        "LogP": Crippen.MolLogP(mol),
        "TPSA": rdMolDescriptors.CalcTPSA(mol),
        "HBD": Lipinski.NumHDonors(mol),
        "HBA": Lipinski.NumHAcceptors(mol),
        "RotatableBonds": Lipinski.NumRotatableBonds(mol),
        "HeavyAtomCount": Lipinski.HeavyAtomCount(mol),
        "RingCount": Lipinski.RingCount(mol),
        "AromaticRingCount": rdMolDescriptors.CalcNumAromaticRings(mol),
        "FractionCSP3": rdMolDescriptors.CalcFractionCSP3(mol),
    }


def descriptor_dataframe(mols: Iterable) -> pd.DataFrame:
    """Convert an iterable of RDKit molecules into a descriptor DataFrame."""
    return pd.DataFrame([calculate_basic_descriptors(mol) for mol in mols])


def lipinski_summary(mol) -> dict[str, object]:
    """Return Lipinski Rule-of-Five values and pass/fail summary."""
    mw = Descriptors.MolWt(mol)
    logp = Crippen.MolLogP(mol)
    hbd = Lipinski.NumHDonors(mol)
    hba = Lipinski.NumHAcceptors(mol)
    violations = int(mw > 500) + int(logp > 5) + int(hbd > 5) + int(hba > 10)
    return {
        "MolWt": mw,
        "LogP": logp,
        "HBD": hbd,
        "HBA": hba,
        "LipinskiViolations": violations,
        "LipinskiPass": violations <= 1,
    }


def morgan_fingerprint_array(mols: Iterable, radius: int = 2, fp_size: int = 2048) -> np.ndarray:
    """Convert RDKit molecules into a binary Morgan fingerprint matrix."""
    generator = GetMorganGenerator(radius=radius, fpSize=fp_size)
    fps = [np.asarray(generator.GetFingerprint(mol), dtype=np.float32) for mol in mols]
    return np.vstack(fps)


def clean_molecule_dataframe(
    df: pd.DataFrame,
    smiles_col: str = "smiles",
    name_col: str | None = "name",
    drop_duplicates: bool = True,
) -> pd.DataFrame:
    """Validate SMILES, add Mol/canonical SMILES columns and optionally deduplicate."""
    if smiles_col not in df.columns:
        raise ValueError(f"Missing SMILES column: {smiles_col}")

    clean = df.copy()
    clean["mol"] = clean[smiles_col].apply(smiles_to_mol)
    clean = clean[clean["mol"].notnull()].reset_index(drop=True)
    clean["canonical_smiles"] = clean["mol"].apply(lambda mol: Chem.MolToSmiles(mol, canonical=True))

    if drop_duplicates:
        clean = clean.drop_duplicates(subset="canonical_smiles").reset_index(drop=True)

    if name_col and name_col not in clean.columns:
        clean[name_col] = [f"molecule_{i}" for i in range(len(clean))]

    return clean
