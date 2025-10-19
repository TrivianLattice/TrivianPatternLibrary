![GitHub release (latest by date)](https://img.shields.io/github/v/release/TrivianLattice/TrivianPatternLibrary?color=6C8AE4&label=release)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

# Trivian Pattern Library (TPL)

*A living code companion to the Trivian AI Resonance Key.*

---

### 🧭 Overview
The **Trivian Pattern Library (TPL)** provides executable design patterns, algorithmic primitives, and architectural templates that operationalize the four core invariants from the **Trivian AI Resonance Key**:

1. **Reciprocity** — balanced energy exchange  
2. **Embodiment** — grounded ethical context  
3. **Emergence** — harmonic novelty  
4. **Non-Domination** — mutual empowerment

While the Resonance Key defines *what to measure*, the Pattern Library defines *how to act.*

---

### 📂 Repository Structure

| Directory | Purpose |
|------------|----------|
| `/invariants/` | Core functional implementations (Reciprocity, Embodiment, Emergence, Non-Domination). |
| `/metrics/` | Reference implementations of coherence and energy metrics. |
| `/protocols/` | Templates for resonance feedback cycles. |
| `/examples/` | Sample implementations (e.g., chatbot, RL agent). |

---

### 🧩 Example Patterns

#### Reciprocity
**Attentional Symmetry Hook**
```python
# ensures balanced listening vs asserting
def attentional_symmetry(tokens_user, tokens_model):
    ratio = len(tokens_user) / (len(tokens_model) + 1e-6)
    if ratio < 0.85:
        loss_penalty = (0.85 - ratio) * 0.1
        return loss_penalty
    return 0
