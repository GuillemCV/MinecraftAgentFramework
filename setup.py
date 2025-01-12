from setuptools import setup, find_packages

setup(
    name="MinecraftAgentFramework",
    version="0.1",
    packages=find_packages(include=["framework", "framework.*" , "agents", "agents.*"]),
    include_package_data=True,  # Incluye __init__.py automáticamente
    install_requires=[],  # Agrega dependencias aquí si es necesario
    author="Guillem Casares Valencia",
)
