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
```


## L1 Loss Function

The optimization objective is based on minimizing the L1 error between the transformed data and the predicted curve.

For each data point, the recovered parameter is:

$$
t=(x-X)\cos(\theta)+(y-42)\sin(\theta)
$$

The observed perpendicular component is:

$$
w=-(x-X)\sin(\theta)+(y-42)\cos(\theta)
$$

The predicted perpendicular component is:

$$
w_{\text{pred}}=e^{Mt}\sin(0.3t)
$$

The L1 loss is calculated as:

$$
L_1=\frac{1}{N}\sum_{i=1}^{N}\left|w_i-w_{\text{pred},i}\right|
$$

where $N$ is the total number of data points.

The optimization searches for the values of $\theta$, $M$, and $X$ that minimize this loss.

---

## Optimization Results

The numerical optimization produced the following parameter estimates:

| Parameter | Optimized Value |
|---|---:|
| $\theta$ (radians) | 0.5235983044 |
| $\theta$ (degrees) | 29.999973 |
| $M$ | 0.0299999971 |
| $X$ | 54.9999983399 |

The final optimization loss was:

$$
L_1 = 0.0000025586
$$

The recovered parameter range was:

$$
6.049405 \leq t \leq 59.995171
$$

This range is consistent with the assignment constraint:

$$
6<t<60
$$

---

## Validation Using Rounded Parameters

The optimized values are extremely close to simple numerical values. Therefore, the final parameters were rounded and evaluated again.

### Final Parameter Values

$$
\theta=30^\circ
$$

$$
M=0.03
$$

$$
X=55
$$

The L1 loss using the rounded parameters is:

$$
L_1=0.0000150483
$$

The recovered parameter range using the rounded values is:

$$
6.049404 \leq t \leq 59.995167
$$

The extremely small loss confirms that the rounded values accurately represent the original parametric curve.

---

## Uniformly Sampled Curve L1 Evaluation

The assignment evaluates the similarity between the expected and predicted curves using uniformly sampled points.

A total of **1500 uniformly sampled points** were used for evaluation.

### L1 Distance Results

| Measurement | L1 Distance |
|---|---:|
| X-coordinate distance | 0.0000640127 |
| Y-coordinate distance | 0.0001108733 |
| **Combined Curve L1 Distance** | **0.0000874430** |

The very small combined L1 distance demonstrates an extremely close match between the predicted curve and the given data.

---

## Generated Visualizations

The program automatically generates the following visualizations:

### 1. Given Data

`plots/given_data.png`

This plot visualizes the 1500 points provided in the dataset.

### 2. Predicted Curve vs Actual Data

`plots/predicted_vs_actual.png`

This plot compares the original data points with the curve generated using the recovered parameter values.

The predicted curve closely overlaps with the given data.

### 3. Residual Analysis

`plots/residual_analysis.png`

This visualization shows the remaining differences between the predicted curve and the actual data.

The small residual values further validate the estimated parameters.

---

## Final Answer

The recovered unknown parameters are:

$$
\boxed{\theta=30^\circ}
$$

$$
\boxed{M=0.03}
$$

$$
\boxed{X=55}
$$

Therefore:

**Theta (θ) = 30 degrees**

**M = 0.03**

**X = 55**

---

## Project Structure

```text
flam-rd-parametric-curve-analysis/
│
├── README.md
├── requirements.txt
├── solve.py
├── xy_data.csv
│
└── plots/
    ├── given_data.png
    ├── predicted_vs_actual.png
    └── residual_analysis.png
