# QuTu — Quantum Tunnelling Simulator

Variational solver for the 1D double-well potential. Designed for the study of
quantum tunnelling in the NH₃ umbrella inversion mode, with full support for
isotope variants (e.g., ND₃).

**Method:** Harmonic oscillator basis expansion + LAPACK diagonalization.
**Language:** Fortran 2008 (core) + Python 3 (visualization).

---

## Quick start

```bash
# 1. Compile
cd src && make
cd ..

# 2. Generate a reference INPUT with NH₃ defaults
./src/QuTu --help > INPUT

# 3. Run
./src/QuTu

# 4. Visualize
python scripts/static/potential.py
python scripts/static/eigenstates.py
python scripts/static/survival.py
```

---

## Directory structure

```
QuTu/
├── INPUT                  ← Main input file (edit this)
├── src/
│   ├── QuTu.f90           ← Main program
│   ├── Makefile
│   └── modules/           ← Fortran modules
├── scripts/
│   ├── static/            ← Publication-quality figures
│   ├── interactive/       ← Interactive matplotlib tools
│   └── animations/        ← Wavepacket animations
├── tutorial/
│   ├── INPUT              ← NH₃ input for the tutorial
│   └── tutorial_NH3.md   ← Step-by-step NH₃ tutorial
├── examples/
│   └── ND3/
│       └── INPUT          ← Ready-to-run ND₃ example
└── docs/
    ├── manual.tex         ← Full technical manual (LaTeX)
    └── manual.pdf         ← Compiled PDF
```

---

## INPUT format

The `INPUT` file uses `key = value` syntax; lines starting with `#` are comments.

```
N_max = 200          # basis size
xe    = 0.3816       # [Å]
Vb    = 2028.6       # [cm⁻¹]
mass_H = 1.00782503207
mass_N = 14.0030740048
xmin = -5.0  xmax = 5.0  dx = 0.02   # grid [a₀]
```

Run `./src/QuTu --help` to print the full annotated template.

---

## Output files

All output is written to `output/` (created automatically):

| File pattern | Contents |
|---|---|
| `out-energias_cm-1.dat` | Eigenvalues in cm⁻¹ |
| `out-funciones_pares_*.dat` | Even eigenfunctions |
| `out-funciones_impares_*.dat` | Odd eigenfunctions |
| `out-densidad_prob_*.dat` | Probability densities |
| `out-prob_sup_alfa=*.dat` | Survival probability P(t) |
| `out-val_esp_x_alfa=*.dat` | Expectation value ⟨x⟩(t) |
| `out-N_vs_W*.dat` | Energy vs basis size (convergence) |

---

## Visualization scripts

All scripts are in `scripts/`. They read from `output/` by default.

**Static (`scripts/static/`):**

| Script | Output |
|--------|--------|
| `potential.py` | V(x) with energy levels |
| `eigenstates.py` | Eigenfunctions Φₙ(x) |
| `densities.py` | Probability densities |
| `convergence.py` | Energy convergence vs N |
| `wavepackets.py` | 4-state wavepackets |
| `survival.py` | Survival probability |
| `expectation_x.py` | ⟨x⟩(t) |

**Interactive (`scripts/interactive/`):**
`interactive_eigenstates.py`, `interactive_wavepackets.py`, `interactive_dynamics.py`

**Animations (`scripts/animations/`):**
`wavepacket_animation.py` — animated wavepacket propagation

---

## Tutorial and examples

- **`tutorial/tutorial_NH3.md`** — Complete step-by-step tutorial for NH₃.
- **`examples/ND3/`** — Ready-to-run ND₃ example showing the isotope effect
  on tunnelling (ΔE ≈ 20× smaller than NH₃).

---

## Documentation

The full technical manual is in `docs/manual.tex` (compile with `make` in `docs/`).
It covers the theoretical background, program structure, wave packet dynamics,
and the NH₃ tutorial and ND₃ example.

---

## Dependencies

| Tool | Version | Purpose |
|------|---------|---------|
| gfortran | ≥ 7 | Fortran compiler |
| LAPACK + BLAS | any | Matrix diagonalization |
| Python | ≥ 3.8 | Visualization |
| matplotlib, numpy | latest | Plot scripts |

---

## Author

Jose Antonio Quinonero Gris
