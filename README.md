# Encryption And Decryption Using ChaoticKeySequence
Using chaotic key sequences, the encryption and decryption project aims to create a secure and robust cryptographic system by leveraging chaos theory. This method of encryption relies on dynamic systems that can generate sequences of numbers with a random-like nature. These numbers are then utilized as keys to modify the pixel values of an image. The implementation of this project involves the use of web technologies.

The basic principle of encryption with chaos is based on the ability of some dynamic systems to produce sequences of numbers that are random in nature. This sequence is used to encrypt an image. For decryption, the sequence of random numbers is highly dependent on the initial condition used for generating this sequence. A very minute deviation in the initial condition will result in a totally different sequence. This sensitivity to initial conditions makes chaotic systems ideal for encryption.

## Explain the process of core key generation of encryption and decryption
![](dataSet/A-Chaotic-encryption-Scheme.png)
Every pixel of an image gets many keys for encryption that's why this algorithm is so strong for CryptoGraphy.

## Full pipeline of encryption and decryption
![](dataSet/Example-of-an-embedded-encryption-scheme-real-time-image-encryption-based-a-chaotic-key.png)

# Run the project 
First of all, install Python dependencies 
> $ pip install -r requirements.txt

Then Run the Flask server 
> $ python app.py

The project will be running on the Werkzeug server 
> $ http://localhost:5000/

# To encrypt an original Image
![chaosSnap1](https://github.com/kunal9922/EncryptionandDecryptionusingChaoticKeySequence/assets/53283003/816c1f24-7787-4464-8199-829f360b36cf)

# To Decrypt an Encrypted Image
![chaosSnap2](https://github.com/kunal9922/EncryptionandDecryptionusingChaoticKeySequence/assets/53283003/ea441a41-2d21-4cc6-82e9-d829f4e75dd1)


# The animation displays the encryption and decryption process as it loads.
![chaosLoadingAnimation1](https://github.com/kunal9922/EncryptionandDecryptionusingChaoticKeySequence/assets/53283003/f87a70e4-e27f-4281-8ced-674dd60959fb)

# Responsive Preview
![Screenshot 2023-07-26 154142](https://github.com/kunal9922/EncryptionandDecryptionusingChaoticKeySequence/assets/53283003/461e8969-f60d-4dc0-ac7c-b82d74ea1faf)

# **Bifurcation diagram** 
a [**bifurcation diagram**](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) the values visited or approached asymptotically (fixed points, [periodic orbits](https://en.m.wikipedia.org/wiki/Periodic_orbit), or [chaotic](https://en.m.wikipedia.org/wiki/Chaos_(mathematics))[attractors](https://en.m.wikipedia.org/wiki/Attractor)) of a system as a function of a [bifurcation parameter](https://en.m.wikipedia.org/wiki/Bifurcation_theory) in the system.

A [Bifurcation Diagram](https://en.m.wikipedia.org/wiki/Bifurcation_diagram) shows that the stability of a system can be highly dependent on the inputs.

It is calculated by looping the following equation, for a number of iterations, and every `r` in a defined range. Then the results are plotted with each `r` on the x-axis, and `x` on the y-axis ![Logistic Map](https://wikimedia.org/api/rest_v1/media/math/render/svg/1d88296028cd6a06bd0007ca050d728e7da7447a)

Then the results are plotted with each `r` on the x-axis, and `x` on the y-axis, resulting in the following diagram.

![](./dataSet/bifucationPlot.png)

* Minimum_r = 3.0
* Maximum_r = 4.0
* Max_itermations = 1000
* Skip_itermations = 100
* Step_r = 0.0001

## References 
- https://www.wikiwand.com/en/Chaos_theory#Media/File:Double-compound-pendulum.gif

- https://en.wikipedia.org/wiki/Chaotic_cryptology




