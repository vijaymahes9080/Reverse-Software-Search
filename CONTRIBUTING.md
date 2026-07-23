# Contributing to Reverse Software Search

Thank you for your interest in contributing to **Reverse Software Search (RSS)**!

## 🚀 How to Contribute

1. **Fork the Repository**: Create a personal fork on GitHub.
2. **Clone your Fork**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/Reverse-Software-Search.git
   ```
3. **Create a Feature Branch**:
   ```bash
   git checkout -b feat/my-new-engine
   ```
4. **Make Your Changes**:
   - Write clean Python/TypeScript code with proper type annotations.
   - Run unit tests: `python -m pytest backend/tests/`
   - Run TypeScript validation: `npx tsc --noEmit` inside `frontend/`
5. **Commit and Push**:
   ```bash
   git commit -m "feat(engine): add new synthesis engine"
   git push origin feat/my-new-engine
   ```
6. **Open a Pull Request**: Submit your PR targeting the `main` branch.

## 📜 Code Style Guidelines
- **Python**: Follow PEP 8 guidelines and include docstrings for all engine functions.
- **TypeScript / React**: Use functional components, Tailwind CSS styling, and strict type definitions.
