# EnvoyVault

EnvoyVault is a secure CLI tool for developers to manage local environment variables across different projects. Instead of cluttering system paths or relying on fragile .env files that are prone to accidental commits, EnvoyVault stores environment configurations in a centralized, encrypted flat-file store. Users can list, switch, and export variables to their shell session using simple commands like 'envoy switch project-a' or 'envoy export'. It uses standard Python libraries like 'json', 'hashlib', and 'os' to manage data, ensuring no external dependencies are required. It helps maintain a clean workspace and prevents sensitive secrets from leaking into version control.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Modules](#modules)
- [Future Work](#future-work)
- [License](#license)

## Installation

```bash
git clone <repo-url>
cd envoyvault
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

Run the main entry point to start EnvoyVault.

## Project Structure

```
├── cli.py
├── vault.py
├── crypto.py
├── storage.py
├── utils.py
├── requirements.txt
└── README.md
```

## Modules

- **interface**: Core module for interface functionality.
- **core**: Core module for core functionality.
- **security**: Core module for security functionality.
- **persistence**: Core module for persistence functionality.
- **utils**: Core module for utils functionality.

## Future Work

- [ ] Add comprehensive test suite
- [ ] Implement CI/CD pipeline
- [ ] Add Docker support
- [ ] Improve error handling and edge cases
- [ ] Add configuration documentation
- [ ] Performance optimization

## License

This project is licensed under the MIT License.
