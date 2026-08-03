# Abelian Contrast Group

Source anchors:

- `specs/formalization/mathematical_formalization.md`
- `specs/operations/boolean_algebra.md`

## Core Claim

The full bit space forms an abelian group under XOR.

## Critical Limitation

The source corpus explicitly warns that well-formed signatures in a context are not necessarily closed under XOR.

Therefore:

- XOR is structurally total on the full space
- XOR is not automatically a valid operation over every semantic signature type
