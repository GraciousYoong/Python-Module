"""
A package is reusable code distributed for other programs to use.
A dependency is an external package/library that our project relies on.

importlib
→ Dynamically imports a module by its name.
→ use it to check whether required packages are installed.

ModuleType
→ A type representing a Python module.
→ for type hints when storing imported modules.

NamedTuple
→ Creates a tuple-like structure with named fields.
→ to store the calculated Matrix statistics in a structured way.

"""
import importlib
import sys
from types import ModuleType
from typing import Any, NamedTuple


REQUIRED_PACKAGES = {
    "numpy": "Numerical computation ready",
    "pandas": "Data manipulation ready",
    "matplotlib.pyplot": "Visualization ready",
}


# average_enemies_defeated
#     → average number of enemies defeated
# average_missions_completed
#     → average number of missions completed
# high_defeat_count
#     → number of members who defeated more than 40 enemies
# total_members
#     → total number of simulated members
class MatrixStats(NamedTuple):
    average_enemies_defeated: float
    average_missions_completed: float
    high_defeat_count: int
    total_members: int


def print_missing_dependency(package_name: str) -> None:
    display_name = package_name.split(".")[0]
    print(f"Missing dependency: {display_name}")
    print()
    print("Install with pip:")
    print("python -m pip install -r requirements.txt")
    print()
    print("Or install with Poetry:")
    print("poetry install")
    print("poetry run python loading.py")


def check_dependencies() -> dict[str, ModuleType] | None:
    modules = {}
    print("Checking dependencies:")
    for package_name, message in REQUIRED_PACKAGES.items():
        try:
            module = importlib.import_module(package_name)
        except ImportError:
            print_missing_dependency(package_name)
            return None
        root_package_name = package_name.split(".")[0]
        root_module = importlib.import_module(root_package_name)
        version = getattr(root_module, "__version__", "unknown")
        print(f"[OK] {root_package_name} ({version}) - {message}")
        modules[root_package_name] = root_module
        if package_name == "matplotlib.pyplot":
            modules["matplotlib.pyplot"] = module
    print()
    return modules


# - Generate 1,000 resistance members. Each member has a random
#   number of enemies defeated and missions completed.
# - DataFrame might look conceptually like:

#    enemies_defeated   missions_completed
# 0         23                  8
# 1         28                 12
# 2         17                 10
# 3         31                 15
# ...
# 999       25                 11

# - NumPy's normal() generates values following a normal distribution.

#   loc   → mean (the center/average of the distribution)
#   scale → standard deviation (how spread out the data is)
#     *The smaller the scale, the more tightly the
#         values are concentrated around the center (loc).
#   size  → number of values to generate

# - np.round() rounds the generated decimal values to whole numbers.
# - np.clip() limits values to a specified range.
#   For enemies: 0 → minimum, 50 → maximum
#   For missions: 0 → minimum, 20 → maximum
# - .astype(int) converts the values to integers because
#   enemies and missions cannot be fractions.
# - A normal distribution is approximately bell-shaped:
#   most values are around the mean, while fewer values
#   are further away from the mean.
def simulate_matrix_data(np: ModuleType, pd: ModuleType) -> Any:
    rng = np.random.default_rng(seed=42)
    enemies_defeated = np.clip(
        np.round(
            rng.normal(loc=25, scale=8, size=1000)
        ),
        0,
        50,
    ).astype(int)

    missions_completed = np.clip(
        np.round(
            rng.normal(loc=10, scale=3, size=1000)
        ),
        0,
        20,
    ).astype(int)

    data = {
        "enemies_defeated": enemies_defeated,
        "missions_completed": missions_completed,
    }
    return pd.DataFrame(data)


def analyze_matrix_data(df: Any) -> MatrixStats:
    print("Analyzing Matrix data...")
    print(f"Processing {len(df)} members...\n")

    average_enemies_defeated = float(
        df["enemies_defeated"].mean()
    )
    average_missions_completed = float(
        df["missions_completed"].mean()
    )
    high_defeats = df[df["enemies_defeated"] > 40]

    return MatrixStats(
        average_enemies_defeated=average_enemies_defeated,
        average_missions_completed=average_missions_completed,
        high_defeat_count=len(high_defeats),
        total_members=len(df),
    )


def generate_visualization(
    df: Any,
    stats: MatrixStats,
    plt: ModuleType
) -> None:
    output_file = "matrix_analysis.png"
    print("Generating visualization...")
    plt.figure(figsize=(8, 5))
    plt.hist(df["enemies_defeated"], bins=20)
    plt.title("Matrix Enemies Defeated Distribution")
    plt.xlabel("Enemies Defeated")
    plt.ylabel("Number of Members")
    summary_text = (
        f"Members analyzed: {stats.total_members}\n"
        f"Avg enemies defeated: "
        f"{stats.average_enemies_defeated:.2f}\n"
        f"Avg missions completed: "
        f"{stats.average_missions_completed:.2f}\n"
        f"High defeats (>40): {stats.high_defeat_count}"
    )
    plt.gcf().text(
        0.98, 0.98, summary_text,
        ha="right", va="top", fontsize=9,
        bbox=dict(
            boxstyle="round",
            facecolor="wheat",
            alpha=0.6
        ),
    )
    plt.tight_layout()
    plt.savefig(output_file)
    plt.close()
    print("\nAnalysis complete!")
    print(f"Results saved to: {output_file}")


def main() -> int:
    print("\nLOADING STATUS: Loading programs...\n")
    modules = check_dependencies()
    if modules is None:
        return 1
    np = modules["numpy"]
    pd = modules["pandas"]
    plt = modules["matplotlib.pyplot"]
    df = simulate_matrix_data(np, pd)
    stats = analyze_matrix_data(df)
    generate_visualization(df, stats, plt)
    return 0


if __name__ == "__main__":
    sys.exit(main())
