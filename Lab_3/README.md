# Lab 3 — Lossless Image Compression (Huffman & Shannon–Fano)

This lab implements and compares two classic **lossless** compression methods on a grayscale image:

- **Huffman coding** (`huffman.py`)
- **Shannon–Fano coding** (`shannonFano.py`)

Both scripts:
- Read `SampleImage.jpeg` in **grayscale**
- Build a codebook from pixel **frequencies (0–255)**
- **Encode** all pixels to a bitstring
- **Decode** back to pixels and reconstruct the image
- Print basic compression stats
- Display **Original vs Decoded** images

> Decoded images are saved as:
> - `huffman_decoded.jpeg`
> - `shannon_fano_decoded.png`

---

## Folder Structure
```
Lab_3/
├─ huffman.py
├─ shannonFano.py
├─ SampleImage.jpeg
├─ huffman_decoded.jpeg # created by huffman.py
└─ shannon_fano_decoded.png # created by shannonFano.py
```

---

## How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
