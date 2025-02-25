# KL-Agent

## Description

KL-Agent is a sophisticated keylogger agent designed for window title monitoring and activity tracking. It provides real-time capture of active window information and maintains detailed logs of user activity.

## Features

- Cross-platform Support
  - Windows compatibility 
  - Linux support (X11 and Wayland)
  - MacOS compatibility
- Active Window Monitoring
  - Process name detection
  - Application switching detection
- Performance & Reliability
  - Lightweight and efficient
  - Low CPU usage
  - Minimal memory footprint
- Enhanced Logging
  - Configurable logging options
  - Structured log format
- Code Quality
  - Clean, readable code structure
  - Comprehensive documentation
  - Type hints and annotations
  - Modular architecture

## Prerequisites

- Python 3.8 or higher
- pip package manager
- virtualenv (recommended)

## Installation

1. Clone the repository:
   ```sh
   git clone <repository_url>
   cd kl-agent
   ```

2. Set up a virtual environment:
   ```sh
   # Install virtualenv if you haven't already
   pip install virtualenv

   # Create a new virtual environment
   python -m venv venv

   # Activate the virtual environment
   # On Windows:
   .\venv\Scripts\activate
   # On Unix or MacOS:
   source venv/bin/activate
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. Ensure your virtual environment is activated:
   ```sh
   # On Windows:
   .\venv\Scripts\activate
   # On Unix or MacOS:
   source venv/bin/activate
   ```

2. Run the agent:
   ```sh
   python main.py
   ```

3. To stop the agent, press `Ctrl+C`

## Project Structure

```
kl-agent/
├── interfaces/
│   ├── i_writer.py          # Writer interface
│   ├── i_window_title.py    # Window title interface
│   ├── i_key_logger.py      # Key logger interface
│   └── i_encryptor.py       # Encryptor interface
├── factories/
│   ├── writer_factory.py    # Writer creation factory
│   └── key_logger_factory.py # Logger creation factory
├── service/
│   ├── file_writer.py       # File writing implementation
│   ├── key_logger.py        # Key logging implementation
│   ├── window_logger.py     # Window tracking implementation
│   └── encryptor.py        # Encryption service
├── main.py                  # Application entry point
├── requirements.txt         # Project dependencies
├── .gitignore              # Git ignore rules
└── README.md               # Project documentation
```

## Troubleshooting

If you encounter any issues:

1. Ensure your virtual environment is activated
2. Verify all dependencies are installed correctly
