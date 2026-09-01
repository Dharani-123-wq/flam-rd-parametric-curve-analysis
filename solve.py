import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
from scipy.optimize import differential_evolution


# ============================================================
# FLAM R&D ASSIGNMENT
# PARAMETRIC CURVE PARAMETER ESTIMATION
# ============================================================

# Create plots folder if it does not already exist
os.makedirs("plots", exist_ok=True)


# ============================================================
# FUNCTION TO GENERATE THE PARAMETRIC CURVE
# ============================================================

def generate_curve(t, theta, M, X):
    """
    Generate x and y coordinates using the given parametric equation.

    Parameters:
        t     : Parameter values
        theta : Rotation angle in radians
        M     : Exponential growth/decay parameter
        X     : Horizontal shift
    """

    x = (
        t * np.cos(theta)
        - np.exp(M * t) * np.sin(0.3 * t) * np.sin(theta)
        + X
    )

    y = (
        42
        + t * np.sin(theta)
        + np.exp(M * t) * np.sin(0.3 * t) * np.cos(theta)
    )

    return x, y


# ============================================================
# STEP 1: LOAD THE DATASET
# ============================================================

data = pd.read_csv("xy_data.csv")

x_data = data["x"].values
y_data = data["y"].values

print("=" * 60)
print("FLAM R&D PARAMETRIC CURVE ANALYSIS")
print("=" * 60)

print(f"\nNumber of data points: {len(data)}")
print(f"Columns: {list(data.columns)}")

print("\nFirst 5 rows:")
print(data.head())


# ============================================================
# STEP 2: VISUALIZE AND SAVE THE GIVEN DATA
# ============================================================

plt.figure(figsize=(10, 6))

plt.scatter(
    x_data,
    y_data,
    s=10,
    label="Given Data Points"
)

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Visualization of the Given Parametric Curve")
plt.legend()
plt.grid(True)
plt.axis("equal")

