[![DOI](https://zenodo.org/badge/1218531080.svg)](https://doi.org/10.5281/zenodo.19702421)

# Julian Carry Dynamics: Part I — The Theory of Recurstable Numbers
## How Terminal Stability Shapes Leading Behavior in Power Sequences

**Author:** Julian Wong  
**Current Grade:** Grade 3 (Age 9)      
**Primary Documenter:** Dong Cang    
**Research Date:** April 2026  
**Location:** Mississauga, Ontario, Canada  
**Version:** Part I — Foundational Phase   
**Keywords:** Number Theory, Power Sequences, Linear Recurrence, Stable-Tail Integers

---

## Foreword 
>It all started on a regular Friday afternoon. I was hanging out in my mom’s room, 
just playing as I usually do. But my brain doesn't really stay still—it’s like there’s always a background track of math problems running in my head. 
Sometimes, right in the middle of playing, a pattern just "pops" into my mind and I have to stop and follow it.   
That day, it was the powers of 5. Suddenly, I saw this hidden rule about how the front of the numbers was growing, and I couldn't keep it to myself. 
I ran to my mom and said, "I found a super cool secret!"   
We started talking about it, and the more we talked, the more excited we got. We stayed up chatting for a long time, and mom said this might actually be a big discovery. I wanted to make sure these ideas were safe and shared properly, 
so I asked her to help me turn my "discovery talk" into a real research paper.   
As I explained my thoughts and calculations out loud, she translated them into the professional language you see here. 
This is the story of how my Friday afternoon discovery became **Julian Carry Dynamics**.

---

## Abstract
This paper shifts the focus from inter-numerical relationships to the internal dynamics of a single value within a sequence — exploring how digit carry-over effects move inside it.

It contains my core research for **Julian Carry Dynamics**, which defines **Recurstable Numbers** and establishes **Julian's First Law** — including the deterministic constant ($C_J$) that shapes the leading digits of power sequences.

As the first paper in the Julian Carry Dynamics series, it lays the groundwork for future research that will map the transition from linear recurrence to deterministic chaos — revealing how numerical structure persists even at the edge of chaos.

---

## 1. What Did I Find?

1. For any integer exponent $n \ge 2$, the value of $5^n$ will always end in the digits **25**.
2. The hundreds digit always flips between $1$ and $6$ .
3. Let $A_n$ be the **leading part** of $5^n$ (the number formed by removing the last two digits, $25$). The relationship between the current leading part ($A_n$) and the previous leading part ($A_{n-1}$) is given by:

$$A_n = 5 \cdot A_{n-1} + 1$$

---

## 2. My Mathematical Intuition

When you multiply the end part **25** by **5**, you get **125**. Since **$4  \times25$ = $100$**, adding another 25 gives 125. This means the result always exceeds a multiple of 100 by 25. Therefore:
- The **$25$** stays at the end.
- The **$1$** always **carries over** to the next place (the hundreds place).

That’s why you take the previous leading part, multiply it by 5, and then **always add 1**! 

This also explains the **1-6 Flip-Flop**:
- If the front ends in **1**: $1 \times 5 + 1 = \mathbf{6}$
- If the front ends in **6**: $6 \times 5 + 1 = 3\mathbf{1}$ (it goes back to 1!)

---

## 3. Let's See It In Action

| Power ($5^n$) | Result | Leading Part ($A_n$)  | Calculation ($5 \cdot A_{n-1} + 1$) | **Hundreds-Digit**  |
|:-------------:|:------:|:---------------------:|:-----------------------------------:|:-------------------:|
|     $5^2$     |   25   |           0           |             (Base Case)             |          -          |
|     $5^3$     |  125   |         **1**         |           $5(0) + 1 = 1$            |        **1**        |
|     $5^4$     |  625   |         **6**         |           $5(1) + 1 = 6$            |        **6**        |
|     $5^5$     |  3125  |        3**1**         |           $5(6) + 1 = 31$           |        **1**        |
|     $5^6$     | 15625  |        15**6**        |          $5(31) + 1 = 156$          |        **6**        |


---

## 4. The "Quinponent" Verification
I originally named my first discovery the **"Quinponent"** pattern—a portmanteau of **Quin** (five) and **Exponent**.   
I wrote this script to verify the leading digits for powers of 5.

```python
def verify_quinponent(n):
    front = 0  # Starting with 5^2
    for i in range(2, n + 1):
        result = 5 ** i
        print(f"5^{i} = {result} | Leading part is {front}")
        front = front * 5 + 1

if __name__ == "__main__":
    verify_quinponent(10)
```

## 5. Are there any similar numbers?
Through computer testing, I identified a class of numbers that follow the same recursive pattern as base 5.

| Tail Length ($k$)  | Base ($B$)  | Stable Tail ($T$)  | Constant ($C$)  |     Recurrence Formula      |
|:------------------:|:-----------:|:------------------:|:---------------:|:---------------------------:|
|       **1**        |      6      |         6          |      **3**      |   $A_n = 6(A_{n-1}) + 3$    |
|       **1**        |     36      |         6          |     **21**      |  $A_n = 36(A_{n-1}) + 21$   |
|       **1**        |     11      |         1          |      **1**      |   $A_n = 11(A_{n-1}) + 1$   |
|       **2**        |    **5**    |       **25**       |      **1**      |   $A_n = 5(A_{n-1}) + 1$    |
|       **2**        |     26      |         76         |     **19**      |  $A_n = 26(A_{n-1}) + 19$   |
|       **2**        |     45      |         25         |     **11**      |  $A_n = 45(A_{n-1}) + 11$   |
|       **2**        |     76      |         76         |     **57**      |  $A_n = 76(A_{n-1}) + 57$   |
|       **3**        |     25      |        625         |     **15**      |  $A_n = 25(A_{n-1}) + 15$   |
|       **3**        |     376     |        376         |     **141**     | $A_n = 376(A_{n-1}) + 141$  |
|       **3**        |     425     |        625         |     **265**     | $A_n = 425(A_{n-1}) + 265$  |

---

## 6. Julian's First Law of Recurstable Numbers
### 6.1 Theorem Statement
For any base $B$ where the power $B^n$ ($n \ge 2$) have a **stable tail ($T$)** of length $k$, the **leading part ($A_n$)** of the sequence can always be expressed as a linear recurrence:

$$A_n = B \cdot A_{n-1} + C_J $$

where $C_J$ is a constant determined by the carry-over from the stable tail when multiplied by the base:

$$C_J = \frac{B \cdot T - T}{10^k}$$

**Variable Definitions**
* **$A_n$**: The leading part of the number, defined as the integer value remaining after removing the last $k$ digits (the stable tail).
* **$B$**: The base of the power being calculated.
* **$n$**: The exponent ($n \ge 2$).
* **$T$ :** The recurring ending value of $B^n$.
* **$k$ :** The number of digits in $T$.
* **$C_J$ (The Julian Constant)**: A fixed integer derived from the interaction between the base and the stable tail. 

---

### 6.2 Computational Verification
I wrote the following Python script to test Julian's First Law.

```python
def verify_julian_first_law(B, k, max_n):
    # Calculate the Stable Tail (T)
    T = (B ** 2) % (10 ** k)
    # Calculate the Julian Constant (C_J)
    C_J = (B * T - T) // (10 ** k)

    # Starting Leading Part (A_2)
    A = (B ** 2) // (10 ** k)

    for n in range(3, max_n+1):

        # Applying Julian's First Law: A_n = B * A_{n-1} + C_J
        predict_A = B * A + C_J

        # Calculating actual value for validation
        actual_A = (B ** n) // (10 ** k)

        # Iterating: The current prediction becomes the base for the next power
        A = predict_A

        # Verify if the Law holds true
        print(f"n={n}: {predict_A == actual_A}")



if __name__ == "__main__":
    verify_julian_first_law(B=5, k=2, max_n=10)
```

---

### 6.3 Mathematical Proof
This is my original handwritten manuscript, providing the formal derivation of Julian’s First Law and the calculation of the Julian Constant ($C_J$).

![Manuscript-01: Algebraic Derivation of CJ and First Law](https://github.com/JulianWong310/Julian-Carry-Dynamics/blob/main/2026-04-15-julian-carry-dynamics/asset/01_algebraic_derivation.png)
*Caption: Original handwritten derivation of Julian's First Law and the Julian Constant.*


#### Step 1: Specific Observation (The Case of 5)

$$5^2 = A_2 \cdot 100 + 25$$
$$5^3 = A_3 \cdot 100 + 25$$
$$\vdots$$
$$5^{n-1} = A_{n-1} \cdot 100 + 25$$
$$5^n = A_n \cdot 100 + 25$$

---

#### Step 2: Proving the Quinponent Pattern 
To find the relationship between $A_n$ and $A_{n-1}$, I used the fact that $5^n = 5^{n-1} \cdot 5$:

$$A_n \cdot 100 + 25 = (A_{n-1} \cdot 100 + 25) \cdot 5$$
$$A_n \cdot 100 + 25 = A_{n-1} \cdot 500 + 125$$
$$A_n \cdot 100 + 25 = A_{n-1} \cdot 500 + 100+25$$
$$A_n \cdot 100 + 25 = 100(A_{n-1} \cdot 5 + 1) + 25$$

By canceling the $25$ and dividing by $100$:

$$A_n = 5 \cdot A_{n-1} + 1$$

---

#### Step 3: Deriving the General Law
For any base $B$ with a stable tail $T$ of length $k$:

$$①. B^n = 10^k \cdot A_n + T$$
$$②. B^{n-1} = 10^k \cdot A_{n-1} + T$$

From ②, multiply by $B$:

$$B^n = 10^k \cdot B \cdot A_{n-1} + T \cdot B$$

Now, set the two expressions for $B^n$ equal:

$$10^k \cdot A_n + T = 10^k \cdot B \cdot A_{n-1} + T \cdot B$$

$$10^k \cdot A_n = 10^k \cdot B \cdot A_{n-1} + (T \cdot B - T)$$

Divide by $10^k$ to isolate $A_n$:

$$A_n = B \cdot A_{n-1} + \frac{T \cdot B - T}{10^k}$$

---

#### Step 4: Final Conclusion (The Core Discovery)
i. The Julian Constant: 

  $$C_J= \frac{T \cdot B - T}{10^k}$$ 

ii. The Julian's First Law Equation:

   $$A_n = B \cdot A_{n-1} + C_J$$

Q.E.D

*Note: According to the formula for the Julian Constant, 
the linear recurrence exists only because the tail (T) stays constant (stable).
If the tail were unstable, the Julian constant would become a variable, 
and the linear structure of the leading part would collapse.*

---

### 6.4 Explanation: The Geometry of Interference

Mathematically, without the carry‑over effect from the tail, one might expect the leading part ($A_n$) to grow purely as a power function ($B^n$). However, the stable tail ($T$) creates a persistent “interference”—the Julian Constant ($C_J$).

Picture a perfectly calm lake as a metaphor for the growth of a number. Multiplying by the base would produce a smooth, predictable wave across the surface. However, at each step, the stable tail acts like a small stone dropped into the water, making ripples that nudge the leading part away from its original path.

The beauty of Julian’s First Law lies in the realization that this shift isn't random; it is a deterministic offset. By pinpointing the Julian Constant, I have precisely mapped the “ripple effect” produced by the tail, demonstrating that what appears to be a deviation is, in fact, a perfectly regular and rhythmic law.

---

## 7. Definition & Properties of Recurstable Numbers

> *"A Recurstable Number is defined through the nature of its structure: the absolute stillness of its Tail and the consistent logic of its Head."*

### 7.1 Etymology 
The term **"Recurstable"** is an original portmanteau created by me, synergizing **Recurrence** (the deterministic evolution of terms) and **Stable** (the invariance of terminal digits).

The knowledge map I sketched below shows where I placed my original ‘Recurstable Number’ within the landscape of Number Theory.

![Manuscript-02: Knowledge Tree of Recurstable Numbers](https://github.com/JulianWong310/Julian-Carry-Dynamics/blob/main/2026-04-15-julian-carry-dynamics/asset/02_knowledge_tree.png)
*Caption: Julian’s original knowledge map of Recurstable Numbers.*

---

### 7.2 Definition
A **Recurstable Number** is a positive integer $B$ such that its power sequence $B^n$ (for $n \ge 2$) has an **invariant suffix** — a stable tail $T$ of length $k$. 


#### Core Properties of Recurstable Numbers 

* **Property I: Linear Recurrence Relation**       
The leading part of a Recurstable Number satisfies the following linear recurrence:      
   $A_n = B \cdot A_{n-1} + C_J$

* **Property II: The Terminal Digit Condition**   
A positive integer $B$ is a Recurstable Number **if and only if** its terminal digit is $0, 1, 5, \text{ or } 6$.

---

### 7.3 Mathematical Intuition of Property II
#### 1. Sufficiency:  Last digit is $0, 1, 5, \text{ or } 6$ ⇒ stable tail
If the last digit of $B$ is $0, 1, 5, \text{ or } 6$, then the last digit of $B^n$ never changes (maintaining the stable tail $T$).

#### 2.  Necessity: Stable tail ⇒ last digit must be $0, 1, 5, \text{ or } 6$
For $k = 1$:    
Let $T$ be the last digit of $B$. For $C_J = \frac{T \cdot (B - 1)}{10}$ to be an integer, the product $T \cdot (B - 1)$ must end in $0$.

Check each possible last digit $T$:
* **$T = 0$:** Product is $0 \rightarrow$ ends in $0$ 
* **$T = 1$:** $(B - 1)$ ends in $0 \rightarrow$ product ends in $0$ 
* **$T = 5$:** $(B - 1)$ is even $\rightarrow$ $5 \times \text{even}$ ends in $0$ 
* **$T = 6$:** $(B - 1)$ ends in $5 \rightarrow$ $6 \times 5 = 30$ ends in $0$ 
* **Any other $T$ ($2, 3, 4, 7, 8, 9$):** The product never ends in $0$. 

Thus, only $T \in \lbrace 0, 1, 5, 6 \rbrace$ satisfies the integrality requirement. 

For $k > 1$: if $C_J$ is an integer, then $10^k$ divides $T  \cdot (B - 1)$. This implies $10$ also divides $T  \cdot (B - 1)$. Hence, the same last-digit condition must still hold. 

**Conclusion:** The requirement that the last digit of $B$ is $0, 1, 5, \text{or } 6$ applies for any tail length $k$.

---

## 8. Future Work: Julian Carry Dynamics
### 8.1 Theoretical Framework

**Julian Carry Dynamics** is my way of observing how the leading digits of a number evolve as the tail (the ending digits) becomes more complex.

I defined a research roadmap to guide my exploration and divided it into three phases, each corresponding to increasing levels of tail complexity.

![Manuscript-03: Research Roadmap of Julian Carry Dynamics](https://github.com/JulianWong310/Julian-Carry-Dynamics/blob/main/2026-04-15-julian-carry-dynamics/asset/03_research_roadmap.png)
*Caption: Three-phase research roadmap of Julian Carry Dynamics.*

---

### 8.2 Phase I: Static Stability (Low Entropy)
**Single base (like $5^n$) — Completed** 
- Julian's First Law  
- Julian Constant ($C_J$)  
- Recurstable Numbers

**Multiple bases (like $5^n + 6^n$) — Working on It**
- The constant still shows up  
- Still writing the clean proof

---

### 8.3 Phase II: Dynamic Transition (Medium Entropy)

At this stage, the tail is no longer constant, but it follows a repeating cycle.

**Example: The $11^n$ Cycle**  
I observed that the last two digits of $11^n$ follow a very predictable pattern:     
$11, 21, 31, 41, 51, 61, 71, 81, 91, 01, \dots$ (repeats every $10$ steps)

**Question:** When the tail exhibits a repeating pattern, does the leading part synchronize and vary with it?  

**Hypothesis:** The leading part will show **coupling effects** — a synchronized, multi-state oscillation.

---

### 8.4 Phase III: Edge of Chaos (High Entropy)
I sketched this conceptual diagram to visualize the phase transition from low to high tail entropy.

![Manuscript-04: Phase Transition Concept](https://github.com/JulianWong310/Julian-Carry-Dynamics/blob/main/2026-04-15-julian-carry-dynamics/asset/04_phase_transition_concept.png)
*Caption: Julian's conceptual diagram mapping the Phase Transition of Julian Carry Dynamics.*

In Phase III, the tail reaches a level of complexity where it seems practically random.

**Example: The $3^n$ "Wild" Cycle**  
I tracked the last two digits of powers of 3, the sequence feels much more chaotic:  
$03, 09, 27, 81, 43, 29, 87, 61, 83, 49, 47, 41, 23, 69, 07, 21, 63, 89, 67, 01, \dots$   

It takes exactly 20 steps to return to the start — not fixed like $5^n$ and not super simple like $11^n$. This behavior lives near the **Edge of Chaos**.

**Question:** When the tail gets this messy, does the leading part still follow a rule? And if so, what is the upper bound on its complexity?

**Goal:** Map the structural persistence and computational upper bound of leading-digit complexity at the edge of chaos.

---

### 8.5 The Big Goal
Even when numbers appear random, there is often a deeper logic hidden beneath the surface.
If this holds true for numbers, perhaps it also applies to other things — seemingly random phenomena like weather patterns, heartbeats, or traffic flow.

That is why I keep exploring.

---

## 9. Acknowledgments 

1. **Intellectual Property & Naming Rights Assertion:**
The core theoretical framework and mathematical insights presented in this study are the independent discoveries of **Julian Wong**. As the primary investigator, Julian Wong claims full naming rights and intellectual priority over the following terminology:

      * **Recurstable Numbers:** The overarching classification for integers with stable-tail power sequences.
      * **Julian’s First Law:** The linear recurrence relation $A_n = B \cdot A_{n-1} + C_J$.
      * **The Julian Constant ($C_J$):** The deterministic integer that captures carry-over dynamics.
      * **The "Quinponent" Pattern:** The foundational discovery for powers of $5$.
      * **Julian Carry Dynamics:** The proposed field studying how terminal stability drives the evolution of leading digits.

2. **Mathematical Guidance:** I would like to thank my mother, Dong Cang. She guided me to use variables (such as $A_n$) to turn my ideas into a clear mathematical framework.

---

**License:** This mathematical manuscript is released under the [Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).
You are free to share and adapt this material for any purpose, provided you give appropriate credit to the original author: **Julian Wong**. 

*Copyright © 2026 Julian Wong. All rights reserved for original mathematical concepts and handwritten manuscripts.*
