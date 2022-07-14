run_test:
	pytest 


build_async:
	export BUILD_TYPE=async
	# python -m build
	
build_sync:
	export BUILD_TYPE=sync
	# python -m build