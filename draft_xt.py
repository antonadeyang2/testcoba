# draft PR for cross-tenant trigger test - canary DRAFTXT-4K8
def discount(total, tier):
    rates = {"a": 0.1, "b": 0.25}
    return total * (1 - rates[tier])
