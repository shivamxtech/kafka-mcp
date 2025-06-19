# 🛠️ Contributing to MCP Python Project

Thank you for your interest in contributing! 🎉  
Whether you're fixing bugs, adding features, or improving documentation — your help is appreciated.

---

## 🧱 Project Structure

```
/src            → Application code (FastMCP, tools, resources)
/.github        → CI/CD workflows, templates
```

---

## ✨ Code Conventions

- **Python version**: 3.11+
- **Formatting**: [`black`](https://black.readthedocs.io/en/stable/)
- **Linting**: [`ruff`](https://docs.astral.sh/ruff/)
- **Tests**: [`pytest`](https://docs.pytest.org/)
- **Tools** and **resources** must use the `@mcp.tool` / `@mcp.resource` decorators from FastMCP.
- Organize files under `src/` according to domain (e.g., `tools/`, `common/`, `api/`)

---

## ✅ Pull Request Guidelines

1. Create a branch:

   ```bash
   git checkout -b feat/your-feature-name
   ```

2. Commit your changes:

   ```bash
   git commit -m "feat: short description"
   ```

3. Push and open a PR **to the `main` branch**.

4. Make sure:
   - [ ] PR has a clear description
   - [ ] CI pipeline is passing (✅ green)
   - [ ] Reviewers are assigned (GitHub auto-assigns via CODEOWNERS)
   - [ ] No lint or formatting errors

5. Include related issue number in the PR description:

   ```
   Fixes #42
   ```

---

## 🔐 Secrets & Environment

Create a `.env` file at the root if needed:

```env
BOOTSTRAP_SERVERS=your_kafka_server
MCP_TRANSPORT=stdio
```

---

## 🐛 Reporting Issues

When reporting a bug or suggesting a feature, include:
- Steps to reproduce
- Expected vs actual behavior
- Stack trace (if error)
- Version (`python --version`, commit hash if relevant)

---

## 📦 Deployment

The project uses GitHub Actions to:
- Lint, test, and build a Docker image
- Push image to Docker Hub on every `main` push

Ensure:
- Your PR **does not break the pipeline**
- You do not hardcode secrets — use GitHub `secrets.*`

---

## 👥 Code Owners & Review

Pull requests must be reviewed by at least **one CODEOWNER**.  
See `.github/CODEOWNERS` for auto-assignment.

---

## 🌳 Branching

| Branch     | Purpose           |
|------------|-------------------|
| `main`     | Production-ready  |
| `feat/*`   | New features      |
| `fix/*`    | Bug fixes         |
| `chore/*`  | Refactor / tooling|


---

Thanks again for contributing 🙌  
We’re excited to build with you!
