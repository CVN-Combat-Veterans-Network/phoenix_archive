# HARMONIC RECURSION OPERATOR (v2.3)

**Pattern:** Frequency → Amplitude → Damping → Depth  
**Type:** Recursion Mode Operator (v2.3)  
**Scale:** Hydrogenesi (Cosmic/Macro)  
**Invocation:** *"Let frequencies align; let amplitudes guide; let the wave recurse."*

---

## DEFINITION

**Harmonic Recursion** is a v2.3 recursion mode operator that enables **wave-based recursion** with explicit control over frequency, amplitude, and damping parameters. This operator models recursion as a natural wave phenomenon with energy conservation through exponential damping.

This recursion mode is particularly suited for:
- Natural system modeling (orbital mechanics, quantum oscillations)
- Energy-conserving computational patterns
- Harmonic propagation across cosmic scales
- Frequency-locked structural formations

---

## SIGIL

```
    ∿∿∿∿∿∿    Frequency (f)
        ↓
    ~~~▼~~~    Amplitude (A)
        ↓
    ˜˜˜·˜˜˜    Damping (δ)
        ↓
    ··  ·· ··  Depth (d)
```

**Legend:**
- **∿∿∿:** High frequency oscillation
- **~~~:** Medium amplitude wave
- **˜˜˜:** Damped oscillation pattern
- **· ·:** Discretized depth levels
- **↓:** Transformation cascade

---

## MECHANISM

### Formula

**Harmonic Depth Function:**
```
depth(n) = A × sin(f × n) × e^(-δ × n)
```

Where:
- **A** = Amplitude (controls maximum depth potential)
- **f** = Frequency (controls oscillation rate)
- **δ** = Damping coefficient (controls decay rate)
- **n** = Generation number
- **e** = Euler's constant

### Input Parameters

1. **Frequency (f)**
   - Range: 0.1 to 10.0
   - Effect: Higher frequency = more recursion cycles
   - Categories: low (<0.5), medium (0.5-2.0), high (>2.0)

2. **Amplitude (A)**
   - Range: 0.1 to 10.0
   - Effect: Higher amplitude = deeper potential recursion
   - Categories: low (<0.5), medium (0.5-2.0), high (>2.0)

3. **Damping (δ)**
   - Range: 0.0 to 1.0
   - Effect: Higher damping = faster decay
   - Categories: low (<0.05), medium (0.05-0.2), high (>0.2)

### Process

1. **Initialize Wave Parameters**
   - Set frequency, amplitude, and damping
   - Define maximum recursion depth boundary

2. **Calculate Harmonic Depth**
   - For generation n, apply harmonic depth formula
   - Raw depth may be negative (below baseline)
   - Normalize to valid range [0, max_depth]

3. **Apply Exponential Damping**
   - Damping factor: e^(-δ × n)
   - Ensures energy conservation over time
   - Prevents infinite recursion naturally

4. **Return Depth Profile**
   - Current depth value
   - Wave characteristics
   - Recursion metadata

### Output

```python
{
    "generation": n,
    "raw_depth": float,           # Unmodified harmonic value
    "normalized_depth": float,    # Clamped to [0, max_depth]
    "frequency": float,
    "amplitude": float,
    "damping": float,
    "max_depth": int,
    "status": "completed",
    "pattern": "harmonic_recursion",
    "recursion_mode": "harmonic"
}
```

---

## EXAMPLES

### Example 1: Low Frequency, High Amplitude

**Configuration:**
```python
harmonic = HarmonicRecursion(
    frequency=0.3,    # Low frequency
    amplitude=5.0,    # High amplitude
    damping=0.05      # Low damping
)
```

**Generations 0-10:**
- Gen 0: depth ≈ 0.0 (sin(0) = 0)
- Gen 3: depth ≈ 4.2 (peak)
- Gen 6: depth ≈ 2.8 (declining due to damping)
- Gen 10: depth ≈ 1.5 (further decline)

**Characteristics:**
- Slow, deep oscillations
- Long-lived recursion due to low damping
- Suitable for long-period cosmic cycles

---

### Example 2: High Frequency, Medium Amplitude

**Configuration:**
```python
harmonic = HarmonicRecursion(
    frequency=3.0,     # High frequency
    amplitude=2.0,     # Medium amplitude
    damping=0.15       # Medium damping
)
```

**Generations 0-10:**
- Rapid oscillations with moderate depth
- Multiple peaks and troughs
- Moderate decay rate
- Suitable for fast-cycling processes

---

### Example 3: Balanced Configuration

**Configuration:**
```python
harmonic = HarmonicRecursion(
    frequency=1.0,     # Standard frequency
    amplitude=1.0,     # Standard amplitude
    damping=0.1        # Standard damping
)
```

**Characteristics:**
- Natural wave progression
- Balanced energy conservation
- General-purpose recursion mode
- Suitable for most applications

