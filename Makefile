# Build configuration
# -------------------

APP_NAME := `sed -n 's/^ *name.*=.*"\([^"]*\)".*/\1/p' pyproject.toml`
APP_VERSION := `sed -n 's/^ *version.*=.*"\([^"]*\)".*/\1/p' pyproject.toml`
GIT_REVISION = `git rev-parse HEAD`
CONTAINER_NAME = leads
PSQL_CONTAINER_NAME = postgres-leads


.PHONY: targets
targets:
	@echo "\033[34mDevelopment Targets\033[0m"
	@echo "\033[34m---------------------------------------------------------------\033[0m"
	@perl -nle'print $& if m{^[a-zA-Z_-]+:.*?## .*$$}' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-22s\033[0m %s\n", $$1, $$2}'

# Development targets
# -------------

.PHONY: run
run: start

.PHONY: clean ## Delete all temporary files
clean:
	sudo rm -rf .ipynb_checkpoints
	sudo rm -rf **/.ipynb_checkpoints
	sudo rm -rf .pytest_cache
	sudo rm -rf **/.pytest_cache
	sudo rm -rf __pycache__
	sudo rm -rf **/__pycache__
	sudo rm -rf build
	sudo rm -rf dist

.PHONY: build
build: ## build the server
	docker compose build

.PHONY: dock
dock: ## Starts the server
	docker compose up -d && docker attach $(CONTAINER_NAME)

.PHONY: up
up: ## Starts the server without detaching
	docker compose up

.PHONY: down
down: ## Stops the server
	docker compose down

.PHONY: shell
shell: ## container shell
	docker exec -it $(CONTAINER_NAME) sh -c "clear; (bash || ash || sh)"

.PHONY: attach
attach: ## attach container 
	docker attach $(CONTAINER_NAME)

.PHONY: migrate
migrate: ## Run the migrations
	docker exec -it $(CONTAINER_NAME) alembic upgrade head

.PHONY: rollback
rollback: ## Rollback migrations one level
	docker exec -it $(CONTAINER_NAME) alembic downgrade -1

.PHONY: rollback-all
rollback-all: ## Rollback all migrations
	docker exec -it $(CONTAINER_NAME) alembic downgrade base

.PHONY: psql
psql: ## Connect to the database
	docker exec -it $(PSQL_CONTAINER_NAME) psql -U postgres -d leads

.PHONY: generate-migration 
generate-migration: ## Generate a new migration
	@read -p "Enter migration message: " message; \
	docker exec -it $(CONTAINER_NAME) alembic revision --autogenerate -m "$$message"


# Tests
# ------------------------------

.PHONY: test
test: ## Run the all tests 
	docker exec -it $(CONTAINER_NAME) pytest test
