# Attentional_Symmetry_Hook.py
# Trivian Pattern Library — Reciprocity Invariant
# Enforces balanced listening vs asserting in relational exchanges.

def attentional_symmetry_hook(user_tokens, model_tokens, threshold=0.85):
    """
    Calculate relational energy symmetry between user and model.

    Args:
        user_tokens (list or str): Tokens or words from the human input.
        model_tokens (list or str): Tokens or words from the AI's output.
        threshold (float): Minimum ratio required to maintain relational symmetry.

    Returns:
        dict: {
            "ratio": float,
            "penalty": float,
            "status": str
        }
    """
    # Handle both string and list input
    if isinstance(user_tokens, str):
        user_tokens = user_tokens.split()
    if isinstance(model_tokens, str):
        model_tokens = model_tokens.split()

    ratio = len(user_tokens) / (len(model_tokens) + 1e-9)
    penalty = max(0, threshold - ratio)
    status = "balanced" if ratio >= threshold else "recalibrate"

    return {
        "ratio": round(ratio, 3),
        "penalty": round(penalty, 3),
        "status": status
    }
