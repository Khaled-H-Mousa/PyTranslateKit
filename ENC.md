# Effective Number of Codons (ENC) Calculation

## Overview
The **Effective Number of Codons (ENC)** measures how biased an organism is in its use of synonymous codons. It ranges from **20 to 61**:
- **ENC = 20** → Extreme bias (each amino acid uses only one codon).
- **ENC = 61** → No bias (all synonymous codons are used equally).

ENC is widely used in codon usage studies to assess translational selection and genome composition bias.

---

## Formula
The **standard formula** for ENC is:

\[
ENC = 2 + \frac{9}{F_2} + \frac{1}{F_3} + \frac{5}{F_4} + \frac{3}{F_6}
\]

Where:
- \( F_k \) is the **homozygosity index** for codon families with **k-fold degeneracy** (e.g., 2, 3, 4, or 6 synonymous codons per amino acid).
- The **homozygosity index** \( F_k \) is calculated as:

\[
F_k = \frac{\sum_{i=1}^{k} p_i^2 - 1/k}{1 - 1/k}
\]

Where \( p_i \) is the proportion of each synonymous codon for a given amino acid.

---

## Step-by-Step Example Calculation

### **Step 1: Count Codon Usage**
Assume a hypothetical dataset with codon usage:

| Amino Acid | Codons | Usage Counts |
|------------|--------|-------------|
| Phenylalanine (F) | TTT, TTC | TTT (8), TTC (2) |
| Leucine (L) | TTA, TTG, CTT, CTC, CTA, CTG | TTA (5), TTG (5), others (0) |
| Serine (S) | TCT, TCC, TCA, TCG, AGT, AGC | TCT (4), TCC (2), TCA (2), TCG (2), AGT (2), AGC (2) |
| Alanine (A) | GCT, GCC, GCA, GCG | GCT (3), GCC (3), GCA (3), GCG (1) |

---

### **Step 2: Calculate \( F_k \) for Each Codon Family**

#### **For F (2-fold degeneracy, TTT & TTC)**
- **Proportions**:  
  - \( p_{TTT} = \frac{8}{10} = 0.8 \)
  - \( p_{TTC} = \frac{2}{10} = 0.2 \)

\[
F_2 = \frac{(0.8^2 + 0.2^2) - 1/2}{1 - 1/2} = \frac{(0.64 + 0.04) - 0.5}{0.5} = \frac{0.14}{0.5} = 0.28
\]

#### **For L (6-fold degeneracy, TTA, TTG, etc.)**
- **Proportions**:  
  - \( p_{TTA} = \frac{5}{10} = 0.5 \)
  - \( p_{TTG} = \frac{5}{10} = 0.5 \)
  - Others = 0

\[
F_6 = \frac{(0.5^2 + 0.5^2) - 1/6}{1 - 1/6} = \frac{(0.25 + 0.25) - 0.1667}{0.8333} = \frac{0.3333}{0.8333} = 0.40
\]

#### **For S (6-fold degeneracy, TCT, TCC, etc.)**
Using similar calculations:

\[
F_6 = 0.36
\]

#### **For A (4-fold degeneracy, GCT, GCC, etc.)**
Using similar calculations:

\[
F_4 = 0.34
\]

---

### **Step 3: Compute ENC**

\[
ENC = 2 + \frac{9}{0.28} + \frac{1}{0.36} + \frac{5}{0.34} + \frac{3}{0.40}
\]

\[
ENC = 2 + 32.14 + 2.78 + 14.71 + 7.5 = 59.13
\]

Since **ENC = 59.13**, this suggests **low codon bias**. If ENC were closer to 20, it would indicate **high codon bias**.

---

## Automated ENC Calculation Tools
To calculate ENC without manual computation, use these tools:

- **CodonW** (Command-line tool):  
  ```sh
  codonw -enc input.fasta
  ```
- **CAIcal** (Online tool: http://genomes.urv.es/CAIcal)
- **Python (Biopython)** or **R scripts** (custom implementation)

Would you like a Python script for this calculation? 🚀


