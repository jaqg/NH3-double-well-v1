# Student Guide — Working on NH3-double-well-v1

This guide walks you through setting up the project, running the code, and
contributing your work via GitHub pull requests.

**Supervisor:** Jose Antonio Quinonero Gris — Universidad de Murcia
**Upstream repo:** https://github.com/jaqg/NH3-double-well-v1

---

## 1. Prerequisites

Install the following before starting:

```bash
# Arch Linux
sudo pacman -S git gfortran lapack python python-matplotlib python-numpy

# Ubuntu / Debian
sudo apt install git gfortran liblapack-dev libblas-dev python3 python3-matplotlib python3-numpy

# macOS (Homebrew)
brew install git gcc lapack python && pip3 install matplotlib numpy
```

---

## 2. Fork and Clone

### 2.1 Fork on GitHub

Go to https://github.com/jaqg/NH3-double-well-v1 and click **Fork** (top-right).
This creates your own copy at `https://github.com/<your-username>/NH3-double-well-v1`.

### 2.2 Clone your fork

```bash
git clone git@github.com:<your-username>/NH3-double-well-v1.git
cd NH3-double-well-v1
```

### 2.3 Add the supervisor's repo as upstream

```bash
git remote add upstream git@github.com:jaqg/NH3-double-well-v1.git
git remote -v   # should show both origin (yours) and upstream (Jose's)
```

---

## 3. Build and Run

### 3.1 Compile

```bash
cd src
make          # standard build
make debug    # debug build (extra runtime checks)
make clean    # remove compiled files
```

The executable `QuTu` is created inside `src/build/`.

### 3.2 Configure

Edit the `INPUT` file in the project root to set the simulation parameters:

```
N_max = 200          # number of basis functions
xe    = 0.3816       # equilibrium position (Angstroms)
Vb    = 2028.6       # barrier height (cm^-1)
```

### 3.3 Run

```bash
./src/build/QuTu
```

Output files are written to `src/data/` automatically.

### 3.4 Make the executable accessible from anywhere

After compiling, you can run `QuTu` from any directory using one of two approaches:

**Option A — Symlink in the project root (recommended)**

Create a symlink in the project root pointing to the compiled binary:

```bash
ln -sf src/build/QuTu QuTu
./QuTu        # run from the project root
```

The symlink is gitignored, so it won't appear in your commits. Recreate it
after each `make clean && make`.

**Option B — Add the build directory to your `$PATH`**

Add this line to your shell config file (`~/.bashrc`, `~/.zshrc`, or `~/.config/fish/config.fish`):

```bash
# bash / zsh
export PATH="$PATH:/absolute/path/to/NH3-double-well-v1/src/build"

# fish
fish_add_path /absolute/path/to/NH3-double-well-v1/src/build
```

Then reload your shell (`source ~/.bashrc` or open a new terminal) and run:

```bash
QuTu          # works from any directory
```

Replace `/absolute/path/to/NH3-double-well-v1` with the actual path on your machine
(run `pwd` from the project root to get it).

### 3.4 Visualise results

```bash
python scripts/static/potential.py       # plot the double-well potential
python scripts/static/eigenstates.py     # plot wavefunctions
python scripts/static/survival.py        # survival probability
python scripts/static/convergence.py     # energy convergence vs N
```

---

## 4. Development Workflow

**Never commit directly to `main`.** Always work on a dedicated branch.

### 4.1 Start from an up-to-date main

```bash
git checkout main
git pull upstream main        # get latest changes from supervisor
git push origin main          # keep your fork in sync
```

### 4.2 Create a feature branch

Name your branch descriptively:

```bash
git checkout -b feature/assymetric-potential
# or
git checkout -b fix/convergence-plot
```

### 4.3 Make changes, commit often

```bash
# after editing files:
git add src/QuTu.f90
git commit -m "feat: add assymetric potential"
```

Good commit message format:
- `feat:` — new feature
- `fix:` — bug fix
- `refactor:` — code restructuring without behaviour change
- `docs:` — documentation only

### 4.4 Push your branch to your fork

```bash
git push origin feature/assymetric-potential
```

### 4.5 Open a Pull Request

1. Go to https://github.com/jaqg/NH3-double-well-v1
2. Click **"Compare & pull request"** (GitHub shows this automatically after a push)
3. Set the base branch to **`develop`** (not `main`)
4. Write a short description of what you changed and why
5. Click **"Create pull request"**

Your supervisor will review, leave comments, and merge when ready.

---

## 5. Keeping Your Fork Up to Date

After your supervisor merges other changes into the upstream repo:

```bash
git fetch upstream
git checkout main
git merge upstream/main
git push origin main

# also update develop:
git checkout develop
git merge upstream/develop
git push origin develop
```

---

## 6. Project Structure

```
NH3-double-well-v1/
├── INPUT                      # simulation parameters (edit this)
├── src/
│   ├── QuTu.f90               # main Fortran program
│   ├── Makefile               # build system
│   ├── modules/               # Fortran modules (constants, hamiltonian, etc.)
│   └── data/                  # output files (auto-created, gitignored)
├── scripts/
│   ├── static/                # Python plotting scripts
│   └── animations/            # wave packet animation scripts
├── docs/                      # documentation
├── examples/                  # worked examples
└── tutorial/                  # step-by-step tutorial
```

---

## 7. Getting Help

- Open an **Issue** on https://github.com/jaqg/NH3-double-well-v1/issues
  to report a bug or ask a question.
- Tag your supervisor (`@jaqg`) in pull request comments for specific questions.
- See the physics background in `docs/` and the `INPUT` file documentation.
