build:
	docker build -t env_comparator .

test: build
	docker run env_comparator pytest .

run: build
	docker run env_comparator bash -c "python compare_env_files.py .env1 .env2"
