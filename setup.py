from setuptools import setup

setup(
    name="traceflare",
    version="1.0.0",
    py_modules=["traceflare"],
    install_requires=[
        "requests>=2.31.0",
        "termcolor>=2.3.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

print("\n=====================================================================")
print("IMPORTANT: Run 'initialize_traceflare.py' to configure your API key.")
print("=====================================================================\n")
