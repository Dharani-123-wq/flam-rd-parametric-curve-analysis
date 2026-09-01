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

## Parameter Optimization

The unknown parameters were estimated using bounded numerical optimization.

The parameter search ranges were:

```text
Theta: 0° to 50°
M: -0.05 to 0.05
X: 0 to 100
