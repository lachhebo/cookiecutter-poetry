PHONY: update the datasets on kaggle
setup:
	poetry add --dev pytest pytest-cov behave flake8  mypy pre-commit
	git init
	pre-commit install


test:
	poetry run pytest tests --cov={{ cookiecutter.project_slug }}  --cov-fail-under=85
