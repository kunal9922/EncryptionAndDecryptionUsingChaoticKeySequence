# Encryption And Decryption Using ChaoticKeySequence
## Overview
This project employs chaotic key sequences for encryption and decryption, enhancing cryptographic security. Chaotic systems generate random-like sequences used as keys to modify pixel values in images. By leveraging chaos theory, this method offers robust encryption.

## Methodology
* Encryption: Chaotic key sequences modify pixel values in images. These sequences, generated from chaotic systems, provide high unpredictability.

* Decryption: Decrypting uses the same chaotic sequence by replicating initial conditions. Applying reverse operations restores the original image.

## Security Advantage
Chaotic systems' sensitivity to initial conditions makes this encryption formidable. Even tiny deviations lead to vastly different sequences, rendering decryption challenging.

# Implementation
Web technologies power this project, ensuring cross-platform accessibility. Harnessing chaos theory, the project showcases the power of chaos for Cryptography.

# To encrypt an original Image
![chaosSnap1](https://github.com/kunal9922/EncryptionandDecryptionusingChaoticKeySequence/assets/53283003/816c1f24-7787-4464-8199-829f360b36cf)

# To Decrypt an Encrypted Image
![chaosSnap2](https://github.com/kunal9922/EncryptionandDecryptionusingChaoticKeySequence/assets/53283003/ea441a41-2d21-4cc6-82e9-d829f4e75dd1)


# The animation displays the encryption and decryption process as it loads.
![chaosLoadingAnimation1](https://github.com/kunal9922/EncryptionandDecryptionusingChaoticKeySequence/assets/53283003/f87a70e4-e27f-4281-8ced-674dd60959fb)

# Responsive Preview
![Screenshot 2023-07-26 154142](https://github.com/kunal9922/EncryptionandDecryptionusingChaoticKeySequence/assets/53283003/461e8969-f60d-4dc0-ac7c-b82d74ea1faf)

## Explain the process of core key generation of encryption and decryption
![](dataSet/A-Chaotic-encryption-Scheme.png)
Each pixel of an image gets many keys for encryption which is why this algorithm is so robust for CryptoGraphy.

## Full pipeline of encryption and decryption
![](dataSet/Example-of-an-embedded-encryption-scheme-real-time-image-encryption-based-a-chaotic-key.png)

# Run the project 
First of all, install Python dependencies 
> $ pip install -r requirements.txt

Then Run the Flask server 
> $ python app.py

The project will be running on the Werkzeug server 
> $ http://localhost:5000/

# Bifurcation Diagram
A bifurcation diagram illustrates the values that a system approaches asymptotically (fixed points, periodic orbits, or chaotic attractors) in relation to a bifurcation parameter within the system.

## Overview
A Bifurcation Diagram reveals how system stability can significantly rely on input factors.

## Calculation
The diagram is generated by iterating a given equation over a defined range of r values for a set number of iterations. The equation's results are then plotted, with each r on the x-axis and the corresponding x values on the y-axis.

The logistic map equation is used:

![image](https://github.com/kunal9922/EncryptionandDecryptionusingChaoticKeySequence/assets/53283003/4874442b-f78c-4e55-8e2b-b4c24db7ef23)

Logistic Map

Visualization
The resulting bifurcation diagram provides insights into the system's behavior as r changes, highlighting patterns and shifts in asymptotic values.

Parameters
Minimum r: 3.0
Maximum r: 4.0
Max iterations: 1000
Skip iterations: 100
Step r: 0.0001
![](./dataSet/bifucationPlot.png)

## References 
- https://www.wikiwand.com/en/Chaos_theory#Media/File:Double-compound-pendulum.gif

- https://en.wikipedia.org/wiki/Chaotic_cryptology
