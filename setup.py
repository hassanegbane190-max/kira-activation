from setuptools import setup, find_packages

setup(
    name="kira_activation",
    version="1.0.0",
    author="Gbane Assane",
    description="Asymmetric Psi-Transcendence (ΨTA) Complex Activation Function",
    long_description="A groundbreaking complex-valued neural network activation layer designed to master chaotic, highly non-linear, and fractal topologies natively.",
    long_description_content_type="text/markdown",
    url="https://github.com/hassanegbane190-max/kira-activation",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "torch>=2.0.0",
        "numpy>=1.20.0"
    ],
    python_requires=">=3.8",
)
