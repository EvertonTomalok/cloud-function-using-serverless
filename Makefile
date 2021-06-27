public:
	gcloud functions add-iam-policy-binding $(function) --member="allUsers" --role="roles/cloudfunctions.invoker" --project=$(project) --region=us-east1

.PHONY: autoflake
autoflake:
	autoflake -r $(AUTOFLAKE_OPTIONS) --exclude */snapshots --remove-unused-variables --remove-all-unused-imports  **/ | tee autoflake.log
	echo "$(AUTOFLAKE_OPTIONS)" | grep -q -- '--in-place' || ! [ -s autoflake.log ]

.PHONY: isort
isort:
	isort ./src --multi-line 3 --trailing-comma --line-width 88 --skip */snapshots $(ISORT_OPTIONS)

.PHONY: black
black:
	black ./src --exclude '.*/snapshots' $(BLACK_OPTIONS)

.PHONY: lint
lint: ISORT_OPTIONS := --check-only
lint: BLACK_OPTIONS := --check
lint: autoflake isort black
	mypy ./src/*.py --ignore-missing-imports
	flake8 ./src

.PHONY: format
format: AUTOFLAKE_OPTIONS := --in-place
format: autoflake isort black
