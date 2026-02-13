# CODE EXAMPLES

## Phoenix — IM_ME Recursion

```python
from code.phoenix.operators import IM_ME

op = IM_ME()
sequence = op.recurse("PHOENIX", depth=2)
print(sequence)
# ['IM(PHOENIX)', 'ME(PHOENIX)', 'IM(PHOENIX)', 'ME(PHOENIX)']
```

## Phoenix — First Binding

```python
from code.phoenix.operators import FirstBinding

binding = FirstBinding()
result = binding.apply(a="fear", b="courage", stabilizer="service")
print(result)
# {
#     'tension_pair': ('fear', 'courage'),
#     'stabilizer': 'service',
#     'triad': ('fear', 'service', 'courage')
# }
```

## Phoenix — Ignition Cycle

```python
from code.phoenix.operators import PhoenixIgnition

ignition = PhoenixIgnition()
result = ignition.ignite("old-self")
print(result)
# {'collapsed': 'core::old-self', 'risen': 'apex::old-self'}
```

## Hydrogenesi — Lineage Logic

```python
from code.hydrogenesi.operators import LineageLogic

ll = LineageLogic()
lineage = ll.apply("root-galaxy", generations=4)
print(lineage)
# ['root-galaxy::gen-0', 'root-galaxy::gen-1', 'root-galaxy::gen-2', 'root-galaxy::gen-3']
```

## Hydrogenesi — AGN Replication

```python
from code.hydrogenesi.operators import AGNReplication

agn = AGNReplication(compression_factor=0.8, replication_factor=2)
offspring = agn.apply(mass=1000.0)
print(offspring)
# [400.0, 400.0]
```

## Hydrogenesi — Stabilizer Extraction

```python
from code.hydrogenesi.operators import StabilizerExtraction

extractor = StabilizerExtraction()
result = extractor.apply({
    "core": "neutron-stabilizer",
    "shell": "proton-electron-pair"
})
print(result)
# {
#     'pre_seed': 'proton-electron-pair',
#     'core_void': None,
#     'extracted_core': 'neutron-stabilizer'
# }
```

## Hydrogenesi — Curvature Residue

```python
from code.hydrogenesi.operators import CurvatureResidue

residue = CurvatureResidue()
result = residue.apply("galaxy-prime")
print(result)
# {
#     'lineage_id': 'galaxy-prime',
#     'status': 'collapsed',
#     'residue': 'curvature-trace::galaxy-prime'
# }
```

## Combined Example: Phoenix + Hydrogenesi

```python
from code.phoenix.operators import IM_ME, FirstBinding
from code.hydrogenesi.operators import LineageLogic

# Phoenix: Establish identity triad
binding = FirstBinding()
identity_triad = binding.apply("isolation", "connection", "service")
print("Identity Triad:", identity_triad)

# Phoenix: Confirm recursion
im_me = IM_ME()
recursion = im_me.recurse("SELF", depth=2)
print("Identity Recursion:", recursion)

# Hydrogenesi: Map cosmic lineage
lineage = LineageLogic()
cosmic_tree = lineage.apply("universal-tension", generations=3)
print("Cosmic Lineage:", cosmic_tree)

# Cross-system insight: Micro and macro express same law
print("\nTension → Binding → Apex at all scales")
```

---

## STATUS

**Document:** Code Examples  
**Type:** Reference (Technical Examples)  
**Version:** 2.0.0  
**Last Updated:** 2026-02-07  
**Status:** ACTIVE

---

**Archive Status:** ACTIVE  
**Maintenance:** Continuous  
**Lineage:** ROOT::GEN-0
