# FLAM Research & Development Assignment

## Parametric Curve Parameter Estimation

## Overview

This project solves the FLAM Research and Development assignment of estimating the unknown parameters of a parametric curve using the provided `xy_data.csv` dataset.

The objective is to determine the three unknown variables:

- $\theta$ (theta)
- $M$
- $X$

The solution uses mathematical coordinate transformation, parameter recovery, bounded optimization, L1 loss minimization, uniformly sampled curve evaluation, and residual analysis.

---

## Problem Statement

The given parametric curve is:

$$
x = t\cos(\theta) - e^{M|t|}\sin(0.3t)\sin(\theta) + X
$$

$$
y = 42 + t\sin(\theta) + e^{M|t|}\sin(0.3t)\cos(\theta)
$$

The unknown variables are:

$$
\theta,\quad M,\quad X
$$

The parameter constraints provided in the assignment are:

| Parameter | Range |
|---|---|
| $\theta$ | $0^\circ < \theta < 50^\circ$ |
| $M$ | $-0.05 < M < 0.05$ |
| $X$ | $0 < X < 100$ |
| $t$ | $6 < t < 60$ |

The provided `xy_data.csv` file contains **1500 points** lying on the parametric curve.

---

## Mathematical Simplification

The assignment specifies:

$$
6 < t < 60
$$

Therefore, $t$ is always positive. Hence:

$$
|t| = t
$$

The original equations can therefore be simplified as:

$$
x = t\cos(\theta) - e^{Mt}\sin(0.3t)\sin(\theta) + X
$$

$$
y = 42 + t\sin(\theta) + e^{Mt}\sin(0.3t)\cos(\theta)
$$

This simplification is used throughout the parameter estimation process.

---

## Mathematical Approach

### Coordinate Transformation

The parametric curve can be interpreted using two perpendicular directions.

The primary direction is:

$$
(\cos(\theta), \sin(\theta))
$$

The perpendicular direction is:

$$
(-\sin(\theta), \cos(\theta))
$$

For a candidate set of parameters $\theta$, $M$, and $X$, the parameter $t$ can be recovered by projecting each data point onto the primary direction:

$$
t = (x-X)\cos(\theta) + (y-42)\sin(\theta)
$$

The perpendicular component is calculated as:

$$
w = -(x-X)\sin(\theta) + (y-42)\cos(\theta)
$$

For the correct parameter values, the perpendicular component satisfies:

$$
w = e^{Mt}\sin(0.3t)
$$

Therefore, the optimization problem becomes finding the values of:

$$
\theta,\quad M,\quad X
$$

rather than independently estimating a separate value of $t$ for every data point.

This significantly reduces the complexity of the problem.

---

## Approach and Thought Process

The following approach was used to solve the problem:

1. Loaded and inspected the provided `xy_data.csv` dataset containing 1500 coordinate points.
2. Analyzed the mathematical structure of the parametric equation.
3. Used the given constraint $6 < t < 60$ to simplify $|t|$ to $t$.
4. Applied a coordinate transformation to recover the parameter $t$ from each data point.
5. Calculated the perpendicular component of the data relative to the main direction of the curve.
6. Constructed an L1 loss function between the transformed data and the predicted curve.
7. Used bounded numerical optimization to estimate $\theta$, $M$, and $X$ within the specified parameter ranges.
8. Rounded the optimized values to meaningful final parameter values and validated them again.
9. Generated uniformly sampled points to compare the predicted curve with the given curve.
10. Visualized the data, predicted curve, and residual errors to validate the final solution.

---

## Parameter Optimization

The unknown parameters were estimated using bounded numerical optimization.

The parameter search ranges were:

```text
Theta: 0° to 50°
M: -0.05 to 0.05
X: 0 to 100