plt.savefig(
    "plots/given_data.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("\nSaved: plots/given_data.png")


# ============================================================
# STEP 3: DEFINE THE LOSS FUNCTION
# ============================================================

def calculate_loss(params):
    """
    Calculate the L1 loss for a given set of parameters.

    The observed data is transformed into coordinates aligned
    with the parametric curve.
    """

    theta, M, X = params

    # Estimate t by projecting points onto the main direction
    t_estimated = (
        (x_data - X) * np.cos(theta)
        + (y_data - 42) * np.sin(theta)
    )

    # Expected perpendicular wave component
    expected_wave = (
        np.exp(M * t_estimated)
        * np.sin(0.3 * t_estimated)
    )

    # Actual perpendicular component from observed data
    actual_wave = (
        -(x_data - X) * np.sin(theta)
        + (y_data - 42) * np.cos(theta)
    )

    # Mean L1 loss
    loss = np.mean(
        np.abs(actual_wave - expected_wave)
    )

    # Penalty for t outside the allowed range
    penalty = np.mean(
        np.maximum(0, 6 - t_estimated)
        + np.maximum(0, t_estimated - 60)
    )

    return loss + 100 * penalty


# ============================================================
# STEP 4: DEFINE PARAMETER BOUNDS
# ============================================================

bounds = [
    (np.deg2rad(0.001), np.deg2rad(49.999)),
    (-0.05, 0.05),
    (0, 100)
]


# ============================================================
# STEP 5: RUN GLOBAL OPTIMIZATION
# ============================================================

print("\nRunning parameter optimization...")
print("Please wait...\n")

result = differential_evolution(
    calculate_loss,
    bounds,
    seed=42,
    tol=1e-9,
    polish=True
)


# ============================================================
# STEP 6: DISPLAY OPTIMIZATION RESULTS
# ============================================================

theta_opt, M_opt, X_opt = result.x
theta_degrees = np.rad2deg(theta_opt)

print("=" * 60)
print("OPTIMIZATION RESULTS")
print("=" * 60)

print(f"\nTheta (radians): {theta_opt:.10f}")
print(f"Theta (degrees): {theta_degrees:.6f}")
print(f"M: {M_opt:.10f}")
print(f"X: {X_opt:.10f}")
print(f"\nFinal L1 Loss: {result.fun:.10f}")


# ============================================================
# STEP 7: RECOVER t VALUES
# ============================================================

t_estimated = (
    (x_data - X_opt) * np.cos(theta_opt)
    + (y_data - 42) * np.sin(theta_opt)
)

print("\nRecovered t range:")
print(f"Minimum t: {t_estimated.min():.6f}")
print(f"Maximum t: {t_estimated.max():.6f}")


# ============================================================
# STEP 8: VALIDATE USING ROUNDED PARAMETERS
# ============================================================

print("\n" + "=" * 60)
print("VALIDATION USING ROUNDED PARAMETERS")
print("=" * 60)

theta_final = np.deg2rad(30)
M_final = 0.03
X_final = 55

t_final = (
    (x_data - X_final) * np.cos(theta_final)
    + (y_data - 42) * np.sin(theta_final)
)

predicted_wave = (
    np.exp(M_final * t_final)
    * np.sin(0.3 * t_final)
)

actual_wave = (
    -(x_data - X_final) * np.sin(theta_final)
    + (y_data - 42) * np.cos(theta_final)
)

rounded_l1_loss = np.mean(
    np.abs(actual_wave - predicted_wave)
)

print("\nFinal Parameter Values:")
print("Theta: 30 degrees")
print(f"M: {M_final}")
print(f"X: {X_final}")
print(f"\nL1 Loss using rounded parameters: {rounded_l1_loss:.10f}")

print("\nRecovered t range using rounded parameters:")
print(f"Minimum t: {t_final.min():.6f}")
print(f"Maximum t: {t_final.max():.6f}")


# ============================================================
# STEP 9: GENERATE FINAL PREDICTED CURVE
# ============================================================

t_curve = np.linspace(6, 60, 1500)

x_curve, y_curve = generate_curve(
    t_curve,
    theta_final,
    M_final,
    X_final
)


# ============================================================
# STEP 10: CREATE AND SAVE COMPARISON GRAPH
# ============================================================

plt.figure(figsize=(10, 6))

plt.scatter(
    x_data,
    y_data,
    s=10,
    label="Given Data",
    alpha=0.7
)

plt.plot(
    x_curve,
    y_curve,
    linewidth=2,
    label="Predicted Curve"
)

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Given Data vs Predicted Parametric Curve")
plt.legend()
plt.grid(True)
plt.axis("equal")

plt.savefig(
    "plots/predicted_vs_actual.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("\nSaved: plots/predicted_vs_actual.png")
# ============================================================
# STEP 11: UNIFORMLY SAMPLED CURVE L1 DISTANCE
# ============================================================

print("\n" + "=" * 60)
print("UNIFORMLY SAMPLED CURVE L1 EVALUATION")
print("=" * 60)

# Number of uniformly sampled points
num_samples = 1500

# ------------------------------------------------------------
# Sort the provided data according to recovered t values.
# This gives the expected curve points in parametric order.
# ------------------------------------------------------------

sort_indices = np.argsort(t_final)

expected_x = x_data[sort_indices]
expected_y = y_data[sort_indices]

expected_t = t_final[sort_indices]


# ------------------------------------------------------------
# Create uniformly spaced t values between the recovered
# minimum and maximum t values.
# ------------------------------------------------------------

uniform_t = np.linspace(
    expected_t.min(),
    expected_t.max(),
    num_samples
)


# ------------------------------------------------------------
# Interpolate the expected curve at uniformly spaced t values
# ------------------------------------------------------------

expected_x_uniform = np.interp(
    uniform_t,
    expected_t,
    expected_x
)

expected_y_uniform = np.interp(
    uniform_t,
    expected_t,
    expected_y
)


# ------------------------------------------------------------
# Generate predicted curve at the same uniformly sampled
# t values using the recovered parameters.
# ------------------------------------------------------------

predicted_x_uniform, predicted_y_uniform = generate_curve(
    uniform_t,
    theta_final,
    M_final,
    X_final
)


# ------------------------------------------------------------
# Calculate L1 distance for x and y coordinates.
# ------------------------------------------------------------

l1_x = np.mean(
    np.abs(expected_x_uniform - predicted_x_uniform)
)

l1_y = np.mean(
    np.abs(expected_y_uniform - predicted_y_uniform)
)

# Combined mean L1 distance
uniform_l1_distance = (l1_x + l1_y) / 2


print(f"\nNumber of uniformly sampled points: {num_samples}")

print("\nL1 Distance Results:")
print(f"L1 distance for X coordinates: {l1_x:.10f}")
print(f"L1 distance for Y coordinates: {l1_y:.10f}")

print(
    f"\nCombined Curve L1 Distance: "
    f"{uniform_l1_distance:.10f}"
)

# ============================================================
# STEP 12: RESIDUAL ANALYSIS
# ============================================================

# Sort the recovered parameter values for visualization
sorted_indices = np.argsort(t_final)

t_sorted = t_final[sorted_indices]
residuals = (
    actual_wave[sorted_indices]
    - predicted_wave[sorted_indices]
)

# Create residual plot
plt.figure(figsize=(10, 6))

plt.plot(
    t_sorted,
    residuals,
    linewidth=1.5,
    label="Residual Error"
)

plt.axhline(
    y=0,
    linestyle="--",
    linewidth=1
)

plt.xlabel("Recovered t")
plt.ylabel("Residual Error")

plt.title("Residual Analysis of the Parametric Curve Model")

plt.legend()
plt.grid(True)

plt.savefig(
    "plots/residual_analysis.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("\nSaved: plots/residual_analysis.png")



# ============================================================
# FINAL ANSWER
# ============================================================

print("\n" + "=" * 60)
print("FINAL ANSWER")
print("=" * 60)

print("\nTheta (theta) = 30 degrees")
print("M = 0.03")
print("X = 55")

print("\nAnalysis completed successfully.")