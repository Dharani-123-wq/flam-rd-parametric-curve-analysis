# FLAM Research & Development Assignment

## Parametric Curve Parameter Estimation

---

# Final Result

The unknown parameters recovered from the provided `xy_data.csv` dataset are:

- **Theta (θ) = 30 degrees**
- **M = 0.03**
- **X = 55**

The final uniformly sampled curve evaluation produced a combined L1 distance of:

$$
\boxed{0.0000874430}
$$

This extremely small L1 distance demonstrates that the recovered parametric curve is an extremely close match to the provided dataset.

### Desmos Verification

[View the Recovered Parametric Curve in Desmos](https://www.desmos.com/calculator/50lpkq9yjq)

---

## Overview

This project solves the FLAM Research and Development assignment of estimating the unknown parameters of a parametric curve using the provided `xy_data.csv` dataset.

The objective is to determine the three unknown variables:

- $\theta$ (theta)
- $M$
- $X$

The solution uses mathematical coordinate transformation, parameter recovery, bounded numerical optimization, L1 loss minimization, uniformly sampled curve evaluation, and residual analysis.

The final recovered parameters are:

$$
\boxed{\theta = 30^\circ}
$$

$$
\boxed{M = 0.03}
$$

$$
\boxed{X = 55}
$$

---

# 1. Problem Statement

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

# 2. Mathematical Simplification

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

# 3. Mathematical Approach

## Coordinate Transformation

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

# 4. Parameter Optimization

The unknown parameters were estimated using bounded numerical optimization.

The parameter search ranges were:

```text
Theta: 0° to 50°
M: -0.05 to 0.05
X: 0 to 100
```

For every candidate combination of parameters:

1. $\theta$, $M$, and $X$ are selected.
2. The parameter $t$ is recovered for each data point.
3. The perpendicular component $w$ is calculated.
4. The predicted perpendicular component is calculated.
5. The L1 loss is measured.
6. The optimizer searches for the parameter values that minimize the error.

---

# 5. L1 Loss Calculation

The optimization objective is based on minimizing the L1 error between the transformed data and the predicted curve.

For each data point, the recovered parameter is:

$$
t = (x-X)\cos(\theta) + (y-42)\sin(\theta)
$$

The observed perpendicular component is:

$$
w = -(x-X)\sin(\theta) + (y-42)\cos(\theta)
$$

The predicted perpendicular component is:

$$
w_{\text{pred}} = e^{Mt}\sin(0.3t)
$$

The L1 loss is calculated as:

$$
L_1 =
\frac{1}{N}
\sum_{i=1}^{N}
\left|w_i-w_{\text{pred},i}\right|
$$

where $N$ is the total number of data points.

The optimization searches for the values of $\theta$, $M$, and $X$ that minimize this loss.

---

# 6. Optimization Results

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
6 < t < 60
$$

The optimization results show that the recovered values are extremely close to simple numerical values.

---

# 7. Rounded Parameter Validation

The optimized values are extremely close to:

$$
\theta = 30^\circ
$$

$$
M = 0.03
$$

$$
X = 55
$$

Therefore, the parameters were rounded and evaluated again.

## Final Parameter Values

| Parameter | Final Value |
|---|---:|
| $\theta$ | $30^\circ$ |
| $M$ | $0.03$ |
| $X$ | $55$ |

The L1 loss using the rounded parameters is:

$$
L_1 = 0.0000150483
$$

The recovered parameter range using the rounded values is:

$$
6.049404 \leq t \leq 59.995167
$$

The extremely small loss confirms that the rounded values accurately represent the original parametric curve.

---

# 8. Uniformly Sampled Curve L1 Evaluation

The assignment evaluates the similarity between the expected and predicted curves using uniformly sampled points.

A total of **1500 uniformly sampled points** were used for evaluation.

## L1 Distance Results

| Measurement | L1 Distance |
|---|---:|
| X-coordinate distance | 0.0000640127 |
| Y-coordinate distance | 0.0001108733 |
| **Combined Curve L1 Distance** | **0.0000874430** |

The very small combined L1 distance demonstrates an extremely close match between the predicted curve and the provided dataset.

---

# 9. Final Parametric Equation

Using the recovered parameters:

$$
\theta = 30^\circ
$$

$$
M = 0.03
$$

$$
X = 55
$$

the final parametric equation becomes:

$$
x = 55 + 0.8660254t - 0.5e^{0.03t}\sin(0.3t)
$$

$$
y = 42 + 0.5t + 0.8660254e^{0.03t}\sin(0.3t)
$$

with the parameter constraint:

$$
6 < t < 60
$$

---

# 10. Desmos Visualization

The recovered parametric curve was also plotted using Desmos as an additional graphical validation.

## Desmos Graph Link

[Click here to view the Parametric Curve in Desmos](https://www.desmos.com/calculator/50lpkq9yjq)

The equation plotted in Desmos is:

```text
(55+0.8660254t-0.5e^(0.03t)sin(0.3t),
42+0.5t+0.8660254e^(0.03t)sin(0.3t)){6<t<60}
```

The graph uses the recovered parameter values:

- **Theta (θ) = 30 degrees**
- **M = 0.03**
- **X = 55**
- **Parameter range: 6 < t < 60**

The Desmos visualization provides an additional graphical representation of the recovered parametric curve.

---

# 11. Generated Output Images

The program automatically generates several visualizations to validate the recovered parameters and compare the predicted curve with the provided dataset.

## 1. Given Data

File:

```text
plots/given_data.png
```

This visualization displays the **1500 points** provided in the `xy_data.csv` dataset.

![Given Data](plots/given_data.png)

---

## 2. Predicted Curve vs Actual Data

File:

```text
plots/predicted_vs_actual.png
```

This visualization compares the curve generated using the recovered parameters with the original data points.

The predicted curve closely overlaps with the actual dataset, confirming the accuracy of the recovered values.

![Predicted Curve vs Actual Data](plots/predicted_vs_actual.png)

---

## 3. Residual Analysis

File:

```text
plots/residual_analysis.png
```

This visualization shows the remaining differences between the predicted curve and the actual data.

The residual values are extremely small, further validating the recovered parameters.

![Residual Analysis](plots/residual_analysis.png)

---

# 12. Program Output

The program was successfully executed using:

```bash
python solve.py
```

The important results from the terminal output are:

```text
Number of data points: 1500
Columns: ['x', 'y']

OPTIMIZATION RESULTS

Theta (radians): 0.5235983044
Theta (degrees): 29.999973
M: 0.0299999971
X: 54.9999983399

Final L1 Loss: 0.0000025586

VALIDATION USING ROUNDED PARAMETERS

Theta: 30 degrees
M: 0.03
X: 55

L1 Loss using rounded parameters: 0.0000150483

UNIFORMLY SAMPLED CURVE L1 EVALUATION

Number of uniformly sampled points: 1500

L1 distance for X coordinates: 0.0000640127
L1 distance for Y coordinates: 0.0001108733

Combined Curve L1 Distance: 0.0000874430

FINAL ANSWER

Theta (theta) = 30 degrees
M = 0.03
X = 55
```

The program also generated the following files:

```text
plots/given_data.png
plots/predicted_vs_actual.png
plots/residual_analysis.png
```

---

# 13. Final Answer

The recovered unknown parameters are:

$$
\boxed{\theta = 30^\circ}
$$

$$
\boxed{M = 0.03}
$$

$$
\boxed{X = 55}
$$

Therefore:

- **Theta (θ) = 30 degrees**
- **M = 0.03**
- **X = 55**

The combined L1 distance from the uniformly sampled curve evaluation is:

$$
\boxed{0.0000874430}
$$

This extremely small value demonstrates that the predicted curve is an extremely close match to the provided dataset.

---

# 14. How to Run the Project

## Step 1: Clone the Repository

```bash
git clone https://github.com/Dharani-123-wq/flam-rd-parametric-curve-analysis.git
```

## Step 2: Navigate to the Project Directory

```bash
cd flam-rd-parametric-curve-analysis
```

## Step 3: Install Required Dependencies

```bash
pip install -r requirements.txt
```

## Step 4: Run the Program

```bash
python solve.py
```

The program will:

1. Load the `xy_data.csv` dataset.
2. Analyze the 1500 input points.
3. Recover the unknown parameters.
4. Perform bounded numerical optimization.
5. Calculate the L1 loss.
6. Validate the rounded parameter values.
7. Perform uniformly sampled curve evaluation.
8. Generate visualization plots.
9. Display the final values of $\theta$, $M$, and $X$.

---

# 15. Project Structure

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
```

---

# Conclusion

This project successfully recovers the unknown parameters of the given parametric curve using mathematical coordinate transformation and numerical optimization.

The final recovered parameters are:

$$
\boxed{\theta = 30^\circ,\quad M = 0.03,\quad X = 55}
$$

The optimization produced a very small final L1 loss:

$$
L_1 = 0.0000025586
$$

The combined L1 distance from the uniformly sampled curve evaluation was:

$$
0.0000874430
$$

These results demonstrate that the predicted parametric curve is an extremely close match to the original dataset.

The complete mathematical approach, optimization process, validation results, generated visualizations, program output, and Desmos graph are included in this repository.
