# Strixhaven HUB API

## Prerequisites

First, you need to have installed in your computer:
- [Python 3.13 or higher](https://www.python.org/downloads/)
- [UV](https://docs.astral.sh/uv/getting-started/installation/) (Package Manager)
- [Make](https://www.gnu.org/software/make/) (Tasks Automation)

## Configuration

Follow the steps below to set up your project
1. Clone the repository ``bash git clone -b main https://github.com/CarlosEPMarques/strixhaven-api.git``
2. Go to the project directory ``bash cd strixhaven-api``
3. Install the dependencies ``bash uv sync``
4. Create and activate a virtual environment using UV: ``bash source .venv/bin/activate``
5. Validate environment variables, If they do not exist, fill in the values in the `.env` file: ``bash make check_env``
6. Execute the application: ``bash make local/start``

## Testing

To run the tests, use the command: ``bash make test``

## Documentation

To see the API's endpoints, access [API Documentation](http://localhost:8008/docs)

Any other documentation files, such as database documentation, can be found in `docs/data-models.md`
