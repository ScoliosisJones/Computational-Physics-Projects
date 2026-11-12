
# Project 1: Numerical Integration

## Overview

This project calculates the time required for an object starting at Earth's orbital radius to fall into the Sun under the influence of solar gravity.

Conservation of mechanical energy is used to derive the object's velocity as a function of its distance from the Sun. The resulting time integral is evaluated numerically using Simpson's rule.

## Methods

- Conservation of mechanical energy
- Numerical integration using Simpson's rule
- Variable substitution to handle the singularity at the initial radius when the initial velocity is zero

## Initial Conditions

The calculation uses the following values:

| Parameter | Value |
|---|---:|
| Earth's orbital radius | 1.5 × 10¹¹ m |
| Solar radius | 7.0 × 10⁸ m |
| Solar mass | 2.0 × 10³⁰ kg |
| Gravitational constant | 6.67 × 10⁻¹¹ N m²/kg² |

The initial velocities examined are 0, 10, and 1000 m/s, directed toward the Sun.

## Results

| Initial velocity (m/s) | Fall time (seconds) | Fall time (days) |
|---:|---:|---:|
| 0 | 5.58605 × 10⁶ | 64.6534 |
| 10 | 5.58437 × 10⁶ | 64.6339 |
| 1000 | 5.42198 × 10⁶ | 62.7543 |

The 0 and 10 m/s cases produce very similar results because the initial velocity is small compared with the velocities reached during the fall.

## Running the Program

Requires Python 3. No external libraries are needed.

```bash
python integration.py
```

## Concepts Demonstrated

- Numerical integration
- Simpson's rule
- Conservation of energy
- Gravitational motion
- Handling integrable singularities in numerical calculations