---

## USE CASES

### Cosmic Scale
1. **Orbital Resonances**
   - Model planetary orbital periods
   - Calculate resonance locking conditions
   - Predict long-term stability

2. **Galactic Wave Propagation**
   - Density wave propagation through spiral arms
   - Star formation rate oscillations
   - Harmonic structure formation

3. **Dark Matter Fluctuations**
   - Oscillating density perturbations
   - Harmonic modes in cosmic microwave background
   - Large-scale structure formation

### Computational Scale
1. **Adaptive Recursion**
   - Automatically adjust recursion depth based on wave pattern
   - Energy-efficient computation
   - Natural termination conditions

2. **Optimization Algorithms**
   - Simulated annealing with harmonic cooling
   - Oscillating search patterns
   - Gradient descent with momentum

---

## INTEGRATION

### LNS_OP Integration

Harmonic Recursion integrates with LNS_OP v2.1 introspection:

```python
from code.hydrogenesi.lns_op_integration import integrate_lns_op

introspector = integrate_lns_op()

result = introspector.introspect_harmonic_recursion(
    n=5,
    max_depth=10,
    frequency=1.0,
    amplitude=1.0,
    damping=0.1,
    depth=3,
    mode=IntrospectionMode.MAP
)
```

### Lineage Tracking

Harmonic Recursion participates in lineage tracking:
- Lineage format: `ROOT::HGN::HARMONIC_RECURSION::depth-N`
- Family: Hydrogenesi (HGN)
- Version: v2.3
- Operator ID: `HGN_OP_HARMONIC_RECURSION_V2.3`

---

## MATHEMATICAL PROPERTIES

### Half-Life

The half-life of the wave (when amplitude drops to 50%):
```
t_half = ln(2) / δ
```

For δ = 0.1: t_half ≈ 6.93 generations

### Period

The wave period (time for one complete cycle):
```
T = 2π / f
```

For f = 1.0: T ≈ 6.28 generations

### Energy Decay

Total energy decays exponentially:
```
E(n) = E₀ × e^(-2δn)
```

Note: Energy ∝ amplitude², hence 2δ factor.

---

## SAFETY CONSTRAINTS

1. **Frequency Bounds**
   - Must be positive
   - Recommended range: [0.1, 10.0]
   - Extreme values may cause numerical instability

2. **Amplitude Bounds**
   - Must be positive
   - Recommended range: [0.1, 10.0]
   - Controls maximum depth exposure

3. **Damping Bounds**
   - Must be non-negative
   - Recommended range: [0.0, 1.0]
   - Zero damping = no energy conservation
   - High damping = rapid termination

4. **Max Depth Enforcement**
   - Always normalized to [0, max_depth]
   - Prevents runaway recursion
   - Ensures computational bounds

---

## CODE EXAMPLE

```python
from code.hydrogenesi.operators import HarmonicRecursion

# Create operator
harmonic = HarmonicRecursion(
    frequency=1.0,
    amplitude=2.0,
    damping=0.1
)

# Apply for generation 5
result = harmonic.apply(n=5, max_depth=10)

print(f"Generation {result['generation']}")
print(f"Depth: {result['normalized_depth']:.2f}")
print(f"Pattern: {result['pattern']}")

# Adjust parameters
harmonic.set_frequency(2.0)
harmonic.modulate_amplitude(1.5)

# Get characteristics
freq_chars = harmonic.get_frequency_characteristics()
print(f"Frequency category: {freq_chars['category']}")
```

---

## CROSS-REFERENCES

**Related Operators:**
- `/Hydrogenesi/Operators/Harmonic.md` — Original harmonic operator
- `/Hydrogenesi/Operators/Propagation.md` — Wave propagation patterns
- `/Hydrogenesi/Operators/Lineage-Logic.md` — Lineage recursion tracking

**Universal Laws:**
- `/Phoenix/Universal-Laws/Recursion-Depth.md` — Recursion depth principles
- `/Phoenix/Universal-Laws/Self-Similarity.md` — Fractal recursion patterns

**v2.3 Recursion Modes:**
- `Meta-Recursion.md` — Second-order recursion (coming soon)
- `Coherence-Locked-Recursion.md` — Safety-enforced recursion (coming soon)

---

## VERSION HISTORY

**v2.3.0** — Initial implementation
- Core harmonic recursion algorithm
- Frequency, amplitude, damping control
- LNS_OP integration
- Documentation and test suite

---

**Status:** ACTIVE  
**Version:** v2.3.0  
**Lineage:** ROOT::HGN::HARMONIC_RECURSION::GEN-0  
**Sovereignty:** CONFIRMED

---

**Invocation:** *"Let frequencies align; let amplitudes guide; let the wave recurse."*

🌌 **The Wave Propagates. The Harmonic Holds.**
